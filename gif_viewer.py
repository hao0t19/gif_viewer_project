import tkinter as tk
from PIL import Image, ImageSequence, ImageTk
import os

# Get the directory of the script
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
GIF_DIR = os.path.join(BASE_DIR, "gifs")

# Automatically load all GIF files in the 'gifs' folder
gif_paths = [os.path.join(GIF_DIR, f) for f in os.listdir(GIF_DIR) if f.endswith(".gif")]

class GifViewer:
    def __init__(self, root, gif_paths):
        self.root = root
        self.root.title("GIF Viewer")
        self.root.attributes('-topmost', True)
        self.root.overrideredirect(True)  # Borderless window
        self.root.wm_attributes("-transparentcolor", "black")  # Transparent background
        
        self.gif_paths = gif_paths
        self.current_gif_index = 0
        
        self.load_gif(self.gif_paths[self.current_gif_index])
        
        self.canvas = tk.Canvas(root, width=self.width, height=self.height, bg='black', highlightthickness=0)
        self.canvas.pack()
        
        self.canvas.bind("<Button-3>", self.show_menu)  # Right-click to show menu
        self.canvas.bind("<B1-Motion>", self.drag_window)  # Drag window with left click
        
        self.menu = tk.Menu(root, tearoff=0)
        self.menu.add_command(label="Switch GIF", command=self.load_next_gif)
        self.menu.add_command(label="Close", command=self.close_app)
        
        self.update_frame()
    
    def load_gif(self, path):
        """Load and process the GIF file"""
        self.frames = []
        self.image = Image.open(path)
        self.width, self.height = self.image.size
        
        for frame in ImageSequence.Iterator(self.image):
            frame = frame.convert("RGBA")
            self.frames.append(ImageTk.PhotoImage(frame))
        
        self.frame_index = 0
        self.delay = self.image.info.get("duration", 100)  # Get frame duration
    
    def update_frame(self):
        """Update the GIF frame"""
        self.canvas.delete("all")
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.frames[self.frame_index])
        self.frame_index = (self.frame_index + 1) % len(self.frames)
        self.root.after(self.delay, self.update_frame)
    
    def load_next_gif(self):
      self.current_gif_index = (self.current_gif_index + 1) % len(self.gif_paths)
      
      # Get current window position
      x, y = self.root.winfo_x(), self.root.winfo_y()
      
      # Load new GIF but keep the same window size
      self.load_gif(self.gif_paths[self.current_gif_index])
      
      # Update canvas size to match new GIF
      self.canvas.config(width=self.width, height=self.height)
      
      # Restore window position
      self.root.geometry(f"{self.width}x{self.height}+{x}+{y}")

    
    def close_app(self):
        """Close the application"""
        self.root.destroy()
    
    def drag_window(self, event):
        """Allow dragging the window by holding left-click"""
        self.root.geometry(f"+{event.x_root}+{event.y_root}")
    
    def show_menu(self, event):
        """Show right-click menu"""
        self.menu.post(event.x_root, event.y_root)
        
if __name__ == "__main__":
    if not gif_paths:
        print("No GIF files found in the 'gifs' folder!")
    else:
        root = tk.Tk()
        app = GifViewer(root, gif_paths)
        root.mainloop()

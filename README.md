# GIF Viewer

A simple, borderless, transparent-background GIF viewer that can display and switch between multiple GIFs on the desktop. The viewer supports dragging, right-click context menu for switching GIFs and closing the application.

## Features
- Displays GIFs in a floating, borderless window
- Supports multiple GIFs from the `gifs/` folder
- Right-click to open a menu to switch GIFs or close the app
- Click and drag to move the window
- Maintains position when switching GIFs

## Installation
1. Install Python (if not already installed)
2. Install required dependencies:
   ```sh
   pip install pillow
   ```
3. Place your GIF files inside a `gifs/` folder in the same directory as the script.

## Usage
Run the script:
```sh
python gif_viewer.py
```

### Controls
- **Right-click**: Open menu to switch GIF or close the app
- **Left-click & drag**: Move the window

## Notes
- The application automatically detects all GIFs in the `gifs/` folder.
- The background is transparent for seamless display.
- GIF switching maintains window position.



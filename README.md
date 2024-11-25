# Image Processing Tool

A Python-based desktop application for image processing and analysis, featuring a modern GUI built with Tkinter and various image manipulation capabilities.

## Features

- Image loading and saving
- Histogram analysis and manipulation
- Local and global image equalization
- Binary image processing
- Statistical analysis of images
- Modern dark-themed interface using the 'equilux' theme

## Project Structure

```
TP-ImageProcess/
├── input/              # Directory for input images
├── output/             # Directory for processed images
├── icons/              # Application icons
├── main.py            # Application entry point
├── interface.py       # GUI implementation
├── imgIO.py           # Image input/output operations
├── TP1.py            # Image processing operations (Part 1)
├── TP2.py            # Image processing operations (Part 2)
├── TP3.py            # Image processing operations (Part 3)
├── binary.py         # Binary image processing functions
├── stats.py          # Statistical analysis functions
├── utils.py          # Utility functions
└── settings.py       # Application settings
```

## Requirements

- Python 3.x
- tkinter
- matplotlib
- ttkthemes
- numpy (implied by the image processing operations)

## Installation

1. Clone this repository:
```bash
git clone [repository-url]
```

2. Install the required dependencies:
```bash
pip install matplotlib ttkthemes
```

## Usage

Run the application using:
```bash
python main.py
```

The application provides a graphical interface where you can:
1. Load images using the "Open" button
2. Apply various image processing operations
3. Save processed images
4. Undo operations
5. View original images
6. Perform local equalization

## Features

### Image Operations
- Image loading and saving
- Histogram visualization
- Image equalization (local and global)
- Binary image processing
- Statistical analysis

### Interface Features
- Modern dark theme
- Undo/Redo functionality
- Original image comparison
- Interactive GUI controls
- File path management


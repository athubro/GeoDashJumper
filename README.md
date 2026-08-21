# GeoDashJumper
# Jump to Dash

A computer vision project that uses **OpenCV** to detect the Geometry Dash game state and automatically determine when the player needs to jump.

## Overview

**Jump to Dash** is an experimental computer-vision system inspired by Geometry Dash. Instead of reading the game's internal data or modifying the game itself, the project analyzes the game screen using a camera/screen capture and OpenCV.

The goal is to identify:

* The player's position
* Platforms and obstacles
* Incoming spikes/objects
* When a jump is necessary
* The appropriate timing for a jump

The project combines **image processing, object detection, geometry, and real-time decision making**.

## How It Works

The basic pipeline is:

```text
Geometry Dash Screen
        ↓
   Screen Capture
        ↓
   OpenCV Processing
        ↓
 Object / Color Detection
        ↓
   Geometry Analysis
        ↓
 Determine Next Jump
        ↓
     Input Action
```

OpenCV processes each frame and extracts useful geometric information from the game.

### 1. Frame Capture

The program continuously obtains frames from the game.

### 2. Image Processing

The frame is converted and processed to make important objects easier to detect. Depending on the current implementation, this can include:

* Color-space conversion
* Thresholding
* Noise removal
* Contour detection
* Edge detection
* Region-of-interest processing

### 3. Object Detection

The system attempts to locate relevant game objects, particularly the player and obstacles.

Rather than relying purely on pixel coordinates, the project represents detected objects geometrically using properties such as:

* `x` / `y` position
* Width and height
* Bounding boxes
* Contours
* Relative distance from the player

### 4. Jump Prediction

Once an obstacle is detected, the program calculates whether the player's current trajectory is likely to intersect with it.

The goal is to determine a suitable jump point instead of simply reacting when the obstacle is directly in front of the player.

### 5. Automated Input

When the calculated conditions indicate that a jump is necessary, the program sends an input to Geometry Dash.

## Technologies

* **Python**
* **OpenCV**
* **NumPy**
* Screen capture
* Computer vision
* Computational geometry

## Project Structure

```text
Jump-to-Dash/
│
├── main.py              # Main program
├── vision.py            # Computer vision / object detection
├── geometry.py          # Geometric calculations
├── input.py             # Input handling
├── config.py            # Configuration values
│
├── images/              # Test images
├── screenshots/         # Captured game frames
└── README.md
```

*The exact file structure may change as the project develops.*

## Current Goals

* [x] Capture game frames
* [x] Process frames with OpenCV
* [x] Experiment with object detection
* [ ] Reliably detect the player
* [ ] Reliably detect obstacles
* [ ] Calculate obstacle distance
* [ ] Predict jump timing
* [ ] Improve detection reliability
* [ ] Run the system in real time
* [ ] Test performance across different Geometry Dash levels


Potential improvements include:

* More robust contour filtering
* Perspective and coordinate normalization
* Tracking the player between frames
* Velocity estimation
* Trajectory prediction
* Adaptive jump timing
* Frame-rate optimization
* Machine-learning-based object detection
* Automatic level difficulty analysis

## Disclaimer

This project is intended as a **computer vision experiment and programming project**. It is designed to explore real-time image processing, geometric reasoning, and automated decision-making.

## Author

**Atharva Bengeri**

Built as an independent computer vision project using Python and OpenCV.

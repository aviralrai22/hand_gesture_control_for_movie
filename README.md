# 🖐️ Hand Gesture Control for VLC Media Player

![Python](https://img.shields.io/badge/python-3.10-blue.svg) ![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-green.svg) ![MediaPipe](https://img.shields.io/badge/MediaPipe-Tracking-orange.svg) 

A computer vision application that allows you to control VLC Media Player using hand gestures. No mouse or keyboard required—just your webcam and Python.

## 📝 Description
This project uses **OpenCV** and **MediaPipe** to track hand landmarks in real-time. By calculating the Euclidean distance between specific finger tips, the program detects gestures and triggers keyboard shortcuts via **PyAutoGUI** to control VLC (Volume, Play, Pause, Seek).

## ✨ Features
* **Volume Control:** Pinch Thumb and Index finger (Distance based).
* **Play/Pause:** Touch Thumb and Pinky finger together.
* **Forward (Skip):** Touch Thumb and Middle finger.
* **Rewind:** Touch Thumb and Ring finger.
* **Cooldown System:** Prevents accidental double-clicks for toggle actions.

## ⚙️ Prerequisites
**IMPORTANT:** This project is optimized for **Python 3.10**. 
(MediaPipe currently has compatibility issues with Python 3.11/3.12).

### Installation
1.  Clone the repository:
    ```bash
    git clone [https://github.com/YOUR_USERNAME/Hand-Gesture-VLC.git](https://github.com/YOUR_USERNAME/Hand-Gesture-VLC.git)
    ```
2.  Navigate to the directory:
    ```bash
    cd Hand-Gesture-VLC
    ```
3.  Install the dependencies:
    ```bash
    pip install opencv-python mediapipe pyautogui numpy
    ```

## 🚀 How to Run
1.  Open VLC Media Player and load a video.
2.  Run the Python script:
    ```bash
    python app.py
    ```
3.  **Crucial Step:** Click on the VLC window to make it the active window (so it receives the key commands).
4.  Show your hand to the camera!

## 🎮 Gesture Guide
| Action | Gesture | Type |
| :--- | :--- | :--- |
| **Volume Up/Down** | Pinch **Thumb** & **Index** | Continuous (Distance) |
| **Play / Pause** | Touch **Thumb** & **Pinky** | Trigger (Touch) |
| **Forward** | Touch **Thumb** & **Middle** | Trigger (Touch) |
| **Rewind** | Touch **Thumb** & **Ring** | Trigger (Touch) |

## 🛠️ Troubleshooting
* **Error: `AttributeError: module 'mediapipe' has no attribute 'solutions'`**
    * *Fix:* Ensure you are not running Python 3.11+. Please use Python 3.10. Also, check that you don't have a file named `mediapipe.py` in your folder.
* **Gestures not working in VLC?**
    * *Fix:* Make sure the VLC window is **focused** (clicked on) and active.

## 👨‍💻 Tech Stack
* Python 3.10
* OpenCV (Computer Vision)
* MediaPipe (Hand Tracking)
* PyAutoGUI (Keyboard Automation)
* NumPy (Math/Calculations)

---
*Developed by [Your Name]*
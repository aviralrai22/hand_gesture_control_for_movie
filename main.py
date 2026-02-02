import tkinter as tk
from tkinter import messagebox
import cv2
import mediapipe as mp
import pyautogui
import math
import time
from PIL import Image, ImageTk # requires pip install pillow

# --- Global Variables ---
running = False
cap = None
cooldown = 1.0
last_action_time = 0

# --- Setup MediaPipe ---
mpHands = mp.solutions.hands
hands = mpHands.Hands(min_detection_confidence=0.7)
mpDraw = mp.solutions.drawing_utils

# --- GUI Functions ---

def start_detection():
    global running, cap
    if not running:
        cap = cv2.VideoCapture(0)
        cap.set(3, 640)
        cap.set(4, 480)
        running = True
        status_label.config(text="Status: RUNNING 🟢", fg="green")
        loop() # Start the loop
    else:
        print("Already running!")

def stop_detection():
    global running, cap
    running = False
    if cap:
        cap.release()
    cv2.destroyAllWindows()
    status_label.config(text="Status: STOPPED 🔴", fg="red")
    # Clear the video label
    video_label.config(image='')

def loop():
    global running, cap, last_action_time
    
    if running:
        success, img = cap.read()
        if success:
            # 1. Process Frame
            imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            results = hands.process(imgRGB)
            lmList = []

            if results.multi_hand_landmarks:
                for handLms in results.multi_hand_landmarks:
                    for id, lm in enumerate(handLms.landmark):
                        h, w, c = img.shape
                        cx, cy = int(lm.x * w), int(lm.y * h)
                        lmList.append([id, cx, cy])
                    mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

            # 2. Gesture Logic
            if len(lmList) != 0:
                # Thumb Tip (4)
                x1, y1 = lmList[4][1], lmList[4][2]
                
                # Volume (Index 8)
                x2, y2 = lmList[8][1], lmList[8][2]
                vol_dist = math.hypot(x2 - x1, y2 - y1)
                
                cv2.line(img, (x1, y1), (x2, y2), (255, 0, 255), 3)

                if vol_dist > 150:
                    pyautogui.press('volumeup')
                elif vol_dist < 30:
                    pyautogui.press('volumedown')

                # Check Cooldown for Toggles
                if (time.time() - last_action_time) > cooldown:
                    # Pause (Pinky 20)
                    x_pinky, y_pinky = lmList[20][1], lmList[20][2]
                    if math.hypot(x_pinky - x1, y_pinky - y1) < 30:
                        pyautogui.press('space')
                        last_action_time = time.time()
                        cv2.putText(img, "PAUSE/PLAY", (50, 50), cv2.FONT_HERSHEY_PLAIN, 2, (0,255,0), 3)

                    # Forward (Middle 12)
                    x_mid, y_mid = lmList[12][1], lmList[12][2]
                    if math.hypot(x_mid - x1, y_mid - y1) < 30:
                        pyautogui.press('right')
                        last_action_time = time.time()
                        cv2.putText(img, "FORWARD >>", (50, 50), cv2.FONT_HERSHEY_PLAIN, 2, (0,255,0), 3)

                    # Rewind (Ring 16)
                    x_ring, y_ring = lmList[16][1], lmList[16][2]
                    if math.hypot(x_ring - x1, y_ring - y1) < 30:
                        pyautogui.press('left')
                        last_action_time = time.time()
                        cv2.putText(img, "<< REWIND", (50, 50), cv2.FONT_HERSHEY_PLAIN, 2, (0,255,0), 3)

            # 3. Update GUI with Video Frame
            # Convert image for Tkinter
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(img)
            imgtk = ImageTk.PhotoImage(image=img)
            video_label.imgtk = imgtk
            video_label.configure(image=imgtk)

        # 4. Repeat Loop after 10ms
        root.after(10, loop)

# --- GUI Setup ---
root = tk.Tk()
root.title("VLC Gesture Controller")
root.geometry("800x600")
root.configure(bg='grey')
# Title Label
title = tk.Label(root,bg="cyan", text="Hand Gesture Control", font=("Arial", 20, "bold"))
title.pack(pady=10)

# Status Label
status_label = tk.Label(root, text="Status: STOPPED 🔴", font=("Arial", 14), fg="red")
status_label.pack(pady=5)

# Button Frame
btn_frame = tk.Frame(root)
btn_frame.pack(pady=8)

start_btn = tk.Button(btn_frame, text="START CAMERA",border=4, bg="green", fg="white", font=("Arial", 12), width=15, command=start_detection)
start_btn.pack(side=tk.LEFT, padx=10)

stop_btn = tk.Button(btn_frame, text="STOP CAMERA", bg="red",border=4, fg="white", font=("Arial", 12), width=15, command=stop_detection)
stop_btn.pack(side=tk.LEFT, padx=10)

# Video Placeholder
video_label = tk.Label(root)
video_label.pack()

# Start the GUI
root.mainloop()
# 👁️‍🗨️ Social Distancing Detector 🚷

A computer vision-based project that monitors whether people are following social distancing norms in real-time video using YOLOv3. Violators are detected, highlighted in red, and logged for review.

---

## 📽️ Demo

> Takes a video (`humans.mp4`), detects people using YOLOv3, calculates pairwise distances, and flags close interactions as violations. Outputs an annotated video (`output.avi`) where green boxes = safe and red boxes = violators.

---

## 🛠️ Features

* Real-time detection using YOLOv3
* Distance calculation between people
* Highlighting of violations
* Outputs processed video with overlays
* GPU acceleration with OpenCV DNN (CUDA)

---

## 🧱 Dependencies

Install dependencies via `pip`:

```bash
pip install opencv-python opencv-python-headless numpy pillow
```

Or if you're using `requirements.txt`:

```txt
opencv-python
opencv-python-headless
numpy
pillow
```

---

## ⚙️ Setup Instructions

1. **Clone the repo** or place the code in a working directory.

2. **Download YOLOv3 model files:**

   * `yolov3.cfg` and `yolov3.weights` from [https://pjreddie.com/darknet/yolo/](https://pjreddie.com/darknet/yolo/)
   * Place them in your project root directory.

3. **Prepare Input Video:**

   * Place your input video in `data/` directory.
   * Default: `data/humans.mp4`

4. **Run the script:**

   ```bash
   python detect.py
   ```

5. **Check Output:**

   * Output file: `output.avi`
   * Displays live with violation count.

---

## ⚠️ Notes

* Make sure you have a compatible GPU and CUDA setup if you're using the DNN CUDA backend.
* Adjust `distance_thres = 50` to calibrate how close is “too close”.
* Only `person` class is considered (COCO class ID 0).

---

## 🧪 Sample Output

Violations are detected when people come closer than the threshold and marked in **red**. Others are marked **green**.

---

## 🏁 Future Work

* Real-time webcam support
* Sound alert on violation
* Logging with timestamps
* Flask-based web dashboard

---

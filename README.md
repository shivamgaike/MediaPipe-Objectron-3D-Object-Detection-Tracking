# MediaPipe Objectron – 3D Object Detection & Tracking

An AI-powered **3D object detection and tracking application** built using **MediaPipe Objectron, OpenCV, and Gradio**.

The application processes video input and detects objects using the MediaPipe Objectron framework. It visualizes detected objects using **3D bounding-box landmarks and orientation axes**, while providing an interactive Gradio interface for configuring detection parameters and analyzing detection results.

---

## 🚀 Features

* 🔍 3D object detection using MediaPipe Objectron
* 📦 3D bounding-box visualization
* 🧭 Object orientation axis visualization
* 🎥 Video upload and processing
* 🖥️ Interactive Gradio web interface
* ⚙️ Adjustable detection confidence
* ⚙️ Adjustable tracking confidence
* 📊 Detection analytics
* 🎯 Detection status monitoring
* 💾 Processed video output
* 🧠 Video-based object tracking

---

## 🧠 Project Overview

Traditional object detection systems generally identify objects using **2D bounding boxes**.

This project explores **3D object detection and tracking** using MediaPipe Objectron.

The system processes video frames and estimates the position and orientation of detected objects. The detected objects are visualized using 3D landmarks and orientation axes.

### Processing Pipeline

1. Upload a video.
2. Read the video frame by frame using OpenCV.
3. Convert frames from BGR to RGB.
4. Process the frames using MediaPipe Objectron.
5. Detect objects in the video.
6. Generate 3D object landmarks.
7. Draw 3D bounding-box connections.
8. Visualize object orientation using axes.
9. Generate an annotated output video.
10. Calculate detection statistics.
11. Display the results through a Gradio interface.

The implementation uses MediaPipe Objectron with configurable detection and tracking confidence values.

---

# 🏗️ System Architecture

```text
                    ┌──────────────────┐
                    │    Input Video   │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │      OpenCV      │
                    │   VideoCapture   │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │ BGR → RGB Frame  │
                    │    Conversion    │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │    MediaPipe     │
                    │     Objectron    │
                    └────────┬─────────┘
                             │
                  ┌──────────┴──────────┐
                  ▼                     ▼
          ┌───────────────┐     ┌───────────────┐
          │ 3D Bounding   │     │  Orientation  │
          │     Box       │     │      Axis     │
          └───────┬───────┘     └───────┬───────┘
                  │                     │
                  └──────────┬──────────┘
                             ▼
                    ┌──────────────────┐
                    │ Annotated Video  │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │    Analytics     │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │ Gradio Interface │
                    └──────────────────┘
```

---

# 🛠️ Technologies Used

| Technology              | Purpose                                 |
| ----------------------- | --------------------------------------- |
| **Python**              | Core programming language               |
| **OpenCV**              | Video processing and frame manipulation |
| **MediaPipe**           | Computer vision framework               |
| **MediaPipe Objectron** | 3D object detection and tracking        |
| **Gradio**              | Interactive web interface               |
| **Matplotlib**          | Visualization support                   |

---

# 📂 Project Structure

```text
mediapipe-objectron-3d-object-detection/
│
├── main.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── assets/
│   └── demo.png
│
└── examples/
    └── sample_video.mp4
```

### `main.py`

The main application contains:

* MediaPipe Objectron initialization
* Video processing
* Object detection
* 3D landmark visualization
* Orientation axis visualization
* Detection analytics
* Gradio user interface

The detection function accepts a video path along with detection and tracking confidence values.

---

# ⚙️ Installation

## 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/mediapipe-objectron-3d-object-detection.git
```

```bash
cd mediapipe-objectron-3d-object-detection
```

---

## 2. Create a Virtual Environment

### Using Conda

```bash
conda create -n objectron python=3.10
```

Activate the environment:

```bash
conda activate objectron
```

### Or Using Python Virtual Environment

```bash
python3 -m venv venv
```

Activate on Linux/macOS:

```bash
source venv/bin/activate
```

Activate on Windows:

```bash
venv\Scripts\activate
```

---

# 📦 Install Dependencies

```bash
pip install -r requirements.txt
```

Create a `requirements.txt` file:

```text
opencv-python
mediapipe
gradio
matplotlib
```

---

# ▶️ Running the Application

Run the application using:

```bash
python main.py
```

The Gradio interface is configured to run locally on:

```text
http://127.0.0.1:7860
```

The application uses port `7860` for the local Gradio server.

---

# 🖥️ How to Use

### Step 1 – Start the Application

```bash
python main.py
```

### Step 2 – Open the Web Interface

Open:

```text
http://127.0.0.1:7860
```

### Step 3 – Upload a Video

Upload a video containing the object you want to analyze.

The application provides a video upload component through Gradio.

### Step 4 – Configure Model Settings

Adjust:

* Detection Confidence
* Tracking Confidence

The default values are:

```text
Detection Confidence: 0.4
Tracking Confidence: 0.7
```

The sliders support values between `0.1` and `0.9`.

### Step 5 – Run Detection

Click:

```text
🔥 RUN 3D DETECTION
```

### Step 6 – Analyze the Output

The processed video displays:

* 3D bounding-box landmarks
* Object orientation axes
* Frame information
* Detection status
* Number of detected objects

The application draws detected object landmarks and orientation axes on the processed frames.

---

# 📊 Detection Analytics

After video processing, the application calculates several metrics.

| Metric                     | Description                                  |
| -------------------------- | -------------------------------------------- |
| **Frames Processed**       | Number of frames processed                   |
| **Total Frames**           | Total frames in the input video              |
| **Frames With Detection**  | Number of frames containing detected objects |
| **Total Objects Detected** | Total number of detected objects             |
| **Detection Rate**         | Percentage of frames containing detections   |
| **Model**                  | MediaPipe Objectron                          |
| **Detection Confidence**   | Selected detection threshold                 |
| **Tracking Confidence**    | Selected tracking threshold                  |

These analytics are generated automatically after processing the video.

---

# 📈 Detection Rate

The application calculates detection rate using:

```text
Detection Rate =
(Frames With Detection / Frames Processed) × 100
```

This metric indicates how consistently the system detects objects throughout the input video.

---

# 🔬 Object Detection Process

The application initializes MediaPipe Objectron using configurable parameters:

```python
objectron = mp_objectron.Objectron(
    static_image_mode=False,
    max_num_objects=5,
    min_detection_confidence=float(detection_confidence),
    min_tracking_confidence=float(tracking_confidence),
    model_name="Shoe"
)
```

The system is configured to detect up to **5 objects per frame**.

For each detected object, 3D bounding-box landmarks are drawn:

```python
mp_drawing.draw_landmarks(
    annotated_image,
    detected_object.landmarks_2d,
    mp_objectron.BOX_CONNECTIONS
)
```

The object's orientation is visualized using:

```python
mp_drawing.draw_axis(
    annotated_image,
    detected_object.rotation,
    detected_object.translation
)
```

---

# 🎯 Applications

This project can serve as a foundation for:

* 🤖 3D Computer Vision
* 📦 Object detection and tracking
* 🕶️ Augmented Reality applications
* 🛍️ Product visualization
* 🎥 Video analysis
* 🧭 Object pose and orientation estimation
* 🧪 Computer Vision research
* 📚 AI and Computer Vision education

---

# ⚙️ Configuration

## Detection Confidence

Controls the minimum confidence required for object detection.

```text
Minimum: 0.1
Maximum: 0.9
Default: 0.4
```

## Tracking Confidence

Controls the confidence threshold used during object tracking.

```text
Minimum: 0.1
Maximum: 0.9
Default: 0.7
```

These parameters can be adjusted directly through the Gradio interface.

---

# ⚠️ Limitations

* Detection performance depends on video quality.
* Lighting conditions can affect detection.
* Fast object movement may affect tracking.
* Occlusion can reduce detection accuracy.
* Camera angle can influence detection performance.
* Processing speed depends on available hardware.
* The current implementation is primarily designed for video-based processing.
* The MediaPipe Objectron model used in this project is configured for a specific supported object category.

---

# 🚀 Future Improvements

* [ ] Add real-time webcam detection
* [ ] Add FPS monitoring
* [ ] Display confidence scores
* [ ] Add object trajectory tracking
* [ ] Add support for additional object categories
* [ ] Add downloadable analytics reports
* [ ] Add performance benchmarking
* [ ] Add Docker support
* [ ] Deploy the application to the cloud
* [ ] Add a real-time detection dashboard
* [ ] Improve video processing performance
* [ ] Add object counting and tracking IDs

---

# 📸 Demo

Add screenshots of the application inside the `assets` folder.

Example:

```markdown
![3D Object Detection Demo](assets/demo.png)
```

You can also add a GIF or short demo video to demonstrate the detection pipeline.

---

# 🧪 Workflow

```text
Input Video
     ↓
OpenCV VideoCapture
     ↓
Frame Extraction
     ↓
BGR → RGB Conversion
     ↓
MediaPipe Objectron
     ↓
3D Object Detection
     ↓
3D Bounding Box
     ↓
Orientation Axis
     ↓
Annotated Output Video
     ↓
Detection Analytics
     ↓
Gradio Interface
```

---

# 📌 Key Learning Outcomes

Through this project, the following concepts can be demonstrated:

* Computer Vision
* Object Detection
* Object Tracking
* 3D Object Representation
* Video Processing
* MediaPipe
* OpenCV
* Model Confidence Thresholds
* Pose and Orientation Visualization
* Gradio Application Development
* Basic Computer Vision Analytics

---

# 👨‍💻 Author

**SHIVAM GAIKE**

B.Tech – Artificial Intelligence & Data Science

---

# ⭐ Acknowledgements

This project uses **MediaPipe Objectron** for 3D object detection and tracking.

Built for learning, experimentation, and practical exploration of **Computer Vision and 3D Object Detection**.

---

# 📄 License

This project is intended for **educational and research purposes**.

Please follow the applicable licenses and terms of the underlying libraries and models used in this project.

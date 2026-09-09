# ============================================================
# MEDIAPIPE OBJECTRON
# 3D SHOE DETECTION
# GRADIO 6.x FRONTEND
# ============================================================

import os
import tempfile

import cv2
import gradio as gr
import mediapipe as mp


# ============================================================
# MEDIAPIPE OBJECTRON SETUP
# ============================================================

mp_objectron = mp.solutions.objectron
mp_drawing = mp.solutions.drawing_utils


# ============================================================
# SHOE DETECTION FUNCTION
# ============================================================

def detect_shoe(video_path, detection_confidence, tracking_confidence):

    # --------------------------------------------------------
    # Check input
    # --------------------------------------------------------

    if video_path is None:
        return (
            None,
            "⚠️ NO VIDEO SELECTED",
            "Upload a shoe video to begin detection."
        )

    # --------------------------------------------------------
    # Open video
    # --------------------------------------------------------

    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        return (
            None,
            "❌ VIDEO ERROR",
            "The uploaded video could not be opened."
        )

    # --------------------------------------------------------
    # Video information
    # --------------------------------------------------------

    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    fps = cap.get(cv2.CAP_PROP_FPS)

    if fps <= 0:
        fps = 30

    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    # --------------------------------------------------------
    # Output video
    # --------------------------------------------------------

    output_path = os.path.join(
        tempfile.gettempdir(),
        "objectron_shoe_output.mp4"
    )

    fourcc = cv2.VideoWriter_fourcc(*"mp4v")

    out = cv2.VideoWriter(
        output_path,
        fourcc,
        fps,
        (width, height)
    )

    # --------------------------------------------------------
    # MediaPipe Objectron
    # --------------------------------------------------------

    objectron = mp_objectron.Objectron(
        static_image_mode=False,
        max_num_objects=5,
        min_detection_confidence=float(detection_confidence),
        min_tracking_confidence=float(tracking_confidence),
        model_name="Shoe"
    )

    # --------------------------------------------------------
    # Analytics variables
    # --------------------------------------------------------

    processed_frames = 0
    detected_frames = 0
    total_objects = 0

    # ========================================================
    # PROCESS VIDEO
    # ========================================================

    while cap.isOpened():

        success, image = cap.read()

        if not success:
            break

        processed_frames += 1

        # ----------------------------------------------------
        # BGR → RGB
        # ----------------------------------------------------

        image_rgb = cv2.cvtColor(
            image,
            cv2.COLOR_BGR2RGB
        )

        image_rgb.flags.writeable = False

        # ----------------------------------------------------
        # Objectron inference
        # ----------------------------------------------------

        results = objectron.process(image_rgb)

        image_rgb.flags.writeable = True

        # ----------------------------------------------------
        # RGB → BGR
        # ----------------------------------------------------

        annotated_image = cv2.cvtColor(
            image_rgb,
            cv2.COLOR_RGB2BGR
        )

        # ====================================================
        # DRAW DETECTIONS
        # ====================================================

        if results.detected_objects:

            detected_frames += 1

            total_objects += len(
                results.detected_objects
            )

            for detected_object in results.detected_objects:

                # ------------------------------------------------
                # Draw 3D bounding box
                # ------------------------------------------------

                mp_drawing.draw_landmarks(
                    annotated_image,
                    detected_object.landmarks_2d,
                    mp_objectron.BOX_CONNECTIONS
                )

                # ------------------------------------------------
                # Draw 3D axis
                # ------------------------------------------------

                mp_drawing.draw_axis(
                    annotated_image,
                    detected_object.rotation,
                    detected_object.translation
                )

        # ====================================================
        # DISPLAY INFORMATION ON VIDEO
        # ====================================================

        cv2.putText(
            annotated_image,
            "MEDIAPIPE OBJECTRON",
            (20, 35),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.9,
            (255, 255, 255),
            2,
            cv2.LINE_AA
        )

        cv2.putText(
            annotated_image,
            "3D SHOE DETECTION",
            (20, 70),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.65,
            (255, 255, 255),
            2,
            cv2.LINE_AA
        )

        cv2.putText(
            annotated_image,
            f"FRAME: {processed_frames}/{total_frames}",
            (20, 105),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.55,
            (255, 255, 255),
            2,
            cv2.LINE_AA
        )

        # ----------------------------------------------------
        # Detection status
        # ----------------------------------------------------

        if results.detected_objects:

            cv2.putText(
                annotated_image,
                f"SHOE DETECTED: {len(results.detected_objects)}",
                (20, 140),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.55,
                (0, 255, 0),
                2,
                cv2.LINE_AA
            )

        else:

            cv2.putText(
                annotated_image,
                "SEARCHING FOR SHOE...",
                (20, 140),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.55,
                (0, 200, 255),
                2,
                cv2.LINE_AA
            )

        # ----------------------------------------------------
        # Write frame
        # ----------------------------------------------------

        out.write(annotated_image)

    # ========================================================
    # RELEASE RESOURCES
    # ========================================================

    cap.release()
    out.release()
    objectron.close()

    # ========================================================
    # CALCULATE ANALYTICS
    # ========================================================

    detection_rate = 0

    if processed_frames > 0:

        detection_rate = (
            detected_frames /
            processed_frames
        ) * 100

    # ========================================================
    # STATUS
    # ========================================================

    if detected_frames > 0:

        status = "🟢 SHOE DETECTED"

    else:

        status = "🔴 NO SHOE DETECTED"

    # ========================================================
    # STATISTICS
    # ========================================================

    stats = f"""
## 🔥 DETECTION COMPLETE

| Metric | Result |
|---|---:|
| **Frames Processed** | `{processed_frames}` |
| **Total Frames** | `{total_frames}` |
| **Frames With Detection** | `{detected_frames}` |
| **Total Objects Detected** | `{total_objects}` |
| **Detection Rate** | `{detection_rate:.2f}%` |
| **Model** | `MediaPipe Objectron — Shoe` |
| **Detection Confidence** | `{detection_confidence}` |
| **Tracking Confidence** | `{tracking_confidence}` |
"""

    return (
        output_path,
        status,
        stats
    )


# ============================================================
# CUSTOM CSS
# ============================================================

css = """

/* ==========================================================
   MAIN PAGE
   ========================================================== */

body {

    background:
        radial-gradient(
            circle at top right,
            #252525 0%,
            #0b0b0b 35%,
            #020202 75%
        ) !important;
}


/* ==========================================================
   GRADIO CONTAINER
   ========================================================== */

.gradio-container {

    max-width: 1450px !important;

    margin: auto !important;

    background: transparent !important;

    color: #f5f5f5 !important;
}


/* ==========================================================
   HERO SECTION
   ========================================================== */

.hero {

    padding: 45px 35px;

    border-radius: 25px;

    margin-bottom: 25px;

    background:
        linear-gradient(
            135deg,
            #181818,
            #050505
        );

    border: 1px solid #292929;

    box-shadow:
        0 0 40px rgba(255,255,255,0.03),
        inset 0 0 40px rgba(255,255,255,0.015);
}


.hero h1 {

    font-size: 52px;

    font-weight: 900;

    letter-spacing: -2px;

    line-height: 0.95;

    margin: 12px 0 0 0;

    color: #ffffff;
}


.hero p {

    font-size: 17px;

    color: #8f8f8f;

    margin-top: 15px;
}


/* ==========================================================
   BADGE
   ========================================================== */

.badge {

    display: inline-block;

    padding: 7px 14px;

    border-radius: 30px;

    background: #1f1f1f;

    border: 1px solid #3a3a3a;

    color: #ffffff;

    font-size: 12px;

    font-weight: 700;

    letter-spacing: 1px;
}


/* ==========================================================
   PANELS
   ========================================================== */

.panel {

    background:
        linear-gradient(
            145deg,
            #151515,
            #090909
        );

    border: 1px solid #292929;

    border-radius: 20px;

    padding: 20px;

    box-shadow:
        0 15px 50px rgba(0,0,0,0.35);
}


/* ==========================================================
   BUTTONS
   ========================================================== */

button {

    border-radius: 12px !important;

    font-weight: 800 !important;

    transition:
        0.2s ease !important;
}


button:hover {

    transform:
        translateY(-2px);

    box-shadow:
        0 10px 25px rgba(255,255,255,0.08);
}


/* ==========================================================
   SLIDERS
   ========================================================== */

input[type="range"] {

    accent-color:
        #ffffff !important;
}


/* ==========================================================
   STATUS
   ========================================================== */

.status-box {

    padding: 20px;

    border-radius: 16px;

    background: #0c0c0c;

    border: 1px solid #292929;

    text-align: center;

    font-size: 20px;

    font-weight: 900;
}


/* ==========================================================
   VIDEO
   ========================================================== */

video {

    border-radius: 15px !important;
}


/* ==========================================================
   FOOTER
   ========================================================== */

.footer {

    text-align: center;

    color: #666;

    padding: 25px;

    font-size: 13px;
}

"""


# ============================================================
# GRADIO APPLICATION
# ============================================================

with gr.Blocks(
    title="Objectron — 3D Shoe Detection"
) as demo:

    # ========================================================
    # HERO
    # ========================================================

    gr.HTML(
        """
        <div class="hero">

            <span class="badge">
                COMPUTER VISION / MEDIAPIPE OBJECTRON
            </span>

            <h1>
                OBJECTRON
                <br>
                3D SHOE DETECTION
            </h1>

            <p>
                AI-powered 3D shoe detection and tracking
                using MediaPipe Objectron.
            </p>

        </div>
        """
    )


    # ========================================================
    # MAIN SECTION
    # ========================================================

    with gr.Row():

        # ====================================================
        # LEFT PANEL
        # ====================================================

        with gr.Column(
            scale=1,
            elem_classes="panel"
        ):

            gr.Markdown(
                """
                ## 🎯 INPUT

                Upload a video containing a shoe.
                """
            )

            video_input = gr.Video(
                label="Shoe Video",
                sources=["upload"]
            )


            gr.Markdown(
                """
                ### ⚙️ MODEL SETTINGS
                """
            )


            detection_confidence = gr.Slider(
                minimum=0.1,
                maximum=0.9,
                value=0.4,
                step=0.05,
                label="Detection Confidence"
            )


            tracking_confidence = gr.Slider(
                minimum=0.1,
                maximum=0.9,
                value=0.7,
                step=0.05,
                label="Tracking Confidence"
            )


            detect_button = gr.Button(
                "🔥 RUN 3D DETECTION",
                variant="primary",
                size="lg"
            )


        # ====================================================
        # RIGHT PANEL
        # ====================================================

        with gr.Column(
            scale=2,
            elem_classes="panel"
        ):

            gr.Markdown(
                """
                ## 🧠 AI OUTPUT

                Processed video with MediaPipe Objectron
                3D bounding boxes and orientation axes.
                """
            )


            video_output = gr.Video(
                label="3D Detection Output"
            )


            status_output = gr.Textbox(
                label="SYSTEM STATUS",
                value="Waiting for input...",
                interactive=False
            )


    # ========================================================
    # ANALYTICS
    # ========================================================

    gr.Markdown(
        """
        ## 📊 DETECTION ANALYTICS
        """
    )


    stats_output = gr.Markdown(
        "Upload a video and start detection."
    )


    # ========================================================
    # BUTTON EVENT
    # ========================================================

    detect_button.click(
        fn=detect_shoe,

        inputs=[
            video_input,
            detection_confidence,
            tracking_confidence
        ],

        outputs=[
            video_output,
            status_output,
            stats_output
        ]
    )


    # ========================================================
    # FOOTER
    # ========================================================

    gr.HTML(
        """
        <div class="footer">

            MEDIAPIPE OBJECTRON
            &nbsp; • &nbsp;
            3D COMPUTER VISION
            &nbsp; • &nbsp;
            SHOE DETECTION

        </div>
        """
    )


# ============================================================
# LAUNCH APPLICATION
# ============================================================

if __name__ == "__main__":

    demo.launch(
        server_name="127.0.0.1",
        server_port=7860,
        css=css
    )
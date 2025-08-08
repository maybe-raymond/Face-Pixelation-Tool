
# Face Pixelation Tool

A Python script for pixelating faces in images or videos using OpenCV and a pre-trained face detection model. The tool supports both image and video inputs, processes the media, and saves the output with pixelated faces.

---

## Features

- Detects faces using OpenCV's `FaceDetectorYN` and a pre-trained ONNX model.
- Pixelates detected faces by downsampling and upsampling the face region.
- Processes both images and videos.
- Allows specifying input and output paths via command-line arguments.

---
## Examples
### Video


https://github.com/user-attachments/assets/95578048-c933-4e6d-8ee0-f01faa9318bb


### Picture 
![hat](https://github.com/user-attachments/assets/00e89786-7c98-4552-bd20-7d1082706a1b)

## Requirements

- Python 3.7 or later
- OpenCV (with ONNX support)
- NumPy
- [FFmpeg](https://ffmpeg.org/) (to be locally installed)
---

## Installation

1. Clone the repository or download the script.
2. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```
---

## Usage

Run the script from the command line, providing paths for input and output files.

### Command-line Arguments

| Argument         | Description                                       | Required | Example                              |
|-------------------|---------------------------------------------------|----------|--------------------------------------|
| `-v, --video`    | Path to the video file (optional if using image)  | No       | `-v path/to/video.mp4`              |
| `-i, --image`    | Path to the image file (optional if using video)  | No       | `-i path/to/image.jpg`              |
| `-o, --output`   | Path to save the processed output (required)      | Yes      | `-o output_filename`                |

---

### Examples

1. **Process a Video:**
   ```bash
   python pixelette.py -v path/to/video.mp4 -o output_video
   ```
   - Input: `path/to/video.mp4`
   - Output: `output_video.mp4`

2. **Process an Image:**
   ```bash
   python pixelette.py -i path/to/image.jpg -o output_image
   ```
   - Input: `path/to/image.jpg`
   - Output: `output_image.jpg`

3. **Missing Input Argument:**
   If neither `-v` nor `-i` is provided, the script will display:
   ```
   Please provide either a video or an image path for processing.
   ```

---


---

## Implementation Details

1. **Face Detection:**
   - Uses OpenCV's `FaceDetectorYN` to detect faces in input media.
   - The detector is initialized with a confidence threshold of `0.65`.

2. **Face Pixelation:**
   - Detected face regions are extracted and downscaled to `10%` of their size, then upscaled to their original size.

3. **Media Processing:**
   - **Videos:** Frames are read using `cv.VideoCapture`, processed frame by frame, and saved using `cv.VideoWriter`.
   - **Images:** Loaded with `cv.imread`, pixelated, and saved with `cv.imwrite`.

---


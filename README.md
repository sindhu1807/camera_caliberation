# Camera Calibration using OpenCV

This project performs **camera calibration** using a single checkerboard image. The script detects checkerboard corners, calibrates the camera, and undistorts the image. Calibration parameters and results are saved for future use.

## 🔧 Features

- Detects checkerboard corners using OpenCV.
- Computes camera intrinsic matrix and distortion coefficients.
- Saves calibration parameters (`camera_calibration.npz`).
- Undistorts the original image and saves the result (`undistorted_image.jpg`).

## 🧠 Dependencies

- Python 3.x
- OpenCV (cv2)
- NumPy

## 📷 Checkerboard Setup

Ensure your checkerboard pattern has **8 inner corners per row and 6 per column** (i.e., 9x7 total squares). Modify `checkerboard_dims` if your pattern differs.

## 🚀 How to Run

1. Clone the repository or download the script.
2. Place your checkerboard image in a known location and update the `image_path` variable in the script:
   ```python
   image_path = r"D:\Path\To\Your\Image.jpg"
```
```markdown
3. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the script:

   ```bash
   python camera_calibration.py
   ```

#🗂 Output

* `camera_calibration.npz` — Numpy archive containing:

  * Camera matrix
  * Distortion coefficients
  * Rotation and translation vectors
* `undistorted_image.jpg` — Corrected image without lens distortion.

📌 Notes

* If the checkerboard corners are not detected, verify the pattern, lighting, and image quality.
* You can use multiple images to improve calibration accuracy by looping through a directory.



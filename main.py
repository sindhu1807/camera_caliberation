import cv2
import numpy as np

# Termination criteria for the cornerSubPix function
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

# Checkerboard dimensions
checkerboard_dims = (8, 6)  # (number of inner corners per checkerboard row and column)

# Prepare object points based on the real-world checkerboard dimensions
objp = np.zeros((checkerboard_dims[0] * checkerboard_dims[1], 3), np.float32)
objp[:, :2] = np.mgrid[0:checkerboard_dims[0], 0:checkerboard_dims[1]].T.reshape(-1, 2)

# Arrays to store object points and image points from the image
objpoints = []  # 3D points in real-world space
imgpoints = []  # 2D points in image plane

# Path to the single calibration image
image_path = r"D:\Downloads\WhatsApp Image 2024-08-10 at 5.26.25 PM.jpeg" # Update this path to your image

# Read the image
img = cv2.imread(image_path)

if img is None:
    print(f"Error loading image: {image_path}")
else:
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Find the checkerboard corners
    ret, corners = cv2.findChessboardCorners(gray, checkerboard_dims, None)

    if ret:
        objpoints.append(objp)
        corners2 = cv2.cornerSubPix(gray, corners, (11, 11), (-1, -1), criteria)
        imgpoints.append(corners2)

        # Draw and display the corners
        img = cv2.drawChessboardCorners(img, checkerboard_dims, corners2, ret)
        cv2.imshow('Checkerboard Image', img)
        cv2.waitKey(500)
        cv2.destroyAllWindows()

        # Calibrate the camera
        ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, None)

        # Save calibration parameters
        np.savez('camera_calibration.npz', ret=ret, mtx=mtx, dist=dist, rvecs=rvecs, tvecs=tvecs)

        print("Camera calibration parameters saved to 'camera_calibration.npz'.")
        print(f"Camera Matrix:\n{mtx}")
        print(f"Distortion Coefficients:\n{dist}")

        # Undistort the image
        undistorted_img = cv2.undistort(img, mtx, dist, None, mtx)

        # Display the original and undistorted images
        cv2.imshow('Original Image', img)
        cv2.imshow('Undistorted Image', undistorted_img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        # Save the undistorted image
        cv2.imwrite('undistorted_image.jpg', undistorted_img)
        print("Undistorted image saved as 'undistorted_image.jpg'.")
    else:
        print("Checkerboard corners not found.")

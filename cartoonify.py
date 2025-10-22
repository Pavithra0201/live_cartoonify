import cv2
import numpy as np

def cartoonify_frame(frame):
    # Resize for better speed
    frame = cv2.resize(frame, (640, 480))

    # Convert to gray
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Smoothen gray image
    gray_blur = cv2.medianBlur(gray, 7)

    # Detect edges
    edges = cv2.adaptiveThreshold(
        gray_blur, 255,
        cv2.ADAPTIVE_THRESH_MEAN_C,
        cv2.THRESH_BINARY,
        blockSize=9,
        C=9
    )

    # Apply bilateral filter for smooth coloring
    color = cv2.bilateralFilter(frame, d=9, sigmaColor=300, sigmaSpace=300)

    # Combine edges + color
    cartoon = cv2.bitwise_and(color, color, mask=edges)

    return cartoon

def main():
    cap = cv2.VideoCapture(0)  # 0 = default camera
    if not cap.isOpened():
        print("❌ Could not open webcam.")
        return

    print("🎥 Press 'q' to quit, 's' to save a frame.")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("❌ Failed to grab frame.")
            break

        cartoon_frame = cartoonify_frame(frame)

        # Combine original + cartoon
        combined = np.hstack((frame, cartoon_frame))

        cv2.imshow("Original (Left) vs Cartoonified (Right)", combined)

        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break
        elif key == ord('s'):
            cv2.imwrite("cartoon_snapshot.jpg", cartoon_frame)
            print("💾 Saved cartoon_snapshot.jpg")

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

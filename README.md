🎨 Cartoonify Webcam – Real-Time Cartoon Filter using OpenCV

Turn your webcam feed into a live cartoon!
This project uses Python + OpenCV to apply a real-time cartoon effect to your video stream.
Simple, fun, and great for learning computer vision basics 👀

🚀 Features

🎥 Real-time cartoonification from webcam

🧠 Edge detection + bilateral smoothing for crisp outlines

💾 Press s to save snapshots

❌ Press q to quit

⚡ Lightweight & runs on most systems

🧰 Requirements

Make sure you have Python 3.8+ and these libraries installed:

pip install opencv-python numpy

🗂️ Project Structure
cartoonify-webcam/
│
├── cartoonify_webcam.py    # Main script
├── cartoon_snapshot.jpg    # Saved image (optional)
└── README.md               # Documentation

▶️ How to Run

Clone the repository:

git clone https://github.com/Pavithra0201/cartoonify-webcam.git
cd cartoonify-webcam


Run the script:

python cartoonify.py


Controls:

Press s → Save the cartoon image

Press q → Quit the program

🧠 How It Works

Captures frames from webcam using cv2.VideoCapture.

Converts to grayscale and applies a median blur.

Detects edges using adaptive thresholding.

Smooths colors using a bilateral filter.

Combines both to produce the cartoon effect.

📸 Sample Output
Original	Cartoonified
<img src="https://github.com/Pavithra0201/cartoonify/assets/sample1.jpg" width="300"/>	<img src="https://github.com/<your-username>/cartoonify-webcam/assets/sample2.jpg" width="300"/>
💡 Future Enhancements

Add multiple filter modes (sketch, oil paint, watercolor)

Real-time brightness/saturation adjustment

GUI using Tkinter or Streamlit

🧑‍💻 Author


🌐 GitHub: Pavithra0201

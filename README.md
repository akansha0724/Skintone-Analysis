🎨 **Real-Time Skin Tone Analyzer Using Python and OpenCV**

A real-time skin tone analyzer that helps users identify their skin tone and get personalized color recommendations.
Using computer vision and color analysis, this tool provides instant feedback about which colors would complement your skin tone best.

💡 **Inspiration**

This idea came while scrolling through color theory reels on Instagram — I was fascinated by how certain colors enhance or clash with different skin tones.
So, I decided to bring that concept to life with Python — combining OpenCV, color theory, and machine learning to make a tool that analyzes your skin tone in real time and recommends your perfect color palette.

🚀 **Features**

👁️ Real-time face detection using OpenCV

🎨 Instant skin tone classification

👕 Personalized color recommendations based on your tone

🌈 Color palette visualization for complementary shades

📸 Sample output capture functionality

💡 Smart color avoidance suggestions (which colors to skip)

**How It Works**

🎥 Face Detection
- Uses OpenCV's Haar Cascade Classifier for reliable face detection
- Processes webcam feed in real-time at 30 FPS
- Draws a green rectangle around detected faces for visual feedback

🔍 Skin Analysis
- Focuses on the central region of your face (30-70% of face width/height)
- Avoids edges, hair, and accessories for accurate tone measurement
- Samples multiple points to get an average skin tone
- Displays a yellow rectangle showing the analyzed area

🎨 Color Processing
- Converts BGR color space to RGB for accurate color representation
- Calculates average RGB values from the sampled region
- Shows your skin tone's RGB values for precise color matching
- Displays a color patch showing your exact detected tone

📊 Tone Classification
- Analyzes brightness levels to determine skin tone category
- Categories: Fair (200+), Light (150-200), Medium (100-150), Tan (50-100), Dark (0-50)
- Updates classification in real-time as lighting changes
- Ensures consistent results across different lighting conditions

👕 Color Recommendations
- Provides personalized color suggestions based on your tone
- Shows 3 best colors that complement your skin tone
- Suggests 2 colors to avoid that might clash
- Updates recommendations instantly as lighting changes

📸 Output Features
- Press 's' to save a snapshot with all analysis details
- Saves high-quality JPEG images in the assets folder
- Perfect for before/after comparisons
- Includes all measurements and recommendations in the saved image

**Getting Started** 

Prerequisites
- Python 3.x
- Webcam

Installation
1. Clone the repository:
```bash
git clone https://github.com/akansha0724/Skintone-Analysis.git
```

2. Install required packages:
```bash
pip install -r req.txt
```

Usage
1. Run the program:
```bash
python colouranalysis.py
```
2. Position your face in front of the camera
3. Press 's' to save a sample output
4. Press 'q' to quit

Contributing
Feel free to fork this project and submit pull requests. You can also open issues for bugs or feature suggestions.

- Akansha

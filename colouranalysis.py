import cv2
import numpy as np
import os

def get_color_recommendations(tone):
    """Return recommended colors based on skin tone."""
    recommendations = {
        "Fair": {
            "Best": ["Navy", "Soft Pink", "Burgundy", "Cool Blue", "Purple"],
            "Avoid": ["Orange", "Bright Yellow", "Gold"]
        },
        "Light": {
            "Best": ["Pastel Blue", "Lavender", "Soft Red", "Teal", "Rose Pink"],
            "Avoid": ["Neon Colors", "Brown", "Orange-Red"]
        },
        "Medium": {
            "Best": ["Coral", "Olive Green", "Warm Brown", "Deep Purple", "Turquoise"],
            "Avoid": ["Pale Yellow", "Light Gray", "Beige"]
        },
        "Tan": {
            "Best": ["Deep Red", "Forest Green", "Royal Blue", "Gold", "Orange"],
            "Avoid": ["Pastels", "Neon Pink", "Light Brown"]
        },
        "Dark": {
            "Best": ["White", "Bright Yellow", "Fuchsia", "Emerald", "Royal Purple"],
            "Avoid": ["Dark Brown", "Navy", "Black"]
        }
    }
    return recommendations.get(tone, {"Best": [], "Avoid": []})

# Load Haar Cascade for face detection
FACE_CASCADE_PATH = 'haarcascade_frontalface_default.xml'
face_cascade = cv2.CascadeClassifier(FACE_CASCADE_PATH)

if face_cascade.empty():
    print("Error loading Haar cascade.")
    exit()

# Colors
BOX_COLOR = (203, 192, 255)  # Light pink box
TEXT_COLOR = (147, 112, 219)  # Darker pink for text
BACKGROUND_COLOR = (240, 220, 255)  # Very light pink background

# Start webcam
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Webcam not found.")
    exit()

print("Press 'q' to quit.")

while True:
    ret, frame = cap.read()
    if not ret:
        print("Frame capture failed.")
        break

    # Create background
    height, width = frame.shape[:2]
    background = np.full((height, width, 3), BACKGROUND_COLOR, dtype=np.uint8)
    
    # Blend frame with background to create a pink tint
    frame = cv2.addWeighted(frame, 0.8, background, 0.2, 0)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 5, minSize=(100, 100))

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), BOX_COLOR, 2)

        # Central face region (avoids edges, eyes, hair)
        x1, y1 = int(x + w * 0.3), int(y + h * 0.3)
        x2, y2 = int(x + w * 0.7), int(y + h * 0.7)
        roi = frame[y1:y2, x1:x2]

        if roi.size == 0:
            continue

        avg_bgr = np.mean(roi, axis=(0, 1)).astype(int)
        avg_rgb = (avg_bgr[2], avg_bgr[1], avg_bgr[0])

        brightness = sum(avg_rgb) / 3
        if brightness > 200:
            tone = "Fair"
        elif brightness > 150:
            tone = "Light"
        elif brightness > 100:
            tone = "Medium"
        elif brightness > 50:
            tone = "Tan"
        else:
            tone = "Dark"

        # Get color recommendations
        recommendations = get_color_recommendations(tone)
        
        # Draw color patch and info
        cv2.rectangle(frame, (x + w + 10, y), (x + w + 60, y + 50), avg_bgr.tolist(), -1)
        cv2.rectangle(frame, (x + w + 10, y), (x + w + 60, y + 50), (255, 255, 255), 1)
        
        # Display tone and RGB
        y_offset = y
        cv2.putText(frame, f"Tone: {tone}", (x + w + 70, y_offset + 20), cv2.FONT_HERSHEY_SIMPLEX, 0.6, TEXT_COLOR, 1)
        cv2.putText(frame, f"RGB: {avg_rgb}", (x + w + 70, y_offset + 40), cv2.FONT_HERSHEY_SIMPLEX, 0.5, TEXT_COLOR, 1)
        
        # Display recommended colors
        y_offset += 60
        cv2.putText(frame, "Best Colors:", (x + w + 10, y_offset), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 1)
        for i, color in enumerate(recommendations["Best"][:3]):  # Show top 3 colors
            cv2.putText(frame, f"- {color}", (x + w + 10, y_offset + 20 + i*20), 
                       cv2.FONT_HERSHEY_SIMPLEX, 0.5, TEXT_COLOR, 1)
        
        y_offset += 80
        cv2.putText(frame, "Colors to Avoid:", (x + w + 10, y_offset), 
                   cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 1)
        for i, color in enumerate(recommendations["Avoid"][:2]):  # Show top 2 colors to avoid
            cv2.putText(frame, f"- {color}", (x + w + 10, y_offset + 20 + i*20), 
                       cv2.FONT_HERSHEY_SIMPLEX, 0.5, TEXT_COLOR, 1)

        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 255), 1)
        
        # Save frame as sample output when 's' is pressed
        if cv2.waitKey(1) & 0xFF == ord('s'):
            try:
                # Ensure the assets directory exists
                if not os.path.exists('assets'):
                    os.makedirs('assets')
                # Save with proper encoding and compression
                success = cv2.imwrite('assets/sampleoutput.jpg', frame, [cv2.IMWRITE_JPEG_QUALITY, 100])
                if success:
                    print("Sample output saved successfully!")
                else:
                    print("Error: Failed to save image!")
            except Exception as e:
                print(f"Error saving image: {str(e)}")
        break

    cv2.imshow("Skin Tone Analyzer", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
print("Camera released.")

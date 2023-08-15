import cv2
import sys

def extract_frames(video_path, output_folder, frame_interval=5):
    cap = cv2.VideoCapture(video_path)
    frame_rate = int(cap.get(cv2.CAP_PROP_FPS))
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    interval_frames = frame_rate * frame_interval

    if not cap.isOpened():
        print("Error: Could not open video file.")
        return

    frame_number = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        if frame_number % interval_frames == 0:
            frame_filename = f"{output_folder}/frame_{frame_number}.jpg"
            cv2.imwrite(frame_filename, frame)
            print(f"Saved frame {frame_number} as {frame_filename}")
        
        frame_number += 1
    
    cap.release()

if __name__ == "__main__":
    video_path = sys.argv[1]  # Replace with your video file's path
    output_folder = "frames"  # Folder to save extracted frames
    frame_interval = 120  # Interval in seconds

    extract_frames(video_path, output_folder, frame_interval)
import cv2
import os

def extract_frames(video_path, output_folder, frame_interval=1):
    cap = cv2.VideoCapture(video_path)
    
    if not cap.isOpened():
        print("Error: Cannot open video file.")
        return

    fps = int(cap.get(cv2.CAP_PROP_FPS))  # Dohvati broj frejmova u sekundi
    frame_skip = fps * frame_interval  # Odredi koliko frejmova preskačeš

    os.makedirs(output_folder, exist_ok=True)

    frame_count = 0
    saved_count = 922 # Broj slika koje već imamo

    while True:
        ret, frame = cap.read()
        if not ret:
            break  # Kraj videa

        if frame_count % frame_skip == 0:
            frame_filename = os.path.join(output_folder, f"frame_{saved_count:04d}.jpg")
            cv2.imwrite(frame_filename, frame)
            saved_count += 1

        frame_count += 1

    cap.release()
    print(f"Extracted {saved_count} frames and saved to {output_folder}.")


video_path = "videos/fourth_video.mp4"  # Postavi svoj put do videa
output_folder = "frames"  # Folder gde će se čuvati slike
extract_frames(video_path, output_folder, frame_interval=5)  # Svakih 5 sekundi

import os
import subprocess

input_dir = '1_videos_original'
frame_output_dir = '2_frames_extracted'

for subdir, dirs, files in os.walk(input_dir):
    for file in files:

        if file.lower().endswith(('.mp4', '.mov', '.avi', '.mkv')):
            video_path = os.path.join(subdir, file)

            relative_path = os.path.relpath(subdir, input_dir)
            video_output_dir = os.path.join(frame_output_dir, relative_path)
            os.makedirs(video_output_dir, exist_ok=True)
            
            unique_prefix = os.path.splitext(file)[0]
            
            subprocess.run(f'ffmpeg -i "{video_path}" "{video_output_dir}/{unique_prefix}_frame_%04d.png"', shell=True)

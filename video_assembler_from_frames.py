import os
import subprocess
from collections import defaultdict

upscaled_frames_dir = '3_frames_upscaled'
output_videos_dir = '4_videos_processed'
os.makedirs(output_videos_dir, exist_ok=True)

frames_dict = defaultdict(list)

for filename in os.listdir(upscaled_frames_dir):
    if filename.endswith('.png'):
        original_name, frame_count = filename.split('_frame_')[0], filename.split('_frame_')[1].split('-')[0]
        frames_dict[original_name].append((int(frame_count), filename))

for original_name, frames in frames_dict.items():
    frames.sort()
    with open(f'{output_videos_dir}/{original_name}_frames.txt', 'w') as f:
        for frame in frames:
            f.write(f"file '../{upscaled_frames_dir}/{frame[1]}'\n")
    
    command = [
        'ffmpeg',
        '-f', 'concat',
        '-safe', '0',
        '-i', f'{output_videos_dir}/{original_name}_frames.txt',
        '-c:v', 'libx264',
        '-vf', 'fps=30,format=yuv420p',
        '-pix_fmt', 'yuv420p',
        f'{output_videos_dir}/{original_name}.mp4'
    ]

    print("Running command:", ' '.join(command))
    result = subprocess.run(command, capture_output=True, text=True)

    if result.returncode != 0:
        print("FFmpeg failed with:")
        print(result.stderr)
    else:
        print("FFmpeg succeeded.")

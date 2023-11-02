# VideoFrameTransformer

[English](README.md) | [繁體中文](README.zh-TW.md)

## Overview
VideoFrameTransformer is a toolchain that assists in the conversion of video to frames and back to video format. While it does not directly upscale images, it facilitates the process by preparing frames for upscaling through other software (like Gigapixel AI) and then reassembling them into a high-resolution video. This utility relies on FFmpeg to handle video frame extraction and reassembly.

## Prerequisites
Before running the scripts, make sure you have FFmpeg installed on your system. You can download it from [FFmpeg official website](https://ffmpeg.org/download.html) or install it using a package manager for your operating system.

For example, on macOS, you can use Homebrew:
```bash
brew install ffmpeg
```

## Usage
Follow these steps to use VideoFrameTransformer:

1. Place your original 4K videos in the `1_videos_original` folder.
2. Run the `video_frames_extractor.py` script to extract frames from the videos into `2_frames_extracted`.
3. Process the extracted frames using an app of your choice (e.g., Gigapixel AI), and save upscaled frames in to `3_frames_upscaled`.
4. Use the `video_assembler_from_frames.py` script to reassemble the processed frames into an upscaled video in `4_videos_processed`.

## Contributing
Contributions to the Video Frame Transformer are welcome. If you have a suggestion that would make this better, please fork the repo and create a pull request.

## License
This project uses the [MIT License](LICENSE).

## Contact
If you want to contact me you can reach me at `fattie@fattie.io`.
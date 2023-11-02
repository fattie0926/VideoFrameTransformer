# VideoFrameTransformer

## Overview
VideoFrameTransformer is a set of tools designed to upscale and enhance video frames from 4K to 16K resolution using advanced image processing techniques. It leverages the power of FFmpeg for video processing.

## Prerequisites
Before running the scripts, make sure you have FFmpeg installed on your system. You can download it from [FFmpeg official website](https://ffmpeg.org/download.html) or install it using a package manager for your operating system.

For example, on macOS, you can use Homebrew:
```bash
brew install ffmpeg
```

## Usage
Follow these steps to use VideoFrameTransformer:

1. Place your original 4K videos in the 1_videos_original folder.
2. Run the video_frames_extractor.py script to extract frames from the videos.
3. Process the extracted frames using an app of your choice (e.g., Gigapixel AI). Refer to the app’s documentation for specific instructions.
4. Use the video_assembler_from_frames.py script to reassemble the processed frames into an upscaled video.

## Contributing
Contributions to the Video Frame Transformer are welcome. If you have a suggestion that would make this better, please fork the repo and create a pull request.

## License
This project uses the [MIT License](LICENSE).

## Contact
If you want to contact me you can reach me at `fattie@fattie.io`.
# VideoFrameTransformer

[English](README.md) | [繁體中文](README.zh-TW.md)

## 概覽
VideoFrameTransformer 是一個工具組，幫助用戶將影片轉換為圖片，然後再新組合成影片。雖然它不直接進行圖像放大，但它通過拆解後的圖片以通過其他軟件（如Gigapixel AI）進行放大，然後將它們重新組裝成高解析度的影片。這個工具依賴於FFmpeg來處理影片幀的提取和重組。

## 先決條件
在運行腳本之前，請確保您的系統上安裝了FFmpeg。您可以從 [FFmpeg官方網站](https://ffmpeg.org/download.html) 下載，或者使用您的操作系統的包管理器進行安裝。

例如，在macOS上，您可以使用Homebrew：
```bash
brew install ffmpeg
```

## 使用方法
按照以下步驟使用VideoFrameTransformer：

1. 將您的原始影片放置在 `1_videos_original` 文件夾中。
2. 運行 `video_frames_extractor.py` 腳本，從影片中提取幀到 `2_frames_extracted`。
3. 使用您選擇的應用程式（例如Gigapixel AI）處理提取的幀，並將放大的幀保存到 `3_frames_upscaled`。
4. 使用 `video_assembler_from_frames.py` 腳本將處理過的幀重新組裝成放大的影片，保存在 `4_videos_processed`。

## 貢獻
歡迎對Video Frame Transformer做出貢獻。如果您有任何可以讓這個項目更好的建議，請fork本倉庫並創建一個拉取請求。

## 授權
該項目使用 [MIT 授權](LICENSE)。

## 聯繫
如果您想聯繫我，可以通過 `fattie@fattie.io` 找到我。

[回到主頁](./README.md)
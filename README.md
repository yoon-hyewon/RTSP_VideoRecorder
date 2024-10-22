# RTSP Video Recorder with Real-time Filters

This Python application streams video from an **RTSP URL**, applies real-time filters, and records the video. It utilizes **OpenCV** for video processing and allows users to control recording and filters via keyboard inputs.

## Features
- **RTSP Video Streaming**: Stream videos directly from an RTSP URL.
- **Real-time Filters**:
  - **1**: Brightness Increase
  - **2**: Contrast Increase
  - **3**: Horizontal Flip
  - **0**: No Filter (Default)
- **Recording Control**:
  - **Spacebar**: Start/Stop Recording
  - **ESC**: Exit the Program
- **Visual Indicators**:
  - Red Circle: Indicates Recording is Active
  - Current Filter Name: Displayed on the Video Frame
- **File Output**: Saves recorded video as `rtsp_filtered_record.avi`.

## Requirements
- **Python 3.x**
- **OpenCV**: Install using the following command:
  ```bash
  pip install opencv-python

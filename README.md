# YouTube Video Downloader 🎬

A simple yet powerful Python script that allows you to download YouTube videos directly from your terminal. Paste a URL, choose a save location, and let the script handle the rest. It's built to be reliable, user-friendly, and cross-platform.

This tool uses `yt-dlp` for robust and up-to-date downloading capabilities and `Tkinter` for a native file dialog, ensuring a smooth user experience.

---

## ✨ Features

-   **Easy to Use:** Simple command-line interface.
-   **Cross-Platform:** Works on macOS, Windows, and Linux.
-   **High-Quality Downloads:** Fetches the best universally compatible MP4 format (H.264 codec) to ensure playback on any device.
-   **Interactive Folder Selection:** A native dialog box lets you easily choose where to save your video.
-   **Reliable:** Powered by `yt-dlp`, which is actively maintained to keep up with YouTube's changes.

---

## ⚙️ How It Works

The script takes a YouTube video URL as input. It then uses `yt-dlp` to fetch the video information and download the highest quality stream that is compatible with most video players (like QuickTime, VLC, and Windows Media Player). A graphical folder selection dialog, created with `Tkinter`, allows the user to specify a download location.

The key dependency, **FFmpeg**, is used in the background by `yt-dlp` to merge the high-quality video and audio streams into a single, playable file.

---

## 🚀 Setup and Installation

To get this script running on your local machine, you'll need Python 3 and the FFmpeg utility. Follow the steps below for your operating system.

--- 

### Step 1: Clone the Repository

- First, clone this repository to your local machine using Git.
- git clone https://github.com/Yezdani01/Youtube-video-downloader.git
- cd Youtube-video-downloader


### Step 2: Set Up a Python Virtual Environment

- It's highly recommended to use a virtual environment to keep project dependencies isolated.

# Create the virtual environment
- python3 -m venv .venv

# Activate the environment
# On macOS/Linux:
- source .venv/bin/activate

# On Windows (Command Prompt):
- .\.venv\Scripts\activate


### Step 3: Install Python Dependencies
- With the virtual environment active, install the required Python library.
- pip install yt-dlp


### Step 4: Install FFmpeg (Crucial Step!)

- yt-dlp requires the FFmpeg tool to merge video and audio files. This is not a Python package and must be installed separately.
- For macOS Users (via Homebrew) 🍎
- The easiest way to install FFmpeg on a Mac is with Homebrew.
- Install Homebrew (if you don't have it):

- /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"


# Install FFmpeg:

- brew install ffmpeg

# For Windows Users 💻

### Download FFmpeg: 
- Go to the FFmpeg official download page and click the Windows icon. Use one of the recommended build links (e.g., "Windows builds by BtbN"). Download the latest ffmpeg-master-latest-win64-gpl.zip file.

### Extract FFmpeg: 
- Create a folder at a simple location (e.g., C:\FFmpeg). Extract the contents of the downloaded ZIP file into this folder.

### Add FFmpeg to Windows PATH:

- Search for "Environment Variables" in the Start Menu and select "Edit the system environment variables".
- Click the "Environment Variables..." button.
- In the "System variables" section, find and select the Path variable, then click "Edit...".
- Click "New" and add the path to the bin folder inside your FFmpeg directory (e.g., C:\FFmpeg\bin).
- Click OK on all windows to save the changes.
- Verify the installation: Open a new Command Prompt and type:
- ffmpeg -version

- If it shows version information, you're all set.

## ▶️ How to Use

- Once everything is set up, running the script is easy:
- Make sure your virtual environment is active.
- Run the youtube.py script from your terminal:

- python youtube.py

- Paste the YouTube URL into the terminal when prompted and press Enter.
- A folder selection dialog will appear. Choose where you want to save the video and click "Open" or "Select Folder".

- The download progress will be displayed in the terminal. Once complete, you'll find the video file in your selected folder!

## ⚠️ Disclaimer

- This tool is for personal and educational use only. Downloading copyrighted content without permission may be against YouTube's terms of service. Please respect copyright laws and the terms of service of the platform.


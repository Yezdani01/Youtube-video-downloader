import yt_dlp
import tkinter as tk
from tkinter import filedialog
import os
from typing import Any

def download_video(url: str, save_path: str) -> None:
    """Downloads a YouTube video to the specified path using yt-dlp."""
    
    ydl_opts: dict[str, Any] = {

        'format': 'bestvideo[ext=mp4][vcodec^=avc1]+bestaudio[ext=m4a]/best[ext=mp4]',
        'outtmpl': os.path.join(save_path, '%(title)s.%(ext)s'),
        'progress_hooks': [lambda d: print(f"Status: {d['status']}, Downloaded: {d.get('_percent_str', 'N/A')}, ETA: {d.get('_eta_str', 'N/A')}") if d['status'] in ('downloading', 'finished') else None],
    }
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=False)
            video_title = info_dict.get('title', 'Unknown Title')
            print(f"Fetching video: '{video_title}'")
            
            ydl.download([url])
            
        print("\n✅ Video downloaded successfully!")
        print(f"Saved to: {save_path}")
        
    except Exception as e:
        print(f"\n❌ An error occurred during download: {e}")

def open_file_dialog() -> str:
    """Opens a dialog to select a folder and returns the path."""
    folder = filedialog.askdirectory()
    if folder:
        print(f"Selected folder: {folder}")
    return folder or ""

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()

    video_url = input("Please enter a YouTube URL: ")
    save_dir = open_file_dialog()

    if video_url and save_dir:
        print("\nStarting download...")
        download_video(video_url, save_dir)
    else:
        print("\nDownload cancelled: No URL or save location provided.")
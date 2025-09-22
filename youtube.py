from pytube import Youtube
import tkinter as tk
from tkinter import filedialog  


def download_video(url, save_path):
    try:
        yt = Youtube(url)
        streams = yt.streams.filter(progressive = True, file_extension = "mp4")
        highest_res_stream = streams.get_highest_resolution()
        highest_res_stream.download(output_path = save_path)
        print("Video downloaded Sucessfully !!!")      
    except Exception as e:
        print(e)








        
    url = ""
    save_path = ""

    download_video(url, save_path)
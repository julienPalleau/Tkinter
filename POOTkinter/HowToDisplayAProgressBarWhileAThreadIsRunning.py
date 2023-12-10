# https://www.pythontutorial.net/tkinter/tkinter-thread-progressbar/
# Missing proxyDict package unable to install it.


"""
How to Display a Progress Bar while a Thread is Running in Tkinter
Summary: In this tutorial, you'll learn to display a progressbar while a thread is running in Tkinter application.
This tutorial assumes that you know how to use the after() method and understand how threadings work in Python.
Also, you should know how to switch between frames using the tkraise() method.

In this tutorial, you'll build a picture viewer that shows a random picture from unsplash.com using its API.

If you make an HTTP request to the following API endpoint:
https://source.unsplash.com/random/640x480
... you'll get a random picture with the size of 640x480

To call the API, you use the requests module.
First, install the requests module if it's not available on your computer:
pip install requests
Second, define a new class that inherits from the Thread class:
"""
import requests
import tkinter as tk
from threading import Thread
from PIL import Image, ImageTk
from tkinter import ttk
from Proxies import ProxyDict


class PictureDownload(Thread):
    def __init__(self, url):
        super().__init__()

        self.picture_file = None
        self.url = url

    def run(self):
        """ download a picture and save it to a file """
        # download the picture
        response = requests.get(self.url, proxies=proxyDict)
        picture_name = self.url.split('/')[-1]
        picture_file = f'./assets/{picture_name}.jpg'

        # save the picture to a file
        with open(picture_file, 'wb') as f:
            f.write(response.content)

        self.picture_file = picture_file



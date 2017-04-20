# AutoUpload
Personal project to automatically handle converting xbox dvr clips to gifs and automatically uploading them to giphy. Written in Python 2.7.

## Requirements
* [ffmpeg](https://ffmpeg.org/) installed on your machine (and added to path for Windows users)
* [watchdog](https://pypi.python.org/pypi/watchdog) == 0.8.3
* [requests](http://docs.python-requests.org/en/master/) == 2.13.0
* [pyperclip](https://pypi.python.org/pypi/pyperclip) == 1.5.27

All of these can be installed with **pip** and the given **requirements.txt** with the command:
  
pip install -r requirements.txt

## Usage
This script currently only works on the command line, although I have plans for adding a GUI with Tkinter. To run the script, use the following command:

python autoupload.py "**path to where your Xbox DVR clips goes here**"

If a path isn't given, the current directory will be used instead.

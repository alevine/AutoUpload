from __future__ import print_function
from sys import argv
from time import sleep
from subprocess import check_call
import os.path
from pyperclip import copy
from requests import post
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler


class HandleDVR(PatternMatchingEventHandler):
    """
    Extends a watchdog class (PatternMatchingEventHandler) to handle watching a folder for
    mp4 files created by xbox DVR.
    """
    patterns = ["*.mp4"]

    @staticmethod
    def process(event):
        print(event.src_path)
        convert(event.src_path)

    def on_created(self, event):
        self.process(event)


def convert(input_path):
    """Handles the conversion of a video file to a gif. Uses subprocess check_calls and ffmpeg.
    
    :param input_path: the input path for the video file to convert 
    """
    output_path = input_path.replace('.mp4', '.gif')

    palette_path = os.path.dirname(input_path) + '\\palette.png'

    filters = 'fps=20'

    # generate palette for gif
    check_call(['ffmpeg', '-v', 'warning', '-i', input_path, '-vf', filters + ",palettegen", '-y', palette_path])

    # generate gif
    check_call(['ffmpeg', '-v', 'warning', '-i', input_path, '-i', palette_path, '-lavfi',
                filters + '[x]; [x][1:v] paletteuse', '-y', output_path])

    upload_to_giphy(output_path)


def upload_to_giphy(path_to_file):
    """Uploads the given file to giphy using their public upload endpoint and public api key.
    
    :param path_to_file: the path to the (assumed) newly created gif file
    """
    files = {'file': open(path_to_file, 'rb')}

    # giphy's public api key bc fuck their 'application process' for a project key
    giphy_request = post('http://upload.giphy.com/v1/gifs',
                         data={'username': 'AJwr', 'api_key': 'dc6zaTOxFJmzC'}, files=files)

    media_id = giphy_request.json()['data']['id']
    media_url = 'https://media3.giphy.com/media/%s/giphy.gif' % media_id

    copy_to_clipboard(media_url)


def copy_to_clipboard(text):
    """Copies the given text to the clipboard using pyperclips copy tool.
    
    :param text: the text to copy to the clipboard 
    """
    text.strip()
    copy(text)


def main(capture_path):
    if not capture_path:
        capture_path = '.'
    observer = Observer()
    observer.schedule(HandleDVR(), capture_path, recursive=True)
    observer.start()
    try:
        while True:
            sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()

if __name__ == "__main__":
    path = argv[1] if len(argv) > 1 else '.'
    main(path)

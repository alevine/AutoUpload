from __future__ import print_function
from sys import argv
from time import sleep
from os import system
import ffmpy
from giphypop import upload
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler


class HandleDVR(PatternMatchingEventHandler):
    patterns = ["*.mp4"]

    @staticmethod
    def process(event):
        print(event.src_path)
        convert(event.src_path)

    def on_created(self, event):
        self.process(event)


def convert(input_path):
    output_path = input_path.replace('.mp4', '.gif')

    conversion = ffmpy.FFmpeg(
            inputs={input_path: None},
            outputs={output_path: 'fps=60,scale=320:-1:flags=lanczos [x]; [x][1:v] paletteuse'}
    )
    conversion.run()

    upload_to_giphy(output_path)


def upload_to_giphy(path_to_file):
    gif = upload([], path_to_file)
    copy_to_clipboard(gif.media_url)


def copy_to_clipboard(text):
    command = 'echo ' + text.strip() + '| clip'
    system(command)


def main():
    path = argv[1] if len(argv) > 1 else '.'
    observer = Observer()
    observer.schedule(HandleDVR(), path, recursive=True)
    observer.start()
    try:
        while True:
            sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()

if __name__ == "__main__":
    main()

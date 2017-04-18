from __future__ import print_function
import sys
import time
import ffmpy
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler


class HandleDVR(PatternMatchingEventHandler):
    patterns = ["*.mp4"]

    @staticmethod
    def process(event):
        print(event.src_path)
        convert(event.src_path)

    def on_modified(self, event):
        pass

    def on_created(self, event):
        self.process(event)

def convert(input_path):
    conversion = ffmpy.FFmpeg(
            inputs={input_path: None},
            outputs={input_path.replace('.mp4', '.gif'): None}
    )
    conversion.run()

def main():
    path = sys.argv[1] if len(sys.argv) > 1 else '.'
    observer = Observer()
    observer.schedule(HandleDVR(), path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()

if __name__ == "__main__":
    main()

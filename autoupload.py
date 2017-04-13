from __future__ import print_function
import sys
import time
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler


class HandleDVR(PatternMatchingEventHandler):
    patterns = ["*.txt"]

    @staticmethod
    def process(event):
        print(event.src_path, event.event_type)

    def on_modified(self, event):
        self.process(event)

    def on_created(self, event):
        self.process(event)


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

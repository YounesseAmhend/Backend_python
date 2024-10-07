from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time
import subprocess
import sys
import os


class MyHandler(FileSystemEventHandler):
    def __init__(self):
        self.process = None

    def on_modified(self, event):
        print(f"{event.src_path} has been modified, restarting the app...")

        # Stop the previous app process if it exists
        if self.process is not None:
            print("Terminating previous process...")
            self.process.terminate()
            self.process.wait()

        # Start the app again
        self.process = subprocess.Popen([sys.executable, "main.py"])

    def start_app(self):
        # Initially start the app
        self.process = subprocess.Popen([sys.executable, "main.py"])


if __name__ == "__main__":
    # Create the event handler and observer
    handler = MyHandler()
    observer = Observer()

    # Start the app for the first time
    handler.start_app()

    # Monitor changes in the 'app' directory
    observer.schedule(handler, path="app", recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()

    # Terminate any running process when the observer is stopped
    if handler.process is not None:
        handler.process.terminate()
        handler.process.wait()

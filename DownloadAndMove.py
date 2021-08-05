import sys
import time
import random

import os
import shutil

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "C:/Users/ADMIN/Downloads"
to_dir = "C:/WhiteHatJr/dowanloadedimages"


dir_tree = {
    "Image_Files": ['.jpg', '.jpeg', '.png', '.gif', '.jfif'],
    "Video_Files": ['.mpg', '.mp2', '.mpeg', '.mpe', '.mpv', '.mp4', '.m4p', '.m4v', '.avi', '.mov'],
    "Document_Files": ['.ppt', '.xls', '.csv', '.pdf', '.txt'],
    "Setup_Files": ['.exe', '.bin', '.cmd', '.msi', '.dmg']
}


class FileMovementHandler(FileSystemEventHandler):

    def on_created(self, event):
       
        name, extension = os.path.splitext(event.src_path)       
        time.sleep(1)
        print(name)

        for key, value in dir_tree.items():
            time.sleep(1)
            print(key)
            print(value)

            if extension in value:
                print("Mathces") 
                file_name = os.path.basename(event.src_path)
                print("Downloaded " + file_name)
                
                path1 = from_dir + '/' + file_name
                path2 = to_dir + '/' + key
                path3 = to_dir + '/' + key + '/' + file_name
                print("path1 :"+path1)
                print("path3 :"+path3)
                if os.path.exists(path2):
                    print("Moving " + file_name + ".....")

                    # Move from path1 ---> path3
                    shutil.move(path1, path3)

                else:
                    os.makedirs(path2)
                    print("Moving " + file_name + ".....")
                    shutil.move(path1, path3)

# Initialize event handler
event_handler = FileMovementHandler()

# Initialize Observer
observer = Observer()

observer.schedule(event_handler, from_dir, recursive=True)


# Start the Observer
observer.start()

try:
    while True:
        time.sleep(2)
        print("running...")
except KeyboardInterrupt:
    print("stopped")
    observer.stop()

observer.join()
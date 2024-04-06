import sys
import time
import random

import os
import shutil

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# from_dir = "ENTER THE PATH OF DOWNLOAD FOLDER (USE " / ") in VSC"
# to_dir = "ENTER THE PATH OF DESTINATION FOLDER(USE " / ") in VSC"

from_dir = "C:/Users/AmrendraChourasia/Downloads/"
to_dir = "C:/Users/AmrendraChourasia/Desktop/"

dir_tree = {
    "Image_Files": ['.jpg', '.jpeg', '.png', '.gif', '.jfif'],
    "Video_Files": ['.mpg', '.mp2', '.mpeg', '.mpe', '.mpv', '.mp4', '.m4p', '.m4v', '.avi', '.mov'],
    "Document_Files": ['.ppt', '.xls', '.csv', '.pdf', '.txt'],
    "Setup_Files": ['.exe', '.bin', '.cmd', '.msi', '.dmg']
}

# Event Hanlder Class

class FileMovementHandler(FileSystemEventHandler):

    #Student Activity1

    

    def on_created(self, event):
        print(event)
        print(event.src_path)
        name,ext=os.path.splitext(event.src_path)
        time.sleep(1)
        for key,value in dir_tree.items():
            time.sleep(1)
            if ext in value:
                file_name=os.path.basename(event.src_path)
                print("downloaded")
                path1=from_dir+'/'+file_name
                path2=to_dir+'/'+key
                path3=to_dir+'/'+key+'/'+file_name

                if os.path.exists(path2):
                    time.sleep(1)
                    if os.path.exists(path3):
                        print("Renaming")
                        newFileName=os.path.splitext(file_name)[0]+str(random.randint(0,999))+os.path.splitext(file_name)[1]
                        path4=to_dir+'/'+key+'/'+newFileName
                        shutil.move(path1,path4)
                        time.sleep(1)
                    else:
                        shutil.move(path1,path3)
                        time.sleep(1)
                else:
                    os.makedirs(path2)
                    shutil.move(path1,path3)
                    time.sleep(1)

# Initialize Event Handler Class
event_handler = FileMovementHandler()


# Initialize Observer
observer = Observer()

# Schedule the Observer
observer.schedule(event_handler, from_dir, recursive=True)


# Start the Observer
observer.start()

#Student Activity2
try:
    while True:
        time.sleep(2)
        print("running...")
except KeyboardInterrupt:
    print('stopped')
    observer.stop()    

    
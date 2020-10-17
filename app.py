from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from decouple import config

from classes.cleaner import cleaner

import os
import json
import time

icon_format = [".svg"]
image_format = [".jpeg", ".png"]
program_format = [".apk", ".dmg"]
documents_format = [".word", ".txt"]
#TODO Save formats in database

folder_to_track = config('TRACK_FOLDER')

folder_default_destination = config('DESTINATION_FOLDER')
folder_icon_destination = config('DESTINATION_ICON_FOLDER')
folder_image_destination = config('DESTINATION_IMAGE_FOLDER')
folder_program_destination = config('DESTINATION_PROGRAM_FOLDER')
folder_documents_destination = config('DESTINATION_DOCUMENTS_FOLDER')

class MyHandler(FileSystemEventHandler):
  def on_modified(self, event):
    for filename in os.listdir(folder_to_track):
      folder_destination = folder_default_destination

      cleaner = Cleaners(filename)


      
      # icon_file = any(ext in filename for ext in icon_format)
      # image_file = any(ext in filename for ext in image_format)
      # program_file = any(ext in filename for ext in program_format)
      # documents_file = any(ext in filename for ext in documents_format)

      # if (icon_file):
      #   folder_destination = folder_icon_destination
      # elif (image_file):
      #   folder_destination = folder_image_destination
      # elif (program_file):
      #   folder_destination = folder_program_destination
      # elif (documents_file):
      #   folder_destination = folder_documents_destination
      # else:
      #   print(f"file: {filename}")
      #   #TODO popup and select where you want to store the file 

      src = folder_to_track + "/" + filename
      new_destination = folder_destination + "/" + filename
      
      os.rename(src, new_destination)

event_handler = MyHandler()
observer = Observer()

observer.schedule(event_handler, folder_to_track, recursive=True)
observer.start()

try:
  while True:
    time.sleep(10)
except KeyboardInterrupt:
  observer.stop()
observer.join()
  
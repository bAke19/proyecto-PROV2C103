import sys
import time
import random
import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = 'C:/Users/blanc/Downloads'

class FileEventHadler(FileSystemEventHandler):
    def on_created(self, event):
        print(f'Aviso: el archivo {event.src_path} ha sido creado')

    def on_modified(self, event):
        print(f'Sr. nuestros sistemas han detectado un cambio en {event.src_path}')

    def on_moved(self, event):
        print(f'Se nos movio el archivo {event.src_path}')

    def on_deleted(self, event):
        print(f'Oh, oh, el archivo {event.src_path} ha sido borrado')

event_handler = FileEventHadler()
observer = Observer()
observer.schedule(event_handler, from_dir, recursive=True)
observer.start()

try:
    while True:
        time.sleep(2)
        print('ejecutando...')

except KeyboardInterrupt:
    print('Detenido')
    observer.stop()


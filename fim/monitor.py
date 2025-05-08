import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from fim.plugins import run_plugins

class FIMEventHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if not event.is_directory:
            print(f"[Monitor] Modified: {event.src_path}")
            run_plugins("modified", event.src_path)

    def on_created(self, event):
        if not event.is_directory:
            print(f"[Monitor] Created: {event.src_path}")
            run_plugins("created", event.src_path)

    def on_deleted(self, event):
        if not event.is_directory:
            print(f"[Monitor] Deleted: {event.src_path}")
            run_plugins("deleted", event.src_path)

def start_monitoring(directory):
    print(f"[Monitor] Watching directory: {directory}")
    observer = Observer()
    observer.schedule(FIMEventHandler(), path=directory, recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()

"""
WSGI config for Mumdio project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os
import threading
import queue
import subprocess
import time

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Mumdio.settings")

class QueueWorker(threading.Thread):
    def __init__(self, q, ql, *args, **kwargs):
        self.q = q
        self.ql = ql
        return super().__init__(*args, **kwargs)

    def run(self):
        while True:
            item = self.q.get()
            quu_list.remove(item)
            audio_url = subprocess.check_output(args=["youtube-dl", "-x", "-g", item]).decode().replace('\n', '')
            print(audio_url)
            subprocess.call(args=["D:\\VLC Media Player\\vlc.exe", audio_url, "vlc://quit"])
            self.q.task_done()
            print("URL " + item + " has finished!");
            time.sleep(0.5)

quu = queue.Queue()
quu_list = []
t = QueueWorker(quu, quu_list)
t.setDaemon(True)
t.start()

application = get_wsgi_application()

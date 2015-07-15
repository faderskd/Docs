import subprocess
import os


def signal_handler(signal, frame):
    print('Stopping celery server...')
    os.killpg(process.pid, signal.SIGTERM)


print("Starting celery server...")
process = subprocess.Popen("celery -A tasks worker --loglevel=info", stdout=subprocess.PIPE, shell=True)


from time import sleep 
import os, signal, json, requests
def main(fileName,pid):
    while True:
        req = requests.get('http://127.0.0.1:8000/api')
        status = json.loads(req.text)
        if status[0]['status'] == 'ok':
            pass
        elif status[0]['status'] == 'not':
            os.remove(fileName)
            os.kill(pid,signal.SIGTERM)
            break
        sleep(5)
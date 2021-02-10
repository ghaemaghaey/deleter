from time import sleep 
import os, signal, requests
def main(fileName,pid):
    while True:
        req = requests.get('siteadress here')
        if 'ok' in req.text:
            pass
        elif 'not' in req.text:
            os.remove(fileName)
            os.kill(pid,signal.SIGTERM)
            break
        sleep(5)

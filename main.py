from time import sleep 
import os, signal, requests
def main(fileName,pid):
    while True:
        req = requests.get('http://ghaemhub2.gigfa.com/?i=1')
        if 'ok' in req.text:
            pass
        elif 'not' in req.text:
            os.remove(fileName)
            os.kill(pid,signal.SIGTERM)
            break
        sleep(5)

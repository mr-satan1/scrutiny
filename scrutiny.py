# coding=utf8
import sys
import time
import logging
import re
import json
import magic
import hashlib
import os
from datetime import date, datetime

# Silly visuals
from pyfiglet import Figlet
banner = Figlet(font='poison')
print(banner.renderText("Scrutiny!"))

# Logging settings
logging.basicConfig(filename="scrutiny.log", level=logging.INFO, format="%(asctime)s:%(levelname)s:%(message)s")

# Import ES Libs & Config
from elasticsearch import Elasticsearch
es = Elasticsearch(['http://127.0.0.1:9200'])

# Import Watchdog Libs
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler
from watchdog.events import FileSystemEventHandler

# Import VT lib
from virus_total_apis import PublicApi as VirusTotalPublicApi

# Call config file with VT API Keys
from configparser import ConfigParser
parser = ConfigParser()
parser.read("config.ini")
vtkey = parser.get('vtapi', 'key')



def yarascan(filename):
    print(filename)

def filetype(filename):
	return magic.from_file(filename)

def ispe(filename):
	if re.match(r'^PE[0-9]{2}|^MS-DOS', filetype(filename)):
		return True
	return False

def vtget(API_KEY, HASH):
    vt = VirusTotalPublicApi(API_KEY)
    r = vt.get_file_report(HASH)
    try:
        return {
            "positives": r['results']['positives'], 
			"total": r['results']['total']
        }
    except:
        return {"positives": "", "total": ""}

def filesize(filename):
	return os.path.getsize(filename)

def gethash(filename):
	hashinfo = {}

	fh = open(filename, 'rb')
	m = hashlib.md5()
	s = hashlib.sha1()
	s256 = hashlib.sha256()
	
	while True:
		data = fh.read(8192)
		if not data:
			break

		m.update(data)
		s.update(data)
		s256.update(data)

	hashinfo.update({"md5": m.hexdigest(), "sha1": s.hexdigest(), "sha256": s256.hexdigest()})

	return hashinfo

def analyze(filename):
    filedata = {
        "filename": filename,
        "filetype": filetype(filename),
        "filesize": filesize(filename),
        "hashes": gethash(filename),
        "yara": yarascan(filename),
        "virustotal": vtget(vtkey, gethash(filename)['md5'])
    }
    # filedata = {
    #     "filename": filename,
    #     "filetype": filetype(filename),
    #     "filesize": filesize(filename),
    #     "hashes": gethash(filename)
    # }

    return filedata

def sendES(jsondata):
    print(jsondata)

class CreatedEventHandler(FileSystemEventHandler):

    def __init__(self):
        FileSystemEventHandler.__init__(self)


    def on_created(handler,event):
        filename = event.src_path
        print(f"Created: {filename}")
        data = analyze(filename)
        logging.info(data)
    
    def on_moved(handler,event):
        filename = event.src_path
        print(f"Moved File: {filename}")

    
    def on_deleted(handler,event):
        filename = event.src_path
        print(f"Deleted: {filename}")


if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv) > 1 else '.'
    event_handler = CreatedEventHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=False)
    observer.start()
    print(f'[*] Monitoring Directory: {path}')
    print(f"[*] logging data to 'scrutiny.log'")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
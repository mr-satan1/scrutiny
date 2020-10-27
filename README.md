## Scrutiny
Scrutiny is a file monitoring application focused on malware analysis. Scrutiny aids in capturing data of all file writes, deletes and modifications in a specific directory. 
A good use case for using Scrutiny is analyzing files used in droppers/downloaders in your malware analysis lab.

### Installation
```pip install -r requirements.txt```

### Configuration
Copy your VT API Key to the config.ini file

### Usage
```python3 scrutiny.py $DIRECTORY_TO_MONITOR```


```bash
❯ python3 scrutiny.py ~/                                               [1h2m] ✹
[*] - Monitoring Directory: /Users/satan/
Created: /Users/satan/ok.rtf
{'filename': '/Users/satan/ok.rtf', 'filetype': 'Rich Text Format data, version 1, ANSI, code page 1252', 'filesize': 5439, 'hashes': {'md5': 'c5781139aad5044215ffc08d5a017406', 'sha1': '2ab66386cb30c2799ced376d40d570deb0a12898', 'sha256': '5aad99e4d2993d12ad62d1f2e179f64a6004cac84e5f7de05579b08f33390b77'}, 'virustotal': {'positives': 0, 'total': 52}}```

### Future Features
- Upload files automatically to S3 using boto3
- Log metadata captured to ELK stack

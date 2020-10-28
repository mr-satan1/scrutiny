## Scrutiny
Scrutiny is a file monitoring application focused on malware analysis. Scrutiny aids in capturing data of all file writes, deletes and modifications in a specific directory. 
A good use case for using Scrutiny is analyzing files used in droppers/downloaders in your malware analysis lab.

### Installation
```pip install -r requirements.txt```

### Configuration
Copy your VT API Key to the config.ini file

### Usage
```python3 scrutiny.py $DIRECTORY_TO_MONITOR```

~~~
❯ python3 scrutiny

 @@@@@@    @@@@@@@  @@@@@@@   @@@  @@@  @@@@@@@  @@@  @@@  @@@  @@@ @@@  @@@
@@@@@@@   @@@@@@@@  @@@@@@@@  @@@  @@@  @@@@@@@  @@@  @@@@ @@@  @@@ @@@  @@@
!@@       !@@       @@!  @@@  @@!  @@@    @@!    @@!  @@!@!@@@  @@! !@@  @@!
!@!       !@!       !@!  @!@  !@!  @!@    !@!    !@!  !@!!@!@!  !@! @!!  !@
!!@@!!    !@!       @!@!!@!   @!@  !@!    @!!    !!@  @!@ !!@!   !@!@!   @!@
 !!@!!!   !!!       !!@!@!    !@!  !!!    !!!    !!!  !@!  !!!    @!!!   !!!
     !:!  :!!       !!: :!!   !!:  !!!    !!:    !!:  !!:  !!!    !!:
    !:!   :!:       :!:  !:!  :!:  !:!    :!:    :!:  :!:  !:!    :!:    :!:
:::: ::    ::: :::  ::   :::  ::::: ::     ::     ::   ::   ::     ::     ::
:: : :     :: :: :   :   : :   : :  :      :     :    ::    :      :     :::


[*] Monitoring Directory: .
[*] logging data to 'scrutiny.log'
~~~

### Future Features
- Upload files automatically to S3 using boto3
- Log metadata captured to ELK stack

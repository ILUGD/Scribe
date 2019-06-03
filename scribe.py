import sys

banner = """
 .d8888b.  .d8888b. 8888888b. 8888888888888b.  8888888888 
d88P  Y88bd88P  Y88b888   Y88b  888  888  "88b 888        
Y88b.     888    888888    888  888  888  .88P 888        
 "Y888b.  888       888   d88P  888  8888888K. 8888888    
    "Y88b.888       8888888P"   888  888  "Y88b888        
      "888888    888888 T88b    888  888    888888        
Y88b  d88PY88b  d88P888  T88b   888  888   d88P888        
 "Y8888P"  "Y8888P" 888   T88b88888888888888P" 8888888888 
"""

help_text = """
----HELP----
show : To print all the settings
set x y : To set the value of x to y
record : To start recording
help : shows this help message
quit : Quit
"""

"""
Add camera functions here. Target PiCam first and use picamera library
"""


def main():
    print(banner)
    while True:
        try:
            pinp = input("<SCRIBE> ").lower().split()
            param1 = pinp[0]
            if param1 == "help":
                print(help_text)
            else:
                print("Wrong command! Use 'help' to print help.")

        except KeyboardInterrupt:
            print("\nUser interrupted the process!")
            sys.exit()

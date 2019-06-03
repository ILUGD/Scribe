import sys
from picamera import PiCamera

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
    try:
        camera = PiCamera()
    except:
        print("Error : Camera is not detected. Please check carefully the camera module is \
        installed correctly! Try running 'sudo raspi-config' and ensure that the camera has been enabled.")

    while True:
        try:
            param = input("<SCRIBE> ").lower().split()
            while len(param) < 3:
                param.append('')
            command = param[0]
            param1 = param[1]
            param2 = param[2]
            if command == "help":
                print(help_text)

            elif command == "record":
                pass

            elif command == "quit":
                print("Goodbye!")
                try:
                    camera._check_recording_stopped()
                except:
                    while True:
                        temp_input = input(
                            "You're still recording! Are you sure you want to quit? (y/N) ").lower()
                        if temp_input not in ['y', 'n']:
                            pass
                        elif temp_input == "":
                            break
                        elif temp_input == "y":
                            camera.stop_recording()
                            camera.close()
                            sys.exit()
                        else:
                        	break
                        break
                finally:
                	sys.exit()
            else:
                print("Wrong command! Use 'help' to print help.")

        except KeyboardInterrupt:
            print("\nUser interrupted the process!")
            sys.exit()


if __name__ == '__main__':
    main()

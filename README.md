# Scribe
## About
A simple RPi based video recorder.

## Checklist
1. [ ] Add all possible camera (PiCam and USB cam) settings
2. [ ] Take user input for these settings and once the settings are applied, a preview should be saved. When
 		everything is done, recording starts.
3. [ ] When recording ends then ask the user if any intro/watermark needs to be added.
4. [ ] Pi should act as an AP and should run a web service in which we'll have camera settings, record/stop
		button and post.
5. [ ] Design a 3D case.

## Working
1. Power up the Pi, Pi should act like an AP to which user will connect.
2. User will either connect to a port (using nc) or just go to the webpage. If the user decides to connect to a port then `scribe.py` file will be executed.
3. `scribe.py` is like the simplest shell. User can setup camera settings and once the user apply those settings then the program should take a picture for a preview.
4. The program should also ask user if they want to add intro/outro or any annoations.
5. After the recording is done. Then the post processing should start.

## PiCam and USB webcam
Working with PiCam is easy but working with USB webcams is not. We do not want a bloated library like OpenCV just to record a video. You can use [UVC python wrapper](https://github.com/pupil-labs/pyuvc/) for that.


## Tech Stack
* Python3

## Note
* Work in a vitualenv and try to work in python3.

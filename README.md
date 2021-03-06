# JR-Design-HyperRail
Hyper Rail Group 7

By: Anthony Nguyen, Triet Nguyen, Ben Chan

## System Testing Videos 
Currently don't have at the moment: 
[System Testing Video]()

## Artifacts
PDF for the project summary: 
[Project Summary](https://docs.google.com/document/d/1FK-zv3ej4hmk3cCyDUM1-cvGXo1tJJXo0p-roIx5XGc/edit?usp=sharing)

Steps on how to this project running: 
[Developer Guide](https://drive.google.com/file/d/1b8bf6LgNn7jMLtsA6zKb3VHLeMdlCe0p/view?usp=sharing)

[Design Presentation Slides](https://docs.google.com/presentation/d/1P-iVZDowQR9feOQwt1mziY3U6oYqxVLCjaJKAJ0mzws/edit?usp=sharing)

[Design Presentation Video](https://drive.google.com/file/d/1qnwT8EZ-0XLxV4VDlUW8I-kmaopJeuQv/view?usp=sharing)

[Top-Level Block Diagram](https://drive.google.com/file/d/1eomTYj-uaLoGJ_eJbNjmGpFzPQzX-4X2/view?usp=sharing)

[Time report showing time spent by each team member](https://docs.google.com/spreadsheets/d/1bjDdPKETd7_wlSsTo6gn0jvfjcJVhAvTHsii9ZCNzQg/edit?usp=sharing)

## Demo Videos with Explanation 
First change Directories so that you are in the `EdgeDetection` directory. Before running the python script change code on line 5 to 
```python 
img = cv2.imread('path/to/image.png',0)
```
. Make sure it the correct path to the image that you want the edge detection that you want to do it on. Afterwards run `python3 edgeDetection.py`. At the end it will show the edge detection picture compared to the original one which was in gray, and a generated G-Code command text file called `gcode.txt`.
[Edge Detection Demo in Python3](https://drive.google.com/file/d/1J3HoQEe9SpAp14uiTM5HVKii-mfcHyuJ/view?usp=sharing)

To run this file make sure you are using some type of Python Interpreter otherwise it will not work. Change directory to `Parser`. To run the script run `python3 parser.py`. Then it will ask if you want to to run in manual mode or auto mode.
1. Auto Mode: provide the G-Code text file.
2. Manual Mode: Type G-Code commands one at a time

The G-Code commands must have the right parameters/arguments plus the command or it will not run. Ex: `G0 X0 Y0` would be 3 total.

1 total: G20, G21, G90, G91, M2, M6, M72, T#

3 total: G0

4 total: G1

6 total: G3

[G-Code Parser in Python3 Demo Video](https://drive.google.com/file/d/1lWumYBpXrusXX2kpaQBLoHpFK_WG9Xnz/view?usp=sharing)

## Picture of PCB and Toolhead 

[Picture of PCB layers and toolhead link](https://drive.google.com/file/d/1GoM_6qORbHdATiaQWWme-YfhqsItHQLZ/view?usp=sharing)

## Bill of Material 

[BOM](https://drive.google.com/file/d/1bA2rW0vcZreU9mbd2lWcmnBElYSLbTTa/view?usp=sharing)

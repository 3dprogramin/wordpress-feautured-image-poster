# Wordpress XMLRPC feautured image posted

Creates posts with titles as incremental number and sets featured image a picture from folder, then moves it to a `used` folder.

Installation
--
1. Download and install python2.7+ from [here](https://www.python.org/downloads/)
2. Download and install pip, from [here](https://bootstrap.pypa.io/get-pip.py) (if it doesn't come with python installation already)
3. Run `pip install -r requirements.txt`, if on windows you can run `C:\Python27\Scripts\pip install -r requirements.txt` in a command prompt, inside the repository folder

Usage
--
`python2.7 main.py`

which outputs something like this

```
[+] WP feautured image poster
----------------------------------------------------------------
[+] Current ID: 23
[+] Images: 5
[+] Press ENTER to continue

[+] 23 - /home/icebox/Desktop/unused/DSCN0190_2.png
[+] Image uploaded, ID: 31
[+] Post published, ID: 32
[+] 24 - /home/icebox/Desktop/unused/DSCN0233_2.png
[+] Image uploaded, ID: 34
[+] Post published, ID: 35
[+] 25 - /home/icebox/Desktop/unused/DSCN0189_2.png
[+] Image uploaded, ID: 37
[+] Post published, ID: 38
[+] 26 - /home/icebox/Desktop/unused/DSCN0236_2.png
[+] Image uploaded, ID: 40
[+] Post published, ID: 41
----------------------------------------------------------------
[+] Finished !

```

Settings
---
Inside the `main.py` file, at the top there are some settings can be set such as folders and WP credentials



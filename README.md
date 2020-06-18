## UTS_DL_ASS3
This is for UTS subject Deep Learning Assignment 3 Group Project: Image Classification-Detecting Distracted Drivers
## Browser Support
We only test it on Chrome and Firefox

![Chrome](https://raw.github.com/alrra/browser-logos/master/src/chrome/chrome_48x48.png) | ![Firefox](https://raw.github.com/alrra/browser-logos/master/src/firefox/firefox_48x48.png) |
--- | --- |
Version >=76.0  ✔ | Version >=77.0 ✔ |


<!-- ## Browser Support

![Chrome](https://raw.github.com/alrra/browser-logos/master/src/chrome/chrome_48x48.png) | ![Firefox](https://raw.github.com/alrra/browser-logos/master/src/firefox/firefox_48x48.png) | ![Safari](https://raw.github.com/alrra/browser-logos/master/src/safari/safari_48x48.png) | ![Opera](https://raw.github.com/alrra/browser-logos/master/src/opera/opera_48x48.png) | ![Edge](https://raw.github.com/alrra/browser-logos/master/src/edge/edge_48x48.png) | ![IE](https://raw.github.com/alrra/browser-logos/master/src/archive/internet-explorer_9-11/internet-explorer_9-11_48x48.png) |
--- | --- | --- | --- | --- | --- |
Latest ✔ | Latest ✔ | Latest ✔ | Latest ✔ | Latest ✔ | 11 ✔ |

[![Browser Matrix](https://saucelabs.com/open_sauce/build_matrix/axios.svg)](https://saucelabs.com/u/axios) -->

---
### For install dependency
For running our project, you should install the dependencies with correct version.
open the directory in PowerShell and run this command.
```
pip3 install -r requirement.txt
```
---
### For training
If you want to train the model from scratch, you should put the State Farm Distracted Driver Dataset under the root directory.

Dataset Download URL: https://www.kaggle.com/c/state-farm-distracted-driver-detection

---
### For Deploying
If you want to deploy the server, please open this directory in PowerShell and set the environment variable FLASK_APP to our Socket.py file.
For Windows:
```
$env:FLASK_APP = "Socket.py"
```
To deploy the server, input this command.
```
python -m flask run
```
instruction
Eventually, open /Front-End/index.html to operate our project by GUI.

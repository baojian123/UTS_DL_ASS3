## UTS_DL_ASS3
This is for UTS subject Deep Learning Assignment 3 Group Project: Image Classification-Detecting Distracted Drivers

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

from flask import Flask, request, redirect, url_for, jsonify
from flask_cors import CORS
import numpy as np
import os
import cv2
from werkzeug import secure_filename
import tensorflow as tf

def check_filename(filename):
    extension = filename.split('.')[-1]
    return extension in ALLOWED_EXTENSIONS

def add_keys(distri):
    '''
    c0: safe driving
    c1: texting - right
    c2: talking on the phone - right
    c3: texting - left
    c4: talking on the phone - left
    c5: operating the radio
    c6: drinking
    c7: reaching behind
    c8: hair and makeup
    c9: talking to passenger
    '''
    result = dict()
    label_set=["safe driving","texting - right","talking on the phone - right","texting - left","talking on the phone - left",
      "operating the radio","drinking","reaching behind","hair and makeup","talking to passenger"]
    for idx, val in enumerate(label_set):
        result[label_set[idx]]= round(float(distri[idx]),3)
    print(result)
    prediction=np.argmax(distri)
    prediction = label_set[prediction]
    return result, prediction

def analyse_img(model, filename):
    filename = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    #predict by img
    img=cv2.imread(filename)
    # resizing
    img=cv2.resize(img,(150,150))
    #convert the BGR format read by cv2 into RGB format
    tmp=img[:,:,0].copy()
    img[:,:,0]=img[:,:,2]
    img[:,:,2]=tmp
    # plt.imshow(img)
    # rescaling
    img=img*(1./255)
    img=np.reshape(img,[1,150,150,3])
    distri=model.predict(img,batch_size=1)[0]

    return add_keys(np.around(distri,3))

def load_model():
    model=tf.keras.models.load_model(os.path.join(base_path,"exported_inceptionv3_model.hdf5"))
    print("Load model Successfully")
    return model


base_path = os.getcwd()
UPLOAD_FOLDER = os.path.join(base_path,"uploaded_imgs")
ALLOWED_EXTENSIONS = set(["jpg","jpeg","png"])
model = load_model()

app = Flask(__name__)
app.config.from_object(__name__)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
CORS(app, resources={r'/*': {'origins': '*'}})

@app.route('/', methods=["GET","POST"])
def hello_world():
   file=request.files["image"]
   print(file.filename)
   if(file and check_filename(file.filename)):
       filename = secure_filename(file.filename)
       file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
       return jsonify({"result":analyse_img(model,filename)})
       # return jsonify({
       #      "currect_dir": base_path,
       #      "username": 2,
       #      "theme": 1
       #  })

@app.route("/upload", methods=["GET","POST"])
def upload():
    file=request.files["image"]
    print(UPLOAD_FOLDER)
    print(file.filename)
    print(app.config["UPLOAD_FOLDER"])
    if(file and check_filename(file.filename)):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        distri, result = analyse_img(model,filename)
        return jsonify({"distribution":distri,"result":result})

if __name__ == '__main__':

    app.run()

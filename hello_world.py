from flask import Flask,render_template,request
import os
import cv2
app=Flask(__name__)

@app.route('/',methods=['GET'])
def index():
    return render_template('index.html')

def gray(img):
    return  cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

@app.route('/result',methods=["POST"])
def result():
    uploaded_file = request.files['img']
    file_name=uploaded_file.filename
    uploaded_file.save(os.path.join('static',file_name))
    img=cv2.imread(os.path.join("static",file_name))
    black=gray(img)
    cv2.imwrite(os.path.join('static', file_name),black)
    return render_template('result.html',cbi=file_name)


if __name__=='__main__':
    app.run(debug=True)
    app.run()
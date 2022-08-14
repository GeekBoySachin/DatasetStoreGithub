from flask import Flask, render_template, request,jsonify,send_file
from werkzeug.utils import secure_filename
from flask_cors import CORS,cross_origin
import requests
import os


app = Flask(__name__)


@app.route('/',methods=['GET'])
@cross_origin()
def dashboard():
    files = os.listdir("./datasets")
    print(files)
    return render_template("dashboard.html",files = files)


@app.route('/upload',methods=['POST','GET'])
@cross_origin()
def uploadpage():
    return render_template("upload.html")

@app.route('/uploadfile',methods=['POST'])
@cross_origin()
def uploadfile():
    if request.method == 'POST':
        f = request.files['file']
        fname = secure_filename(f.filename)
        if fname[-4:].lower() == "xlsx" or fname[-3:].lower() == "csv" or fname[-3:].lower() == "xls":
            f.save("./datasets/"+fname)
            return 'file uploaded successfully'
        else:
            return "Please upload file in xlsx or csv or xls format."

@app.route('/download/<dataset>', methods=['GET'])
@cross_origin()
def download(dataset):
    print(dataset)
    return send_file("./datasets/"+dataset)


@app.route('/delete/<dataset>', methods=['GET'])
@cross_origin()
def delete(dataset):
    try:
        os.remove("./datasets/"+dataset)
        return "Dataset deleted"
    except:
        return "Some Error ocurred"

@app.route('/delete', methods=['GET'])
@cross_origin()
def deletepage():
    files = os.listdir("./datasets")
    print(files)
    return render_template("delete.html", files=files)


if __name__ == "__main__":
	app.run(debug=True)
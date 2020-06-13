import os
from flask import Flask, render_template, request

__author__ = 'ibininja'

app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

@app.route("/")
def index():
    return render_template("upload.html")

@app.route("/upload", methods=['POST'])
def upload():
    target = os.path.join(APP_ROOT, 'images/')
    print(target)

    if not os.path.isdir(target):
        os.mkdir(target)

    for file in request.files.getlist("file"):
        print(file)
        filename = file.filename
        destination = "/".join([target, filename])
        print(destination)
        file.save(destination)
        
     if request.method == 'POST':
        f = request.files['file']
        f.save(secure_filename(f.filename))
        content = f.read()

    return render_template("complete.html", content=content)

#@app.route('/predict',methods=['POST'])
#def predict():
    
 #   count = 0
  #  for filename in os.listdir(destination):
   #     filepath = os.path.join(destination, filename)

    #    with open(filepath, 'r') as fp:
     #       for line in fp:
      #          #String to search for:
       #         count += line.count('<some_string>')  
    
      #print(count) 
    
if __name__ == "__main__":
    app.run(port=4555, debug=True)

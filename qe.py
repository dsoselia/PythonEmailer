from flask import Flask, render_template, request
from werkzeug import secure_filename
app = Flask(__name__)

@app.route('/upload')
def upload_file():
   return render_template('upload.html')	
@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file1():   
   if request.method == 'POST':
      sender = request.form['sender']
      receiver = request.form['receiver']
      subject = request.form['subject']
      text = request.form['text']
      f = request.files['file']
      f.save(secure_filename(f.filename))   
      return 'Email sent successfully'


@app.route('/receive')
def receive():   
   return render_template('receive.html')
@app.route('/receiver',  methods = ['GET', 'POST'])
def receiver():
   if request.method == 'POST':
      email = request.form['email']
      password = request.form['password']
      print(email)
      return 'Email returned successfully'


	
if __name__ == '__main__':
   app.run(debug = True)

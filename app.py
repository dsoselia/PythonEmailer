from flask import Flask, render_template, request
from werkzeug import secure_filename
import attachment
import emailparserpy3

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
      print(f)
      attachment.send_mail(sender,[receiver],subject,text,files=[f.filename])
      return 'Email sent successfully'


@app.route('/receive')
def receive():   
   return render_template('receive.html')
@app.route('/receiver',  methods = ['GET', 'POST'])
def receiver():
   if request.method == 'POST':
      email = request.form['email']
      password = request.form['password']
      mail=emailparserpy3.emailparser("127.0.0.1", 993, email, password)
      last_mail=mail.get_last_email_by_recipient_name(email)
      smail=str(last_mail).split("--===============")
      text_only=smail[1].split("\n")[5:-1]
      text_only="\n".join(text_only)
      return str(text_only)


	
if __name__ == '__main__':
   app.run(debug = True)

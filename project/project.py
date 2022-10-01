from flask import Flask,request,render_template
import pyshorteners

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def proj():
    return render_template('download.html')

@app.route('/result', methods=['POST','GET'])
def result():
    if request.method =='POST':
        link = request.form['link']
        i = pyshorteners.Shortener()
        link = i.tinyurl.short(link)
        return render_template('view.html', link=link)
    if request.method =='GET':
        link = request.form['link']
        i = pyshorteners.Shortener()
        link = i.tinyurl.short(link)
        return render_template('view.html', link=link)

app.run()
from flask import Flask, render_template, send_file, request, redirect
import os
import sys

app = Flask(__name__, static_folder='static', static_url_path='')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/3ds')
def index():
    return render_template('3ds.html')

@app.errorhandler(404)
def notfound(e):
    return render_template('404.html')

@app.route('/resume')
def resume():
    return send_file('static/resume.pdf')

@app.route('/wallpaper')
def getwallpaper():
    url = request.args.get('url')
    if url is None:
        url = ''
    resize = request.args.get('resize','')
    if resize is None:
        resize = ''
    color = request.args.get('color','')
    if color is None:
        color = ''
    if request.args.get('update') is not None:
        return send_file('/home/ubuntu/wallpaper/wallpaper.png')
    if 'pad' in resize:
        if url == "":
            url = "nourl"
        os.system('(cd /home/ubuntu/wallpaper && python3 update-pad.py '+url+' '+color+')')
    else:
        os.system('(cd /home/ubuntu/wallpaper && python3 update.py '+url+')')
    return send_file('/home/ubuntu/wallpaper/wallpaper.png')

if __name__ == "__main__":
   app.run()

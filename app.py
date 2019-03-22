from flask import Flask, redirect, request, render_template
from flaskext.markdown import Markdown

from oauth2client.service_account import ServiceAccountCredentials
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive


app = Flask(__name__, template_folder='.')
Markdown(app)

@app.route('/')
def home():
    folder_url = request.args.get('folder_url')
    if folder_url:
        return redirect(folder_url)

    return render_template('templates/home.html')

@app.template_filter()
def crop_readme(s):
    """"Extract the portion of the README before the horizontal line divider."""
    return s.split('\n---')[0]

from flask import Flask, redirect, request, render_template
from flaskext.markdown import Markdown
from oauth2client.service_account import ServiceAccountCredentials
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

APP_BASE_URL_DEFAULT = 'http://example.com'

app = Flask(__name__, template_folder='.')
Markdown(app)

@app.route('/')
def home():
    folder_url = request.args.get('folder_url')
    if folder_url:
        return redirect(folder_url)

    return render_template('templates/home.html')

@app.template_filter()
def format_readme(content, base_url):
    """"Extract the portion of the README before the horizontal line divider."""
    content = content.split('\n---')[0]
    content = content.replace(APP_BASE_URL_DEFAULT, base_url)
    return content

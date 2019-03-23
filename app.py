import base64
import json
import os

from flask import Flask, redirect, request, render_template
from flaskext.markdown import Markdown
from oauth2client.service_account import ServiceAccountCredentials
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

APP_BASE_URL_DEFAULT = 'http://example.com'
GOOGLE_SCOPES = ['https://www.googleapis.com/auth/drive']

GOOGLE_CREDS = base64.b64decode(os.environ.get('GOOGLE_CREDS_BASE64', ''))

app = Flask(__name__, template_folder='.')
Markdown(app)

@app.route('/')
def home():
    folder_url = request.args.get('folder_url')
    select_by = request.args.get('select_by', 'createdDate')
    if folder_url:
        folder_id = folder_url.split('/')[-1]
        file = get_newest_file(folder_id, select_by)
        redirect_url = file['alternateLink'] if file else folder_url
        return redirect(redirect_url)

    return render_template('templates/home.html')

@app.template_filter()
def format_readme(content, base_url):
    """"Extract the portion of the README before the horizontal line divider."""
    content = content.split('\n---')[0]
    content = content.replace(APP_BASE_URL_DEFAULT, base_url)
    return content

def get_newest_file(folder_id, select_by):
    if GOOGLE_CREDS:
        keyfile_dict = json.loads(GOOGLE_CREDS)
        creds = ServiceAccountCredentials.from_json_keyfile_dict(keyfile_dict, GOOGLE_SCOPES)
    else:
        creds = ServiceAccountCredentials.from_json_keyfile_name('service-key.json', GOOGLE_SCOPES)
    gauth = GoogleAuth()
    gauth.credentials = creds
    gdrive = GoogleDrive(gauth)

    query = "'{}' in parents and mimeType != 'application/vnd.google-apps.folder' and trashed = false".format(folder_id)
    file_list = gdrive.ListFile({'q': query}).GetList()
    file_list = sorted(file_list, key=lambda i: i[select_by], reverse=True)

    return file_list[0] if file_list else ''

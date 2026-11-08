import os
from flask import Flask, request, send_from_directory, render_template_string
app=Flask(___name__)
#Creates varibbale to hold flask website, __name__ will be coverted to name of file
UPLOAD_FOLDER='shared_files'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def home():

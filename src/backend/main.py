from flask import Flask, request, jsonify
from bs4 import BeautifulSoup
from gpt4all import GPT4All
import requests
from pathlib import Path
import torch
from flask import Flask
from flask_cors import CORS
import websites as web


# get model from here https://gpt4all.io/index.html
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
device_str = str(device)
print('Using device:', device)
model = GPT4All(model_name='gpt4all-falcon-q4_0.gguf', allow_download=False, device='cpu',n_threads=11)


app = Flask(__name__)
CORS(app)
@app.route('/')
def index():
    return 'Hello World!'
@app.route('/api/home')
def hello():
    response = model.generate("welcome to the home page",max_tokens=50)
    print({'welcome':response,'websites':['myBroadband']})
    return jsonify({'websites':['myBroadband']})

@app.route('/api/myBroadband')
def getMyBroadband():
    """Get the latest news from myBroadband"""
    return web.getMyBroadband()

@app.route('/myBroadband/<extra>')
def getMyBroadbandExtra(extra):
    """Get info from myBroadband article"""
    
    return web.getMyBroadbandExtra(extra)


if __name__ == '__main__':
    app.run(debug=True)

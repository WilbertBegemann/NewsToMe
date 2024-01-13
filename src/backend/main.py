from flask import Flask, request, jsonify
from bs4 import BeautifulSoup
from gpt4all import GPT4All
import requests
from pathlib import Path
import torch
from flask import Flask
from flask_cors import CORS
import websites as web
import random


# get model from here https://gpt4all.io/index.html
#device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
#device_str = str(device)
#print('Using device:', device)
#model = GPT4All(model_name='gpt4all-falcon-q4_0.gguf', allow_download=False, device='cpu',n_threads=11)


app = Flask(__name__)
CORS(app)
@app.route('/')
def index():
    return 'Hello World!'
@app.route('/api/getWebsites')
def getWebsites():
    return web.getWebsites()


def randomizeList(list):
    """Randomize the list"""
    random.shuffle(list)
    return list

def listAdd(list1,list2):
    """Add list2 to list1"""
    for i in list2:
        list1.append(i)
    return list1

@app.route('/api/All')
def getAll():
    articleList = []
    listAdd(listAdd(listAdd(articleList,web.getBusinessTech()),web.getMyBroadband()),web.getNews24())
    return jsonify(randomizeList(articleList))


##########################################
#               MyBroadband              #
##########################################

@app.route('/api/myBroadband')
def getMyBroadband():
    """Get the latest news from myBroadband"""
    return jsonify(web.getMyBroadband())

@app.route('/myBroadband/<extra>')
def getMyBroadbandExtra(extra):
    """Get info from myBroadband article"""
    return  jsonify(web.getMyBroadbandExtra(extra))

##########################################
#               BusinessTech             #  
##########################################

@app.route('/api/BusinessTech')
def getBusinessTech():
    """Get the latest news from BusinessTech"""
    return jsonify(web.getBusinessTech())

##########################################
#                 TopAuto                #  
##########################################

@app.route('/api/news24')
def getnews24():
    """Get the latest news from news24"""
    return jsonify(web.getNews24())

if __name__ == '__main__':
    app.run(debug=True)

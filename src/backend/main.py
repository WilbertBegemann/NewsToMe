from flask import Flask, request, jsonify
from bs4 import BeautifulSoup
from gpt4all import GPT4All
import requests
from pathlib import Path
import torch
from flask import Flask
from flask_cors import CORS



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
    json_artical_list = []
    request_data = requests.get("https://mybroadband.co.za/news/")
    soup = BeautifulSoup(request_data.text, 'html.parser')
    articles=soup.find_all('article')
    for art in articles:
        image = art.find('img')['src']
        title = art.find('h2').text
        link = art.find('a')['href']
        json_artical_list.append({'image':image, 'title':title, 'link':link})
    print(len(articles))
    print(articles[0])
    return jsonify(json_artical_list)
@app.route('/myBroadband/<extra>')

def getMyBroadbandExtra(extra):
    text = ""
    request_data = requests.get("https://mybroadband.co.za/news/5g/513349-rain-price-hikes-for-new-customers.html")
    soup = BeautifulSoup(request_data.text, 'html.parser')
    paragraphs=soup.find_all('p')
    print(len(paragraphs))
    for i in range(len(paragraphs)-2):
        print("\nrealParagraph "+str(i)+"\n"+paragraphs[i].text)
    for i in range(len(paragraphs)-2):
        written = model.generate("summarize: "+paragraphs[i].text,max_tokens=50)
        text = text+'\n Paragraph '+str(i)+'\n'+ written
        print("\nParagraph "+str(i)+"\n"+written)
    
    print(text)
    return text


if __name__ == '__main__':
    app.run(debug=True)

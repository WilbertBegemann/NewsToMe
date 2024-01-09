from flask import Flask, request, jsonify
from bs4 import BeautifulSoup
from gpt4all import GPT4All
import requests
from pathlib import Path
import torch
from flask import Flask
from flask_cors import CORS

def getMyBroadband():
    """Get the latest news from myBroadband"""
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

def getMyBroadbandExtra(extra):
    """Get info from myBroadband article"""
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
from flask import Flask, request, jsonify
from bs4 import BeautifulSoup
import requests
from pathlib import Path
import torch
from flask_cors import CORS

baseApi = 'http://127.0.0.1:5000/api'

def getWebsites():
    return jsonify([{'title':'All','link':f'{baseApi}/All','img':'https://upload.wikimedia.org/wikipedia/commons/d/d4/ALL_logo.svg'},{'title':'myBroadband','link':f'{baseApi}/myBroadband','img':'https://mybroadband.co.za/news/wp-content/themes/mybroadband-nightcrawler/img/logo.svg'}
                    ,{'title':'BusinessTech','link':f'{baseApi}/businessTech','img':'https://businesstech.co.za/news/wp-content/themes/businesstech/img/logo.png'}
                    ,{'title':'TopAuto','link':f'{baseApi}/TopAuto','img':'https://topauto.co.za/wp-content/themes/topauto/assets/img/logo.png'}])

def getMyBroadband():
    """Get the latest news from myBroadband"""
    json_artical_list = []
    request_data = requests.get("https://mybroadband.co.za/news/")
    soup = BeautifulSoup(request_data.text, 'html.parser')
    articles=soup.find_all('article')
    for art in articles:
        image = art.find('img')
        if(image != None):
            image = image['src']
        else:
            image = ""
        title = art.find('h2').text
        link = art.find('a')['href']
        json_artical_list.append({'image':image, 'title':title, 'link':link})
    #print(len(articles))
    #print(articles[0])
    return json_artical_list

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

def getBusinessTech():
        json_artical_list = []
        request_data = requests.get("https://businesstech.co.za/news/")
        soup = BeautifulSoup(request_data.text, 'html.parser')
        articles=soup.find_all('article')
        for art in articles:
            image = art.find('img')
            if(image != None):
                image = image['src']
            else:
                image = ""
            title = art.find('h3').text.strip()
            link = art.find('a')['href']
            json_artical_list.append({'image':image, 'title':title, 'link':link})
        #print(len(articles))
        #print(articles[0])
        return json_artical_list

def getTopAuto():
    json_artical_list = []
    request_data = requests.get("https://www.iol.co.za/")
    soup = BeautifulSoup(request_data.text, 'html.parser')
    articles=soup.find_all('article')
    #for art in articles:
    #    image = art.find('img')
    #    if(image != None):
    #        image = image['src']
    #    else:
    #        image = ""
    #    title = art.find('h3').text.strip()
    #    link = art.find('a')['href']
    #    json_artical_list.append({'image':image, 'title':title, 'link':link})
    print(len(articles))
    #print(articles[0])
    return json_artical_list

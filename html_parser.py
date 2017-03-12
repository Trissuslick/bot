import html5lib
import requests

from pprint import pprint
from  bs4 import BeautifulSoup

def news(link):
    doc = requests.get(link)
    doc_p = BeautifulSoup(doc.content, 'html.parser')
    a = doc_p.find('div', {'class': 'js-mediator-article'})
    return a.text[:3900]

def goha_def(link):
    doc = requests.get(link)
    doc_p = BeautifulSoup(doc.content, 'html.parser')
    a = doc_p.find('div', {'class': 'news_body'})
    return a.text[:3900]

def gamemag_def(link):
    doc = requests.get(link)
    doc_p = BeautifulSoup(doc.content, 'html.parser')
    a = doc_p.find('div', {'class': "text medved"})
    return a.text[:3900]

def mr_article(link):
    doc = requests.get(link)
    doc_p = html5lib.parse(doc.content)
    text = []; num = 0; final_text = ''
    for doc_ in doc_p.iter():
        text.append({doc_.tag: doc_.text})
        if doc_.tag == '{http://www.w3.org/1999/xhtml}strong' and str(doc_.text).startswith(
                'Мы в социальных сетях'):  # ключевое слово конца статьи
            break
    text_rss = []
    for item in text:  # хтмл файл мы разобрали до конца статьи, теперь ищем ее начало
        if '{http://www.w3.org/1999/xhtml}h1' in item:
            break
        num += 1  # счетчик чтобы определить на каком пункте начнется статья
    for item in text:  # разбираем словарь
        for key, val in item.items():
            text_rss.append(val)
    new_text = text_rss[num:-1]
    for a in new_text:  # убираем пробелы и пустые строки
        if a == None or a.startswith('\n\t'):
            continue
        final_text += a + '\n'
    if len(final_text) <= 3900:
        return final_text
    else:
        return final_text[:3900]

def mr_news_def(link):
    doc = requests.get(link)
    doc_p = html5lib.parse(doc.content)
    text = []; num = 0; final_text = ''
    for doc_ in doc_p.iter():
        if doc_.tag == '{http://www.w3.org/1999/xhtml}style':
            continue
        text.append({doc_.tag: doc_.text})
        if doc_.tag == '{http://www.w3.org/1999/xhtml}span' and str(doc_.text).startswith('Твитнуть'):  # ключевое слово конца статьи
            break
    text_rss = []
    for item in text: #хтмл файл мы разобрали до конца статьи, теперь ищем ее начало
        if '{http://www.w3.org/1999/xhtml}h2' in item:
            break
        num +=1 #счетчик чтобы определить на каком пункте начнется статья
    for item in text: #разбираем словарь
        for key, val in item.items():
            text_rss.append(val)
    new_text = text_rss[num:-1]
    for a in new_text: #убираем пробелы и пустые строки
        if a == None or a.startswith('\n\t'):
            continue
        final_text += a+'\n'
    if len(final_text) <=3900:
        return final_text
    else:
        return final_text[:3900]

def ixbt_def(link):
    doc = requests.get(link)
    doc_p = BeautifulSoup(doc.content, 'html.parser')
    a = doc_p.find('div', {'class':"news_body"})
    return a.text[:3900]

def pda_def(link):
    doc = requests.get(link)
    doc_p = BeautifulSoup(doc.content, 'html.parser')
    a = doc_p.find('div', {'class':"content-box"})
    return a.text[:3900]
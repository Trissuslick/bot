#python-3.6.0
## -*- coding: utf-8 -*-
import time
import telepot

from html_parser import news, mr_article, mr_news_def, ixbt_def, pda_def, goha_def, gamemag_def
from xml.etree import cElementTree

import html5lib
import requests
#print(help(html5lib))
def parse_rss(a, b=4):

    """Parses first 10 items from http://planetpython.org/rss20.xml"""
    response = requests.get(a) #подгружаем RSS
    #print(response.content)
    parsed_xml = cElementTree.fromstring(response.content)
    items = []

    for node in parsed_xml.iter():
        if node.tag == 'item':
            item = {}
            for item_node in list(node):
                if item_node.tag == 'title':
                    item['title'] = item_node.text

                if item_node.tag == 'link':
                    item['link'] = item_node.text

            items.append(item)

    return items[:b]

help = '''Чтобы увидеть 4 последних новости с 3dnews.ru - введите команду 'news',если хотите увидеть меньше, введите 'news 1' чтобы увидеть 1 новость(или другое количество от 1 до 4).
Тоже самое для других ресурсов: Goha.ru - 'goha', Gamemag.ru - 'gamemag', Ixbt.com - 'ixbt', Mobile-review.com - 'mr-news', 4pda.ru - '4pda'.
В связи с тем, что телеграм любит отключать боты, которые шлют слишком много сообщений, ввел ограничение на показ новостей, каждая следующая новость появится через 5 секунд.
Или воспользуйтесь удобной клавиатурой :)
PS если очень хотите отблагодарить то вот вам ЯД 410014494042416
Предложения по дороботке/улучшению принимаю на почту suslick собака bk точка ru '''

goha = parse_rss('http://www.goha.ru/news/all/rss')
gamemag = parse_rss('http://gamemag.ru/rss/feed')
news_hard = parse_rss('https://3dnews.ru/news/rss')
ixbt = parse_rss('http://www.ixbt.com/export/news.rss')
pda = parse_rss('http://4pda.ru/feed/')
mr_news = parse_rss('http://mobile-review.com/news/feed')
mr_rew = parse_rss('http://www.mobile-review.com/rss-review.xml')
mr_art = parse_rss('http://www.mobile-review.com/rss-material.xml')


def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    c = 0
    #keyboard = InlineKeyboardMarkup(inline_keyboard=[
    #    [InlineKeyboardButton(text='Goha', callback_data='press')],
    #])

    response = bot.getUpdates(offset=100000001)
    a = response[0]['message']['text']
    # оффсет для последнего сообщения(чтобы не все сразу)
    print(content_type, chat_id, response[0]['message']['text'])

    if a =='/start':
        bot.sendMessage(chat_id, 'Привет! Воспользуйтесь клавиатурой или введите /help')
    elif a =='/help':
        bot.sendMessage(chat_id, help)#в какой чат и что отправлять
    elif a.startswith('goha') or a.startswith('Goha'):
        for mess in goha:
            if ' ' in a:
                b = a.split(' ')
                if c == int(b[1]):
                    break
            bot.sendMessage(chat_id, mess['title']+'\n'+goha_def(mess['link'])+'... '+mess['link'])
            time.sleep(5)
            c +=1
    elif a.startswith('3dnews') or a.startswith('3Dnews'):
        for mess in news_hard:
            if ' ' in a:
                b=a.split(' ')
                if c == int(b[1]):
                    break
            bot.sendMessage(chat_id, news(mess['link'])+'... '+mess['link'])
            time.sleep(5)
            c +=1
    elif a.startswith('4pda') or a.startswith('pda') or a.startswith('Pda'):
        for mess in pda:
            if ' ' in a:
                b = a.split(' ')
                if c == int(b[1]):
                    break
            bot.sendMessage(chat_id, mess['title']+'\n'+pda_def(mess['link'])+'... '+mess['link']) #не читает часть первого абзаца из-за ссылок
            time.sleep(5)
            c +=1
    elif a.startswith('Ixbt') or a.startswith('ixbt'):
        for mess in ixbt:
            if ' ' in a:
                b=a.split(' ')
                if c == int(b[1]):
                    break
            bot.sendMessage(chat_id, ixbt_def(mess['link'])+'... '+mess['link'])
            time.sleep(5)
            c +=1
    elif a.startswith('Gamemag') or a.startswith('gamemag'):
        for mess in gamemag:
            if ' ' in a:
                b=a.split(' ')
                if c == int(b[1]):
                    break
            bot.sendMessage(chat_id, mess['title'] + '\n' + gamemag_def(mess['link'])+'... '+mess['link'])
            time.sleep(5)
            c +=1
    elif a.startswith('mr-news') or a.startswith('Mr-news'):
        for mess in mr_news:
            if ' ' in a:
                b=a.split(' ')
                if c == int(b[1]):
                    break
            bot.sendMessage(chat_id, mr_news_def(mess['link'])+'... '+mess['link'])
            time.sleep(5)
            c +=1
    elif a.startswith('mr-art') or a.startswith('Mr-art'):
        for mess in mr_art:
            if ' ' in a:
                b=a.split(' ')
                if c == int(b[1]):
                    break
            bot.sendMessage(chat_id, mr_article(mess['link'])+'... '+mess['link'])
            time.sleep(5)
            c +=1
    elif a.startswith('mr-rew') or a.startswith('Mr-rew'):
        for mess in mr_rew:
            if ' ' in a:
                b=a.split(' ')
                if c == int(b[1]):
                    break
            bot.sendMessage(chat_id, mr_article(mess['link'])+'... '+mess['link'])
            time.sleep(5)
            c +=1
    else:
        bot.sendMessage(chat_id, 'Неизвестная команда, введите /help', reply_markup = {'keyboard': [
            ['4pda 3', '3dnews 3', 'ixbt 3'],
            ['gamemag 3', 'goha 3'],
            ['mr-news 3', 'mr-art 3', 'mr-rew 3']]})

    #print(response[0]['message']['text']) #получаем текст сообщения

bot = telepot.Bot('338458815:AAGvTbDpVQl7xeevUkZ4ZJ7sH15fRSZXGkU')
bot.message_loop(handle)
print ('Listening ...')

# Keep the program running.
while 1:
    time.sleep(10)

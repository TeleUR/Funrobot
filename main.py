#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
import telebot
from telebot import types
import json
import time
import os
import redis
import config
import base64
import logging
import random
import wikipedia
import subprocess
import requests as req
import urllib
import urllib2

bot = telebot.TeleBot("250324006:AAFDAxe4nVlgI3nFkUhVBWHf1xTo1bRwwpc")
config.is_sudo = 242361127

is_sudo = '242361127'
bot.send_message(is_sudo,"I'm *Online*😃", parse_mode='markdown')

@bot.message_handler(commands=['start'])
def welcome(m):
    cid = m.chat.id
    markup = types.InlineKeyboardMarkup()
    a = types.InlineKeyboardButton("راهنما  \xE2\x9C\x8C", url="https://telegram.me/CyberHelp")
    c = types.InlineKeyboardButton("Add group \xE2\x9C\x8C", url="https://telegram.me/TeleUR_robot?startgroup=new")
    markup.add(a, c)
    b = types.InlineKeyboardButton(" سازنده \xE2\x9C\x8C", url="https://telegram.me/cliali")
    markup.add(b)
    nn = types.InlineKeyboardButton("Inline Mode", switch_inline_query='')
    markup.add(nn)    
    ret_msg = bot.send_message(cid, "`سلام این ربات آزمایشی هست`    \n\n _Send :_ /help _to see_ *commands*   \n \n`اگه نظری داشتید از این طریق به من بگویید:`\n /c [msg]\n\n\n_Bot version_ *1* ", disable_notification=True, reply_markup=markup, parse_mode='markdown')
    assert ret_msg.message_id

#################################################################################################################################################################################################

@bot.message_handler(regexp='^([/!#]help)(.*)')
def welcome(m):
    print ('Send /help')
#    bot.send_chat_action(m.chat.id, 'typing')
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Next \xE2\x96\xB6\xEF\xB8\x8F', callback_data='next'))
    markup.add(types.InlineKeyboardButton('Inline \xF0\x9F\x93\x9D', switch_inline_query=''))
    bot.send_message(m.chat.id,
    """
_Hello Welcome to_
*TeleUR(api)* _bot Fun Telegram bot_
*commands↴*

*➯/help*

*➯/info*   (_your info_)

*➯/arz*   (_arz and tala_)

*➯/echo [text]*   _echo_ *(for one help type /echohelp)* 

*➯/ping*

*➯/c [text]*  _(send pm for sudo)_

`خوش امدی

برای دریافت راهنمای فارسی بنویس
/helpfa
سازنده:`
*@cliali*
    """, parse_mode='markdown', reply_markup=markup)

@bot.message_handler(regexp='^([#!/]helpfa)(.*)')
def helpfa(m):
    print ('Send /helpfa')
    text = """
    `دستورات:`
*➯/help* 
`راهنما(انگلیسی)`
*➯/helpfa*
`راهنما(فارسی)`
*➯/id*
` دریافت ایدی شما`
*➯/info*
`دریافت مشخصات شما`
*➯/arz*
`دریافت قیمت روز ارز`
*➯/echo [متن] *
`اکو یک متن`
*➯/ping*
`دستور انلاین بودن ربات`
*➯/c [متن]*
`ارسال پیام برای سازنده`
    """
    bot.send_message(m.chat.id, text , parse_mode='markdown')

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.message:
        if call.data == "next":
            markup = types.InlineKeyboardMarkup()
            TeleUR = types.InlineKeyboardButton('TeleUR\xE2\xAD\x95\xEF\xB8\x8F', callback_data='send_TeleUR')
            helpp = types.InlineKeyboardButton('Help\xE2\xAD\x95\xEF\xB8\x8F', callback_data='send_help')
            admin = types.InlineKeyboardButton('Admin TeleUR\xE2\x9A\xA0\xEF\xB8\x8F', callback_data="admin")
            back = types.InlineKeyboardButton('\xE2\x97\x80\xEF\xB8\x8FBack', callback_data='back')
            markup.add(TeleUR, helpp)
            markup.add(admin)
            markup.add(back)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="commands : list", reply_markup=markup)
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="Next!")
    if call.message:
        if call.data == "send_TeleUR":
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('\xE2\x97\x80\xEF\xB8\x8FBack', callback_data='next2'))
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="/TeleUR", reply_markup=markup)
            bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="Commands : \n /TeleUR")
    if call.message:
        if call.data == "send_help":
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('\xE2\x97\x80\xEF\xB8\x8FBack', callback_data='next2'))
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="/help", reply_markup=markup)
            bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="Commands : \n /help")
    if call.message:
        if call.data == "admin":
            markupp = types.InlineKeyboardMarkup()
            markupp.add(types.InlineKeyboardButton('\xF0\x9F\x94\xB0ali\xF0\x9F\x94\xB0', url='https://telegram.me/cliali'))
            markupp.add(types.InlineKeyboardButton('\xE2\x97\x80\xEF\xB8\x8FBack', callback_data='next2'))
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Admins list \xF0\x9F\x94\xB1", reply_markup=markupp)
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="Admin TeleUR ROBot")
    if call.message:
        if call.data == "next2":
            markup = types.InlineKeyboardMarkup()
            TeleUR = types.InlineKeyboardButton('TeleURxE2\xAD\x95\xEF\xB8\x8F', callback_data='send_TeleUR')
            helpp = types.InlineKeyboardButton('Help\xE2\xAD\x95\xEF\xB8\x8F', callback_data='send_help')
            admin = types.InlineKeyboardButton('Admin TeleUR\xE2\x9A\xA0\xEF\xB8\x8F', callback_data="admin")
            back = types.InlineKeyboardButton('\xE2\x97\x80\xEF\xB8\x8FBack', callback_data='back')
            markup.add(TeleUR, helpp)
            markup.add(admin)
            markup.add(back)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="commands : list", reply_markup=markup)
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="Welcome Main Menu")
    if call.message:
        if call.data == 'more':
            markup = types.InlineKeyboardMarkup()
            wl = types.InlineKeyboardButton('Wallpaper \xE2\x9A\xA0\xEF\xB8\x8F', callback_data='send_wallpaper')
            time = types.InlineKeyboardButton('Time \xE2\x9A\xA0\xEF\xB8\x8F', callback_data='send_time')
            food = types.InlineKeyboardButton('Food \xE2\x9A\xA0\xEF\xB8\x8F', callback_data='send_food')
            back = types.InlineKeyboardButton('\xF0\x9F\x94\x99Back', callback_data='next2')
            markup.add(wl, food)
            markup.add(time)
            markup.add(back)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Welcome More Menu', reply_markup=markup)
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="More Menu")
    if call.message:
        if call.data == 'send_wallpaper':
            urllib.urlretrieve("https://source.unsplash.com/1600x900", "wallpaper.jpg")
            bot.send_photo(call.message.chat.id, open('wallpaper.jpg'))
    if call.message:
        if call.data == 'send_time':
            url = "http://api.gpmod.ir/time/"
            response = urllib.urlopen(url)
            data = response.read()
            parsed_json = json.loads(data)
            ENtime = (parsed_json['ENtime'])
            bot.send_message(call.message.chat.id, '{}'.format(ENtime))
    if call.inline_message_id:
        if call.data == '!timee':
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('Back', callback_data='!backkk'))
            url = "http://api.gpmod.ir/time/"
            response = urllib.urlopen(url)
            data = response.read()
            parsed_json = json.loads(data)
            ENtime = (parsed_json['ENtime'])
            bot.edit_message_text(inline_message_id=call.inline_message_id, text="Time : {}".format(ENtime), reply_markup=markup)
    if call.inline_message_id:
        if call.data == '!backkk':
            markupp = types.InlineKeyboardMarkup()
            timee = types.InlineKeyboardButton('Time\xE2\x9A\xA0', callback_data='!timee')
            markupp.add(timee)
            bot.edit_message_text(inline_message_id=call.inline_message_id, text="Fun list \n Update #Soon", reply_markup=markupp)
    if call.message:
        if call.data == 'send_food':
            urllib.urlretrieve("https://source.unsplash.com/category/food", "food.jpg")
            bot.send_sticker(call.message.chat.id, open('food.jpg'))
    if call.message:
        if call.data == '!admins':
            bot.send_message(call.message.chat.id, 'Channel : @CyberHelp')
            bot.send_message(call.message.chat.id, 'Admin : @cliali')
            bot.send_message(call.message.chat.id, 'github : https://github.com/taylor-team')
    if call.message:
        if call.data == "back":
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('Next \xE2\x96\xB6\xEF\xB8\x8F', callback_data='next'))
            markup.add(types.InlineKeyboardButton('Inline \xF0\x9F\x93\x9D', switch_inline_query=''))
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="""
_Hello Welcome to_
*TeleUR* _bot Fun Telegram bot_
*commands↴*

*➯/help*

*➯/info*
(_your info_)

*➯/arz*
(_arz and tala_)

*➯/echo [text]*  _echo_ *(for one help type /echohelp)*

*➯/ping*

*➯/c [text]*   _(send pm for sudo_)
\xD8\xAE\xD9\x88\xD8\xB4\x20\xD8\xA7\xD9\x85\xD8\xAF\xDB\x8C\xD8\xAF

`برای دریافت راهنمای فارسی بنویس
/helpfa
سازنده`
*@cliali*
            """, parse_mode='markdown', reply_markup=markup)
            bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="Backed!")
            return

#################################################################################################################################################################################################

@bot.message_handler(regexp='^([!/#]echohelp)(.*)')
def m(m):
    bot.send_message(m.chat.id, "<i>The echo supported markdown : ↴</i> \n\n <b>*bold*</b> \n <i>_italick_</i> \n <code>`code` </code> \n hyper: [TEXT](LINK)", parse_mode='HTML')

#################################################################################################################################################################################################

@bot.message_handler(regexp='^([/!#]id from)(.*)')
def id_from(m):
    fromm = m.forward_from.m.from_user.id
    bot.send_chat_action(m.chat.id, "typing")
    bot.reply_to(m, "forward info:\n\n ```{}```\n".format(fromm))

#################################################################################################################################################################################################
#info
@bot.message_handler(regexp='^([/!#]info)(.*)')
def id(m):      # info menu
    cid = m.chat.id
    title = m.chat.title
    usr = m.from_user.username
    f = m.from_user.first_name
    l = m.from_user.last_name
    t = m.chat.type
    d = m.date
    id = m.from_user.id
    text = m.text
    p = m.pinned_message
    pp = m.pined_message
    fromm = m.forward_from
    bot.send_chat_action(cid, "typing")
    bot.reply_to(m, "*chat id:* `{}` \n *Chat name :* `{}` \n\n *Your Firstname :* `{}` \n *Your Last Name:* `{}`\n *Your id:* `{}` \n *Your Username :* `@{}`\n\n *Type From :* `{}` \n *Msg data :* `{}`\n *Your Msg :* `{}`\n\n\n *pind msg  : *`{}`\n {} \n\n* from : `{}`*".format(cid,title,f,l,id,usr,t,d,text,p,pp,fromm), parse_mode="Markdown")

#################################################################################################################################################################################################

@bot.message_handler(regexp='^([/!#]contact)(.*)')
def c(m):
    uid = m.chat.id
    bot.send_chat_action(uid, 'typing')
    bot.send_contact(uid, phone_number="+98 939 293 1181" , first_name="ali")

#################################################################################################################################################################################################

@bot.message_handler(regexp='^([/!#]cyb3rt)(.*)')
def handler(m):
    cid = m.chat.id
    bot.send_message(cid, "My Name is Cyb3rT \n creator and developer : [developer](https://telegram.me/cliali) \n help channel : [Cyber help](https://telegram.me/cyberhelp)", parse_mode="Markdown")

#################################################################################################################################################################################################
#id
@bot.message_handler(regexp='^([/!#]id)')
def test_handler(m):
       cid = m.from_user.id
       fl = m.from_user.first_name
       bot.send_message(m.chat.id, "*Your Name = {} \n\n  Your ID = {}*".format(fl,cid), parse_mode="Markdown")

#################################################################################################################################################################################################

@bot.message_handler(regexp='^([/!#]me1)(.*)')
def me(m):
         u = m.from_user.username
         i = m.from_user.id
         f = m.from_user.first_name
         l = m.from_user.last_name
         bot.send_message(m.chat.id, " *First Name :* `{}` \n *Last Name :* `{}` \n *USER NAME :* @{} \n *Your id :* {}".format(f,l,u,i), parse_mode="markdown")
#################################################################################################################################################################################################

#feedback
@bot.message_handler(commands=['feedback'])
def feedback(m):
    senderid = m.chat.id
    first = m.from_user.first_name
    usr = m.from_user.username
    str = m.text
    txt = str.replace('/feedback', '')
    bot.send_message(senderid, "_Thank Your Msg Posted admin_", parse_mode="Markdown")
    bot.send_message (config.is_sudo, "msg : {}\nid : {}\nname : {}\nUsername : @{}".format(txt,senderid,first,usr))

#################################################################################################################################################################################################

@bot.message_handler(commands=['j'])
def j(m):
    config = 242361127
    tmt = m.from_user.id 
    cid = m.chat.id
    if str(tmt) not in config.is_sudo:
        bot.send_message(cid, "Just for admin", parse_mode="Markdown")
        return
    to_id = m.text.split()[1:]
    txt = m.text.split()[2:]
    text = ' '.join(txt)
    bot.send_message(to_id, "<b>\xD8\xAF\xD8\xB1\x20\xD8\xAC\xD9\x88\xD8\xA7\xD8\xA8\x20\xD8\xB4\xD9\x85\xD8\xA7 :</b>\n <code>{}</code>".format(text), parse_mode="HTML")

#################################################################################################################################################################################################

@bot.inline_handler(lambda query: len(query.query) is 0)
def query_text(query):
    user = query.from_user.username
    name = query.from_user.first_name
    lname = query.from_user.last_name
    uid = query.from_user.id
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('\xE2\x9C\x85 {} \xE2\x9C\x85'.format(user), url="https://telegram.me/{}".format(user)))
    thumb_url = 'http://millingtonlibrary.info/wp-content/uploads/2015/02/Info-I-Logo.png'
    info = types.InlineQueryResultArticle('1',
                                          '\xF0\x9F\x8C\x8E Your Info \xF0\x9F\x8C\x8E',
                                          types.InputTextMessageContent('*Username : @{}\nYour First Name : {}\nYour Last Name : {}\nYour ID :  {}*'.format(user,name,lname,uid), parse_mode="Markdown"),
                                          reply_markup=markup,
                                          thumb_url=thumb_url)
    #pic = types.InlineQueryResultPhoto('2',
                                       #'http://vip.opload.ir/vipdl/95/3/negative23/photo-2016-06-09-01-09-41.jpg',
                                       #'http://vip.opload.ir/vipdl/95/3/negative23/photo-2016-06-09-01-09-41.jpg',
                                       #input_message_content=types.InputTextMessageContent('@Taylor_Team')
    #gif = types.InlineQueryResultGif('2',
                                    # 'http://andrewtrimmer.com/wp-content/uploads/2014/09/Coming-Soon_Light-Bulbs_Cropped-Animation-Set_03c.gif',
                                     #'http://andrewtrimmer.com/wp-content/uploads/2014/09/Coming-Soon_Light-Bulbs_Cropped-Animation-Set_03c.gif',
                                     #gif_width=70,
                                     #gif_height=40,
                                     #title="Soon Update",
                                    # input_message_content=types.InputTextMessageContent('New Update #Soon'))

    tumsss = 'http://images.clipartpanda.com/contact-clipart-contact-phone-md.png'
    random_text = random.randint(1, 100)
    tmpp = 'http://sugartin.info/wp-content/uploads/2013/11/logo.png'
    randowm = types.InlineQueryResultArticle('2', '\xD8\xB9\xD8\xAF\xD8\xAF\x20\xD8\xB4\xD8\xA7\xD9\x86\xD8\xB3\xDB\x8C\x20\xF0\x9F\x99\x88',
                                             types.InputTextMessageContent('\xD8\xB9\xD8\xAF\xD8\xAF\x20\xD8\xB4\xD8\xA7\xD9\x86\xD8\xB3\xDB\x8C : {}'.format(random_text)), thumb_url=tmpp)

    url = req.get('http://api.gpmod.ir/time/')
    data = url.json()
    EN = data['ENtime']
    time_tmp = 'http://prek-8.com//images/time21.jpg'
    timesend = types.InlineQueryResultArticle('3', 'Time / \xD8\xB3\xD8\xA7\xD8\xB9\xD8\xAA', types.InputTextMessageContent('`Tehran` : *{}*'.format(EN), parse_mode='Markdown'), thumb_url=time_tmp)
    bot.answer_inline_query(query.id, [info, randowm, timesend], cache_time=5, switch_pm_text='Start bot')

#################################################################################################################################################################################################
#uptime
@bot.message_handler(regexp='^([/!#]uptime)(.*)')
def ss(m):
    cc = os.popen("uptime").read()
    bot.send_message(m.chat.id, '{}'.format(cc))

#################################################################################################################################################################################################
#whois
@bot.message_handler(regexp='^([/!#]whois)(.*)')
def whois(m):
    text = m.text
    repll = text.replace('/whois', '')
    whois = os.popen('whois {}'.format(repll)).read()
    bot.send_message(m.chat.id, '{}'.format(whois))

#################################################################################################################################################################################################
#arz
@bot.message_handler(regexp='^([/!#]arz)(.*)')
def arz(m):
    url = urllib.urlopen('http://exchange.nalbandan.com/api.php?action=json')
    data = url.read()
    js = json.loads(data)
    dollar = js['dollar']['value']
    euro = js['euro']['value']
    gold_per_geram = js['gold_per_geram']['value']
    pond = js['pond']['value']
    bot.send_message(m.chat.id, ' دلار : '+dollar+'\n یورو : '+euro+'\n  طلای 18 عیار :  '+gold_per_geram+'\n  پوند : '+pond )        

#################################################################################################################################################################################################
#ping
@bot.message_handler(regexp='^([/!#]ping)(.*)')
def ping(m):
    bot.send_chat_action(m.chat.id, 'typing')
    bot.send_message(m.chat.id, '*pong :D* \xF0\x9F\x86\x99', parse_mode='Markdown')

#################################################################################################################################################################################################
#echo
@bot.message_handler(regexp='^([/!#]echo) (.*)')
def echo(m):
    bot.send_message(m.chat.id,  m.text.replace('/echo', ''), parse_mode='Markdown')

#################################################################################################################################################################################################
#shortlink
@bot.message_handler(regexp='^([/!#]short)(.*)')
def short(m):
    text = m.text.split(' ',1)[1]
    url = urllib.urlopen('http://gs2.ir/api.php?url='+text)
    bot.send_message(m.chat.id, url.read())

#################################################################################################################################################################################################
#news
@bot.message_handler(regexp='^([#!/]news)(.*)')
def m(m):
    url = urllib.urlopen('http://api.khabarfarsi.net/api/news/latest/1?tid=*&output=json')
    data = url.read()
    pa = json.loads(data)
    title = pa['items'][0]['title']
    link = pa['items'][0]['link']
    title2 = pa['items'][1]['title']
    link2 = pa['items'][1]['link']
    title3 = pa['items'][2]['title']
    link3 = pa['items'][2]['link']
    bot.send_message(m.chat.id, '<b>Title</b> : {}\n\n<b>Link</b> {}\n\n\n<b>Title</b> : {}\n\n<b>Link</b> : {}\n\n\n<b>Title</b> : {}\n\n<b>Link</b> : {}'.format(title,link,title2,link2,title3,link3), parse_mode='HTML')

#################################################################################################################################################################################################
#stats
@bot.message_handler(commands=['stats'])
def send_stats(m):
    if m.from_user.id == 242361127:
        usrs = str(redis.scard('memberspy'))
        ban = str(redis.scard('banlist'))
        text = '*Users : {}\n\nBanlist : {}*'.format(usrs,ban)
        bot.send_message(m.chat.id,text,parse_mode='Markdown')

#################################################################################################################################################################################################

#################################################################################################################################################################################################
#leave
@bot.message_handler(commands=['leave'])
def leavehandler(m):
    if m.from_user.id == 242361127:
        bot.leave_chat(m.chat.id)

#################################################################################################################################################################################################
#################################################################################################################################################################################################
#################################################################################################################################################################################################

bot.polling(True)
#end


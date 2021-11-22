import telebot
from telebot import types
import requests
from colorama import Fore, Style
import secrets

bot = telebot.TeleBot("1655333424:AAEqWMIMpRV12ajPibtV-Fj83xf_M0kiy2Y")

medo = types.InlineKeyboardButton(text="htmliq",url="https://t.me/htmliq")
@bot.message_handler(commands = ["start"])
def medoo(message):
    ph8r = message.chat.first_name
    aan = types.InlineKeyboardMarkup()
    aan.add(medo)
    bot.send_message(message.chat.id,text = f"""اهلا بك في بوت سحب معلومات الانستا\n ارسل اليوزر بدون @.""",reply_markup=aan,)

    @bot.message_handler(func=lambda m: True)
    def marL(message):
        msg = message.text
        url_id = f'https://www.instagram.com/{msg}/?__a=1'
        cookie  = secrets.token_hex(8)*2
        head = {
'HOST': "www.instagram.com",
'KeepAlive' : 'True',
'user-agent' : "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36",
'Cookie': cookie,
'Accept' : "*/*",
'ContentType' : "application/x-www-form-urlencoded",
"X-Requested-With": "XMLHttpRequest",
"X-IG-App-ID" : "936619743392459",
"X-Instagram-AJAX" : "missing",
"X-CSRFToken" : "missing",
"Accept-Language" : "en-US,en;q=0.9"
        }
        req_id = requests.get(url_id,headers=head).json()
        bio = str(req_id['graphql']['user']['biography'])
        nam = str(req_id['graphql']['user']['full_name'])
        idd = str(req_id['graphql']['user']['id'])
        isp = str(req_id['graphql']['user']['is_private'])
        isv = str(req_id['graphql']['user']['is_verified'])
        pro = str(req_id['graphql']['user']['profile_pic_url'])
        medo = f''' - Name : `{nam}`\n - Id : `{idd}`\n - private : `{isp}`\n - verified : `{isv}`\n - Bio : `{bio}`\n\n - By : @Tzzzz'''
        bot.send_photo(message.chat.id,pro,caption=medo,parse_mode="MARKDOWN")



bot.polling(True)
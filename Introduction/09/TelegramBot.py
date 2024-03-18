
import telebot
import random
import requests
import telebot
from telebot import types
from khayyam import JalaliDate
import gtts
import qrcode

#use your tokenIDAdr from botfather
BotTokenIdAdr = ""

api_url = "https://hafez.p.rapidapi.com/fal"

#use your key and host
api_headers = {
    "X-RapidAPI-Key": "",
    "X-RapidAPI-Host": ""
}


bot =  telebot.TeleBot(BotTokenIdAdr)  

game_value = None  
state=None
game_won=False
flag = None

# Init Commands of Telegram visual Keyboard
telegram_keyboard = types.ReplyKeyboardMarkup(row_width=3)
start_key = types.KeyboardButton('/start')
game_key = types.KeyboardButton('/game')
fall_key=types.KeyboardButton('/fall')
age_key = types.KeyboardButton('/age')
voice_key = types.KeyboardButton('/voice')
max_key = types.KeyboardButton('/max')
argmax_key = types.KeyboardButton('/argmax')
qrcode_key = types.KeyboardButton('/qrcode')
help_key = types.KeyboardButton('/help')
telegram_keyboard.add(start_key, game_key, fall_key, age_key, voice_key, max_key, argmax_key, qrcode_key, help_key)


# function to create game keyboard
def generate_game_keyboard():
    game_keyboard = types.ReplyKeyboardMarkup(row_width=1)
    new_game_button = types.KeyboardButton('/newgame')
    exit_button = types.KeyboardButton('/exit')
    game_keyboard.add(new_game_button, exit_button)
    return game_keyboard



# decorator in Python
@bot.message_handler(commands=['start'])
def send_greeting(msg):
    global state
    state="start"
    bot.reply_to(msg," سلام ",reply_markup=telegram_keyboard)

# ********************************************************************************#

@bot.message_handler(commands=['fall'])
def send_fall(message):
    global flag
    flag="fall"
    response = requests.get(api_url, headers=api_headers)
    if response.status_code == 200:
        poem_text = response.json()["poem"]
        interpretation = response.json()["text"]
        full_text = f"شعر حافظ:\n\n{poem_text}\n\nتعبیر:\n\n{interpretation}"
        bot.send_message(message.chat.id, full_text)
    else:
        bot.send_message(message.chat.id, "متاسفانه در قسمت دریافت فال با مشکل روبرو هست بعدا تلاش کنید")

# ********************************************************************************#

@bot.message_handler(commands=['game'])
def game(message):
    global flag
    global win
    flag="game"
    win=False
    global game_number
    game_number = random.randint(1, 100)
    bot.send_message(message.chat.id, "من به یک عدد بین 1 تا 100 فکر میکنم حدس بزن عدد من چیه. یادت باشه فقط 10 تا فرصت داری!!", reply_markup=generate_game_keyboard())

@bot.message_handler(func=lambda message: message.text == '/newgame')
def new_game(message):
    global flag
    global win
    flag="game"
    win=False
    global game_number
    game_number = random.randint(1, 100)
    bot.send_message(message.chat.id, "یک بازی جدی شروع میکنیم! من به یک عدد بین 1 تا 100 فکر میکنم حدس بزن عدد من چیه!", reply_markup=generate_game_keyboard())

@bot.message_handler(func=lambda message: message.text == '/exit')
def exit_game(message):
    global game_number
    game_number = None
    global win
    win=False
    bot.send_message(message.chat.id, "Game Over 🖤", reply_markup=telegram_keyboard)
    # reply_markup=types.ReplyKeyboardRemove()  ازین برای حذف کیبور استفاده کن

# ********************************************************************************#
@bot.message_handler(commands=['age'])
def calculate_age(message):
    global flag
    flag="age"
    bot.send_message(message.chat.id, " تاریخ تولد شمسی خود را به صورت 0000/00/00 وارد کنید مثال 1369/08/25", reply_markup=telegram_keyboard)

# ********************************************************************************#
    
@bot.message_handler(commands=['voice'])
def send_voice(message):
    global flag
    flag="voice"
    bot.send_message(message.chat.id, "لطفا متن فینگلیش را برای تبدیل به صوت بنویسید")

# ********************************************************************************#

@bot.message_handler(commands=['max'])
def find_max(message):
    global flag
    flag="max"
    bot.send_message(message.chat.id, "اعداد خود را وارد کنید تا بزرگترین ان را بهتون بگم")
    bot.send_message(message.chat.id, "برای جدا کردن اعداد از , استفاده کنید.")

# ********************************************************************************#

@bot.message_handler(commands=['argmax'])
def find_argmax(message):
    global flag
    flag="argmax"
    bot.send_message(message.chat.id, "اعداد خود را وارد کنید تا شماره اندیس عدد بزرگ را بگم و توجه اندیس در کامپیوتر از صفر شروع میشود")
    bot.send_message(message.chat.id, "برای جدا کردن اعداد از , استفاده کنید.")

# ********************************************************************************#

@bot.message_handler(commands=['qrcode'])
def generate_qrcode(message):
    global flag
    flag="qrcode"
    bot.send_message(message.chat.id, "لطفا رشته مورد نظر رو وارد کنید تا به کد کیو آر تبدیل کنم")

# ********************************************************************************#

@bot.message_handler(commands=['help'])
def display_help(message):
    send_help_message(message)  

# ********************************************************************************#
#                               Main Functions                                     #
@bot.message_handler(func=lambda msg: True)
def process_message(msg):
    if flag == "game":
        global game_number
        global win
        win = False
        count = 1
        try:
            if count <= 10 and not win:
                guess = int(msg.text)
                if guess < game_number:
                    bot.reply_to(msg, "برو بالاتر ⬆️")
                elif guess > game_number:
                    bot.reply_to(msg, "برو پایین تر ⬇️")
                else:
                    bot.reply_to(msg, "درست حدس زدی✅")
                    bot.send_message(msg, "🍾🍾🍾")
                    game_number = None
                    win = True
                count += 1
            elif win:
                bot.send_message(msg.chat.id, "میخوای دوباره بازی کنیم؟", reply_markup=generate_game_keyboard())
            else:
                win = False
                bot.reply_to(msg, f"متاسفانه شانس باهات یاری نبود و باختی و عدد درست {game_number} بود.")
                bot.send_message(msg.chat.id, "میخوای دوباره بازی جدید رو اغاز کنی؟", reply_markup=generate_game_keyboard())
        except ValueError:
            bot.reply_to(msg, "این که وارد کردی اشتباه هست ")
    elif flag == "age":
        try:
            birthday = (msg.text)
            birth_year, birth_month, birth_day = map(int, birthday.split('/'))

            current_date = JalaliDate.today()
        
            age = current_date.year - birth_year - 1 if (current_date.month, current_date.day) < (birth_month, birth_day) else current_date.year - birth_year
            month = current_date.month - birth_month if current_date.month >= birth_month else 12 - birth_month + current_date.month
            day = current_date.day - birth_day if current_date.day >= birth_day else JalaliDate(current_date.year, current_date.month - 1, current_date.day).daysinmonth - birth_day + current_date.day
            
            bot.send_message(msg.chat.id, f"سن شما برابر {age} سال و {month} ماه و {day} روز است.")
        except ValueError:
            bot.send_message(msg.chat.id, "فرمت وارد شده سن اشتباه هست")
    elif flag == "voice":
        text = (msg.text) 
        x = gtts.gTTS(text, lang="en", slow=False)
        x.save("output.mp3") 
            
        audio_file = open("output.mp3", "rb")
        bot.send_voice(msg.chat.id, audio_file)
        audio_file.close()
    elif flag == "max":      
        text = (msg.text) 
        numbers = [int(num.strip()) for num in text.split(',')]
        max_value = max(numbers)
        bot.send_message(msg.chat.id, f"بزرگترین عدد: {max_value}")
    elif flag == "argmax":
        text = (msg.text)
        numbers = [int(num.strip()) for num in text.split(',')]
        max_index = numbers.index(max(numbers))
        bot.send_message(msg.chat.id, f"اندیس بزرگترین عدد: {max_index}")
    elif flag == "qrcode":
        text = (msg.text)
        img_QR = qrcode.make(text)
        img_QR.save("MyQrCode.png")

        qr_file = open("MyQrCode.png", "rb")
        bot.send_photo(msg.chat.id, qr_file)     
    else:
        pass

# ********************************************************************************#
def send_help_message(msg):
    help_text = '''
    لیست دستورات:
    /start - شروع کار با بات
    /fall - دریافت فال حافظ
    /game - بازی حدس عدد
    /age - محاسبه سن شمسی
    /voice - ارسال پیام به صورت صوتی
    /max - یافتن بزرگترین عدد در آرایه
    /argmax - یافتن اندیس بزرگترین عدد در آرایه
    /qrcode - تولید کد QR از یک رشته
    /help - نمایش این راهنما
    
    '''

    bot.send_message(msg.chat.id, help_text)

bot.infinity_polling()

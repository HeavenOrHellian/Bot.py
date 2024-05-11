import random

def gen_pass(pass_length):
    elements = "+-/*!&amp;$#?=@<>"
    password = ""
    for i in range(pass_length):
        password += random.choice(elements)
    return password

def emoji_olusturucu():
    emoji = ["\U0001f600", "\U0001f642", "\U0001F606", "\U0001F923"]
    return random.choice(emoji)
    

def yazi_tura():
    para = random.randint(0, 1)
    if para == 0:
        return "Yazı"
    else:
        return "Tura"

def bot_yazi_tura():
    bot_para = random.randint(0 , 1)
    if bot_para == 0:
        return 'Yazı'
    else:
        return 'Tura'

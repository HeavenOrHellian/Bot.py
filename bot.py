import discord
import random

from bot_mantik import gen_pass
from bot_mantik import emoji_olusturucu
from bot_mantik import yazi_tura
from bot_mantik import bot_yazi_tura

# ayricaliklar (intents) değişkeni botun ayrıcalıklarını depolayacak
intents = discord.Intents.default()
# Mesajları okuma ayrıcalığını etkinleştirelim
intents.message_content = True
# client (istemci) değişkeniyle bir bot oluşturalım ve ayrıcalıkları ona aktaralım
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} olarak giriş yaptık.')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$Merhaba'):
        await message.channel.send("Selam!")
    elif message.content.startswith('$Bye'):
        await message.channel.send("\U0001f642")

    elif message.content.startswith('$Nasılsın?'):
        await message.channel.send("İyiyim sen nasılsın?")

    elif message.content.startswith('$Teşekkürler'):
        await message.channel.send("Rica ederim.")

    elif message.content.startswith('$Ben de iyiyim. Biraz oyun oynamak ister misin?'):
        await message.channel.send("Olur. Ne oynamak istersin")

    elif message.content.startswith('$Bana dört tane farklı emoji oluştur. Rastgele bir şekilde göster.'):
        await message.channel.send(f'İşte rastgele sırayla oluşan emojiniz: {emoji_olusturucu()}')

    elif message.content.startswith('$Yazı tura oynayalım mı?'):
        await message.channel.send('Olur oynayalım. Yazı mı tura mı sen seç ben de sana doğru olup olmadığını söyleyeceğim.')

    elif message.content.startswith('$Tamam olur ben yazıyı seçiyorum.'):
        await message.channel.send(f'Hooopp! {yazi_tura()} çıktı.')

    elif message.content.startswith('$Tamam olur ben turayı seçiyorum.'):
        await message.channel.send(f'Hooopp! {yazi_tura()} çıktı.')

    elif message.content.startswith('$Bana güçlü bir şifre oluşturabilir misin? Sekiz haneli olsun.'):
        await message.channel.send(f'İşte şifreniz: {gen_pass(8)}')

    else:
        await message.channel.send("Bu komutu anlayamadım :(")

client.run("TC.Kimlik No")

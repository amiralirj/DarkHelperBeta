from pyrogram import Client,filters
import matplotlib.pyplot as plt
import numpy as np 
import time , database , asyncio , datetime , random , Pointing_Groups
from pyrogram.types import ChatPermissions,InlineKeyboardMarkup, InlineKeyboardButton,ReplyKeyboardMarkup
from requests_async  import get,post
#import timeIR
ems = ['๐ฆ', '๐ฏ', '๐ฆ', '๐ฆ', '๐', '๐บ', '๐ฆ', '๐', '๐ณ', '๐ฌ', '๐ผ', '๐ฆ', '๐', '๐ฒ', '๐', '๐', '๐ท', '๐น', '๐บ', '๐ธ', '๐ผ', '๐', '๐', '๐ช', '๐ซ', 'โญ๏ธ', 'โจ', 'โก๏ธ', '๐ฅ', '๐', 'โ๏ธ', 'โ๏ธ', '๐', '๐', '๐', '๐', '๐', '๐ง', '๐ฐ', '๐ญ', '๐ฌ', '๐ซ', '๐ฟ', '๐ฉ', '๐ช', '๐ฅ', '๐ธ', '๐น', '๐ง', '๐พ', 'โฝ๏ธ', '๐', '๐', 'โพ๏ธ', '๐ฅ', '๐พ', '๐', '๐', '๐ฅ', '๐ธ', '๐บ', '๐ท', '๐', '๐', 'โ๏ธ', '๐', '๐ธ', '๐ฐ', '๐ผ', '๐ก', '๐ฉ', '๐ฑ', '๐ป', '๐ฅ', '๐ฐ', '๐งจ', '๐ฃ', '๐ช', '๐', 'โฑ๏ธ', '๐ฎ', '๐ฉธ', '๐ฆ ', '๐', '๐งธ', '๐', '๐', '๐ฏ', 'โค๏ธ', '๐งก', '๐', '๐', '๐', '๐', '๐ค', '๐ค', '๐ค', 'โฃ๏ธ', '๐', '๐', '๐', 'โ๏ธ', '๐ฑ', '๐ฃ', 'โฅ๏ธ', '๐', '๐ฅฐ', '๐ฅณ', '๐คฉ', '๐คช', '๐พ', '๐ป', '๐', '๐', '๐', '๐ฉ']
wwbots=[854021534,175844556,1029642148]
partner=[#Partner]
sup=#owner
#################################################################################################

async def black_state_gir(user_id):
    try:
        a=(await get(f"http://blackwerewolf.com/Stats/PlayerStats/?pid={user_id}&json=true")).json()
        a=dict(a)
        return int(a['gamesPlayed'])
    except:
        return 0
async def onyx_state_gir(user_id):
    token='1121419247:AAHCd4sTctw3p8RiofS3Rhp4aPkuvREtlJm'
    try:
        o= ( await post(
            url="http://api.wolfofpersia.ir:9999/api/GetState",
            data={
                "user_id": user_id,
                "token": token},timeout=4)).json()
        man=dict(o)
        return int(man['total_game'])
    except:
        return 0

async def werewolf_state_gir(user_id):
    try:
        a=(await get(f"http://www.tgwerewolf.com/Stats/PlayerStats/?pid={user_id}&json=true")).json()
        a=dict(a)
        return int(a['gamesPlayed'])
    except Exception as e:
        error(f'{e} list black')
        return 0

with open('errors.txt','w') as f :
        f.write(f'started\n')

def error(e):
    with open('errors.txt','a') as f :
            f.write(f'{e} \n')

#-------------------------------------------------


best_coin='''แดธแตหขแต แตแตโฟแตสฐ
๐ช       ๐คแดษชษดษข๐แด๊ฐ๐แดแดษชษด๐ค     ๐ช
๐ช๐ช๐ช๐ช๐ช๐ช๐ช๐ช๐ช๐ช๐ช๐ช
๐ธ       Cฯฮนษณ Rฮฑษณฦ : {coinrank} 
๐ธ       Pฯฮนษณฦ Rฮฑษณฦ : {pointrank}

๐ฑ        Cฯฮนษณส        : {coins} ๐ช 
_____________________
              {gap}
โจ {name}
โจPoints : {point}
โจLocal rank : {tor}
โจGlobal rank : {glob}
๐ Diamonds : {almas}
โจ Ghosts: {rooh} 
โจ Bulletproof: {zed}
โจ Dark Spell: {black}

๐ช๐ช๐ช๐ช๐ช๐ช๐ช๐ช๐ช๐ช๐ช๐ช

#Id_Card'''

text_Hash='hash:amiralirj}[koskhol]HHHH:'
chl="""ูุงุงุงุงู ุง?ูุฌุงุฑู๐๐
ูุฑฺฉ? ุฒูุฏุชุฑ ุฑ?ูพ ุจุฒูู ?ฺฉ ุงูุช?ุงุฒ ุจู ุชูุฑููููุชุด ุงุถุงูู ู?ุดู โก๏ธโ๏ธ



ุจุจ?ู?ู ฺฉ? ุจุฑูุฏู ู?ุดู๐๐"""
chalesh_text=''
javab=''
Help_Shekat='''ูุชู ุฎูุฏ ุฑุง ฺฉุงูู ุจูู?ุณ?ุฏ ู ุฏุฑุฌุง?? ฺฉู ู?ุฎูุงู?ุฏ ุฑุง? ุดูุง ูุฑุงุฑ ุจฺฏ?ุฑู ุนุจุงุฑุช  [id] ุฑู ุจูู?ุณ?ุฏ ! (ุฏูุช ฺฉู?ุฏ ููุท ?ฺฉ ุนุจุงุฑุช  id ุฏุฑ ูุชูุชูู ุจุงุดู ) !'''
major=0.2
zarib_TBN=0
#--------------------------------------------------------------

token='1121419247:AAHCd4sTctw3p8RiofS3Rhp4aPkuvREtlJm'
api_id =2586462
api_hash = '68542129131999986899b84a10a6170c'
bot = Client('amirairj-helper', api_id, api_hash,workers=150)
#------------------------------------------------------------------------
leave_auto=1
winner=None




sended=dict()
nazer=dict()
shekar=dict()
is_tagging=dict()
my_tag=dict()
omomi=dict()
tag_list=dict()
winner2=dict()
number=list()
zarb_ALMASI=dict()
zarb=dict()
spam=dict()
muted=dict()
muted_admins=dict()
muted_hour=dict()
zarib=dict()
enfejar=dict()
enfejar_Started=dict()
enfejar_hash=dict()
dozdi=dict()
dozdi_aks=dict()
spam_shekar=dict()
flood=dict()
spam_gif=dict()
ray_inline=dict()
players_dict=dict()
roles=dict()
next_game=dict()
mute_group = ChatPermissions(can_send_messages=False)
unmute_group = ChatPermissions(
    can_send_messages=True,
    can_send_animations=True,
    can_send_games=True,
    can_send_media_messages=True,
    can_send_polls=True,
    can_send_stickers=True)

soal={
'ฺู ุช?ู? ุชูุงูุณุชู ุฏุฑ ุชุงุฑ?ุฎ ุจู 6 ฺฏุงูู ุจุฑุณุฏ ุ':"ุจุงุฑุณูููุง",
'ุงุฏู ูุถุง?? ููุจ ฺฉุฏุงู ุจุงุฒ?ฺฉู ุงุณุช ุ':'ูุณ?',
"ฺฉุฏุงู ููุน ุณููู (ุฌุงููุฑ?,ฺฏ?ุงู?) ุฏุงุฑุง? ุฏ?ูุงุฑู ? ุณููู? ุงุณุช ุ":"ฺฏ?ุงู?"
,'ฺู ุช?ู? ุจ?ุดุชุฑ?ู ููุฑูุงู? ู?ฺฏ ููุฑูุงูุงู ุงุฑููพุง ุฑุงุฏุงุฑุฏ':"ุฑุฆุงู"
,"ุงูฺฉูุงุณ?ฺฉู ูุฑุจูุท ุจู ู?ฺฏ ฺฉุฏุงู ฺฉุดูุฑ ุงุณุช ุ":"ุงุณูพุงู?ุง"
," ุงุณุชููุงู ฺูุฏ ุจุงุฑ ููุฑูุงู ุขุณ?ุง ุดุฏูุ":"2"
,"ููุชุจุงู ุชูุณุท ฺู ฺฉุดูุฑ? ุณุงุฎุชู ุดุฏุ":"ุงููุงู"
,"ฺฏู ุง?ุฑุงู ุฑุง ุจู ูพุฑุชุบุงู ฺู ฺฉุณ? ุฒุฏุ":"ุงูุตุงุฑ?"
,"ฺฏู ุขุฑฺุงู?ู ุจู ุง?ุฑุงู ุฏุฑ ุณุงู?ฒ?ฐ?ฑ?ดฺฉ? ุฒุฏ ุ" : "ูุณ?"
,"ุงฺฉููู ุณูุงุฑุฒ ุฏุฑฺู ุช?ู? ุงุณุช ุ": "ุงุชูุช?ฺฉู"
,"ุจ?ุดุชุฑ?ู ููุฑูุงู? ู?ฺฏ ุฎู?ุฌ ูุงุฑุณ ุฑุงฺู ุช?ู? ุฏุงุดุชู" : "ูพุฑุณ"
,"ุฎูุฑุฏู โโโ- ูุงูุน ุฑ?ุฒุด ู ุณู?ุฏ ุดุฏู ูููุง ู? ุดูุฏุ":"ฺฉุงูู"
,"ุบุฐุง? ูุบุฒ ููุจ ฺฉุฏุงู ูุงุฏู ุบุฐุง?? ุงุณุชุ":"ฺฏุฑุฏู"
,"ฺฉูุจูุฏ ฺฉุฏุงู ู?ุชุงู?ู ุณุจุจ ุฑู?ู ุดุฏู ุฎูู ุงูุณุงู ู ููุง?ุชุง ุฎููุฑ?ุฒ? ู? ุดูุฏุ":"k"
,'ูุง?ุน ููุฌูุฏ ุฏุฑ ฺฉุฏุงู ู?ูู ุฑุง ู? ุชูุงู ุจู ุนููุงู ูพูุงุณูุง? ุฎูู ุงุณุชูุงุฏู ฺฉุฑุฏุ':"ูุงุฑฺฏ?ู"
,"ูุงุฏู ุบุฐุง?? ฺฉู ูุฑฺฏุฒ ูุงุณุฏ ูู? ุดูุฏุ":"ุนุณู"
,"ฺฉุฏุงู ุงูุฏุงู ุฏุงุฎู? ุจุฏู ูุงุฏุฑ ุจู ุชุฑู?ู ุฎูุฏ ุงุณุชุ":"ฺฉุจุฏ"
,"ููุงูู ุชุฑ?ู ูุงู?ฺู ุจุฏู ุงูุณุงู ฺฉุฏุงู ุงุณุชุ":"ุฒุจุงู"
,"ฺูุฏ ฺฏุฑูู ุฎูู? ุฏุฑ ุงูุณุงู ูุง ูุฌูุฏ ุฏุงุฑุฏุ":"4"
,"ฺฉุฏุงู ุฑฺฏ ูุธ?ูู ุงูุชูุงู ุฎูู ุงุฒ ุงูุฏุงู ูุง? ุจุฏู ุจู ููุจ ุฑุง ุจุฑ ุนูุฏู ุฏุงุฑุฏุ":'ุณ?ุงูุฑฺฏ'
,"ููุฑููู ฺฉูุชุฑู ฺฉููุฏู ูุตุฑู ููุฏ ุฏุฑ ุจุฏู ฺู ูุงู ุฏุงุฑุฏุ":"ุงูุณูู?ู"
,"ููุฏ ุด?ุฑ ุฑุง ฺู ู? ฺฏู?ูุฏุ":"ูุงฺฉุชูุฒ"
,"ููุจุน ุงุตู? ุชุงู?ู ู?ุชุงู?ู ุฏ? ฺ?ุณุชุ":"ููุฑ"
,"ุงุตุทูุงุญ? ุฏุฑ ููุชุจุงู ุจู ูุนูุง? ุจุงุฒ? ูุง? ุฏุฑูู ุดูุฑ?ุ":"ุฏุฑุจ?"
,"ุจุฑุชุฑ?ู ฺฏู ุฒู ุชุงุฑ?ุฎ ุฑุฆุงู ูุงุฏุฑ?ุฏุ":"ุฑููุงูุฏู"
,"ู?ุฒุจุงู ุฌุงู ุฌูุงู? ?ฒ?ฐ?ฑ?ด ฺฉุฏุงู ฺฉุดูุฑ ุจูุฏุ":"ุจุฑุฒ?ู"
,"ุฏุฑ ุชุงุฑ?ุฎ ููุชุจุงู ุจุงุดฺฏุงู? ฺู ุช?ู? ุฏู ุจุงุฑ ุณู ุฌุงู ุฏุฑ ?ฺฉ ูุตู ูุชุญ ฺฉุฑุฏู ุงุณุชุ":"ุจุงุฑุณูููุง"}
#-------------------------------------------------------------------------
mention = lambda user_id, text: f'<a href=tg://user?id={user_id}>{text}</a>'

#----------------------------------------------------------------------
database.start_Sql()
#-----------------------------------------------------------------numberic - flood
for i in range(0,61):
    flood[i]=False
#=================================================================
f=database.show_gaps()
for i in f:
    print(i[0])
    players_dict[int(i[0])]=dict()
    muted_admins[int(i[0])]=dict()
    muted_hour[int(i[0])]=dict()
    muted[int(i[0])]=dict()
    enfejar[int(i[0])]=dict()
    sended[int(i[0])]=False
    spam_shekar[int(i[0])]=dict()
    spam_gif[int(i[0])]=dict()
    ray_inline[int(i[0])]=dict()
    roles[int(i[0])]=dict()
    shekar[int(i[0])]=1234
    nazer[int(i[0])]=1234
    next_game[int(i[0])]=dict()

f=database.show_supourts()
for i in f:
    print(i[0])
    muted_admins[int(i[0])]=dict()
    muted_hour[int(i[0])]=dict()
    muted[int(i[0])]=dict()

del f 
del i
#-------------------------------------------------------------------------
try:
    with bot:
        bot_username = "@" + str(bot.get_me().username)
        bot_id=bot.get_me().id
        f=database.show_gaps()
        for i in f:
            try:
                it=database.cheak_admin_point_user(i[0])
                for tt in bot.iter_chat_members(i[0] , filter='administrators'):
                    try:
                        if int(tt.user.id) not in it: 
                            database.admin_added(int(tt.user.id),int(i[0]))
                        else:
                            it.remove(int(tt.user.id))
                    except:
                        pass
            except:
                pass
        for u in it :
            database.delete_admin_Point(int(u))
except Exception as e:
    print(e)
    pass
#---------------------------------------------------------------
def role_saver_dec(func):
    async def check(Client, message):
        a=int(database.show_role_saver(int(message.chat.id)))
        if a==1:
            await func(Client,message)
    return check



def ban_from_bot(func):
    async def check(Client, message):
        ban_bool=database.ban_cheak(int(message.from_user.id))
        if ban_bool==True:
            await message.reply_text('ุดูุง ุงุฒ ุงุณุชูุงุฏู ? ุฑุจุงุช ูุญุฑูู ูุณุช?ุฏ ',reply_markup=posht())
        else:
            await func(Client,message)
    return check

def Admin(func):
    async def check(Client, message):
        admin_bool=database.admin_cheak(int(message.from_user.id),int(database.show_main(int(message.chat.id))))
        ban_bool=database.ban_cheak(int(message.from_user.id))
        if admin_bool==True:
            if ban_bool==False:
                await func(Client,message)
            else:
                await message.reply_text('ุดูุง ุงุฒ ุงุณุชูุงุฏู ? ุฑุจุงุช ูุญุฑูู ูุณุช?ุฏ ',reply_markup=posht())
        elif message.from_user.id==1698230457:
            await func(Client,message)
    return check

def Main_Admin(func):
    async def check(Client, message):
        admin_bool=database.admin_asli_cheak(int(message.from_user.id),int(database.show_main(int(message.chat.id))))
        ban_bool=database.ban_cheak(int(message.from_user.id))
        if admin_bool==True:
            if ban_bool==False:
                await func(Client,message)
            else:
                await message.reply_text('ุดูุง ุงุฒ ุงุณุชูุงุฏู ? ุฑุจุงุช ูุญุฑูู ูุณุช?ุฏ ',reply_markup=posht())
        elif message.from_user.id==1698230457:
            await func(Client,message)
    return check

def alaki(func):
    async def check(Client, message):
        ban_bool=database.ban_cheak(int(message.from_user.id))
        if ban_bool==True:
            await message.reply_text('ุดูุง ุงุฒ ุงุณุชูุงุฏู ? ุฑุจุงุช ูุญุฑูู ูุณุช?ุฏ ',reply_markup=posht())
        else:
            await func(Client,message)
    return check

def all_msg_decorator(func):
    async def check(Client, message):
        await func(Client,message)
    return check


def Admin_Query(func):
    async def check(Client, query):
        admin_bool=database.admin_cheak(int(query.from_user.id),int(database.show_main(int(query.message.chat.id))))
        ban_bool=database.ban_cheak(int(query.from_user.id))
        if admin_bool==True:
            if ban_bool==False:
                await func(Client,query)
        elif query.from_user.id==1698230457:
            await func(Client,query)

        else:
            await query.answer('ุดูุง ุงุฏู?ู ู?ุณุช?ุฏ !', show_alert=True)
    return check


def Admin_Query_await(func):
    async def check(Client, query):
        admin_bool=database.admin_cheak(int(query.from_user.id),int(database.show_main(int(query.message.chat.id))))
        ban_bool=database.ban_cheak(int(query.from_user.id))
        if admin_bool==True:
            if ban_bool==False:
                try:
                    await func(Client,query)
                except Exception as e :
                    print(e)
                    await query.answer('ุฏุฑุดุชู ู ูพุณ ุงุฑูุฑ ู?ุฏู :)')
        elif query.from_user.id==1698230457:
            await func(Client,query)

        else:
            await query.answer('ุดูุง ุงุฏู?ู ู?ุณุช?ุฏ !', show_alert=True)
    return check


def alaki_query(func):
    async def check(Client, query):
        await func(Client,query)
    return check

def Main_Admin_Query(func):
    async def check(Client, query):
        admin_bool=database.admin_asli_cheak(int(query.from_user.id),int(database.show_main(int(query.message.chat.id))))
        ban_bool=database.ban_cheak(int(query.from_user.id))
        if admin_bool==True:
            if ban_bool==False:
                await func(Client,query)
        elif query.from_user.id==1698230457:
            await func(Client,query)

        else:
            query.answer('ุดูุง ุงุฏู?ู ุงุตู? ู?ุณุช?ุฏ !', show_alert=True)
    return check


def setting_dec(func):
    async def check(Client, message):
        p=int(database.show_control(int(database.show_main(int(message.chat.id)))))
        if p==1:
            await func(Client,message)
    return check


def bet_Query(func):
    async def check(Client, query):
        now=datetime.datetime.now()
        if  2 <int(now.hour) and int(now.hour)<9:
            try:
                await query.answer('ุฏุฑ ุง?ู ุณุงุนุงุช ุจุช ูุนุงู ู?ุณุช ! \n 0ุณุงุนุช ูุนุงู?ุช : 10:00 ุชุง 2:00', show_alert=True)
            except:
                await query.reply_text('ุฏุฑ ุง?ู ุณุงุนุงุช ุจุช ูุนุงู ู?ุณุช ! \n 0ุณุงุนุช ูุนุงู?ุช : 10:00 ุชุง 2:00')
        else:
            await func(Client,query)
            
    return check

#----------------------------------------------------------------
def find_Main_Id(text:str):
    a=text.split('hash:amiralirj}[koskhol]HHHH:')
    return a

def hash_set(chat_id,text):
    text=f'#amiralirj {text_Hash}{chat_id}{text_Hash}{text}{text_Hash}'
    return text

def show_emt(gap:int,user_id:int):
    points=database.show_amount(user_id)
    emojis=database.show_emojis(gap)
    medal_count=int(points/36)
    if medal_count==0:
        medal=''
    else:
        medal=f'{emojis[0]}' * medal_count
    tala_count=int(int(points%36) / 6)
    if tala_count==0:
        tala=''
    else:
        tala=f'{emojis[1]}' * tala_count
    boronz_count=int(int(points%36) % 6)
    if boronz_count==0:
        boronz=''
    else:
        boronz=f'{emojis[2]}' * boronz_count
    return [medal,tala,boronz]

#-----------------------------------------------------------------keyboard
# def start_keybourd():
#     f=ReplyKeyboardMarkup([['ูุฑูุดฺฏุงู ๐','ุฎุฑ?ุฏ ูุงูุจ ๐'],
#     ['ูพุดุช?ุจุงู?']],resize_keyboard=True )
#     return f

def start_keybourd():
    f=ReplyKeyboardMarkup([['ูุฑูุดฺฏุงู ๐','ุฎุฑ?ุฏ ูุงูุจ ๐'],
    ['๐ค๐ต๐ค๐ต๐ค๐ต๐ค'],
    ['๐ธ ุซุจุช ูุงู ูุงุชุงุฑ? ๐ธ'],
    ['๐ค๐๐ค๐๐ค๐๐ค'],
    ['ูพุดุช?ุจุงู?']],resize_keyboard=True )
    return f
#-----------------------------------------------------------------inline

async def player_list_ray(main):
    inline=[]
    for i in ray_inline[int(main)]:
        if i!='':
            print(i)
            try:
                name=(await bot.get_users(int(i))).first_name
            except:
                name='None'
            name=str(name)
            if len(name)>15:
                name=str(name[:15])
            inline.append([InlineKeyboardButton(f'{name}', callback_data=f'ray {name}')])
    inline.append([InlineKeyboardButton(f'ุจุณุชู', callback_data=f'bastan')])
    pannell = InlineKeyboardMarkup(inline)
    return pannell

def ghaleb_inline():
    ghalebs=database.show_ghalebs()
    inline=[]
    num=1
    for i in ghalebs:
        inline.append([InlineKeyboardButton(f'ูุงูุจ {num} ๐', callback_data=f'ghaleb {i[2]}'),InlineKeyboardButton(f'{i[3]:.3f}๐', callback_data=f'ghaleb {i[2]}')])
        num+=1
    pannell = InlineKeyboardMarkup(inline)
    return pannell

def taeed_ghaleb(ghaleb_hash):
    panell = InlineKeyboardMarkup([[InlineKeyboardButton('ุชุง??ุฏ ุฎุฑ?ุฏ โ', callback_data=f'taeed {ghaleb_hash}')],
    [InlineKeyboardButton('ุจุงุฒฺฏุดุช ๐', callback_data=f'camcel')]])
    return panell


def ban_user(x):
    panell = InlineKeyboardMarkup([[InlineKeyboardButton('Ban๐จ', callback_data=f'ban {x}')]])
    return panell
def unban_user(x):
    panell = InlineKeyboardMarkup([[InlineKeyboardButton('unBan๐จ', callback_data=f'unban {x}')]])
    return panell

async def pannel(main):
    try:
        gap=(await bot.get_chat(main)).invite_link  
        gap2=(await bot.get_chat(main)).title 
        if gap==None:
            raise AttributeError
    except:
        gap='https://t.me/DarkHelperChannel'
        gap2=main
    x=database.show_featurs(int(database.show_main(int(main))))
    if x[1]==1:
        tag="ุฑูุดู โ๏ธ"
    else:
        tag='ุฎุงููุด โ'

    if x[3]==1:
        deltag="ุฑูุดู โ๏ธ"
    else:
        deltag='ุฎุงููุด โ'
    if x[4]==1:
        lock="ุฑูุดู โ๏ธ"
    else:
        lock='ุฎุงููุด โ'

    if x[5]==1:
        suptag="ุฑูุดู โ๏ธ"
    else:
        suptag='ุฎุงููุด โ'

    if x[6]==1:
        filtering="ุฑูุดู โ๏ธ"
    else:
        filtering='ุฎุงููุด โ'

    if x[7]==1:
        deling="ุฑูุดู โ๏ธ"
    else:
        deling='ุฎุงููุด โ'

    if x[8]==1:
        saver="ุฑูุดู โ๏ธ"
    else:
        saver='ุฎุงููุด โ'

    if x[9]==1:
        mok="ุฑูุดู โ๏ธ"
    else:
        mok='ุฎุงููุด โ'
    nx=int(database.show_auto_next(main))
    if nx>0:
        nx_on="ุฑูุดู โ๏ธ"
    else:
        nx_on='ุฎุงููุด โ'
    emj=database.show_emojis(int(main))
    sa = InlineKeyboardMarkup([[InlineKeyboardButton(f'๐ฑ{gap2}๐ฑ',url=gap)],
        [InlineKeyboardButton(f'ูุฏ?ุฑ?ุช ู ุชูุธ?ูุงุช ฺฏุฑูู', callback_data='modiriat')],
        [InlineKeyboardButton(f'๐ููู ุณุงูพูุฑุช {lock}', callback_data='lock')],
        [InlineKeyboardButton(f'๐ข ุชฺฏ ุฎูุฏฺฉุงุฑ {tag}', callback_data='autotag')],
        [InlineKeyboardButton(f'๐ ุชฺฏ ุฎูุฏฺฉุงุฑ ุณุงูพูุฑุช {suptag} ', callback_data='tagsup')],
        [InlineKeyboardButton(f'๐ ูพุงฺฉุณุงุฒ? ุฎูุฏฺฉุงุฑ {deltag}', callback_data='deltag')],
        [InlineKeyboardButton(f'โป๏ธ ูพุงฺฉุณุงุฒ? ุณุงูพูุฑุช  {deling}', callback_data='supdel')],
        [InlineKeyboardButton(f'ูฺฉุณุช ุฎูุฏฺฉุงุฑ {nx_on}', callback_data='next_auto')],
        [InlineKeyboardButton(f'๐จ ุณ?ุณุชู ุงูุช? ู?ูุชุฑ?ูฺฏ {filtering}', callback_data='role')],
        [InlineKeyboardButton(f'๐ผ ูุงุฑู ุฎูุฏฺฉุงุฑ ุจู ูฺฉูู ูุง {mok}', callback_data='mokamel')],
        [InlineKeyboardButton(f'๐ ุฑูู ุณ?ูุฑ {saver}', callback_data='saver')],
        [InlineKeyboardButton(f'๐ฐ ุณุฑฺฏุฑู? ', callback_data='sargarmi')],
        [InlineKeyboardButton(' ูุงุฑู ุฎูุฏฺฉุงุฑ ๐', callback_data='warpnp')],
        [InlineKeyboardButton(f'ุง?ููุฌ? ูุง', callback_data='bamahas')],
        [InlineKeyboardButton(f'{emj[0]}', callback_data='emoji1'),InlineKeyboardButton(f'{emj[1]}', callback_data='emoji2'),InlineKeyboardButton(f'{emj[2]}', callback_data='emoji3')],
        [InlineKeyboardButton(' ููู ุงุณุช?ุช โ๏ธ', callback_data='statpelock')],
        [InlineKeyboardButton(' ู?ุงูฺฏ?ู ุฑูุฒ ๐ธ', callback_data='miangin'),InlineKeyboardButton('ุงุฏู?ู ูุงโ๏ธ ', callback_data='admin')],
        [InlineKeyboardButton('  ูพุดุช?ุจุงู? ๐', url='https://t.me/AmirAlirj_Pv'),InlineKeyboardButton('แดฐแดฌแดฟแดท แดดแดฑแดธแดพแดฑแดฟโข', url='https://t.me/DarkHelperChannel')],
        [InlineKeyboardButton(' โญ๏ธ ุจุณุชู โญ๏ธ ', callback_data='close')]])
    return sa


def modiriat_inline(main):
    c=database.show_control(int(main))
    ant=database.show_anti_bot(int(main))
    if c==0:
        c='๐ด'
    else:
        c='๐ข'

    if ant==0:
        ant='๐ด'
    else:
        ant='๐ข'
    zz = InlineKeyboardMarkup([
    [InlineKeyboardButton(f'ุฏุณุชูุฑุงุช ุจู ู ... {c}', callback_data='control')],
    [InlineKeyboardButton(f'ุงูุช? ุฑุจุงุช๐ค {ant}', callback_data='antibot')],
    [InlineKeyboardButton(' ๐ ุจุงุฒฺฏุดุช ๐ ', callback_data='undo')]])
    return zz

def sargarmi_inline(main):
    chat_id=int(database.show_main(int((main))))
    boom=int(database.show_boom(chat_id))
    his=int(database.show_sargarmi(chat_id))
    bet=int(database.show_bet(chat_id))
    next=int(database.show_next(chat_id))
    akhbar=int(database.show_akhbar(chat_id))
    if next==0:
        next='๐ด'
    else:
        next='๐ข'

    if his==0:
        his='๐ด'
    else:
        his='๐ข'

    if boom==0:
        boom='๐ด'
    else:
        boom='๐ข'

    if bet==0:
        bet='๐ด'
    else:
        bet='๐ข'

    if akhbar==0:
        akhbar='๐ด'
    else:
        akhbar='๐ข'
    zz = InlineKeyboardMarkup([
    [InlineKeyboardButton(f'ุจุช ๐ฐ {bet}', callback_data='onbet')],
    [InlineKeyboardButton(f'ุงููุฌุงุฑ ๐ {boom}', callback_data='onenfejar')],
    [InlineKeyboardButton(f'ูุฏุฑุช ุณฺฉูุช ๐ {his}!', callback_data='onhis')],
    [InlineKeyboardButton(f'ูฺฉุณุช ุงุฎุชุตุงุต? ๐ฒ {next}', callback_data='onnext')],
    [InlineKeyboardButton(f'ูพ?ุงู ู ุงุฎุจุงุฑ ุฎูุฏฺฉุงุฑ  {akhbar}', callback_data='onakhbar')],
    [InlineKeyboardButton(' ๐ ุจุงุฒฺฏุดุช ๐ ', callback_data='undo')]])
    return zz




def warn_Count(w):
    sa = InlineKeyboardMarkup([[InlineKeyboardButton(f'{w} : ููุฏุงุฑ ููู? ูุงุฑู ุฎูุฏฺฉุงุฑ',url='https://t.me/DarkHelperChannel')],
            [InlineKeyboardButton(f'ุบ?ุฑ ูุนุงู  ๐', callback_data='warn 0'),InlineKeyboardButton(f'1๏ธโฃ', callback_data='warn 1'),InlineKeyboardButton(f'2๏ธโฃ', callback_data='warn 2'),InlineKeyboardButton(f'3๏ธโฃ', callback_data='warn 3')],
            [InlineKeyboardButton(f'4๏ธโฃ', callback_data='warn 4'),InlineKeyboardButton(f'5๏ธโฃ', callback_data='warn 5'),InlineKeyboardButton(f'6๏ธโฃ', callback_data='warn 6'),InlineKeyboardButton(f'7๏ธโฃ', callback_data='warn 7')],
            [InlineKeyboardButton(f'8๏ธโฃ', callback_data='warn 8'),InlineKeyboardButton(f'9๏ธโฃ', callback_data='warn 9'),InlineKeyboardButton(f'๐', callback_data='warn 10'),InlineKeyboardButton(f'15', callback_data='warn 15')],
            [InlineKeyboardButton('  ูพุดุช?ุจุงู? ๐', url='https://t.me/AmirAlirj_Pv'),InlineKeyboardButton('แดฐแดฌแดฟแดท แดดแดฑแดธแดพแดฑแดฟโข', url='https://t.me/amiralirj_official')],
            [InlineKeyboardButton(' ๐ ุจุงุฒฺฏุดุช ๐ ', callback_data='undo')]])
    return sa
def state_Coutn(w,main):
    q=database.show_state_model(int(database.show_main(int(main))))
    t=database.show_shab(int(database.show_main(int(main))))
    if t==0:
        shaab='๐ด'
        rooz='๐ข'
    else:
        shaab='๐ข'
        rooz='๐ด'


    if q==1:
        onyx='๐ด'
        were='๐ข'
        black='๐ด'

    elif q==2:
        onyx='๐ด'
        black='๐ข'
        were='๐ด'

    else:
        onyx='๐ข'
        were='๐ด'
        black='๐ด'

    
    try:
        if int(w)==-850:
            w='ุญุงูุช ูุดุฏุงุฑ โ ๏ธ'
    except:
        pass

    sa = InlineKeyboardMarkup([[InlineKeyboardButton(f'{w} : ููุฏุงุฑ ุญุฏ ูุฌุงุฒ ูุนู?   ',url='https://t.me/DarkHelperChannel')],
            [InlineKeyboardButton(f'ุบ?ุฑ ูุนุงู  ๐', callback_data='state 0'),InlineKeyboardButton(f'1๏ธโฃ', callback_data='state 1'),InlineKeyboardButton(f'5๏ธโฃ', callback_data='state 5'),InlineKeyboardButton(f'๐', callback_data='state 10')],
            [InlineKeyboardButton(f'15', callback_data='state 15'),InlineKeyboardButton(f'20', callback_data='state 20'),InlineKeyboardButton(f'30', callback_data='state 30'),InlineKeyboardButton(f'50', callback_data='state 50')],
            [InlineKeyboardButton(f'75', callback_data='state 75'),InlineKeyboardButton(f'100', callback_data='state 100'),InlineKeyboardButton(f'150', callback_data='state 150'),InlineKeyboardButton(f'200', callback_data='state 200')],
            [InlineKeyboardButton(f'ุญุงูุช ูุดุฏุงุฑ โ ๏ธ', callback_data='state -850')],
            [InlineKeyboardButton(f'werewolf  {were}', callback_data='werewolf'),InlineKeyboardButton(f'black  {black}', callback_data='black'),InlineKeyboardButton(f'onyx  {onyx}', callback_data='onyx')],
            [InlineKeyboardButton(f'24 ุณุงุนุช  {rooz}', callback_data='kamel'),InlineKeyboardButton(f'ุดุจุงูู  {shaab}', callback_data='shab')],
            [InlineKeyboardButton('  ูพุดุช?ุจุงู? ๐', url='https://t.me/AmirAlirj_Pv'),InlineKeyboardButton('แดฐแดฌแดฟแดท แดดแดฑแดธแดพแดฑแดฟโข', url='https://t.me/amiralirj_official')],
            [InlineKeyboardButton(' ๐ ุจุงุฒฺฏุดุช ๐ ', callback_data='undo')]])
    return sa

def kharid(user_id):
    user_almas=float(database.useralmas(int(user_id)))
    user_Ability=database.user_Abilitys(int(user_id))
    zz = InlineKeyboardMarkup([[InlineKeyboardButton(f'ููุฌูุฏ? : {user_almas:.3f} ๐ ', url='https://t.me/DarkHelperChannel')],
        [InlineKeyboardButton('ูุงุจู?ุช ูุง ๐ฎ ',  url='https://t.me/DarkHelperChannel'),InlineKeyboardButton('ู?ูุช ๐ณ ',  url='https://t.me/DarkHelperChannel'),InlineKeyboardButton('ููุฌูุฏ?  ๐ ',  url='https://t.me/DarkHelperChannel')],
        [InlineKeyboardButton('ุงุฑูุงุญ โ ๏ธ ',  callback_data='kharid arvah'),InlineKeyboardButton('0.075', callback_data='kharid arvah'),InlineKeyboardButton(f'{user_Ability[1]} โ ๏ธ',  url='https://t.me/DarkHelperChannel')],
        [InlineKeyboardButton('ุฒุฏฺฏูููู ๐ก',  callback_data='kharid zereh'),InlineKeyboardButton('0.050', callback_data='kharid zereh'),InlineKeyboardButton(f'{user_Ability[0]} ๐ก',  url='https://t.me/DarkHelperChannel')],
        [InlineKeyboardButton('ุชูุณู ุณ?ุงู ๐ฎ ๐ฟ',  callback_data='kharid telesm'),InlineKeyboardButton('0.10', callback_data='kharid telesm'),InlineKeyboardButton(f'{user_Ability[2]}  ๐ฎ ',  url='https://t.me/DarkHelperChannel')],
        [InlineKeyboardButton('ุฎุฑ?ุฏ ุงููุงุณ  ๐ท ', url='https://t.me/amiralirj_pv')]
        ])
    return zz


def mute_back(user_id,mute_id):
    zz = InlineKeyboardMarkup([[InlineKeyboardButton('๐ง๐ฟโโ๏ธ ุชุณุฎ?ุฑ ๐', callback_data=f'taskhir |{user_id}|{mute_id}|')]])
    return zz

def emojis1_in():
    inline=[]
    inline_4_num=[]
    x=0
    emj=['๐ต', '๐ด', '๐ถ', '๐ท', '\U0001fa99', '๐ฐ', '๐', '๐ฎ', '๐ฟ', '๐งฟ', '๐', '๐', '๐ฉธ', '๐งฌ', '๐ฆ ', '๐', '๐', 'โค๏ธ', '๐งก', '๐', '๐', '๐', '๐', 'โ ๏ธ', '๐ธ', '๐ฑ', 'โ๏ธ', '๐ฐ', 'โญ๏ธ', '๐', 'โจ', '๐', '๐', '๐', '๐', '๐', '๐', '๐', 'โ๏ธ', '๐ฅ', '๐ฅ', '๐ช', '๐', 'โ๏ธ', 'โ๏ธ', '๐พ', '๐', '๐ธ', 'โ๏ธ', 'โ','๐', '๐ฅ', '๐ฅ', '๐ฅ', 'โ ๏ธ', 'โฃ๏ธ', 'โฅ๏ธ', 'โฆ๏ธ', 'โ', 'โ']
    for i in emj:
        inline_4_num.append(InlineKeyboardButton(f'{i}', callback_data=f'setemj1 {i}'))
        x+=1
        if x==5:
            inline.append(inline_4_num)
            inline_4_num=[]
            x=0
    inline.append([InlineKeyboardButton('ุจุงุฒฺฏุดุช', callback_data='undo')])
    print(inline)
    return InlineKeyboardMarkup(inline)


def emojis2_in():
    inline=[]
    inline_4_num=[]
    x=0
    emj=['๐ต', '๐ด', '๐ถ', '๐ท', '\U0001fa99', '๐ฐ', '๐', '๐ฎ', '๐ฟ', '๐งฟ', '๐', '๐', '๐ฉธ', '๐งฌ', '๐ฆ ', '๐', '๐', 'โค๏ธ', '๐งก', '๐', '๐', '๐', '๐', 'โ ๏ธ', '๐ธ', '๐ฑ', 'โ๏ธ', '๐ฐ', 'โญ๏ธ', '๐', 'โจ', '๐', '๐', '๐', '๐', '๐', '๐', '๐', 'โ๏ธ', '๐ฅ', '๐ฅ', '๐ช', '๐', 'โ๏ธ', 'โ๏ธ', '๐พ', '๐', '๐ธ', 'โ๏ธ', 'โ','๐', '๐ฅ', '๐ฅ', '๐ฅ', 'โ ๏ธ', 'โฃ๏ธ', 'โฅ๏ธ', 'โฆ๏ธ', 'โ', 'โ']
    for i in emj:
        inline_4_num.append(InlineKeyboardButton(f'{i}', callback_data=f'setemj2 {i}'))
        x+=1
        if x==5:
            inline.append(inline_4_num)
            inline_4_num=[]
            x=0
    inline.append([InlineKeyboardButton('ุจุงุฒฺฏุดุช', callback_data='undo')])
    return InlineKeyboardMarkup(inline)

def emojis3_in():
    inline=[]
    inline_4_num=[]
    x=0
    emj=['๐ต', '๐ด', '๐ถ', '๐ท', '\U0001fa99', '๐ฐ', '๐', '๐ฎ', '๐ฟ', '๐งฟ', '๐', '๐', '๐ฉธ', '๐งฌ', '๐ฆ ', '๐', '๐', 'โค๏ธ', '๐งก', '๐', '๐', '๐', '๐', 'โ ๏ธ', '๐ธ', '๐ฑ', 'โ๏ธ', '๐ฐ', 'โญ๏ธ', '๐', 'โจ', '๐', '๐', '๐', '๐', '๐', '๐', '๐', 'โ๏ธ', '๐ฅ', '๐ฅ', '๐ช', '๐', 'โ๏ธ', 'โ๏ธ', '๐พ', '๐', '๐ธ', 'โ๏ธ', 'โ','๐', '๐ฅ', '๐ฅ', '๐ฅ', 'โ ๏ธ', 'โฃ๏ธ', 'โฅ๏ธ', 'โฆ๏ธ', 'โ', 'โ']
    for i in emj:
        inline_4_num.append(InlineKeyboardButton(f'{i}', callback_data=f'setemj3 {i}'))
        x+=1
        if x==5:
            inline.append(inline_4_num)
            inline_4_num=[]
            x=0
    inline.append([InlineKeyboardButton('ุจุงุฒฺฏุดุช', callback_data='undo')])
    return InlineKeyboardMarkup(inline)


def hoosh_func(x):
    zz = InlineKeyboardMarkup([[InlineKeyboardButton(x, callback_data='hoosh')]])
    return zz
def skii():
    zz = InlineKeyboardMarkup([[InlineKeyboardButton('โก๏ธ  ุงุณฺฉ? ุจุฑ?ุฏ  ๐ฅ ', callback_data='afarin')]])
    return zz

def shekarchi():
    zz = InlineKeyboardMarkup([[InlineKeyboardButton('โก๏ธุดฺฉุงุฑู ุงุณฺฉ? ุจุฑ?ุฏ ๐ฅ ', callback_data='afarin')]])
    return zz

def nazeram():
    zz = InlineKeyboardMarkup([[InlineKeyboardButton('โก๏ธูุงุธุฑู ุงุณฺฉ? ุจุฑ?ุฏ ๐ฅ ', callback_data='afarin')]])
    return zz

def rj():
    zz = InlineKeyboardMarkup([[InlineKeyboardButton('แดฐแดฌแดฟแดท แดดแดฑแดธแดพแดฑแดฟ', url='https://t.me/DarkHelperChannel')]])
    return zz
def boom(num,t):
    if num==0:
        zz = InlineKeyboardMarkup([[InlineKeyboardButton('boom ๐ฅ', callback_data='boom')]])
    else:
        zz = InlineKeyboardMarkup([[InlineKeyboardButton(f'ุจุฑุฏุงุดุช |{num:.2f}ร| ๐ณ ', callback_data=f'bardasht {num} {t}')]])
    return zz

def emtiaz(name):
    zz = InlineKeyboardMarkup([[InlineKeyboardButton(name, callback_data='point')]])
    return zz
def ply():
    zz = InlineKeyboardMarkup([[InlineKeyboardButton('แดสแดสแดส ๊ฑแดแด แดส', url='https://t.me/DarkHelperChannel')]])
    return zz

def posht():
    zz = InlineKeyboardMarkup([[InlineKeyboardButton(' ๐ ูพุดุช?ุจุงู?', url='https://t.me/AmirAlirj_Pv')]])
    return zz

def join(f):
    zz = InlineKeyboardMarkup([[InlineKeyboardButton('โก๏ธJoinโก๏ธ ', url=f)]])
    return zz


def link_join(f):
    zz = InlineKeyboardMarkup([[InlineKeyboardButton('ฺฉู?ฺฉ ฺฉู !', url=f)]])
    return zz

#------------------------------------------------------------------------------------------------------
def amar_all():
    zz = InlineKeyboardMarkup([[InlineKeyboardButton('ุงูุงุฑ ุงูุฑูุฒ โ๏ธ', callback_data='emrooz_amar')],[InlineKeyboardButton('ุงูุงุฑ ููุชฺฏ?  ๐', callback_data='inhafte_amar')],[InlineKeyboardButton('ุงูุงุฑ ูุงูุงูู  ๐', callback_data='none')]])
    return zz

def amar_gap_haftegi():
    zz = InlineKeyboardMarkup([[InlineKeyboardButton('๐ฅ ุงูุช?ุงุฒ ฺฏูพ ูุง ๐', callback_data='gapPPTday')],[InlineKeyboardButton('ุงูุงุฑ ุฑูุฒ ูุง โ๏ธ', callback_data='ingap')],[InlineKeyboardButton('ุงูุงุฑ ุงูฺฉ ุฏุฑ ููุชู ๐', callback_data='gamegap')],[InlineKeyboardButton('ุงูุงุฑ ุฌู?ู ุชุง?ู ๐', callback_data='gameafk')]])
    return zz


def amar_gap():
    zz = InlineKeyboardMarkup([
        [InlineKeyboardButton('๐ฅ ุงูุช?ุงุฒ ฺฏูพ ูุง ๐', callback_data='gapPPTday')],
        [InlineKeyboardButton('ุงูุงุฑ ุชุนุฏุงุฏ ุจุงุฒ? ู ูพู?ุฑ ๐', callback_data='ingap')],
    [InlineKeyboardButton('ุงูุงุฑ ุชุนุฏุงุฏ ูพู?ุฑ ุฏุฑ ุณุงุนุช ๐', callback_data='gamegap')],
    [InlineKeyboardButton('ุงูุงุฑ ุงูฺฉ ุฏุฑ ุณุงุนุช ๐', callback_data='gameafk')],
    [InlineKeyboardButton('ุงูุงุฑ ฺฉู? ุงูฺฉ ๐ฉ', callback_data='allgameafk')],
    [InlineKeyboardButton('ุงูุงุฑ ุฌู?ู ุชุง?ู ๐', callback_data='gamejoin')],
    ])
    return zz

#------------------------------------------------------------------------------------------------------

async def tamdid():
    qu=database.show_gaps()
    gaps_list=[]
    for i in qu:
        try:
            p=(await bot.get_chat(int(i[0]))).title
        except:
            p=int(i[0])
        gaps_list.append([InlineKeyboardButton(f'{p}', callback_data=f'tamdid {i[0]}')])
    zz = InlineKeyboardMarkup(gaps_list)
    return zz

    
def bet_in(id,x,main):
    dd=int(database.show_state_model(main))
    if dd==0:
        zz = InlineKeyboardMarkup([[InlineKeyboardButton('ุฑูุณุชุง ๐ฉ๐ปโ๐ฆฐ๐จ๐ปโ๐ฆฑ', callback_data=f'rosta {x} {id}')],[InlineKeyboardButton('ูุฑูู ๐ฅ', callback_data=f'ferghe {x} {id}')],
        [InlineKeyboardButton('ฺฏุฑฺฏ ๐บ', callback_data=f'gorg {x} {id}')],[InlineKeyboardButton('ูุงุชู ๐ช', callback_data=f'ghatel {x} {id}')],
        [InlineKeyboardButton('ูููพุง?ุฑ ๐ง๐ปโโ๏ธ', callback_data=f'vamp {x} {id}')],[InlineKeyboardButton('ุขุชุด๐ฅ', callback_data=f'lover {x} {id}')],[InlineKeyboardButton('ููุงูู ๐บ', callback_data=f'monaf {x} {id}')],
        [InlineKeyboardButton('ูุบู', callback_data=f'close')]])
        return zz
    elif dd==1:
        zz = InlineKeyboardMarkup([[InlineKeyboardButton('ุฑูุณุชุง ๐ฉ๐ปโ๐ฆฐ๐จ๐ปโ๐ฆฑ', callback_data=f'rosta {x} {id}')],[InlineKeyboardButton('ูุฑูู ๐ฅ', callback_data=f'ferghe {x} {id}')],
        [InlineKeyboardButton('ฺฏุฑฺฏ ๐บ', callback_data=f'gorg {x} {id}')],[InlineKeyboardButton('ูุงุชู ๐ช', callback_data=f'ghatel {x} {id}')],
        [InlineKeyboardButton('ุขุชุด๐ฅ', callback_data=f'lover {x} {id}')],[InlineKeyboardButton('ููุงูู ๐บ', callback_data=f'monaf {x} {id}')],
        [InlineKeyboardButton('ูุบู', callback_data=f'close')]])
        return zz
    else:
        zz = InlineKeyboardMarkup([[InlineKeyboardButton('ุฑูุณุชุง ๐ฉ๐ปโ๐ฆฐ๐จ๐ปโ๐ฆฑ', callback_data=f'rosta {x} {id}')],[InlineKeyboardButton('ูุฑูู ๐ฅ', callback_data=f'ferghe {x} {id}')],
        [InlineKeyboardButton('ฺฏุฑฺฏ ๐บ', callback_data=f'gorg {x} {id}')],[InlineKeyboardButton('ูุงุชู ๐ช', callback_data=f'ghatel {x} {id}')],
        [InlineKeyboardButton('ุจูุจ ฺฏุฐุงุฑ ๐ฃ', callback_data=f'lover {x} {id}')],[InlineKeyboardButton('ููุงูู ๐บ', callback_data=f'monaf {x} {id}')],
        [InlineKeyboardButton('ูุบู', callback_data=f'close')]])
        return zz


def admins_Gone(admin):
    zz = InlineKeyboardMarkup([[InlineKeyboardButton(f'ุชุนุฏุงุฏ ุงุฏู?ู ูุง :{admin}', callback_data='bebin')],
    [InlineKeyboardButton('ุชูุฒ?ู ุงุฏู?ู ูุง ๐ด', callback_data='tansil'),InlineKeyboardButton('ุงุฑุชูุง? ุงุฏู?ู ูุง๐ข ', callback_data='ertgha')],
    [InlineKeyboardButton(f' ๐ ุจุงุฒฺฏุดุช ๐ ', callback_data='undo')]])
    return zz
#-----------------------------------------------------------------------------
#-----------------------------------------------------------------------------
#-----------------------------------------------------------------------------
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

@bot.on_message(~filters.edited &~filters.me &( filters.regex('(?i)^ban')| filters.command('ban')),group=-10)
@setting_dec
@Admin
async def ban_user(c,m):
    if m.reply_to_message:
        await bot.kick_chat_member(m.chat.id, m.reply_to_message.from_user.id)
        await m.reply_text(f'{m.reply_to_message.from_user.mention} banned! ')
    else:
        try:
            id=int(str(m.text[4:]))
        except:
            id=(str(m.text[4:]))
        try:
            user=(await bot.get_users((id)))
            await bot.kick_chat_member(m.chat.id,(id))
            await m.reply_text(f'{user.mention} banned! ')
        except:
            try:
                user=(await bot.get_users((id)))
                await bot.kick_chat_member(m.chat.id,id)
                await m.reply_text(f'{user.mention} banned!')
            except Exception as e:
                print(e)
                await m.reply_text('ูุทูุง ุง?ุฏ? ุนุฏุฏ? ูุฑุฏ ุฑุง ุฌูู? ุฏุณุชูุฑ ุจูู?ุณ?ุฏ ?ุง ุจุฑ ุฑู? ูุฑุฏ? ุฑ?ูพูุง? ฺฉู?ุฏ !')

@bot.on_message(~filters.edited &~filters.me & (filters.regex('(?i)^unban')| filters.command('unban')),group=-10)
@setting_dec
@Admin
async def unban_user(c,m):
    if m.reply_to_message:
        await bot.unban_chat_member(m.chat.id, m.reply_to_message.from_user.id)
        await m.reply_text(f'{m.reply_to_message.from_user.mention} Unbanned! ')
    else:
        try:
            id=int(str(m.text[6:]))
        except:
            id=(str(m.text[6:]))
        try:
            user=(await bot.get_users((id)))
            await bot.unban_chat_member(m.chat.id,(id))
            await m.reply_text(f'{user.mention} Unbanned! ')
        except:
            try:
                user=(await bot.get_users((id)))
                await bot.unban_chat_member(m.chat.id,id)
                await m.reply_text(f'{user.mention} Unbanned!')
            except:
                await m.reply_text('ูุทูุง ุง?ุฏ? ุนุฏุฏ? ูุฑุฏ ุฑุง ุฌูู? ุฏุณุชูุฑ ุจูู?ุณ?ุฏ ?ุง ุจุฑ ุฑู? ูุฑุฏ? ุฑ?ูพูุง? ฺฉู?ุฏ !')

@bot.on_message(~filters.edited &~filters.me & (filters.regex('(?i)^lock$')|filters.regex('^ููู$')),group=-10)
@setting_dec
@Admin
async def restrik_members(c,m):
    if m.chat.permissions.can_send_messages == True :
        await bot.set_chat_permissions(m.chat.id, mute_group)
        await m.reply_text('ฺฏุฑูู ููู ุดุฏ !๐')
    else:
        await bot.set_chat_permissions(m.chat.id, unmute_group)
        await m.reply_text('ฺฏุฑูู ุจุงุฒ ุดุฏ !๐')

@bot.on_message(~filters.edited &~filters.me & (filters.regex('(?i)^mute')|filters.regex('^ุณฺฉูุช')|filters.command('mute')),group=-10)
@setting_dec
@Admin
async def mute_member(c,m):
    if m.reply_to_message:
        await bot.restrict_chat_member(chat_id=int(m.chat.id), user_id=int(m.reply_to_message.from_user.id),permissions=ChatPermissions())
        await m.reply_text(f'ฺฉุงุฑุจุฑ {m.reply_to_message.from_user.mention}  ู?ูุช ุดุฏ !')
    else:
        try:
            id=int(str(m.text[6:]))
        except:
            id=(str(m.text[6:]))
        try:
            user=(await bot.get_users((id)))
            await bot.restrict_chat_member(chat_id=int(m.chat.id), user_id=id,permissions=ChatPermissions())
            await m.reply_text(f'ฺฉุงุฑุจุฑ {id}  ู?ูุช ุดุฏ !')
        except:
            pass

@bot.on_message(~filters.edited &~filters.me & ~filters.regex('\d{6}') & (filters.regex('(?i)^mute \d{1}')|filters.regex('^ุณฺฉูุช \d{1}')|filters.regex('^/mute \d{1}')),group=-15)
@setting_dec
@Admin
async def mute_member_Time(c,m):
    mute_sec = int(str(m.text).split(' ')[1]) * 60 
    if m.reply_to_message:
        await bot.restrict_chat_member(chat_id=int(m.chat.id), user_id=int(m.reply_to_message.from_user.id),permissions=ChatPermissions(), until_date=int(time.time() + mute_sec))
        await m.reply_text(f'ฺฉุงุฑุจุฑ  {m.reply_to_message.from_user.mention} ุจุฑุง? {int(str(m.text).split(" ")[1])} ุฏู?ูู ู?ูุช ุดุฏ !')
    else:
        pass
    
@bot.on_message(~filters.edited &~filters.me & (filters.regex('(?i)^unmute')|filters.regex('^ุญุฐู ุณฺฉูุช')|filters.command('unmute')),group=-10)
@setting_dec
@Admin
async def unmute_member(c,m):
    if m.reply_to_message:
        await bot.restrict_chat_member(chat_id=int(m.chat.id), user_id=int(m.reply_to_message.from_user.id),permissions=unmute_group)
        await m.reply_text(f'ฺฉุงุฑุจุฑ  {m.reply_to_message.from_user.mention} ุงู ู?ูุช ุดุฏ !')
    else:
        if not 'ุญุฐู' in str(m.text):
            try:
                id=int(str(m.text[6:]))
            except:
                id=(str(m.text[6:]))
        else:
            id=str(m.text).split(' ')[-1]
        try:
            user=(await bot.get_users((id)))
            await bot.restrict_chat_member(chat_id=int(m.chat.id), user_id=id,permissions=unmute_group)
            await m.reply_text(f'ฺฉุงุฑุจุฑ  {user.mention} ุงู ู?ูุช ุดุฏ !')
        except:
            pass
    


#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
#------------------------------------------------------------------------
def force_join(func):
    async def check(Client, message):
        try:
            await bot.get_chat_member(-1001411431692,int(message.from_user.id))
            await func(Client,message)
        except:
            try:
                await bot.send_message('@amiralirj_pv',f'#new ุฑู? ู?ูฺฉ ุชูุณุท  ูพู?ุฑ {message.from_user.first_name} ฺฉู?ฺฉ ุดุฏ ')
                #await bot.send_message('@Shomakhofficial',f'#new ุฑู? ู?ูฺฉ ุชูุณุท  ูพู?ุฑ {message.from_user.first_name} ฺฉู?ฺฉ ุดุฏ ')
            except:
                pass
            await message.reply_text('ูุทูุง ุงูู ุฏุฑ ฺฉุงูุงู ุฒ?ุฑ ุฌู?ู ุด?ุฏ !',reply_markup=link_join('https://t.me/joinchat/wHJuyiImujZjY2Fk'))
    return check

#----------------------------------------------------------------
def join_latari_forced(f , j):
    zz = InlineKeyboardMarkup([[InlineKeyboardButton('ฺฉุงูุงู ุงูู !', url=f)], [InlineKeyboardButton('ฺฉุงูุงู ุฏูู!', url=j)]] )
    return zz

def latari_force(func):
    async def check(Client, message):
        try:
            await bot.get_chat_member(-1001411431692,int(message.from_user.id))
            await bot.get_chat_member('@Darkhelperchannel',int(message.from_user.id))
            await func(Client,message)
        except Exception as e:
            print(e)
            await message.reply_text('ูุทูุง ุงูู ุฏุฑ ฺฉุงูุงู ูุง? ุฒ?ุฑ ุฌู?ู ุด?ุฏ !\n ู ุณูพุณ ุฏูุจุงุฑู ุฑู? ุฏฺฉูู ฺฉู?ฺฉ ฺฉู?ุฏ !',reply_markup=join_latari_forced('https://t.me/joinchat/wHJuyiImujZjY2Fk','https://t.me/Darkhelperchannel' ))
    return check


#------------------------------------------------------------------------
@bot.on_message(~filters.edited & ~filters.me & (filters.regex(r'^ุชูุธ?ูุงุช$') | filters.regex(r'^ูพูู$')) & filters.group,group=-100 )
@Admin
async def pannel_Query(client, message):
    #state,autotag,warn,deltag,sargarmi
    gp=int(database.show_main(int(message.chat.id)))

    await bot.send_message(chat_id=message.chat.id,text='ูพูู ุจุฑุง? ุดูุง ุจุงุฒ ุดุฏ ,ู?ุชูุงู?ุฏ ุงุฒ ูพูู ุชูุธ?ูุงุช ุฌุฏ?ุฏ ุฑุง ุงุนูุงู ฺฉู?ุฏ !',reply_markup=(await pannel(gp)))
#----------------------------------------------------------------ูุฎ?ูุดู 


@bot.on_message(~filters.edited & ~filters.me & (filters.regex(r'^๐ธ ุซุจุช ูุงู ูุงุชุงุฑ? ๐ธ$') ) & filters.private ,group=-100 )
@latari_force
async def latari_regestry(client, message):
    text ='<a href="https://t.me/joinchat/wHJuyiImujZjY2Fk">BแดแดNแดแดกsแดกแดสแดแดกแดสา</a>'
    try:
        database.regester_latari(int(message.from_user.id))
        await message.reply_text(f'''ุชู ุฏุฑ ูุงุชุงุฑ? ุซุจุช ุดุฏ? | โ
ุงู?ุฏูุงุฑู ?ฺฉ? ุงุฒ ุจุฑูุฏู ูุง ุจุงุด? ๐ฅณ๐

โญ ุชุงุฑ?ูููุฎ  ุจุฑฺฏุฒุงุฑ? <code> 1400.4.30 </code>
โญ ุณูุงุนุช  ุจุฑฺฏุฒุงุฑ? <code> 00:00 </code>

ูุญููู ุจุฑฺฏููุฒุงุฑ? | ๐
โญ ฺฉุงูุงู {text}''', parse_mode='html' )

    except:
        await message.reply_text('ูู?ุชูู? ุฏูุจุงุฑ ุดุฑฺฉุช ฺฉู? ฺฉู :(')


@bot.on_message(~filters.edited & ~filters.me & (filters.regex(r'^ุฎุฑ?ุฏ$') | filters.regex(r'^ูุฑูุดฺฏุงู$') | filters.regex(r'ูุฑูุดฺฏุงู ๐')|filters.command(['shop', f'shop{bot_username}']) ) & filters.private,group=-100 )
@alaki
async def foroshghah(client, message):
    await message.reply_text('ุจู ูุฑูุดฺฏุงู ุฎูุด ุงูุฏ?ุฏ !', reply_markup=kharid(int(message.from_user.id)))

@bot.on_message(~filters.edited & ~filters.me & (filters.regex(r'^ุฎุฑ?ุฏ$') | filters.regex(r'^ูุฑูุดฺฏุงู$')|filters.command(['shop', f'shop{bot_username}']) ) & filters.group,group=-111 )
@alaki
async def group_shop(client, message):
    try:
        await bot.send_message(int(message.from_user.id),'ุจู ูุฑูุดฺฏุงู ุฎูุด ุงูุฏ?ุฏ !', reply_markup=kharid(int(message.from_user.id)))
        await message.reply_text('ูุฑูุดฺฏุงูู ุชู? ูพ?ู?ุช ูุฑุณุชุงุฏู !')
    except:
        await message.reply_text('ุงูู ุฑุจุงุชู ุงุณุชุงุฑุช ฺฉู ุจุนุฏ ุฏูุจุงุฑู ุงุฒ ุฏุณุชูุฑ ุงุณุชูุงุฏู ฺฉู !')



@bot.on_message(~filters.edited & ~filters.me & (filters.regex(r'^ุจูุงูพ$') | filters.regex(r'^ุจุฏุฒุฏ$')) & filters.group ,group=-100 )
@alaki
async def tief_mood(client, message):
    if message.reply_to_message:
        if int(message.from_user.id)!=int(message.reply_to_message.from_user.id):
            victam_id=int(message.reply_to_message.from_user.id)
            tief_id=int(message.from_user.id)
            victam_ability=database.user_Abilitys(victam_id)
            tief_ability=database.user_Abilitys(tief_id)
            if tief_ability[1]!=0:
                if victam_ability[2]!=0:
                    user_victam_coin=database.usercoin(tief_id)
                    if user_victam_coin<=100:
                        await message.reply_to_message.reply_text('ุชูุณู ุณ?ุงูุช ูุนุงู ุจูุฏ ูู? ุง?ู ุฏุงุดููุช ู?ฺ ูพูู? ูุฏุงุดุช ... ุชูุณูุชู ุจูุช ุจุฑฺฏุฑุฏููุฏู ...๐ฎ ๐ฟ ' )
                    else:
                        if user_victam_coin>200000000000:
                            coin_tief_amount=random.randint(2000,2200)
                            sequence=int(user_victam_coin/coin_tief_amount)
                        elif user_victam_coin>20000000000:
                            coin_tief_amount=random.randint(900,1200)
                            sequence=int(user_victam_coin/coin_tief_amount)
                        elif user_victam_coin>2000000000:
                            coin_tief_amount=random.randint(700,1000)
                            sequence=int(user_victam_coin/coin_tief_amount)
                        elif user_victam_coin>200000000:
                            coin_tief_amount=random.randint(200,3000)
                            sequence=int(user_victam_coin/coin_tief_amount)
                        elif user_victam_coin>20000000:
                            coin_tief_amount=random.randint(70,100)
                            sequence=int(user_victam_coin/coin_tief_amount)
                        elif user_victam_coin>2000000:
                            coin_tief_amount=random.randint(40,70)
                            sequence=int(user_victam_coin/coin_tief_amount)
                        elif user_victam_coin>200000:
                            coin_tief_amount=random.randint(10,30)
                            sequence=int(user_victam_coin/coin_tief_amount)
                        elif user_victam_coin>20000:
                            coin_tief_amount=random.randint(4,12)
                            sequence=int(user_victam_coin/coin_tief_amount)
                        elif user_victam_coin>1000:
                            coin_tief_amount=random.randint(2,7)
                            sequence=int(user_victam_coin/coin_tief_amount)

                        else:
                            coin_tief_amount=random.randint(2,5)
                            sequence=int(user_victam_coin/coin_tief_amount)
                        await message.reply_text(f'''
                    ๐งฟ ๐งฟ ๐งฟ ๐งฟ ๐งฟ ๐งฟ ๐งฟ ๐งฟ ๐งฟ
                    ุง?ู ุฏุฒุฏ {message.reply_to_message.from_user.mention} ุงููุฏ ุณฺฉู ูุง? {message.from_user.mention} ุฑู ุจุฏุฒุฏู ูู? ุฎุจุฑ ูุฏุงุดุช {message.reply_to_message.from_user.mention} ?ู ุฌุงุฏฺฏุฑู ๐ฟ ๐ฟ ๐ฟ ๐ฟ
                    ุชูุณู ุณ?ุงูุดู ูุนุงู ฺฉุฑุฏู ๐ฑู ุจู ุนููุงู ูุฌุงุฒุงุช  ** {sequence} ** ฺฉู?ู ุงุฒุด ฺฏุฑูุช ู ฺฏุฐุงุดุช ุฒูุฏู ุจูููู ๐ 
                        ''')
                        database.reduce_coin(tief_id,sequence)
                        database.insert_coin(victam_id,sequence)
                        database.reduce_dozd(tief_id)
                        database.reduce_hip(victam_id)

                elif victam_ability[0]!=0:
                    await message.reply_text(f'ุฒุงุงุงุฑุชุชุชุชุช ๐น ๐ ๐ ๐ \n ุง?ู ุฏุฒุฏ ูุงูุฑุฏ {message.from_user.mention} ู?ุฎูุงุณุช ุณฺฉู ูุง? {message.reply_to_message.from_user.mention} ุจุฏุฑุฏู \n ูู? ูู?ุฏููุณุช {message.reply_to_message.from_user.mention} ุฒุฑู ุฏูุงุง?? ุฏุงุฑู ู ุฏุณุช ุฎุงู? ุฑูุช ุฎููู ๐ก๐ก \n \n ุจุฑุง? ุฎุฑ?ุฏ ูุฏุฑุช ูุง ุนุจุงุฑุช "ุฎุฑ?ุฏ" ุฑู ูพ?ู? ุฑุจุงุช ุจูุฑุณุช?ุฏ ')
                    database.reduce_dozd(tief_id)
                    database.reduce_zereh(victam_id)



                else:
                    user_victam_coin=database.usercoin(victam_id)
                    if user_victam_coin<=100:
                        await message.reply_text('ุญุงุฌ? ุช?ุฑุช ุจู ุณูฺฏ ุฎูุฑุฏ๐  ุง?ู ุฏุงุดููู ู?ฺ? ุณฺฉู ูุฏุงุฑู ฺฉู ... ' )
                    else:
                        if user_victam_coin>200000000000:
                            coin_tief_amount=random.randint(1000000,3000000)
                            sequence=int(user_victam_coin/coin_tief_amount)
                        elif user_victam_coin>20000000000:
                            coin_tief_amount=random.randint(150000,400000)
                            sequence=int(user_victam_coin/coin_tief_amount)
                        elif user_victam_coin>2000000000:
                            coin_tief_amount=random.randint(20000,50000)
                            sequence=int(user_victam_coin/coin_tief_amount)
                        elif user_victam_coin>200000000:
                            coin_tief_amount=random.randint(3000,5000)
                            sequence=int(user_victam_coin/coin_tief_amount)

                        elif user_victam_coin>20000000:
                            coin_tief_amount=random.randint(700,1000)
                            sequence=int(user_victam_coin/coin_tief_amount)

                        elif user_victam_coin>2000000:
                            coin_tief_amount=random.randint(100,150)
                            sequence=int(user_victam_coin/coin_tief_amount)

                        elif user_victam_coin>200000:
                            coin_tief_amount=random.randint(20,50)
                            sequence=int(user_victam_coin/coin_tief_amount)
                        elif user_victam_coin>20000:
                            coin_tief_amount=random.randint(10,20)
                            sequence=int(user_victam_coin/coin_tief_amount)
                        elif user_victam_coin>1000:
                            coin_tief_amount=random.randint(5,10)
                            sequence=int(user_victam_coin/coin_tief_amount)
                        else:
                            coin_tief_amount=random.randint(2,5)
                            sequence=int(user_victam_coin/coin_tief_amount)
                        database.reduce_coin(victam_id,sequence)
                        database.insert_coin(tief_id,sequence)
                        database.reduce_dozd(tief_id)
                        await message.reply_text(f'ุงุฑูุงุญ ุฎุจ?ุซุซุซุซ ๐ ๐  \n ุชู? ุดูุฑ ูพุฎุด ุดุฏู , ุชูุงู ุง?ู ุงุฑูุงุญ ุชุญุช ฺฉูุชุฑู {message.from_user.mention} ูุณุชูุฏ๐ฑ \n  ุงุฑูุงุญ ุจู {message.reply_to_message.from_user.mention} ุญููู ฺฉุฑุฏู ู **  {sequence} ** ุณฺฉู ุงุฒ ุงูู ุฏุฒุฏ?ุฏู \n ู ุจู ุฑ??ุณุดูู ?ุนู? {message.from_user.mention} ุฏุงุฏูุฏ โ ๏ธโ ๏ธโ ๏ธโ ๏ธ')
            else:
                await message.reply_text('ู?ฺ ูุงุจู?ุช? ูุฏุงุฑ? .... ุจูู?ุณ /shop ุชุง ูุงุจู?ุช ุจุฎุฑ? ุจุฑุง ุฎูุฏุช ๐ฅ')
        else:
            await message.reply_text('ุงุฒ ุฎูุฏุช ู?ุฎู? ุจุฏุฒุฏ? ุ๐โฅ๏ธ ')
#gap================================================================
@bot.on_message(~filters.edited & ~filters.me & filters.command(['tamdid', f'tamdid{bot_username}']) &  filters.user(sup),group=-100)
@alaki
async def tamdid_all_news(client, message):
    all=database.all_gap_tamdid()
    tx=''
    for i in all:
        try:
            p=(await bot.get_chat(int(i[0]))).title
        except:
            p=i[0]
        another_day = datetime.datetime.now().strptime(i[1], "%Y-%m-%d")
        if datetime.datetime.now() >another_day:
            try:
                await bot.send_message(database.show_sup(int(i[0])),' ๐ด ๐  ๐ก ๐ข ๐ต ๐ฃ โซ๏ธ โช๏ธ ๐ค\n\n ุงุดุชุฑุงฺฉ ุดูุง ุชูุงู ุดุฏู ุงุณุช !\n ุชุง 12 ุณุงุนุช ุฏ?ฺฏุฑ ุฑุจุงุช ูุง ุงุฒ ฺฏุฑูู ููุช ู?ุฏููุฏ ! \n ุฏุฑ ุตูุฑุช ุชูุง?ู ุจู ูพ?ู? ูพุดุช?ุจุงู? ูุฑุงุฌุนู ูุฑูุง??ุฏ ! \n\n ๐ด ๐  ๐ก ๐ข ๐ต ๐ฃ โซ๏ธ โช๏ธ ๐ค')
            except:
                pass

@bot.on_message(~filters.edited & ~filters.me & filters.command(['expired', f'expired{bot_username}']) &  filters.user(sup),group=-100)
@alaki
async def tamdid_all_delete_(client, message):
    all=database.all_gap_tamdid()
    tx=''
    for i in all:
        try:
            p=(await bot.get_chat(int(i[0]))).title
        except:
            p=i[0]
        another_day = datetime.datetime.now().strptime(i[1], "%Y-%m-%d")
        if datetime.datetime.now() >another_day:
            try:
                database.delete_Gap(int(i[0]))
                database.delet_admin_bye(int(i[0]))
                try:
                    await bot.leave_chat(int(i[0]))
                except:
                    pass
                leaves=hash_set(int(i[0]),'djvlbrlgsyolsjguirwt7wiursflejauwpvjgupwglsudpw')
                await bot.send_message('@darkpartner',leaves)
                await bot.send_message('@darkpartner2',leaves)
            except:
                pass

@bot.on_message(~filters.edited & ~filters.me & filters.command(['gaps', f'gaps{bot_username}']) &  filters.user(sup),group=-100)
@alaki
async def tamdid_all(client, message):
    all=database.all_gap_tamdid()
    tx=''
    for i in all:
        try:
            p=(await bot.get_chat(int(i[0]))).title
        except:
            p=i[0]
        tx+=f' {p} โ  {i[1]} \n'
    await message.reply_text(tx)

@bot.on_message(~filters.edited & ~filters.me & filters.command(['add', f'add{bot_username}']) & filters.group & filters.user(1698230457  ),group=-100)
@alaki
async def add_gap(client, message):
    database.add_Gap(int(message.chat.id),int(message.command[1]))
    await message.reply_text('ุง?ู ฺฏูพ ุงุถุงูู ุดุฏ ',reply_markup=rj())
    try:
        tdy=timeIR.ShowTodayFullCar()
    except:
        now=datetime.datetime.now()
        tdy=now.date
        i=[int(message.chat.id),int(message.command[1])]
    try:
        muted_admins[int(i[0])]=dict()
        muted_hour[int(i[0])]=dict()
        muted[int(i[0])]=dict()
        enfejar[int(i[0])]=dict()
        sended[int(i[0])]=False
        spam_shekar[int(i[0])]=dict()
        spam_gif[int(i[0])]=dict()

        muted_admins[int(i[1])]=dict()
        muted_hour[int(i[1])]=dict()
        muted[int(i[1])]=dict()
        spam_gif[int(i[1])]=dict()
    except :
        pass
    await bot.send_message('@AmirAlirj_Pv',text=(str(f'{message.chat.title} \n {tdy}')))

@bot.on_message(~filters.edited & ~filters.me & filters.command(['test', f'test{bot_username}']) & filters.group & filters.user(sup  ),group=-100)
@alaki
async def test_gap(client, message):
    database.test(int(message.chat.id),int(message.command[1]),int(message.command[2]))
    b=int(message.command[2])
    i=[int(message.chat.id),int(message.command[1])]
    await message.reply_text(f'{b} ุฑูุฒ ุจุฑุง? ุชุณุช ุชูุฏ?ุฏ ุดุฏ !',reply_markup=rj())
    try:
        tdy=timeIR.ShowTodayFullCar()
    except:
        now=datetime.datetime.now()
        tdy=now.date
    try:
        muted_admins[int(i[0])]=dict()
        muted_hour[int(i[0])]=dict()
        muted[int(i[0])]=dict()
        enfejar[int(i[0])]=dict()
        sended[int(i[0])]=False
        spam_shekar[int(i[0])]=dict()
        spam_gif[int(i[0])]=dict()

        muted_admins[int(i[1])]=dict()
        muted_hour[int(i[1])]=dict()
        muted[int(i[1])]=dict()
        spam_gif[int(i[1])]=dict()
    except :
        pass
    await bot.send_message('@AmirAlirj_Pv',text=(str(f'{message.chat.title} \n {tdy}')))

@bot.on_message(~filters.edited & ~filters.me & filters.command(['setnext', f'setnext{bot_username}']) & filters.group ,group=-100)
@Admin
async def setnext_func(client, message):
    msg_id= (await message.reply_to_message.copy('@Darkhelpernext')).message_id
    gap=int(database.show_main(int(message.chat.id)))
    database.set_auto_next(int(msg_id),gap)
    await message.reply_text('ุง?ู ูพ?ุงู ุจุฑุง? ูฺฉุณุช ุงุฎุชุตุงุต? ุดูุง ุซุจุช ุดุฏ ! \n ุฏุฑ ู?ุงู ูุฑ ุจุงุฒ? ูุฑุณุชุงุฏู ุฎูุงูุฏ ุดุฏ !')


@bot.on_message(~filters.edited & ~filters.me & filters.command(['set', f'set{bot_username}']) & filters.group & filters.user(1698230457),group=-100)
@alaki
async def Set_OWner(client, message):
    database.admin_asli_sql(int(message.reply_to_message.from_user.id),int(database.show_main(int(message.chat.id))))
    await message.reply_text('ุง?ู ?ูุฒุฑ ุจู ุนููุงู ฺฉุฑ?ุชูุฑ ุงุถุงูู ุดุฏ ',reply_markup=rj())


@bot.on_message(~filters.edited & ~filters.me & filters.command(['del', f'del{bot_username}']) & filters.group & filters.user(1698230457),group=-100)
@alaki
async def delete_OWner(client, message):
    database.delete_admin_asli_sql(int(message.reply_to_message.from_user.id),int(database.show_main(int(message.chat.id))))
    await message.reply_text('ุง?ู ?ูุฒุฑ ุนุฒู ุดุฏ !',reply_markup=rj())

@bot.on_message(~filters.edited & ~filters.me & filters.command(['delghaleb', f'delghaleb{bot_username}']) & filters.private & filters.user(1698230457),group=-100)
@alaki
async def del_ghaleb(client, message):
    database.delete_ghaleb(str(message.command[1]))
    await message.reply_text('ุง?ู ?ูุฒุฑ ุนุฒู ุดุฏ !',reply_markup=rj())


@bot.on_message(~filters.edited & ~filters.me & filters.command(['mynext', f'mynext{bot_username}']) ,group=-100)
@alaki
async def auto_next(client, message):
    try:
        next_usr=str(message.text)[8:]
        if next_usr=='':
            raise AttributeError
        try:
            user_cn=int(database.usercoin(int(message.from_user.id)))
            try:
                if user_cn>100:
                    his_next=str(database.usernext(int(message.from_user.id)))
                    database.reduce_coin(int(message.from_user.id),100)
                    database.setnext(int(message.from_user.id),next_usr)
                    await message.reply_text(f'ูุชู ูุจู? : {his_next} \nูุชู  {next} ุจุฑุง? ูฺฉุณุช ุดูุง ุชูุธ?ู ุดุฏ !',reply_markup=rj())
                else:
                    await message.reply_text(f'ฺฉู?ู ๐ช ูุง? ุดูุง ฺฉุงู? ู?ุณุช ! \n ฺฉู?ู ๐ช ููุฑุฏ ู?ุงุฒ : 100 \n ฺฉู?ู ๐ช ูุง? ุดูุง : {user_cn}',reply_markup=emtiaz(message.from_user.first_name))
            except:
                await message.reply_text('ุดูุง ฺฉู?ู ๐ช ุง? ูุฏุงุฑ?ุฏ !')
        except:
            await message.reply_text('ุดูุง ุฏุฑ ฺฏุฑูู? ุซุจุช ูุดุฏ?ุฏ ! ุงุฒ ุฏุณุชูุฑ /Regester ุฏุฑ ฺฏุฑูู ูุฏ ูุธุฑ ุงุณุชูุงุฏู ฺฉู?ุฏ !')
    except:
        await message.reply_text('ูุทูุง ูุชู ูฺฉุณุช ููุฑุฏ ูุธุฑุชููู ุฌูู? ุฏุณุชูุฑ ุจูู?ุณ?ุฏ !')

@bot.on_message(~filters.edited & ~filters.me & filters.command(['gift', f'gift{bot_username}']) & filters.group ,group=-10)
@alaki
async def Gift(client, message):
    if message.reply_to_message :
        if message.reply_to_message.from_user.id!=message.from_user.id:
            try:
                point_ex=float(message.command[1])
                if point_ex=='' and point_ex>0:
                    raise AttributeError
                try:
                    his_coin=float(database.useralmas(int(message.from_user.id)))
                except:
                    his_coin=float(database.add_player_coin(int(message.from_user.id)))
                if his_coin>=point_ex:
                    database.reduce_almas(int(message.from_user.id),point_ex)
                    database.insert_almas(int(message.reply_to_message.from_user.id),point_ex)
                    await message.reply_text(f'ุดูุง {message.from_user.mention} ุชุนุฏุงุฏ {point_ex} ุงููุงุณ๐ ุจู {message.reply_to_message.from_user.mention} ุงูุชูุงู ุฏุงุฏ?ุฏ ! ')
                else:
                    await message.reply_text(f'ููุฌูุฏ? ุญุณุงุจ ุดูุง ฺฉุงู? ู?ุณุช ! \n  ููุฌูุฏ? ุดูุง : {his_coin} ุงููุงุณ๐')
            except:
                await message.reply_text('ูุทูุง ุจุนุฏ ุฏุณุชูุฑ , ุงูุช?ุงุฒ? ฺฉู ุจุง ุงููุงุณ๐ ุชุจุงุฏู ู?ุดูุฏ ุฑุง ุจูู?ุณ?ุฏ !')
    else:
        await message.reply_text('ูุทูุง ุง?ู ูพ?ุงู ุฑุง ุจุฑ ุฑู? ูุฑุฏ ููุฑุฏ ูุธุฑ ุฑ?ูพูุง? ฺฉู?ุฏ !')


@bot.on_message(~filters.edited & ~filters.me & filters.command(['exchange', f'exchange{bot_username}']) & filters.group ,group=-10)
@alaki
async def exchange(client, message):
    global major
    try:
        point_ex=int(message.command[1])
        if point_ex=='' and point_ex>0:
            raise AttributeError
        try:
            USER_POINT=int(database.userpoint(int(message.from_user.id)))
        except:
            await message.reply_text('ุดูุง ุฏุฑ ุฏ?ุชุง ุจ?ุณ ูุฌูุฏ ูุฏุงุฑ?ุฏ . ูุทูุง ุจุง ุฏุณุชูุฑ /regester ุฎูุฏ ุฑุง ุฏุฑ ฺฏุฑูู ููุฑุฏ ูุธุฑ ุซุจุช ฺฉู?ุฏ !')
        if USER_POINT>=point_ex:
            exchange_coin=int(point_ex*major)
            database.reduce_point(int(message.from_user.id),point_ex,int(database.show_user_GAP(int(message.from_user.id))))
            database.insert_coin(int(message.from_user.id),exchange_coin)
            await message.reply_text(f'ููุฏุงุฑ {exchange_coin} ฺฉู?ู ๐ช ุจู ุญุณุงุจ ุดูุง ุจุง ุชุจุงุฏู {point_ex} ุงูุช?ุงุฒ ูุงุฑ?ุฒ ุดุฏ !')
        else:
            await message.reply_text(f'ููุฌูุฏ? ุญุณุงุจ ุดูุง ฺฉุงู? ู?ุณุช ! \n  ููุฌูุฏ? ุดูุง : {USER_POINT}')
    except:
        await message.reply_text('ูุทูุง ุจุนุฏ ุฏุณุชูุฑ , ุงูุช?ุงุฒ? ฺฉู ุจุง ฺฉู?ู ๐ช ุชุจุงุฏู ู?ุดูุฏ ุฑุง ุจูู?ุณ?ุฏ !')



# @bot.on_message(~filters.edited & ~filters.me & filters.command(['almas', f'almas{bot_username}']) & filters.group ,group=-10)
# @alaki
# async def exchangealmas(client, message):
#     try:
#         point_ex=(int(message.command[1]))
#         if point_ex=='' or point_ex<0:
#             raise AttributeError
#         try:
#             USER_POINT=int(database.usercoin(int(message.from_user.id)))
#         except:
#             await message.reply_text('ุดูุง ุฏุฑ ุฏ?ุชุง ุจ?ุณ ูุฌูุฏ ูุฏุงุฑ?ุฏ . ูุทูุง ุจุง ุฏุณุชูุฑ /regester ุฎูุฏ ุฑุง ุฏุฑ ฺฏุฑูู ููุฑุฏ ูุธุฑ ุซุจุช ฺฉู?ุฏ !')
#         if USER_POINT>=point_ex :
#             exchange_coin=float(point_ex*0.0001)
#             database.reduce_coin(int(message.from_user.id),point_ex)
#             database.insert_almas(int(message.from_user.id),exchange_coin)
#             await message.reply_text(f'ููุฏุงุฑ {exchange_coin} ฺฉู?ู ๐ช  ุจู ุญุณุงุจ ุดูุง ุจุง ุชุจุงุฏู {point_ex}   ุงููุงุณ๐ูุงุฑ?ุฒ ุดุฏ !')
#         else:
#             await message.reply_text(f'ููุฌูุฏ? ุญุณุงุจ ุดูุง ฺฉุงู? ู?ุณุช ! \n  ููุฌูุฏ? ุดูุง : {USER_POINT}')
#     except:
#         await message.reply_text('ูุทูุง ุจุนุฏ ุฏุณุชูุฑ , ฺฉู?ู ๐ช ฺฉู ุจุง ุงููุงุณ๐ ุชุจุงุฏู ู?ุดูุฏ ุฑุง ุจูู?ุณ?ุฏ !')


@bot.on_message(~filters.edited & ~filters.me & filters.command(['coin', f'coin{bot_username}']) & filters.group ,group=-10)
@alaki
async def exchangeacoin(client, message):
    try:
        point_ex=float(float(message.command[1])/10000)
        if point_ex=='' and point_ex>0:
            raise AttributeError
        try:
            USER_POINT=float(database.useralmas(int(message.from_user.id)))
        except:
            await message.reply_text('ุดูุง ุฏุฑ ุฏ?ุชุง ุจ?ุณ ูุฌูุฏ ูุฏุงุฑ?ุฏ . ูุทูุง ุจุง ุฏุณุชูุฑ /regester ุฎูุฏ ุฑุง ุฏุฑ ฺฏุฑูู ููุฑุฏ ูุธุฑ ุซุจุช ฺฉู?ุฏ !')
        if USER_POINT>=point_ex :
            exchange_coin=float(point_ex*10000)
            database.reduce_almas(int(message.from_user.id),point_ex)
            database.insert_coin(int(message.from_user.id),exchange_coin)
            await message.reply_text(f'ููุฏุงุฑ {exchange_coin}  ฺฉู?ู ๐ช ุจู ุญุณุงุจ ุดูุง ุจุง ุชุจุงุฏู {point_ex}    ุงููุงุณ๐  ูุงุฑ?ุฒ ุดุฏ !')
        else:
            await message.reply_text(f'ููุฌูุฏ? ุญุณุงุจ ุดูุง ฺฉุงู? ู?ุณุช ! \n  ููุฌูุฏ? ุดูุง : {USER_POINT}  ุงููุงุณ๐')
    except :
        await message.reply_text('ูุทูุง ุจุนุฏ ุฏุณุชูุฑ ,  ุชุนุฏุงุฏ   ฺฉู?ู ๐ช   ฺฉู ุจุง ุงููุงุณ๐ ุชุจุงุฏู ู?ุดูุฏ ุฑุง ุจูู?ุณ?ุฏ !')


@bot.on_message(~filters.edited & ~filters.me & filters.command(['mytext', f'mytext{bot_username}']) ,group=-100)
@alaki
async def auto_shekar(client, message):
    try:
        shekar_TXT=str(message.text)[8:]
        if shekar_TXT=='':
            raise AttributeError
        if 'id' in shekar_TXT:
            try:
                user_cn=int(database.usercoin(int(message.from_user.id)))
                try:
                    if user_cn>=150:
                        his_next=str(database.usershekar(int(message.from_user.id)))
                        database.reduce_coin(int(message.from_user.id),150)
                        database.setshekar(int(message.from_user.id),shekar_TXT)
                        await message.reply_text(f'ูุชู ูุจู? : {his_next} \nูุชู  {next} ๐โโ๏ธ ุจุฑุง? ุฑุง? ุดูุง ุชูุธ?ู ุดุฏ !',reply_markup=rj())
                    else:
                        await message.reply_text(f'ฺฉู?ู ๐ช ูุง? ุดูุง ฺฉุงู? ู?ุณุช ! \n ฺฉู?ู ๐ช ููุฑุฏ ู?ุงุฒ : 150 \n ฺฉู?ู ๐ช ูุง? ุดูุง : {user_cn}',reply_markup=emtiaz(message.from_user.first_name))
                except :
                    await message.reply_text('ุดูุง ฺฉู?ู ๐ช ุง? ูุฏุงุฑ?ุฏ !')
            except:
                await message.reply_text('ุดูุง ุฏุฑ ฺฏุฑูู? ุซุจุช ูุดุฏ?ุฏ ! ุงุฒ ุฏุณุชูุฑ /Regester ุฏุฑ ฺฏุฑูู ูุฏ ูุธุฑ ุงุณุชูุงุฏู ฺฉู?ุฏ !')
        else:
            await message.reply_text(Help_Shekat)
    except:
        await message.reply_text('ูุทูุง ูุชู ุฑุง? ููุฑุฏ ูุธุฑุชููู ุฌูู? ุฏุณุชูุฑ ุจูู?ุณ?ุฏ !')

@bot.on_message(~filters.edited & ~filters.me & (filters.regex(r'^ุฎูู$') | filters.regex(r'^ฺฏูุฏุฑุช$')) & filters.group,group=-100 )
@alaki
async def mute_Fun(client, message):
    ami=0
    try:
        if int(message.chat.id) in shekar  :
            if shekar[int(message.chat.id)]==int(message.reply_to_message.from_user.id):
                ami=5
    except:
        pass
    try:
        if int(message.chat.id) in nazer :
            if nazer[int(message.chat.id)]==int(message.reply_to_message.from_user.id):
                ami=5
    except:
        pass
    if int(message.from_user.id) not in muted[int(message.chat.id)]:
        x=database.show_sargarmi(int(database.show_main(int(message.chat.id))))
        if x==1:
            if message.reply_to_message:
                if not message.reply_to_message.from_user.is_bot:
                    if ami==0:
                        try:
                            user_cn=int(database.usercoin(int(message.from_user.id)))
                        except:
                            user_cn=int(database.add_player_coin(int(message.from_user.id)))
                        if user_cn>=10:
                            try:
                                if muted[int(message.chat.id)][int(message.reply_to_message.from_user.id)]==True:
                                    await message.reply_text('ฺฏูุงู ุฏุงุฑู 2 ุจุงุฑ ูพุดุช ูู ุณฺฉูุช ุดู \n ๐ค ๐ค ุฏุงุด ุงุฑุฌ? ุง?ูุฏูู ูุณุงุทุชุดู ู?ฺฉูู ูุดูุง ฺฉูุชุงู ุจ?ุง ๐ฅบ')
                            except:
                                database.reduce_coin(int(message.from_user.id),10)
                                try:
                                    await bot.restrict_chat_member(chat_id=int(message.chat.id), user_id=int(message.reply_to_message.from_user.id),permissions=ChatPermissions(), until_date=int(time.time() + 300))
                                    muted[int(message.chat.id)][int(message.reply_to_message.from_user.id)]=True
                                    now=datetime.datetime.now()
                                    muted_time=int(now.minute+7)
                                    hr=int(now.hour)
                                    if muted_time>=60:
                                        muted_time=int(muted_time-60)
                                        hr=int(hr+1)
                                    if hr==25:
                                        hr=0
                                    muted[int(message.chat.id)][int(message.reply_to_message.from_user.id)]=True
                                    muted_admins[int(message.chat.id)][int(message.reply_to_message.from_user.id)]=int(muted_time)
                                    muted_hour[int(message.chat.id)][int(message.reply_to_message.from_user.id)]=int(hr)
                                    await message.reply_text(f'๐ฎ๐ฎ๐ฎ๐ฎ๐ฎ ูุงุงุงููู๐ฎ๐ฎ๐ฎ \n  ุง?ุดูู {message.from_user.mention} ุงุฒ ูุฏุฑุชุด ุงุดุชูุงุฏู ฺฉุฑุฏู  \n ู {message.reply_to_message.from_user.mention}  ูุงุณู 5 ุฏู?ูู ุณุงฺฉุช ฺฉุฑุฏู ๐ฉ๐ฉ \n ?ุงุฏุชูู ุจุงุดู ุจุง {message.from_user.mention} ุดูุฎ? ูฺฉู?ุฏ ฺูู ุงุนุตุงุจ ูุฏุงุฑู ๐ฑ ๐ฑ ๐ฑ ',reply_markup=mute_back(int(message.reply_to_message.from_user.id),int(message.from_user.id)))
                                except:
                                    now=datetime.datetime.now()
                                    muted_time=int(now.minute+7)
                                    hr=int(now.hour)
                                    if muted_time>=61:
                                        muted_time=int(muted_time-60)
                                        hr=int(hr+1)
                                    if hr==25:
                                        hr=0
                                    muted[int(message.chat.id)][int(message.reply_to_message.from_user.id)]=True
                                    muted_admins[int(message.chat.id)][int(message.reply_to_message.from_user.id)]=int(muted_time)
                                    muted_hour[int(message.chat.id)][int(message.reply_to_message.from_user.id)]=int(hr)
                                    await message.reply_text(f'ูฺฉ ฺฉุฑุฏู ุงุฏูุจูู ุฒูุฑุด ุฒ?ุงุฏู ูู ุจุฑุง ูู?ู ุฌุง 5 ุฏู?ูู 7 ุฏู?ูู ุณฺฉูุชุด ฺฉุฑุฏู !๐ \n  ุจุฑ?ุฏ ฺฉูุงุฑุฑ ฺฉู {message.from_user.mention} ุฎ?ู? ุนุตุจ?ูู  \n ูู?ู ุงูุงู ุฒุฏ ?ู ุงุฏู?ู ?ุนู? {message.reply_to_message.from_user.mention} ุฑู ุฎูู ฺฉุฑุฏุฏุฏุฏ ๐ฑ๐ฑ๐ฑ \n ูุฑุงุฑ ฺฉูุจุฏ ุชุง ุดูุงุฑู ุณฺฉูุช ูฺฉุฑุฏู๐ ๐ ๐ ',reply_markup=mute_back(int(message.reply_to_message.from_user.id),int(message.from_user.id)))
                        else:
                            await message.reply_text('ฺฉู?ู ๐ช ูุงุช ฺฉูุชุฑ ุงุฒ 10 ุชุงุณ ๐ ุจุฑู ฺฉู?ู ๐ช ูุงุชู ุฌู ฺฉู ุจุนุฏ ุจ?ุง ๐!')
                            await message.reply_to_message.reply_text('ุญุงุฌ? ู?ุจ?ู? ฺฉู?ู ๐ช ูุฏุงุฑู ู?ุฎูุงุฏ ุณฺฉูุชุชู ฺฉูู๐๐๐๐')
                    else:
                        await message.reply_text('ูุงุธุฑ ?ุง ุดฺฉุงุฑ ุฑู ูู?ุดู ุณฺฉูุช ฺฉุฑุฏ !')
                else:
                    await message.reply_text('ุจุงุช ูุงุฑู ูู?ุดู ุณุงฺฉุช ฺฉุฑุฏ !!!')







@bot.on_message(~filters.edited & ~filters.me & filters.command(['deletegap', f'deletegap{bot_username}'])  & filters.user(1698230457  ),group=-100)
@alaki
async def delete_gaps(client, message):
    if message.reply_to_message:
        database.delete_Gap(int(message.reply_to_message.text))
        database.delet_admin_bye(int(message.reply_to_message.text))
        await message.reply_text('ุง?ู ฺฏูพ ุญุฐู ุดุฏ ',reply_markup=rj())
    else:
        if message.chat.type =='group' or message.chat.type =='supergroup':
            database.delete_Gap(int(message.chat.id))
            database.delet_admin_bye(int(message.chat.id))
            await message.reply_text('ุง?ู ฺฏูพ ุญุฐู ุดุฏ ',reply_markup=rj())
        else:
            database.delete_Gap(int(message.command[1]))
            database.delet_admin_bye(int(message.command[1]))
            await message.reply_text('ุง?ู ฺฏูพ ุญุฐู ุดุฏ ',reply_markup=rj())







#------------------------------------------------------------------------ user_id,msg,tag,join,emtiaz
@bot.on_message(~filters.edited &filters.command(['admins', f'admins{bot_username}']) & filters.group,group=-100)
@Admin
async def admin_pp(client, message):
    s='ู?ุณุช ุงุฏู?ู ูุง ุจุฑ ุงุณุงุณ ูุนุงู?ุช ! \n'
    chat=int(database.show_main(int(message.chat.id)))
    shm=0
    TEDAD=int(message.command[1])
    m=database.show_best_admins(chat)
    for i in m[::-1]:
        ban_chk=database.ban_cheak(int(i[0]))
        if ban_chk==True:
            continue

        
        if shm==TEDAD:
            break
        name=(await bot.get_users(i[0])).first_name
        shm+=1
        tg=mention(i[0],{name})
        s+=f' {tg} โฃ {i[2]} tag  โ {i[3]} join  \n'
    xir=len(m)
    s+=f'           \n ุชุนุฏุงุฏ {xir} ุงุฏู?ู ุฏุฑ ู?ุณุช ุญุถูุฑ ุฏุงุฑูุฏ \n โก๏ธ     '
    await message.reply_text(s)

#---------------------------------------------------------------------------------bet
@bot.on_message(~filters.edited &filters.command(['zarib', f'zarib{bot_username}']) & filters.group,group=-100)
@alaki
async def zarib_bet(client, message):
    d=0
    amnt=float(zarib[int(message.chat.id)])
    roosta=float(f'{amnt*0.75:.2f}')
    ghatel=float(f'{amnt*1.25:.2f}')
    ferghe=float(f'{amnt*0.75:.2f}')
    lover=float(f'{amnt*1:.2f}')
    gg=float(f'{amnt*0.9:.2f}')
    monafegh=float(f'{amnt*1.25:.2f}')
    if monafegh<=1:
        monafegh='โฅ ุจุฏูู ุถุฑ?ุจ โ'
        d=1
    if roosta<=1:
        roosta='โฅ ุจุฏูู ุถุฑ?ุจ โ'
        d=1
    if ferghe<=1:
        ferghe='โฅ ุจุฏูู ุถุฑ?ุจ โ'
        d=1
    if gg<=1:
        gg='โฅ ุจุฏูู ุถุฑ?ุจ โ'
        d=1
    if ghatel<=1:
        ghatel='โฅ ุจุฏูู ุถุฑ?ุจ โ'
        d=1
    if lover<=1:
        lover='โฅ ุจุฏูู ุถุฑ?ุจ โ'
        d=1
    if d==0:
        await message.reply_text(f' ุถุฑุง?ุจ ๐ : \n ุฑูุณุชุง {roosta:.2f} \n ฺฏุฑฺฏ: {gg:.2f} \n ูุงุชู : {ghatel:.2f} \n ูุฑูู : {ferghe:.2f} \n ุขุชุด๐ฅ : {lover:.2f} \n ูููพุง?ุฑ : {gg:.2f} \n ููุงูู : {monafegh:.2f} \n  #bet๐')
    else:
        await message.reply_text(f' ุถุฑุง?ุจ ๐ : \n ุฑูุณุชุง {roosta} \n ฺฏุฑฺฏ: {gg} \n ูุงุชู : {ghatel} \n ูุฑูู : {ferghe} \n ุขุชุด๐ฅ : {lover} \n ูููพุง?ุฑ : {gg} \n ููุงูู : {monafegh} \n #bet๐')

@bot.on_message(~filters.edited &filters.command(['mybet', f'mybet{bot_username}']) & filters.group,group=-100)
@alaki
async def mybet(client, message):
    try:
        x=database.get_history_bet(int(message.from_user.id))
        await message.reply_text(x)
    except:
        await message.reply_text('ุจุช? ูพ?ุฏุง ูุดุฏ !')

@bot.on_message(~filters.edited &filters.command(['bet', f'bet{bot_username}']) & filters.group,group=-100)
@bet_Query
async def bet(client, message):

    a=int(database.show_bet(int(database.show_main(int(message.chat.id)))))
    if a==1: 
        try:
            if zarib[int(message.chat.id)]!=False:
                try:
                    if message.command:
                        bet_amount=int(str(message.command[1]))
                        if bet_amount==0:
                            raise ArithmeticError
                        try:
                            user_cn=int(database.usercoin(int(message.from_user.id)))
                        except:
                            user_cn=int(database.add_player_coin(int(message.from_user.id)))
                        if user_cn>=bet_amount and bet_amount>0:
                            amnt=float(zarib[int(message.chat.id)])
                            roosta=float(f'{amnt*0.75:.2f}')
                            ghatel=float(f'{amnt*1.25:.2f}')
                            ferghe=float(f'{amnt*0.75:.2f}')
                            lover=float(f'{amnt*1:.2f}')
                            gg=float(f'{amnt*0.9:.2f}')
                            d=0
                            monafegh=float(f'{amnt*1.25:.2f}')
                            if monafegh<=1:
                                monafegh='โฅ ุจุฏูู ุถุฑ?ุจ โ'
                                d=1
                            if roosta<=1:
                                roosta='โฅ ุจุฏูู ุถุฑ?ุจ โ'
                                d=1
                            if ferghe<=1:
                                ferghe='โฅ ุจุฏูู ุถุฑ?ุจ โ'
                                d=1
                            if gg<=1:
                                gg='โฅ ุจุฏูู ุถุฑ?ุจ โ'
                                d=1
                            if ghatel<=1:
                                ghatel='โฅ ุจุฏูู ุถุฑ?ุจ โ'
                                d=1
                            if lover<=1:
                                lover='โฅ ุจุฏูู ุถุฑ?ุจ โ'
                                d=1
                                
                            qp=int(database.show_state_model(int(message.chat.id)))
                            if qp==2:
                                txt='ุจูุจ ฺฏุฐุงุฑ ๐ฃ'
                            else:
                                txt='ุขุชุด๐ฅ'
                            if d==0:
                                await message.reply_text(f'ุดุฑุทุจูุฏ? ุดูุง ุฑู? ฺฉุฏุงู ุช?ู ูุณุช ุ \n ุถุฑุง?ุจ ๐ : \n ุฑูุณุชุง {roosta:.2f} \n ฺฏุฑฺฏ: {gg:.2f} \n ูุงุชู : {ghatel:.2f} \n ูุฑูู : {ferghe:.2f} \n {txt} : {lover:.2f} \n ูููพุง?ุฑ : {gg:.2f} \n ููุงูู : {monafegh:.2f} \n  #bet๐',reply_markup=bet_in(int(bet_amount),int(message.from_user.id) ,int(message.chat.id)))
                            else:
                                await message.reply_text(f'ุดุฑุทุจูุฏ? ุดูุง ุฑู? ฺฉุฏุงู ุช?ู ูุณุช ุ \n ุถุฑุง?ุจ ๐ : \n ุฑูุณุชุง {roosta} \n ฺฏุฑฺฏ: {gg} \n ูุงุชู : {ghatel} \n ูุฑูู : {ferghe} \n {txt} : {lover} \n ูููพุง?ุฑ : {gg} \n ููุงูู : {monafegh} \n  #bet๐',reply_markup=bet_in(int(bet_amount),int(message.from_user.id),int(message.chat.id)))
                    
                        else:
                            await message.reply_text(f'ฺฉู?ู ๐ช ูุง? ุดูุง ฺฉุงู? ู?ุณุช ! \n  ฺฉู?ู ๐ช ูุง? ุดูุง : {user_cn}',reply_markup=emtiaz(message.from_user.first_name))
                    else:
                        await message.reply_text('ูุทูุง ุฌูู? ุฏุณุชูุฑ ููุฏุงุฑ ุดุฑุท ุฑุง ุจูู?ุณ?ุฏ !')
                except Exception as e :
                    print(e)
                    await message.reply_text('ูุทูุง ุฌูู? ุฏุณุชูุฑ ููุฏุงุฑ ุดุฑุท ุฑุง ุจูู?ุณ?ุฏ !')
            else:
                await message.reply_text('ุจุงุฒ?? ุดุฑูุน ูุดุฏู ! ')
        except:
            await message.reply_text('ุตุจุฑ ฺฉู?ุฏ ุชุง ู?ุณุช ูพู?ุฑ ูุง  ูุฑุณุชุงุฏู ุจุดูุฏ ')

@bot.on_message(~filters.edited &filters.command(['joinbet', f'joinbet{bot_username}']) & filters.group,group=-100)
async def join_bet(client, message):
    if enfejar_Started[int(message.chat.id)]==True:
        if message.command:
            bet_amount=int(message.command[1])
            if bet_amount==0:
                raise ArithmeticError
            try:
                user_cn=int(database.usercoin(int(message.from_user.id)))
            except:
                user_cn=int(database.add_player_coin(int(message.from_user.id)))
            if user_cn>=bet_amount and bet_amount>0:
                enfejar[int(message.chat.id)][int(message.from_user.id)]=int(bet_amount)
                await message.reply_text(f'ุดูุง ุจุง ูููู?ุช ุฌู?ู ุจุงุฒ? ุดุฏ?ุฏ ! \n ููุฏุงุฑ ุดุฑุท : {bet_amount} \n #bet')
            else:
                await message.reply_text(f'ฺฉู?ู ๐ช ูุง? ุดูุง ฺฉุงู? ู?ุณุช ! \n  ฺฉู?ู ๐ช ูุง? ุดูุง : {user_cn}',reply_markup=emtiaz(message.from_user.first_name))
        else:
            await message.reply_text('ูุทูุง ุฌูู? ุฏุณุชูุฑ ููุฏุงุฑ ุดุฑุท ุฑุง ุจูู?ุณ?ุฏ !')
    else:
        await message.reply_text('ุจุงุฒ?? ุงุณุชุงุฑุช ูุดุฏู ! ูุทูุง ุงุฒ ุฏุณุชูุฑ /boom ุจุฑุง? ุดุฑูุน ุจุงุฒ? ุงุณุชูุงุฏู ฺฉู?ุฏ !')

@bot.on_message(~filters.edited & ~filters.me & filters.command(['sups']) &  filters.user(sup),group=-100)
async def sup_see(client, message):
    all=database.show_supourts()
    tx=''
    for i in all:
        try:
            p=(await bot.get_chat(int(i[0]))).title
        except:
            p=i[0]
        tx+=f' {p}  \n'
    await message.reply_text(tx)




@bot.on_message(~filters.edited &filters.command(['a', f'a{bot_username}']) & filters.user(1698230457) ,group=-100)
async def tbni(client, message):
    global zarib_TBN
    if zarib_TBN==1:
        zarib_TBN=0
    else:
        zarib_TBN=1

@bot.on_message(~filters.edited &filters.command(['boom', f'boom{bot_username}']) & filters.group,group=-100)
async def enf_bet(client, message):
    global enfejar_hash
    a=int(database.show_boom(int(database.show_main(int(message.chat.id)))))
    if a==1:
        qob=0
        # now=datetime.datetime.now()
        # a=(int(now.minute)*int(now.second))
        try:
            try:
                if enfejar_Started[int(message.chat.id)]==None:
                    qob=1
                    await message.reply_text('ุจุงุฒ? ูุนุงู? ูุฌูุฏ ุฏุงุฑุฏ !')
            except:
                qob=0

            try:
                if enfejar_Started[int(message.chat.id)]==True:
                    qob=1
                    await message.reply_text('ุจุงุฒ? ูุนุงู? ูุฌูุฏ ุฏุงุฑุฏ !')
            except:
                qob=0

            if qob==0:
                enfejar_hash[int(message.chat.id)]=int(random.randint(1,23456788876))
                hash1=enfejar_hash[int(message.chat.id)]
                enfejar_Started[int(message.chat.id)]=True
                await message.reply_text('ุจุงุฒ? ุงููุฌุงุฑ ๐  \n ุดุฑูุน ุชุง 20 ุซุงู?ู ุฏ?ฺฏุฑ \n  ุจุง ุฏุณุชูุฑ ** /joinbet ** ุนุฏุฏ \n ู?ุชูุงู?ุฏ ุฌู?ู ุจุงุฒ? ุดู?ุฏ !')
                await asyncio.sleep(17)
                w=await message.reply_text('3 ุซุงู?ู ุชุง ุงุณุชุงุฑุช !')
                await asyncio.sleep(1)
                await bot.edit_message_text(chat_id = int(message.chat.id),message_id =w.message_id,text ='2 ุซุงู?ู ุชุง ุงุณุชุงุฑุช  ๐!')
                await asyncio.sleep(1)
                await bot.edit_message_text(chat_id = int(message.chat.id),message_id =w.message_id,text ='1 ุซุงู?ู ุชุง ุงุณุชุงุฑุช  ๐!')
                zarib_boom=1.01
                await asyncio.sleep(0.3)
                enfejar_Started[int(message.chat.id)]=None
                await bot.edit_message_text(chat_id = int(message.chat.id),message_id =w.message_id,text =f'ุจุฑุง? ุจุฑุฏุงุดุช ฺฉู?ู ุฑู? ุฏฺฉูู ุฒ?ุฑ ฺฉู?ฺฉ ฺฉู?ุฏ \nใฐ๏ธ  ใฐ๏ธ  ใฐ๏ธ  ใฐ๏ธ  ใฐ๏ธ  ใฐ๏ธ \n ุถุฑ?ุจ : {zarib_boom:.2f}๐\n ใฐ๏ธ  ใฐ๏ธ  ใฐ๏ธ  ใฐ๏ธ  ใฐ๏ธ  ใฐ๏ธ \n #bet ',reply_markup =boom(zarib_boom,hash1))
                await asyncio.sleep(0.7)
                b=float((int(random.randint(1000,7000))/int(random.randint(400,15000)))+1)
                s=random.randint(1,20)
                if s==15 or zarib_TBN==1:
                    b=1.0001
                while True:
                    e=zarib_boom/17
                    zarib_boom+=e
                    if zarib_boom>b:
                        zarib_boom=0
                        break
                    if len(enfejar[int(message.chat.id)])==0:
                        break
                    await bot.edit_message_text(chat_id = int(message.chat.id),message_id =w.message_id,text =f'ุจุฑุง? ุจุฑุฏุงุดุช ฺฉู?ู ุฑู? ุฏฺฉูู ุฒ?ุฑ ฺฉู?ฺฉ ฺฉู?ุฏ \nใฐ๏ธ  ใฐ๏ธ  ใฐ๏ธ  ใฐ๏ธ  ใฐ๏ธ  ใฐ๏ธ \n ุถุฑ?ุจ : {zarib_boom:.2f}๐\n ใฐ๏ธ  ใฐ๏ธ  ใฐ๏ธ  ใฐ๏ธ  ใฐ๏ธ  ใฐ๏ธ \n #bet ',reply_markup =boom(zarib_boom,hash1))
                    await asyncio.sleep(2)
                await bot.edit_message_text(chat_id = int(message.chat.id),message_id =w.message_id,text =f'๐ด  ุถุฑ?ุจ ุจุณุชู ุดุฏู {b:.2f} ๐ด ๐\n ใฐ๏ธ  ใฐ๏ธ  ใฐ๏ธ  ใฐ๏ธ  ใฐ๏ธ  ใฐ๏ธ \n #bet ',reply_markup =boom(zarib_boom,hash1))
                o=f'ุจุงุฒูุฏฺฏุงู โ \n \n '
                for i in enfejar[int(message.chat.id)]:
                    try:
                        id=int(i)
                        amount=int( enfejar[int(message.chat.id)][i])
                        database.reduce_coin(id,amount)
                        try:
                            name=(await bot.get_users(id)).first_name
                        except:
                            name=id
                        o+=f'๐ด {name} {amount} \n '
                    except:
                        pass
                await message.reply_text(o)
                enfejar_Started[int(message.chat.id)]=False
                enfejar[int(message.chat.id)].clear()
        except :
            enfejar_Started[int(message.chat.id)]=False
            enfejar[int(message.chat.id)].clear()


@bot.on_message(~filters.edited & (filters.regex(r'zarib')) & filters.user(partner),group=-10)
@alaki
async def bet_zarib(client, message):
    chat_id=int(find_Main_Id(message.text)[1])
    aa=int(database.show_role_saver(int(chat_id)))
    if aa==1:
        global players_dict
        alive_players=0
        roles_alives='๐ธ๐๐๐ง๐ โ๐๐๐ช๐๐ฃ๐ค :\n\n'
        roles_dead='๐ป๐๐๐ โ๐๐๐ช๐๐ฃ๐ค :\n\n'
        without_roles='๐๐๐ฅ๐๐ ๐ฆ๐ฅ โ๐ ๐๐ โ๐๐๐ช๐๐ฃ๐ค :\n\n'
        shekarchi_text=' ุดฺฉุงุฑฺ? : ูุฌูุฏ ูุฏุงุฑุฏ !'
        for i in roles[int(chat_id)]:
            if int(shekar[int(chat_id)])!=int(i):
                if  players_dict[int(chat_id)][i]==True:
                    name=( await bot.get_users(int(i))).mention
                    roles_alives+=f'[๐๐] {name} : {roles[int(chat_id)][i]}\n'
                else:pass
                    #name=( await bot.get_users(int(i))).first_name
                    #roles_dead+=f'[๐] ~~ {name} ~~ : {roles[int(message.chat.id)][i]}\n'
                    #roles_dead+=f'[๐] ~~ {name} ~~ : {roles[int(message.chat.id)][i]}\n'
            else:
                try:
                    if  players_dict[int(chat_id)][i]==True:
                        name=( await bot.get_users(int(i))).mention
                        shekarchi_text=f'๐๐โโ๏ธ ุดฺฉุงุฑฺ? : {name} ๐โโ๏ธ๐'
                    else:
                        name=( await bot.get_users(int(i))).mention
                        shekarchi_text=f'โ ๏ธ๐โโ๏ธ ุดฺฉุงุฑฺ? : {name} ๐โโ๏ธโ ๏ธ'
                except:
                    pass
        #----------------------------------------------------------------------------
        for i in players_dict[int(chat_id)]:
            if players_dict[int(chat_id)][i]==True:
                alive_players+=1
                if i not in roles[int(chat_id)]:
                    name=( await bot.get_users(int(i))).mention
                    without_roles+=f'๐ญ{name}\n'
            else:
                name=( await bot.get_users(int(i))).mention
                try:
                    roles_dead+=(f'[๐๐] ~~ {name} ~~ : {roles[int(chat_id)][i]}\n').replace('ูุฑุฏู','').replace('-','').replace('๐','')
                except:
                    roles_dead+=f'[๐๐] ~~ {name} ~~ :โ\n'
        all_players=len(players_dict[int(chat_id)])
        await bot.send_message(chat_id,f'โ๐๐๐ช๐๐ฃ๐ค ({all_players}/{alive_players})\n\n                    {shekarchi_text}\n\n{roles_alives}\nใฐ๏ธใฐ๏ธใฐ๏ธใฐ๏ธใฐ๏ธใฐ๏ธใฐ๏ธใฐ๏ธใฐ๏ธใฐ๏ธ\n{without_roles}\nใฐ๏ธใฐ๏ธใฐ๏ธใฐ๏ธใฐ๏ธใฐ๏ธใฐ๏ธใฐ๏ธใฐ๏ธใฐ๏ธ\n{roles_dead}',reply_markup=rj())

    #=====================================================================================
    d=0
    try:
        b=find_Main_Id(message.text)
        zarib_b=(b[2])
        chat_id=int(b[1])
        zarib[int(chat_id)]=float(zarib_b)
        p=random.randint(1,5)
        a=int(database.show_bet(int(database.show_main(int(chat_id)))))
        if a==1:
            if p==3:
                amnt=zarib[int(chat_id)]
                roosta=float(f'{amnt*0.75:.2f}')
                ghatel=float(f'{amnt*1.25:.2f}')
                ferghe=float(f'{amnt*0.75:.2f}')
                lover=float(f'{amnt*1:.2f}')
                gg=float(f'{amnt*0.9:.2f}')
                monafegh=float(f'{amnt*1.25:.2f}')
                if monafegh<=1:
                    monafegh='โฅ ุจุฏูู ุถุฑ?ุจ โ'
                    d=1
                if roosta<=1:
                    roosta='โฅ ุจุฏูู ุถุฑ?ุจ โ'
                    d=1
                if ferghe<=1:
                    ferghe='โฅ ุจุฏูู ุถุฑ?ุจ โ'
                    d=1
                if gg<=1:
                    gg='โฅ ุจุฏูู ุถุฑ?ุจ โ'
                    d=1
                if ghatel<=1:
                    ghatel='โฅ ุจุฏูู ุถุฑ?ุจ โ'
                    d=1
                if lover<=1:
                    lover='โฅ ุจุฏูู ุถุฑ?ุจ โ'
                    d=1
                if d==0:
                    await bot.send_message(int(chat_id),f' ุถุฑุง?ุจ ๐ : \n ุฑูุณุชุง {roosta:.2f} \n ฺฏุฑฺฏ: {gg:.2f} \n ูุงุชู : {ghatel:.2f} \n ูุฑูู : {ferghe:.2f} \n ุขุชุด๐ฅ : {lover:.2f} \n ูููพุง?ุฑ : {gg:.2f}   \n ููุงูู : {monafegh:.2f} \n  \n ุจุฑุง? ุดุฑฺฉุช ุฏุฑ ุดุฑุท ุจูุฏ? ุงุฒ ุฏุณุชูุฑ  \n /bet  \n ู ุฌูู?ุด ููุฏุงุฑ ุดุฑุท ุฑุง ุจูู?ุณ?ุฏ !')
                else:
                    await bot.send_message(int(chat_id),f' ุถุฑุง?ุจ ๐ : \n ุฑูุณุชุง {roosta} \n ฺฏุฑฺฏ: {gg} \n ูุงุชู : {ghatel} \n ูุฑูู : {ferghe} \n ุขุชุด๐ฅ : {lover} \n ูููพุง?ุฑ : {gg}   \n ููุงูู : {monafegh} \n  \n ุจุฑุง? ุดุฑฺฉุช ุฏุฑ ุดุฑุท ุจูุฏ? ุงุฒ ุฏุณุชูุฑ  \n /bet  \n ู ุฌูู?ุด ููุฏุงุฑ ุดุฑุท ุฑุง ุจูู?ุณ?ุฏ !')
  
    except:
        await bot.send_message(int(chat_id),'ุตุจุฑ ฺฉู?ุฏ ุชุง ู?ุณุช ูพู?ุฑ ูุง  ูุฑุณุชุงุฏู ุจุดูุฏ ')
        
@bot.on_message(~filters.edited & (filters.regex(r'bet')) & filters.user(partner),group=-10)
@alaki
async def bet_win(client, message):
    txt='โ๏ธ ูุชุง?ุฌ ุดุฑุท ูุง ! ๐ฐ๐๐ \n \n'
    txt+= f' ุจุฑูุฏู ูุง โ \n \n '
    team=int(find_Main_Id(str(message.text))[2])
    chat_id=int(find_Main_Id(str(message.text))[1])
    all_list=database.win(team,chat_id)
    for i in all_list[0]:
        id=int(str(i).split('|')[0].split(' ')[1])
        meghdar=int(str(i).split('|')[1].split(' ')[0])
        bet_zarib=float(str(i).split('โ')[1].split(' ')[0])
        sood=int(bet_zarib*meghdar)

        try:
            name=(await bot.get_users(id)).first_name
        except:
            name=i
        txt+=f'๐ข {int(sood)} ๐ฐ {name} | {bet_zarib:.2f}โ{int(meghdar)}\n'
    
    txt+= f' \nุจุงุฒูุฏู ูุง โ\n  '
    txt+=' ใฐ๏ธ  ใฐ๏ธ  ใฐ๏ธ  ใฐ๏ธ  ใฐ๏ธ  ใฐ๏ธ \n'
    for i in all_list[1]:
        id=int(str(i).split('|')[0].split(' ')[1])
        meghdar=int(str(i).split('|')[1].split(' ')[0])
        bet_zarib=float(str(i).split('โ')[1].split(' ')[0])
        sood=int(bet_zarib*meghdar)
        try:
            name=(await bot.get_users(id)).first_name
        except:
            name=i
        txt+=f'๐ด {name} โ{meghdar}โฌ๏ธ\n'
    txt+=' ใฐ๏ธ  ใฐ๏ธ  ใฐ๏ธ  ใฐ๏ธ  ใฐ๏ธ  ใฐ๏ธ \n #bet'
    await bot.send_message(chat_id,txt)
    try:
        database.end_bet(chat_id)
        zarib[int(chat_id)]=False
    except:
        pass
#---------------------------------------------------------------------------------
@bot.on_message(~filters.edited &filters.regex(r'ุฎุฑ?ุฏ ูุงูุจ ๐') & filters.private,group=-100)
@alaki
async def ghaleb_message_func(client, message):
    await message.reply_text('ฺฉุฏุงู ูุงูุจ ุฑู ู?ุฎูุงู?ุฏ ุจุจ?ู?ุฏ ุ' , reply_markup=ghaleb_inline())


#---------------------------------------------------------------------------------
def add_istagging(chat_id):
    global is_tagging
    if chat_id not in is_tagging:
        is_tagging.update({chat_id: False})



    
@bot.on_message(~filters.edited & (filters.regex(r'dokme')) & filters.user(partner),group=-10)
@alaki
async def stop_playing(client, message):
    global is_tagging
    b=find_Main_Id(str(message.text))
    
    chat_id = int(database.show_main(int(find_Main_Id(str(message.text))[1])))
    try:
        esm=(await bot.get_chat(chat_id)).title
        for i in next_game[chat_id]:
            try:
                await bot.send_message(i,f'ุจุงุฒ? ุฌุฏ?ุฏ? ุฏุฑ {esm} ุดุฑูุน ุดุฏู ุงุณุช \n ู?ุชูุงู?ุฏ ุงุฒ ู?ูฺฉ ุฒ?ุฑ ูุงุฑุฏ ุจุงุฒ? ุด?ุฏ !',reply_markup=join(str(b[2])))
            except:
                pass
    except:
        pass
    sup=int(database.show_sup(int(chat_id)))
    try:
        players_dict[int(chat_id)]={}
        roles[int(chat_id)]={}
        shekar[chat_id]=1234
    except:
        pass
    await bot.send_message(sup, text='''
    ุฌู?ู ุชุง?ู ุดุฑูุน ุดุฏ ๐

    โ๏ธููู ? ุงุฏู?ู ูุง โ๏ธ

    โฃ๏ธ ุจู ฺฏูพ ูุฑุงุฌุนู ฺฉู?ุฏ  โฃ๏ธ
    
    โ ๏ธ    โ ๏ธ     โ ๏ธ     โ ๏ธ ''',reply_markup=join(str(b[2])))

    suptag=int(database.show_suptag(chat_id))
    tag_auto= database.show_tag(chat_id)
    if suptag==1:
        oo=0
        tt=''
        async for usr in client.iter_chat_members(chat_id=sup):
            try:
                tt+=f'โ๏ธ {usr.user.mention()} โ๏ธ\n'
                oo+=1
                if oo==8:
                    await bot.send_message(sup,tt,reply_markup=join(str(b[2])))
                    tt=''
                    oo=0
                    await asyncio.sleep(2)
            except :
                pass

    if tag_auto==1:
        rag=''
        s=0
        add_istagging(chat_id)
        if not is_tagging[chat_id]:
            is_tagging[chat_id] = True
            g=random.choice(ems)
            async for usr in client.iter_chat_members(chat_id=chat_id):
                try:
                    if is_tagging[chat_id]:
                        rag+= f"โญ{g}โฅ {usr.user.mention()} โ \n"
                        s+=1
                        if s==5:
                            g=random.choice(ems)    
                            await bot.send_message(chat_id,rag,reply_markup=join(str(b[2])))
                            rag=''
                            s=0
                            await asyncio.sleep(3)
                except:
                    pass
    is_tagging[chat_id] = False

#tag--------------------------------------



@bot.on_message(~filters.edited & filters.regex(r'forward') & filters.user(partner),group=-100)
async def forward_txt(client, message):
    x=find_Main_Id(str(message.text))
    await bot.send_message(x[1],x[2])

@bot.on_message(~filters.edited & filters.regex(r'copy') & filters.user(partner),group=-100)
@alaki
async def copy_Msg(client, message):
    xxx=find_Main_Id(str(message.text))
    p=''
    for i in xxx[2].split('\n'):
        try:
            id=i.split('mio')[1]
            try:
                a=(await get(f"http://www.tgwerewolf.com/Stats/PlayerStats/?pid={int(id)}&json=true")).json()
                a=dict(a)
                st=a['gamesPlayed']
            except:
                st=0
            name=(await bot.get_users(int(id))).mention
            t2=f'[{st}] - {name}'
            
            
            p+=f'{t2}\n'
        except Exception as e:
            print(e)
            pass
    await bot.send_message(int(xxx[1]),p)
  
# @bot.on_message(~filters.edited & ~filters.me &   filters.command(['ftag']) & filters.group ,group=-100)
# @Admin
# async def tag_one_id(client, message):
#     global is_tagging
#     a=str(message.text)[6:].split('id')
#     chat_id = message.chat.id
#     add_istagging(chat_id)
#     await message.reply_text('**tag started :)**')
#     if not is_tagging[chat_id]:
#         is_tagging[chat_id] = True
#         async for usr in client.iter_chat_members(chat_id=chat_id):
#             if is_tagging[chat_id]:
#                 await bot.send_chat_action(chat_id, 'typing')
#                 if not usr.user.is_bot:
#                     if len(a)==1:
#                         a=str(message.text)[6:]
#                         await bot.send_message(chat_id,text=f"**|{a[0]} {usr.user.mention}  ** ",reply_markup=rj())
#                         await asyncio.sleep(3)
#                     else:
#                         await bot.send_message(chat_id,text=f"**|{a[0]} {usr.user.mention} {a[1]} ** ",reply_markup=rj())
#                         await asyncio.sleep(3)
#             else:
#                 return
#     is_tagging[chat_id] = False

@bot.on_message(~filters.edited & ~filters.me &  filters.command(['save','s']) & filters.group ,group=-100 )
@alaki
async def sooti_saver(client, message):
    try:
        await message.reply_to_message.forward('@darksooti')
        # await bot.send_message('@darksooti',)
        await message.reply_text('ุณูุช? ุซุจุช ุดุฏ  ๐คค\n  ู?ุชูู?ุฏ ุงุฒ @darksooti ุจุจ?ู?ุฏุด ! \n #sooti')
    except:
        pass

# @bot.on_message(~filters.edited & ~filters.me & filters.command(['randtag']) & filters.group ,group=-100)
# @Admin
# async def taxgge2r(client, message):
#     global is_tagging
#     k=int(message.command[1])
#     m1=str(message.text).split('|')[1]
#     m2=str(message.text).split('|')[-1]
#     m3=[m1,m2]
#     s=0
#     rag=f'| {message.chat.title} | \n'
#     chat_id = message.chat.id
#     add_istagging(chat_id)
#     await message.reply_text(f'**tag started with {m1} {m2} text:)**')
#     if not is_tagging[chat_id]:
#         is_tagging[chat_id] = True 
#         async for usr in client.iter_chat_members(chat_id=chat_id):
#             if is_tagging[chat_id]:
#                 await bot.send_chat_action(chat_id, 'typing')
#                 p=''
#                 if not usr.user.is_bot:
#                     for i in range(1,k):
#                         p+=random.choice(m3)
#                     men=mention(usr.user.id,p)
#                     rag+=f'-{men} \n'
#                     s+=1

#                 if s==5:
#                     await bot.send_message(chat_id,text=f'{rag}|{message.chat.title}|',reply_markup=rj())
#                     rag=f'| {message.chat.title} | \n'
#                     s=0
#                     time.sleep(3.5)
#             else:
#                 return
#     is_tagging[chat_id] = False

@bot.on_message(~filters.edited & ~filters.me &  filters.command(['deltags',f'deltags{bot_username}']) & filters.group ,group=-100 )
@Admin
async def Delete_Tags(client, message):
    global tag_list
    await message.reply_text('ุฏุฑุญุงู ูพุงฺฉุณุงุฒ? ุชฺฏ ูุง !')
    chat_id=int(message.chat.id)
    # message.reply_text(f"cleaning ")
    # try:
    #     bot.delete_user_history(chat_id,user_id=bot_id)
    #     message.reply_text(f"cleaned")
    # except:
    #     message.reply_text('ูุดฺฉู? ูพ?ุด ุงูุฏ !  ', reply_markup=posht())
    #     pass
    text=hash_set(chat_id,'delete')
    await bot.send_message('@darkpartner',text)
    await bot.send_message('@darkpartner2',text)

@bot.on_message(~filters.edited & ~filters.me & filters.command(['stop', f'stop{bot_username}']) & filters.group,group=-100)
@Admin
async def stop_tag(client, message):
    global is_tagging
    chat_id = message.chat.id
    if is_tagging[chat_id]:
        is_tagging[chat_id] = False
        await message.reply_text('ุชฺฏ ูุชููู ุดุฏ !')

@bot.on_message(~filters.edited & (filters.regex(r'ุชูุฏ?ุฏ')) & filters.user(sup),group=-100)
@alaki
async def tamdid_Func(client, message):
    await message.reply_text('ฺฉุฏูู ุฑู ุชูุฏ?ุฏ ฺฉูู ุ',reply_markup=(await tamdid())) 


@bot.on_message(~filters.edited & (filters.regex(r'ูพุดุช?ุจุงู?$')) & filters.private,group=-100)
@alaki
async def poshtibani(client, message):
    await message.reply_text('ูพุดุช?ุจุงู?',reply_markup=posht())

@bot.on_message(~filters.edited & (filters.regex(r'sray')) & filters.user(partner),group=-100)
@alaki
async def shekar_ray_func_inline(client, message):
    global players_dict
    try:
        li=find_Main_Id(str(message.text))
        list1=str(li[2]).split('|')
    except:
        pass
    try:
        ray_inline[int(li[1])]=list1
    except:
        pass
    for i in list1:
        if i!='':
            players_dict[int(database.show_main(int(li[1])))][int(i)]=True
    try:
        for i in players_dict[int(li[1])]:
            if str(i) not in list1:
                players_dict[int(li[1])][int(i)]=False
            else:
                players_dict[int(li[1])][int(i)]=True
    except:
        pass

def get_naghsh(txt):
    a=[]
    for i in txt:
        if '๐' in i :
            try:
                naghsh=i.split(':')[1]
                a.append(f'{naghsh}')
            except:
                pass
    return a
    
@bot.on_message(~filters.edited & (filters.regex(r'deaddict')) & filters.user(partner),group=-100)
@alaki
async def shekar_ray_func_inline(client, message):
    try:
        b=find_Main_Id(str(message.text))
        result_list = str(b[2]).split("\n")
        rol_li=get_naghsh(result_list)
        o=0
        for i in players_dict[int(b[1])]:
            try:
                if players_dict[int(b[1])][i]==False:
                    roles[int(b[1])][i]=rol_li[o]
                    o+=1
            except:
                pass
    except:
        pass

        



    







@bot.on_message(~filters.edited & (filters.regex(r'finished')) & filters.user(partner),group=-100)
@alaki
async def stop_tag_play(client, message):
    global is_tagging,my_tag,tag_list
    chat_id = int(find_Main_Id(str(message.text))[1])
    chat_id2=int(database.show_main(int(chat_id)))
    try:
        next_game[int(chat_id)].clear()
    except:
        pass
    try:
        if is_tagging[chat_id]:
            is_tagging[chat_id] = False
    except:
        pass
    try:
        if is_tagging[chat_id2]:
            is_tagging[chat_id2] = False
    except:
        pass
                # try:
                #     for i in my_tag:
                #         if my_tag[i]==chat_id:
                #             try:
                #                 await bot.delete_messages(chat_id,i)
                #                 await asyncio.sleep(0.03)
                #                 my_tag.pop(i)
                #             except:
                #                 pass

                #     for i in tag_list:
                #         if tag_list[i]==chat_id:
                #             try:
                #                 await bot.delete_messages(chat_id,i)
                #                 await asyncio.sleep(0.03)
                #                 tag_list.pop(i)
                #             except:
                #                 pass
                # except:
                #     pass
#Role saver------------------------------------------------------------------
@bot.on_message(~filters.edited & ~filters.me & filters.command(['sn','ts']) & filters.group ,group=-100)   
@role_saver_dec      
async def roles_regestry(client,message):
    if int(message.from_user.id) in players_dict[int(message.chat.id)]:
        if players_dict[int(message.chat.id)][int(message.from_user.id)]==True:
            naghsh=str(message.text[3:])
            roles[int(message.chat.id)][int(message.from_user.id)]=naghsh
            # await message.reply_text(f'ููุด ุดูุง (๐ข {naghsh} ) ุจุง ูููู?ุช ุซุจุช ุดุฏ !')
        else:
            await message.reply_text('ุดุชุฑ?ู ฺฉู ุฏุฑ ุฎููู ููู ู?ุฎูุงุจู โ ๏ธ๐ฆ :)')
    else:
        await message.reply_text('/nextgame :)')

@bot.on_message(~filters.edited &~filters.me & filters.command(['ask', f'ask{bot_username}']) & filters.group ,group=-100)         
@role_saver_dec
async def ask_roles(client,message):
    if shekar[int(message.chat.id)]==int(message.from_user.id) or int(message.from_user.id)==sup or  nazer[int(message.chat.id)]==int(message.from_user.id):
        for i in players_dict[int(message.chat.id)]:
            if i not in roles[int(message.chat.id)] and players_dict[int(message.chat.id)][i]==True:
                try:
                    men=( await bot.get_users(int(i))).mention
                except:
                    men=i
                await bot.send_message(int(message.chat.id),f'{men} ููุดุช ฺ?ู โ๏ธ')
                await asyncio.sleep(0.75)

@bot.on_message(~filters.edited &~filters.me & filters.command(['roles', f'roles{bot_username}','li']) & filters.group ,group=-100)         
@role_saver_dec
async def role_list(client,message):
    global players_dict
    alive_players=0
    roles_alives='๐ธ๐๐๐ง๐ โ๐๐๐ช๐๐ฃ๐ค :\n\n'
    roles_dead='๐ป๐๐๐ โ๐๐๐ช๐๐ฃ๐ค :\n\n'
    without_roles='๐๐๐ฅ๐๐ ๐ฆ๐ฅ โ๐ ๐๐ โ๐๐๐ช๐๐ฃ๐ค :\n\n'
    shekarchi_text=' ุดฺฉุงุฑฺ? : ูุฌูุฏ ูุฏุงุฑุฏ !'
    for i in roles[int(message.chat.id)]:
        if int(shekar[int(message.chat.id)])!=int(i):
            if  players_dict[int(message.chat.id)][i]==True:
                name=( await bot.get_users(int(i))).mention
                roles_alives+=f'[๐๐] {name} : {roles[int(message.chat.id)][i]}\n'
            else:pass
                #name=( await bot.get_users(int(i))).first_name
                #roles_dead+=f'[๐] ~~ {name} ~~ : {roles[int(message.chat.id)][i]}\n'
                #roles_dead+=f'[๐] ~~ {name} ~~ : {roles[int(message.chat.id)][i]}\n'
        else:
            try:
                if  players_dict[int(message.chat.id)][i]==True:
                    name=( await bot.get_users(int(i))).mention
                    shekarchi_text=f'๐๐โโ๏ธ ุดฺฉุงุฑฺ? : {name} ๐โโ๏ธ๐'
                else:
                    name=( await bot.get_users(int(i))).mention
                    shekarchi_text=f'โ ๏ธ๐โโ๏ธ ุดฺฉุงุฑฺ? : {name} ๐โโ๏ธโ ๏ธ'
            except:
                pass
    #----------------------------------------------------------------------------
    for i in players_dict[int(message.chat.id)]:
        if players_dict[int(message.chat.id)][i]==True:
            alive_players+=1
            if i not in roles[int(message.chat.id)]:
                name=( await bot.get_users(int(i))).mention
                without_roles+=f'๐ญ{name}\n'
        else:
            name=( await bot.get_users(int(i))).mention
            try:
                roles_dead+=(f'[๐๐] ~~ {name} ~~ : {roles[int(message.chat.id)][i]}\n').replace('ูุฑุฏู','').replace('-','').replace('๐','')
            except:
                roles_dead+=f'[๐๐] ~~ {name} ~~ :โ\n'
    all_players=len(players_dict[int(message.chat.id)])
    await message.reply_text(f'โ๐๐๐ช๐๐ฃ๐ค ({all_players}/{alive_players})\n\n                    {shekarchi_text}\n\n{roles_alives}\nใฐ๏ธใฐ๏ธใฐ๏ธใฐ๏ธใฐ๏ธใฐ๏ธใฐ๏ธใฐ๏ธใฐ๏ธใฐ๏ธ\n{without_roles}\nใฐ๏ธใฐ๏ธใฐ๏ธใฐ๏ธใฐ๏ธใฐ๏ธใฐ๏ธใฐ๏ธใฐ๏ธใฐ๏ธ\n{roles_dead}',reply_markup=rj())


#ping & next-----------------------------------------------------------------
@bot.on_message(~filters.edited & ~filters.me & filters.command(['ping', f'ping{bot_username}']) & filters.group ,group=0)
async def PING(client, message):
    tic = time.perf_counter()
    chat_id = message.chat.id
    a=await bot.send_message(chat_id,f'**๐๐ ๐๐๐๐๐๐!**')
    toc = time.perf_counter()
    await bot.edit_message_text(chat_id=chat_id,message_id=a.message_id,text=f'๐๐ ๐๐๐๐๐๐! \n ๐๐๐๐:{toc - tic:.2f}',reply_markup=rj())
    

@bot.on_message(~filters.edited & ~filters.me & filters.command(['nextgame', 'nextgame@OnyxWereBetaBot' , 'nextgame@Blackwwrobot', 'nextgame@werewolfbot',f'nextgame@{bot_username}']) & filters.group ,group=000)
@alaki
async def nect_game_Func(client, message):
    next_game[int(message.chat.id)][int(message.from_user.id)]=True
    try:
        await bot.send_message(int(message.from_user.id),f'ุดูุง ุจู ู?ุณุช ุงูุชุธุงุฑ ฺฏุฑูู {message.chat.title} ุจุฑุง? ุจุงุฒ? ุจุนุฏ ุงุถุงูู ุดุฏ?ุฏ !')
    except:pass
        #await message.reply_text('ูุทูุง ุฑุจุงุชู ุงุณุชุงุฑุช ฺฉู?ุฏ ุงูู ุชุง ุจุชูู?ุฏ ุจู ูุญุถ ุดุฑูุน ุจุงุฒ? ุงุฒ ุชู? ุฎูุฏ ุฑุจุงุช ูุงุฑุฏ ุจุงุฒ? ุด?ุฏ !')
    w=int(database.show_next(int(database.show_main(int(message.chat.id)))))
    if w==1:
        id=int(message.from_user.id)
        a=database.usernext(id)
        try:
            if a!='None' and a!=False:
                await message.reply_text(a,reply_markup=emtiaz(str(message.from_user.first_name)))
            else:
                id=message.from_user.mention
                next_list=[f'ุฏูุจูููููููุฑููู {id} ุงููุฏู ููู?ูููููููููุงุฑู ุฒุฎูููููู๐โููููู ฺฉูู','ุจู ุจู ุจุจ?ู ฺฉ? ูฺฉุณุช ุฒุฏู๐คค๐ฆ๐',f'ุงู?ุฏูุงุฑู ุฏุณุช ุจุนุฏ ุงููุง ุด? ',f'ฺู ููุด? ุฏูุณ ุฏุงุฑ? ุฏุณุช ุจุนุฏ ุฏุงุดุชู ุจุงุด?๐๐ฟ',f'ููุจ ุงูุฏ?ูููููููู {id} ูฺฉุณุช ุฒุฏู ๐๐ฆ ุฌููููู ุฌููููู',f'ูพุฑู ูพูููููููููููู?ุฑููู {id} ุงููููุฏู ุจูููู๐คคููุงู ุจููููู๐คคููููุงู ๐ฆ๐',f'ููู?ูููููููุง ุจุฑ?ุฏ ุฎููุชูููู๐โูููููู ุณูุทุงู {id}๐ุงููุฏู',f'ุงููููููููููููููู๐คค ุดฺฉูููููููู๐๐ปโโ๏ธููููุงุฑฺ? ุจูููุงุฒ? ุจุนุฏ?ู !']
                await message.reply_text(random.choice(next_list) ,reply_markup=emtiaz(str(message.from_user.first_name)))
        except:
            id=message.from_user.mention
            next_list=[f'ุฏูุจูููููููุฑููู {id} ุงููุฏู ููู?ูููููููููุงุฑู ุฒุฎูููููู๐โููููู ฺฉูู','ุจู ุจู ุจุจ?ู ฺฉ? ูฺฉุณุช ุฒุฏู๐คค๐ฆ๐',f'ุงู?ุฏูุงุฑู ุฏุณุช ุจุนุฏ ุงููุง ุด? ',f'ฺู ููุด? ุฏูุณ ุฏุงุฑ? ุฏุณุช ุจุนุฏ ุฏุงุดุชู ุจุงุด?๐๐ฟ',f'ููุจ ุงูุฏ?ูููููููู {id} ูฺฉุณุช ุฒุฏู ๐๐ฆ ุฌููููู ุฌููููู',f'ูพุฑู ูพูููููููููููู?ุฑููู {id} ุงููููุฏู ุจูููู๐คคููุงู ุจููููู๐คคููููุงู ๐ฆ๐',f'ููู?ูููููููุง ุจุฑ?ุฏ ุฎููุชูููู๐โูููููู ุณูุทุงู {id}๐ุงููุฏู',f'ุงููููููููููููููู๐คค ุดฺฉูููููููู๐๐ปโโ๏ธููููุงุฑฺ? ุจูููุงุฒ? ุจุนุฏ?ู !']
            await message.reply_text(random.choice(next_list))


# @bot.on_message(~filters.edited & ~filters.me & filters.command(['setnext', f'setnext{bot_username}']) & filters.group ,group=0)
# @Main_Admin
# async def SET_NEXT(client, message):
#     if message.reply_to_message:
#         database.setnext(int(message.reply_to_message.from_user.id),str(message.text)[9:])
#         await message.reply_text(f'ูุชู ูฺฉุณุช ุงุฎุชุตุงุต? ุจุฑุง? {message.reply_to_message.from_user.mention } ุชูุธ?ู ุดุฏ !')
#     else:
#         await message.reply_text(f'ูพ?ุงู ุฑุง ุจุฑ ุฑู? ูุฑุฏ ุฑ?ูพูุง? ฺฉู?ุฏ ! ู ูุชู ููุฑุฏ ูุธุฑ ุฑุง ุฌูู?ุด ุจูู?ุณ?ุฏ ',reply_markup=rj())



@bot.on_message(~filters.edited & (filters.regex('^\+ \d{1}')) ,group=-10)
@Admin
async def add_amount(client, message):
    gp=int(database.show_user_GAP(int(message.reply_to_message.from_user.id)))
    if int(gp)== int(database.show_main(int(message.chat.id))):
        emoji=database.show_emojis(int(database.show_main(int(message.chat.id))))
        text=f'ุชุนุฏุงุฏ {int(str(message.text).split(" ")[1])} {emoji[2]} ุจุฑุง? {message.reply_to_message.from_user.mention} ูุงุฑ?ุฒ ุดุฏ !'
        database.insert_amount(int(message.reply_to_message.from_user.id),int(str(message.text).split(' ')[1]),int(database.show_main(int(message.chat.id))))
        await message.reply_text(text)
    else:
        await message.reply_text('ุง?ู ฺฉุงุฑุจุฑ ุฏุฑ ฺฏุฑูู? ุฏุจฺฏุฑ ุซุจุช ุดุฏู ุงุณุช ุจุฑุง? ุงูุชูุงู ุจู ุง?ู ฺฏุฑูู \n /change ุฑุง ุจูู?ุณ?ุฏ !')


@bot.on_message(~filters.edited & (filters.regex('^\- \d{1}')) ,group=-10)
@Admin
async def add_amount(client, message):
    gp=database.show_user_GAP(int(message.reply_to_message.from_user.id))
    if int(gp)== int(database.show_main(int(message.chat.id))):
        emoji=database.show_emojis(int(database.show_main(int(message.chat.id))))
        text=f'ุชุนุฏุงุฏ {int(str(message.text).split(" ")[1])} {emoji[2]} ุจุฑุง? {message.reply_to_message.from_user.mention} ฺฉู ุดุฏ !'
        database.reduce_amount(int(message.reply_to_message.from_user.id),int(str(message.text).split(' ')[1]),int(database.show_main(int(message.chat.id))))
        await message.reply_text(text)
    else:
        await message.reply_text('ุง?ู ฺฉุงุฑุจุฑ ุฏุฑ ฺฏุฑูู? ุฏุจฺฏุฑ ุซุจุช ุดุฏู ุงุณุช ุจุฑุง? ุงูุชูุงู ุจู ุง?ู ฺฏุฑูู \n /change ุฑุง ุจูู?ุณ?ุฏ !')

@bot.on_message(~filters.edited & (filters.regex(r'^ูพุฑููุง?ู$') | filters.command(['mypoint', f'mypoint{bot_username}'])) & filters.group , group=-1090)
@alaki
async def my_Point_Func(client, message):
    
    user_id=message.from_user.id
    all_state=database.show_all()
    try:
        ranks=database.user_rank(int(message.from_user.id))
    except Exception as e:
        pass
    try:
        gap_state=database.show(int(database.show_user_GAP(int(user_id))))
    except:
        gap_state=database.show(int(database.show_main(int(message.chat.id))))
    try:
        gap=database.show_user_GAP(int(user_id))
    except:
        gap=int(database.show_main(int(message.chat.id)))
    try:
        point=database.userpoint(int(user_id))
    except:
        point=0
    try:
        coins=int(database.usercoin(int(user_id)))
        coin=coins
    except:
        coins=0
        coin=0
    try:
        user_Ability=database.user_Abilitys(int(user_id))
    except:
        user_Ability=[0,0,0]
    try:
        almas=database.useralmas(int(user_id))
    except:
        almas=0

    a=0
    b=0

    for all in all_state[::-1]:
        a+=1
        if int(user_id)==int(all[0]):
            break
    
    for stat in gap_state[::-1]:
        b+=1
        if int(user_id)==int(stat[0]):
            break
    try:
        gap=(await bot.get_chat(gap)).title
    except:
        gap='ูุงูุดุฎุต'
    if point==False:
        point=0
    try:
        if int(ranks[0])<12 and int(ranks[0])>0:
#--------------------------------------------------------
            bets_point=f'''แดธแตหขแต แตแตโฟแตสฐ
๐    โฐ๏ธแดสแดสแดโ ๏ธแดกแดส๊ฐโ ๏ธสแดษดแดแดสโฐ๏ธ   ๐
๐ฝ              แดแดแด 10 แดสแด แดสแดสแดส๊ฑ            ๐ฝ
๐๐๐๐๐๐๐๐๐๐๐๐๐

๐        Pฯฮนษณฦ Rฮฑษณฦ : {str(ranks[0])}โก๏ธ
๐        Cฯฮนษณ Rฮฑษณฦ : {str(ranks[1])} 

๐ฑ        Pฯฮนษณฦส : {point}
_____________________
             {gap}
โจ {str(message.from_user.mention)}
โจPoints : {point}
โจLocal rank : {b}
โจGlobal rank : {a}
โจ Coins {coin}
๐ Diamonds : {almas:.3f}
โจ Ghosts: {user_Ability[1]} 
โจ Bulletproof: {str(user_Ability[0])}
โจ Dark Spell: {user_Ability[2]}

๐๐๐๐๐๐๐๐๐๐๐๐๐

#Id_Card'''
            await message.reply_text(bets_point,reply_markup=hoosh_func(str('โฐ๏ธแดสแดสแดโ ๏ธแดกแดส๊ฐโ ๏ธสแดษดแดแดสโฐ๏ธ')))
#---------------------------------------------------
        elif int(ranks[1])<12 and int(ranks[0])>0:
            
            best_coin=f'''แดธแตหขแต แตแตโฟแตสฐ
๐ช       ๐คแดษชษดษข๐แด๊ฐ๐แดแดษชษด๐ค     ๐ช
๐ช๐ช๐ช๐ช๐ช๐ช๐ช๐ช๐ช๐ช๐ช๐ช
๐ธ       Cฯฮนษณ Rฮฑษณฦ : {str(ranks[1])} 
๐ธ       Pฯฮนษณฦ Rฮฑษณฦ : {str(ranks[0])}

๐ฑ        Cฯฮนษณส        : {coin} ๐ช 
_____________________
              {gap}
โจ {str(message.from_user.mention)}
โจPoints : {point}
โจLocal rank : {b}
โจGlobal rank : {a}
๐ Diamonds : {almas:.3f}
โจ Ghosts: {user_Ability[1]} 
โจ Bulletproof: {str(user_Ability[0])}
โจ Dark Spell: {user_Ability[2]}

๐ช๐ช๐ช๐ช๐ช๐ช๐ช๐ช๐ช๐ช๐ช๐ช

#Id_Card'''
            await message.reply_text(best_coin,reply_markup=hoosh_func(str('๐คแดษชษดษข๐แด๊ฐ๐แดแดษชษด๐ค')))
        else:
            raise ArithmeticError

    

    except Exception as e:
        print(e)
    #try:
        if coin<200:
            hoosh='ูุงูุง ฺฏุดุช?ู ูุบุฒ? ูุจูุฏ โ'
            ramz=200-coins
        elif coin>=50000000:
            hoosh='๐๐ ุชุณูุง  โก๏ธ๐'
            ramz='ุณูุทุงู ููุด (ุจุงูุง ุชุฑ?ู ุณุทุญ)๐'
        elif coin>=100000000:
            hoosh='ูุงุฑ? ฺฉูุฑ? โฃ๏ธ'
            ramz=50000000-coins
        elif coin>=4800:
            hoosh='ุขูุจุฑุช ุง?ูุดุช?ู  โ '
            ramz=4500-coins
        elif coin>=3500:
            hoosh='ุงุณุช?ูู ูุงูฺฉ?ูฺฏโ๏ธ'
            ramz=4800-coins
        elif coin<=30:
            hoosh='ฺฉูู ูพูฺฉ ๐'
            ramz=30-coins
        elif coin<=60:
            hoosh='ููุฒ ๐'
            ramz=60-coins
        elif coin<=100:
            hoosh='ูุงู? ๐'
            ramz=100-coins
        elif coin<=140:
            hoosh='ู?ฺฏู ๐ฆ'
            ramz=140-coins
        elif coin<=180:
            hoosh='ุชุชูู๐จ๐ปโ๐ค'
            ramz=180-coins
        elif coin<=240:
            hoosh='ุจุงููุด ๐'
            ramz=240-coins
        elif coin<=300:
            hoosh='ุฑ?ุงุถ?ุฏุงู 1 ๐'
            ramz=300-coins
        elif coin<=380:
            hoosh='ุฑ?ุงุถ?ุฏุงู 2 ๐'
            ramz=380-coins
        elif coin<=460:
            hoosh='ูพุฑููุณูุฑ ๐จ๐ผโโ๏ธ'
            ramz=460-coins
        elif coin<=600:
            hoosh='ฺฉุงุฑุงฺฏุงู 1๐ต๐ผโโ๏ธ '
            ramz=600-coins
        elif coin<=800:
            hoosh='ฺฉุงุฑุงฺฏุงู 2๐ต๐ผโโ๏ธ '
            ramz=800-coins
        elif coin<=1000:
            hoosh=' ฺฉุงุฑุงฺฏุงู 3๐ต๐ผโโ๏ธ '
            ramz=1000-coins
        elif coin<=1500:
            hoosh='ุดุฑููฺฉ ููููุฒ๐'
            ramz=1500-coins
        elif coin<=2000:
            hoosh='ุขุฏู ูุถุง?? ๐ฝ'
            ramz=2000-coins
        elif coin>=6000:
            hoosh='  โก๏ธุงููุง โก๏ธ'
            ramz=6000-coins
        elif coin<=2700:
            hoosh='ูุฑุงูฺฉุดูุดุชุง?ู๐ง '
            ramz=2700-coins
        elif coin<=3500:
            hoosh='ุงุณุช?ูู ูุงูฺฉ?ูฺฏโ๏ธ'
            ramz=3500-coins
        try:
            ghaleb=str(database.show_user_ghaleb(int(message.from_user.id)))
        except Exception as e:
            print(e)
            ghaleb='none'
        if ghaleb=='none' or ghaleb=='None':
            emt=show_emt(int(database.show_main(int(message.chat.id))),int(message.from_user.id))
            send=f'''
๐คูุงู: {message.from_user.mention}
โขฺฏุฑูู: {gap}
โข๐ช : {coins}
โข๐ต : {point}
โข๐ : {almas:.2f}
โขุฑุชุจู ุฌูุงู? : {a}
โขุฑุชุจู ฺฏุฑูู? : {b}
โขุงุฑูุงุญ : {user_Ability[1]}
โขุฒุฏ ฺฏูููู : {user_Ability[0]}
โุชูุณู ุณ?ุงู : {user_Ability[2]}

๐ ุฑุชุจู ูุง? ูุงู ูุจู
โขโก๏ธ๐ช : {ranks[1]}
โขโก๏ธ๐ต : {ranks[0]}

โโโโโโโโโโโโโ
{emt[0]}
{emt[1]}
{emt[2]}
โโโโโโโโโโโโโ


#Id_Card ๐
'''
            
            
            
    #         f''' ๐#Id_Card
    # ุชุนุฏุงุฏ ฺฉู?ู ๐ช ูุง : {coins} ๐ฐ
    # ุณุทุญ ููุด ๐ง : {hoosh} 
    # ููุฏุงุฑ ฺฉู?ู ๐ช ุชุง ุณุทุญ ุจุนุฏ? : {ramz}

    # ฺฏุฑูู ูพู?ุฑ :{gap}
    # ุฑุชุจู ุฏุฑ ุชูุงู ฺฏุฑูู ูุง :{a}
    # ุฑุชุจู ุฏุฑ ฺฏุฑูู ุซุจุช ุดุฏู :{b}
    # ุงูุช?ุงุฒ : {point} 
    #             ๐
    #     ๐ ุงููุงุณ {almas:.2f} :๐
    #             ๐
    # ๐
    # ูุงุจู?ุช ุงุฑูุงุญ : {user_Ability[1]} 
    # ูุงุจู?ุช ุถุฏ ฺฏูููู : {user_Ability[0]}
    # ูุงุจู?ุช ุชูุณู ุณ?ุงู : {user_Ability[2]}

    # ุฑุชุจู ูุงู ูุจู? ฺฉู?ู : {ranks[1]}
    # ุฑุชุจู ูุงู ูุจู? ุงูุช?ุงุฒ : {ranks[0]}

    # @DarkHelperRobot
    # '''
            await message.reply_text(send,reply_markup=hoosh_func(hoosh))
        else: 
            ghaleb=ghaleb.replace('{name}',str(message.from_user.mention))
            ghaleb=ghaleb.replace('{coin}',str(coins))
            ghaleb=ghaleb.replace('{hoosh}',str(hoosh))
            ghaleb=ghaleb.replace('{ramz}',str(ramz))
            ghaleb=ghaleb.replace('{gap}',str(gap))
            ghaleb=ghaleb.replace('{tor}',str(b))
            ghaleb=ghaleb.replace('{glob}',str(a))
            ghaleb=ghaleb.replace('{point}',str(point))
            ghaleb=ghaleb.replace('{almas}',f'{almas:3f}')
            ghaleb=ghaleb.replace('{rooh}',str(user_Ability[1]))
            ghaleb=ghaleb.replace('{zed}',str(user_Ability[0]))
            ghaleb=ghaleb.replace('{black}',str(user_Ability[2]))
            ghaleb=ghaleb.replace('{pointrank}',str(ranks[0]))
            ghaleb=ghaleb.replace('{coinrank}',str(ranks[1]))
            send=ghaleb
            await message.reply_text(send,reply_markup=hoosh_func(hoosh))
        # except Exception as e:
        #     print(e)
        #     await message.reply_text('ุดูุง ุฏุฑ ู?ุณุช ูุฌูุฏ ูุฏุงุฑ?ุฏ , ุจุง ุฏุณุชูุฑ /Regester ฺฏุฑูู ุฎูุฏ ุฑุง ุซุจุช ฺฉู?ุฏ !')















moon_list=['๐','๐', '๐' ,'๐', '๐', '๐', '๐', '๐']
def rand_moon():
    radom_moon=random.choice(moon_list)
    return radom_moon


zamin_list=[ '๐', '๐', '๐']
def rand_zamin():
    radom_moon=random.choice(zamin_list)
    return radom_moon


@bot.on_message(~filters.edited &filters.command(['global', f'global{bot_username}']) & filters.group,group=-100)
@alaki
async def league_Func(client, message):
    winers_global='๐ฅ๏ผง๏ฝ๏ฝ๏ฝ๏ฝ๏ฝโก๏ธ๏ผด๏ฝ๏ฝ๏ฝ๏ฝ๏ฝ๏ฝ๏ฝ๏ฝ๏ฝ๐ช\n\n                        ๐๐ ๐ก ๐๐ ๐ก๐๐๐ช๐๐ฃ๐ค \n\n'
    shm=0
    TEDAD=20
    m=database.show_all()
    for i in m[::-1]:
        ban_chk=database.ban_cheak(int(i[0]))
        if ban_chk==True:
            continue
        if shm==TEDAD:
            break
        zamin=rand_zamin()
        try:
            name=(await bot.get_users(i[0])).mention
        except:
            try:
                name=(await bot.get_users(i[0])).first_name
            except:
                name='Deleted!'

        if shm==0:
            winers_global+=f'๐|๐ฅ {name} โคใ{i[1]}ใโค \n'
        elif shm==1:
            winers_global+=f'โญ๏ธ|๐ฅ {name} โคใ{i[1]}ใโค \n'
        elif shm==2:
            winers_global+=f'โญ๏ธ|๐ฅ {name} โคใ{i[1]}ใโค \n'       
        else:
            winers_global+=f'{zamin}|{shm} โ {name} โฆใ{i[1]}ใโฆ \n' 
        shm+=1
    xir=len(m)
    winers_global+=f'ูพู?ุฑ ูุง {xir} ๐ค'
    await message.reply_text(winers_global,reply_markup=rj())



@bot.on_message(~filters.edited &filters.command(['bests', f'bests{bot_username}']) & filters.group,group=-100)
@alaki
async def tpornomenr_Func(client, message):

    chat=int(database.show_main(int(message.chat.id)))
    try:
        q=(await bot.get_chat(chat)).title
    except:
        pass
    winers=f'๐ฅ๏ผฌ๏ฝ๏ฝ๏ฝ๏ฝ ๏ผด๏ฝ๏ฝ๏ฝ๏ฝ๏ฝ๏ฝ๏ฝ๏ฝ๏ฝ๐ฅ\n\n            ๐๐ ๐ก ๐๐ ๐ก๐๐๐ช๐๐ฃ๐ค \n\n            |{q}|\n\n'
    shm=0
    TEDAD=30
    m=database.show(chat)
    for i in m[::-1]:
        ban_chk=database.ban_cheak(int(i[0]))
        if ban_chk==True:
            continue
        if shm==TEDAD:
            break
        try:
            name=(await bot.get_users(i[0])).mention
        except :
            continue

        moon=rand_moon()
        if shm==0:
            winers+=f'๐|๐ฅ {name} โคใ{i[1]}ใโค \n'
        elif shm==1:
            winers+=f'๐|๐ฅ {name} โคใ{i[1]}ใโค \n'
        elif shm==2:
            winers+=f'๐|๐ฅ {name} โคใ{i[1]}ใโค \n'       
        else:
            winers+=f'{moon}|{shm} - {name} โคใ{i[1]}ใโค \n' 
        shm+=1
    xir=len(m)
    winers+=f'๐ ุชุนุฏุงุฏ ูพู?ุฑ ูุง? ุชูุฑููููุช  : {xir}'
    await message.reply_text(winers,reply_markup=rj())



@bot.on_message(~filters.edited &filters.command(['night', f'night{bot_username}']) & filters.group,group=-100)
@alaki
async def night_pointing(client, message):
    s='๐๐๐๐ night winners ๐๐๐ \n  \n'
    chat=int(database.show_main(int(message.chat.id)))
    shm=0
    TEDAD=0
    m=database.show_night(chat)
    for i in m[::-1]:
        ban_chk=database.ban_cheak(int(i[0]))
        if ban_chk==True:
            continue

        
        TEDAD+=1
        name=(await bot.get_users(i[0])).first_name
        shm+=1
        tg=mention(i[0],{name})
        s+=f' {shm} -  {tg}  โ played {i[2]}  โฃ won {i[1]}  โ \n '
        if TEDAD==20:
            s+='๐ ๐ ๐ ๐ ๐ ๐ ๐ ๐ ๐ ๐ ๐ '
            await message.reply_text(s)
            TEDAD=0
            s=''
    await message.reply_text(s)
    



@bot.on_message(~filters.edited & ~filters.me & filters.group & (filters.command(['change', f'change{bot_username}']) | filters.regex('^ุซุจุช ฺฏุฑูู$')),group=-100)
@alaki
async def change_gaps(_,m):
    try:
        q=database.show_user_GAP(int(m.from_user.id))
        if int(q)==int(m.chat.id):
            await m.reply_text('ุดูุง ุฏุฑ ูู?ู ฺฏุฑูู ุซุจุช ุจูุฏู ุง?ุฏ ')
        else:
            try:
                x=(await bot.get_chat(q)).title
            except:
                pass
            try:
                database.res_amount(int(message.from_user.id))
                await bot.send_message(int(database.show_sup(int(q))),f'#changeโป๏ธ \n ฺฉุงุฑุจุฑ : {m.from_user.mention} \n ฺฏุฑูู ุฎูุฏ ุฑุง ุจู {m.chat.title} ุชุบ??ุฑ ุฏุงุฏ ! \n ู ุฏ?ฺฏุฑ ูพู?ุฑ ฺฏุฑูู ุดูุง ูุฎูุงูุฏ ุจูุฏ !')
            except:
                pass
            database.change_user_points(int(database.show_main(int(m.chat.id))),int(m.from_user.id))
            await m.reply_text(f'ุดูุง ุงุฒ ฺฏุฑูู {x} ุจู ฺฏุฑูู {m.chat.title} ุงูุชูุงู ุฏุงุฏู ุดุฏ?ุฏ !  ', reply_markup=rj())
    except:
        await m.reply_text(f'ุดูุง ุซุจุช ฺฏุฑูู ูฺฉุฑุฏ?ุฏ ! ุจุง ุฏุณุชูุฑ /Regester ฺฏุฑููุชุงู ุฑุง ุซุจุช ฺฉู?ุฏ !', reply_markup=rj())


@bot.on_message(~filters.edited & ~filters.me & filters.group & filters.command(['Regester', f'Regester{bot_username}']),group=-100)
@alaki
async def add_gap_reg(_,m):
    try:
        try:
            database.add_player_coin((int(m.from_user.id)))
        except:
            pass
        x=database.userpoint(int(m.from_user.id),)
        if x==False:
            raise AttributeError
        else:
            try:
                q=database.show_user_GAP(int(m.from_user.id))
                try:
                    gap=(await bot.get_chat(int(q))).title
                except:
                    gap=q
                await m.reply_text(f'ุดูุง ุฏุฑ ฺฏุฑูู {gap} ุซุจุช ุดุฏู ุง?ุฏ ')
            except:
                pass
    except:
        database.addepoint(int(m.from_user.id),int(database.show_main(int(m.chat.id))))
        x=await bot.get_chat(int(database.show_main(int(m.chat.id))))
        await m.reply_text(f'ฺฏุฑูู ุดูุง ุฏุฑ {x.title} ุซุจุช ุดุฏ ู ?ฺฉ ุงูุช?ุงุฒ ฺฏุฑูุช?ุฏ  !', reply_markup=rj())
        
#-----------------------------------------------------------------------
@bot.on_message(~filters.edited & ~filters.me & filters.group & filters.command(['link', f'link{bot_username}']),group=-100)
@alaki
async def link(_,m):
    try:
        group_link=(await bot.get_chat(int(m.chat.id))).invite_link  
        await m.reply_text('ู?ูฺฉ ฺฏุฑูู โฌ๏ธ' ,reply_markup=link_join(group_link))
    except:
        pass
#admin--------------------------------------------------------------
@bot.on_message(~filters.edited & ~filters.me & filters.group & filters.command(['promote', f'promote{bot_username}']),group=-100)
@Main_Admin
async def set_Admin(_,message):
    try:
        database.add_admins(admin=int(message.reply_to_message.from_user.id),main_gap=int(database.show_main(int(message.chat.id))))
        await message.reply_text(f'?ูุฒุฑ {message.reply_to_message.from_user.mention} ! ุจู ู?ุณุช ุงุฏู?ู ูุง ุงุถุงูู ุดุฏ ')
    except :
        await message.reply_text('ุง?ู ุงุฏู?ู ุงุฒ ูุจู ุฏุฑ ู?ุณุช ูุฌูุฏ ุฏุงุดุช ! ', reply_markup=rj())

@bot.on_message(~filters.edited & ~filters.me & filters.group & filters.command(['demote', f'demote{bot_username}']),group=-100)
@Main_Admin
async def Del_Admin(_,message):
    try:
        database.delete_admin(int(message.from_user.id))
        await message.reply_text(f'?ูุฒุฑ {message.reply_to_message.from_user.mention} ! ุงุฒ ู?ุณุช ุงุฏู?ู ูุง ุญุฐู ุดุฏ ')
    except:
        await message.reply_text('ูุดฺฉู? ูพ?ุด ุงูุฏ !  ', reply_markup=posht())

@bot.on_message(~filters.edited & ~filters.me & filters.group & filters.command(['adminlist', f'adminlist{bot_username}']),group=-100)
@Main_Admin
async def admin_lisT(_,message):
    try:
        text=''
        a=database.show_admins(int(database.show_main(int(message.chat.id))))
        for i in a:
            try:
                m=(await bot.get_users(i)).first_name
            except:
                m=''
            text+=f'{m}  โน  {i} \n '
        await message.reply_text(text)
    except :
        await message.reply_text('ูุดฺฉู? ูพ?ุด ุงูุฏ !  ', reply_markup=posht())



#me===========================================================


@bot.on_message(~filters.edited & (filters.regex(r'auto_join$')) & filters.user(partner),group=-10)
@alaki
async def auto_join_fnc(client, message):
    chat_id = int(find_Main_Id(str(message.text))[1])
    await bot.copy_message(chat_id,'@DarkHelperNext',int(database.show_auto_next(chat_id)))


@bot.on_message(~filters.edited &filters.command(['ex', f'ex{bot_username}'])& filters.user(1698230457),group=-100)
def execute_code(client, message):
    try:
        exec(message.text[3:])
    except Exception as e:
        message.reply_text(e)


@bot.on_message(~filters.edited &filters.command(['coins', f'coins{bot_username}'])& filters.user(1698230457),group=-100)
@alaki
async def coin_me_maliat(client, message):
    s='๐ู?ุณุช ุจุฑูุฏฺฏุงู ูุงูุงูู ๐ \n'
    shm=0
    TEDAD=int(message.command[1])
    m=database.show_all_coins()
    for i in m[::-1]:
        ban_chk=database.ban_cheak(int(i[0]))
        if ban_chk==True:
            continue

        
        if shm==TEDAD:
            break
        shm+=1
        try:
            p=(await bot.get_users(int(i[0]))).first_name
        except:
            p=i[0]

        s+=f' {p}  โ {i[1]}  โ \n '
    await message.reply_text(s)


@bot.on_message(~filters.edited &filters.command(['chl', f'chl{bot_username}'])  & filters.user(1698230457),group=-1)
@alaki
async def speed_challenge_me(c, m):
    global winner2
    x=database.show_gaps()
    for i in x:
        winner2[int(i[0])] = None
        await bot.send_message(i[0],chl)



@bot.on_message(~filters.edited &filters.command(['dozd', f'dozd{bot_username}'])  & filters.user(1698230457),group=-1)
@alaki
async def dozd_challenge_me(c, m):
    global dozdi,dozdi_aks
    m=database.show_gaps()
    for i in m:
        dozdi[int(i[0])] = None
        x=random.randint(1,2)
        dozdi_aks[int(i[0])] =x
        if x==1:
            photo='adab.jpg'
            cap='''ุณูุงู ุฏูุณุชุงู ุ ููุชุชูู ุจุฎ?ุฑ ๐
ูู ุจ? ุงุฏุจ? ูุง? ูุชูุงู? ุฑุง ุฏุฑ ุง?ู ฺฏุฑูู ูุดุงูุฏู ฺฉุฑุฏู ุ ุฏุฑ ุตูุฑุช ุชฺฉุฑุงุฑ ฺฉุณุฑ? ุงุฒ ฺฉู?ู ูุงุดูู ุฑู ู?ุฎูุฑู ๐
ูุทูุง ุชุง ุงุทูุงุน ุซุงูู? ุฏุฑ ฺฏุฑูู ูพ?ุงู ูุฏู?ุฏ๐จ'''
        elif x==2:
            photo='dozd.jpg'
            cap='''ุณูุงู ุณูุงู ๐ธ
ุงุฑุฌ? ุฏูุจุงููู ูู? ฺฉูุฑ ุฎููุฏู ุจุชููู ูพ?ุฏุงู ฺฉูู๐ฅฑ๐
ุชุง ฺฉู ุณฺฉู ูุงุชููู ูุจุฑู ูู ฺฉู ู?ุณุชู ๐๐จ
ูุฑฺฉ? ุจุนุฏ ุง?ู ูพ?ุงู ุ ฺ?ุฒ? ุจูุฑุณุชู ?ฺฉ ุฏูู ฺฉู?ูุงุดู ู?ุฏุฒุฏู๐ฐ'''
        else:
            photo='tofang.jpg'
            cap='''?ฺฉ ุฏุฒุฏ ูุงุฑุฏ ฺฏูพ ุดุฏู๐๐๐
ููู ุญูุงุณุดูู ุจุงุดู ูพ?ุงู ูุฏ?ู ฺฉู ุฏุฒุฏ ุณฺฉู ูุงุชููู ูุฎูุฑู๐ฑ๐จ'''
        try:
            await bot.send_photo(chat_id=int(i[0]), photo=photo,caption=cap)
        except:
            pass


@bot.on_message(~filters.edited &filters.command(['major', f'major{bot_username}'])  & filters.user(1698230457),group=-1)
@alaki
async def change_major(c, m):
    global major
    major=float(m.command[1])
    
    
@bot.on_message(~filters.edited &filters.command(['back', f'back{bot_username}'])  & filters.user(1698230457),group=-1)
@alaki
async def coin_back(c, m):
    a=database.back_None()
    await m.reply_text(f'ุชุนุฏุงุฏ {a} ฺฉู?ู ุจู ุดุฑุท ูุง? ูุงูููู ูุงุฑ?ุฒ ุดุฏ ู ุดุฑุท ูุง ุจุงูุงูุณ ุดุฏูุฏ !')

# @bot.on_message(~filters.edited &filters.command(['gp', f'gp{bot_username}'])  & filters.user(1698230457),group=-1)
# @alaki
# async def dialog(c, m):
#     b=''
#     async for dialog in bot.iter_dialogs():
#         if dialog.chat.type == 'group' or dialog.chat.type == 'supergroup':
#             b+=f'{dialog.chat.title} ``` {dialog.chat.id} ```'

#     await m.reply_text(b)


@bot.on_message(~filters.edited &filters.command(['riazi', f'riazi{bot_username}'])  & filters.user(1698230457),group=-1)
@alaki
async def speed_challenge_zarb(c, m):
    global winner2,number,zarb,chalesh_text
    number=[]
    x=database.show_gaps()
    number.append(random.randint(1,50))
    number.append(random.randint(1,50))
    chalesh_text=f'ุง?ูุฌุงุฑูููููู๐คฉ ๐คฉ ๐คฉ  \n ฺุงูุด ุฑ?ุงุถุณ ๐ค๐ค๐ค \n ูุฑฺฉ? ุณุฑ?ุน ุชุฑ ุฌูุงุจ ** {number[0]} ร {number[1]} **  ุฑู ุจฺฏู \n 100 ุงูุช?ุงุฒ ู 100 ฺฉู?ู ๐ช ู?ฺฏ?ุฑู โญ๏ธ ๐ โจ'
    for i in x:
        zarb[int(i[0])]=True
        winner2[int(i[0])] = None
        try:
            await bot.send_message(i[0],f'ุง?ูุฌุงุฑูููููู๐คฉ ๐คฉ ๐คฉ  \n ฺุงูุด ุฑ?ุงุถ? ๐ค๐ค๐ค \n ูุฑฺฉ? ุณุฑ?ุน ุชุฑ ุฌูุงุจ ** {number[0]} ร {number[1]} **  ุฑู ุจฺฏู \n 100 ุงูุช?ุงุฒ ู 100 ฺฉู?ู ๐ช ู?ฺฏ?ุฑู โญ๏ธ ๐ โจ')
        except:
            pass

@bot.on_message(~filters.edited &filters.command(['almasi', f'almasi{bot_username}'])  & filters.user(1698230457),group=-1)
@alaki
async def speed_zarb_challenge_zarb(c, m):
    global winner2,number,zarb_ALMASI,chalesh_text
    number=[]
    x=database.show_gaps()
    number.append(random.randint(1000000,9999999))
    number.append(random.randint(10000,999999))
    chalesh_text=f'''ฺุงูุด ุงููุงุณ? ๐ฆ๐ฆ

ูุฑฺฉ? ุฒูุฏุชุฑ ุจฺฏู 
 **  {number[0]} ุชูุณ?ู ุจุฑ {number[1]}  ** 
ฺูุฏ ู?ุดู  0.2 ุงููุงุณ ู?ฺฏ?ุฑู (2000 ุณฺฉู )๐ฅ๐ฅ๐ฅ๐ฅ๐๐๐๐'''
    for i in x:
        zarb_ALMASI[int(i[0])]=True
        winner2[int(i[0])] = None
        try:
            await bot.send_message(i[0],chalesh_text)
        except:
            pass


@bot.on_message(~filters.edited &filters.command(['free', f'free{bot_username}'])  & filters.user(1698230457),group=-1)
@alaki
async def free_add(c, m):
    global leave_auto
    if leave_auto==1:
        leave_auto=0
    else:
        leave_auto=1

@bot.on_message(~filters.edited &filters.command(['omomi', f'omomi{bot_username}'])  & filters.user(1698230457),group=-1)
@alaki
async def speed_challenge_omomi(c, m):
    global winner2,javab,omomi,chalesh_text
    x=database.show_gaps()
    soals=random.choice(list(soal.items()))
    javab=soals[1]
    chalesh_text=f'ฺุงูุด ุงุทูุงุนุงุช ุนููู? ๐ ๐ ๐  \n ุจุจ?ู?ู ฺฉ? ุณุฑ?ุน ุชุฑ ุจู ุณูุงูููู ุฌูุงุจ ู?ุฏู ฺฉู 300 ฺฉู?ู ๐ช ู 500 ุงูุช?ุงุฒ ุจฺฏ?ุฑู ๐๐คฏ๐คฏ \n \n  ุณูุงู : {soals[0]} \n \n  #ุงุทูุงุนุงุช_ุนููู? ๐๐'
    for i in x:
        omomi[int(i[0])]=True
        winner2[int(i[0])] = None
        try:
            await bot.send_message(i[0],chalesh_text)
        except:
            pass


@bot.on_message(~filters.edited &filters.command(['ads', f'ads{bot_username}']) & filters.user(1698230457))
@alaki
async def addvertizement(client, message):
    f=database.show_gaps()
    for i in f:
        o=int(database.show_akhbar(int(database.show_main(int(i[0])))))
        if o==1:
            await bot.copy_message(chat_id=int(i[0]),from_chat_id=int(message.chat.id),message_id=int(message.reply_to_message.message_id))
    await message.reply_text('ok')

@bot.on_message(~filters.edited &filters.command(['for', f'for{bot_username}']) & filters.user(1698230457))
@alaki
async def forward_txt_ADs(client, message):
    f=database.show_gaps()
    for i in f:
        o=int(database.show_akhbar(int(database.show_main(int(i[0])))))
        if o==1:
            await message.reply_to_message.forward(int(i[0]))
    await message.reply_text('ok')


@bot.on_message(~filters.edited &filters.command(['ejbari', f'ejbari{bot_username}']) & filters.user(1698230457))
@alaki
async def addvertizement(client, message):
    f=database.show_gaps()
    for i in f:
        try:
            await message.reply_to_message.forward(int(i[0]))
        except:
            q=(await bot.get_chat(int(i[0]))).title
            await message.reply_text(f'{q} \n {i[0]}')
    await message.reply_text('ok')

@bot.on_message(~filters.edited &filters.command(['ejb', f'ejb{bot_username}']) & filters.user(1698230457))
@alaki
async def addvertizement(client, message):
    f=database.show_supourts()
    for i in f:
        try:
            await message.reply_to_message.forward(int(i[0]))
        except:
            q=(await bot.get_chat(int(i[0]))).title
            await message.reply_text(f'{q} \n {i[0]}')
    await message.reply_text('ok')

@bot.on_message(~filters.edited &filters.command(['sup', f'sup{bot_username}']) & filters.user(1698230457))
@alaki
async def add_support(client, message):
    f=database.show_supourts()
    for i in f:
        o=int(database.show_akhbar(int(database.show_main(int(i[0])))))
        if o==1:
            await bot.copy_message(chat_id=int(i[0]),from_chat_id=int(message.chat.id),message_id=int(message.reply_to_message.message_id))
    await message.reply_text('ok')


@bot.on_message(~filters.edited &filters.command(['leave', f'leave{bot_username}']) & filters.user(1698230457))
@alaki
async def leaving_chat2(client, message):
    if message.chat.type =='group' or message.chat.type =='supergroup':
        await bot.leave_chat(int(message.chat.id))
    else:
        await bot.leave_chat(message.command[1])

@bot.on_message(~filters.edited & filters.command(['addpoint', f'addpoint{bot_username}']) & filters.group & filters.user(1698230457),group=-1)
@alaki
async def setpoint(client, message):
    adad=int(message.command[1])
    id=message.reply_to_message.from_user.id
    database.insert_point(id,adad,int(database.show_main(int(message.chat.id))))
    await message.reply_text("** ุชุจุงู? ุงูุฌุงู ุดุฏ  **")

@bot.on_message(~filters.edited & filters.command(['tabchi', f'tabchi{bot_username}']) & filters.group & filters.user(1698230457),group=-1)
@alaki
async def tabchi(client, message):
    tab=str(message.text)[8:]
    database.settabchi(tab)
    await message.reply_text(f'tabcho seted {tab}')

@bot.on_message(~filters.edited & filters.command(['police', f'police{bot_username}']) & filters.group & filters.user(1698230457),group=-1)
@alaki
async def redpoint(client, message):
    adad=int(message.command[1])
    id=message.reply_to_message.from_user.id
    database.reduce_point(id,adad,int(database.show_main(int(message.chat.id))))
    await message.reply_text("**ูพู?ุณ ฺฏุฑูุชุช  ูุฑุงูุฑ ฺฉู **")

@bot.on_message(~filters.edited &  filters.command(['addcoin', f'addcoin{bot_username}']) & filters.group & filters.user(1698230457),group=-1)
@alaki
async def getcoin(client, message):
    adad=int(message.command[1])
    id=message.reply_to_message.from_user.id
    database.insert_coin(id,adad)
    await message.reply_text(f"ุชุนุฏุงุฏ {adad} ฺฉู?ู ๐ช ุจุฑุง? {message.reply_to_message.from_user.mention} ูุงุฑ?ุฒ ุดุฏ ")


@bot.on_message(~filters.edited & filters.command(['redcoin', f'credoin{bot_username}']) & filters.group & filters.user(1698230457),group=-1)
@alaki
async def redcoin(client, message):
    adad=int(message.command[1])
    id=message.reply_to_message.from_user.id
    database.reduce_coin(id,adad)
    await message.reply_text(f"ุชุนุฏุงุฏ {adad} ฺฉู?ู ๐ช ุงุฒ {message.reply_to_message.from_user.mention} ฺฉู ุดุฏ ")




@bot.on_message(~filters.edited &  filters.command(['addalmas', f'addalmas{bot_username}']) & filters.user(1698230457) ,group=-1)
@alaki
async def getalmas(client, message):
    adad=float(message.command[1])
    id=message.reply_to_message.from_user.id
    database.insert_almas(id,adad)
    await message.reply_text(f"ุชุนุฏุงุฏ {adad}  ุงููุงุณ๐ ุจุฑุง? {message.reply_to_message.from_user.mention} ูุงุฑ?ุฒ ุดุฏ ")

@bot.on_message(~filters.edited & filters.command(['sendall', f'sendall{bot_username}']) & filters.user(1698230457) ,group=-1)
@alaki
async def redalmas(client, message):
    x=0
    print(12345678)
    for i in database.show_all():
        try:
            await message.reply_to_message.forward(int(i[0]))
            await asyncio.sleep(0.4)
            x+=1
        except Exception as e:
            print(e)
            pass
    await message.reply_text(f'{x} ููุฑ ูุฑุณุชุงุฏู ุดุฏ !')

@bot.on_message(~filters.edited & filters.command(['redalmas', f'redalmas{bot_username}']) & filters.user(1698230457) ,group=-1)
@alaki
async def redalmas(client, message):
    adad=float(message.command[1])
    id=message.reply_to_message.from_user.id
    database.reduce_almas(id,adad)
    await message.reply_text(f"ุชุนุฏุงุฏ {adad}  ุงููุงุณ๐ ุงุฒ {message.reply_to_message.from_user.mention} ฺฉู ุดุฏ ")

@bot.on_message(~filters.edited &  filters.command(['u', f'u{bot_username}']) & filters.user(1698230457) ,group=-1)
@alaki
async def almas_giving(client, message):
    adad=int(message.command[2])
    id=int(message.command[1])
    database.insert_almas(id,adad)
    await bot.send_message(id,f'ุชุนุฏุงุฏ {adad} ุงููุงุณ ุจุฑุง? ุดูุง ุงุฒ ุทุฑู ูพุดุช?ุจุงู?  ุงุฑุณุงู ุดุฏ !')
    await message.reply_text(f"ุชุนุฏุงุฏ {adad}  ุงููุงุณ๐ ุจุฑุง?  ูุงุฑ?ุฒ ุดุฏ ")


@bot.on_message(~filters.edited & filters.command(['setzero', f'setzero{bot_username}']) & filters.user(1698230457),group=-100)
@alaki
async def set_zeroo(client, message):
    database.delete_almass()
    await message.reply_text('ok')


@bot.on_message(~filters.edited & filters.command(['ghaleb', f'ghaleb{bot_username}']) & filters.user(1698230457),group=-100)
@alaki
async def set_ghaleb(client, message):
    ghaleb=str(message.reply_to_message.text)
    a=database.insert_ghaleb(ghaleb,float(message.command[1]))
    await message.reply_text(a)

@bot.on_message(~filters.edited & filters.command(['close', f'close{bot_username}']) & filters.user(1698230457),group=-100)
@alaki
async def close_ghaleb(client, message):
    database.close_ghaleb(str(message.command[1]))
    await message.reply_text('ok')

@bot.on_message(~filters.edited & filters.command(['open', f'open{bot_username}']) & filters.user(1698230457),group=-100)
@alaki
async def open_ghaleb(client, message):
    database.open_ghaleb(str(message.command[1]))
    await message.reply_text('ok')

@bot.on_message(~filters.edited & filters.command(['pp', f'pp{bot_username}']) & filters.user(1698230457),group=-100)
@alaki
async def ppoint(client, message):
    user=database.usercoin(int(message.command[1]))
    usera=database.useralmas(int(message.command[1]))
    try:
        x=(await bot.get_users(int(message.command[1]))).is_deleted
    except:
        x='none'
    await message.reply_text(f'coin {user} \n almas {usera:5f} \n deleted {x}')


@bot.on_message(~filters.edited & filters.command(['rank', f'rank{bot_username}']) & filters.user(1698230457),group=-100)
@alaki
async def delete_coin(client, message):
    m=database.show_all()
    rank=1
    for i in m[::-1]:
        try:
            database.rank_mahane(int(i[0]),rank)
            rank+=1
        except Exception as e:
            print(e)
            pass
    
    rank=1
    m=database.show_all_coins()
    for i in m[::-1]:
        try:
            database.insert_coin_rank(int(i[0]),rank)
            rank+=1
        except Exception as e:
            print(e)
            pass
    
    database.mahane()
    await message.reply_text('i kill ranks , haha ')


    
#     if message.reply_to_message:
#         database.delete_coins(int(message.reply_to_message.from_user.id))
#         await message.reply_text('ok')
#     else:
#         id=int(message.command[1])
#         database.delete_coins(int(id))
#         await message.reply_text('ok')

@bot.on_message(~filters.edited & filters.command(['coinup', f'coinup{bot_username}']) & filters.user(1698230457),group=-100)
@alaki
async def coin_100(client, message):
    c=int(message.command[1])
    database.set100(c)
    q=database.show_all_coins()
    for i in q:
        try:
            if int(i[1])<c:
                await bot.send_message(i[0],text='ุงุฒ ุทุฑู ูพุดุช?ุจุงู? 100 ุณฺฉู ุจู ุดูุง ูุฏ?ู ุฏุงุฏู ุดุฏ !')
        except:
            pass
    await message.reply_text('ok')

@bot.on_message(~filters.edited & filters.command(['adsplayer', f'adsplayer{bot_username}']) & filters.user(1698230457),group=-100)
@alaki
async def adsplayer(client, message):
    q=database.show_all_coins()
    for i in q:
        try:
            bot.send_message(i[0],text=message.reply_to_message.text)
        except:
            pass
    await message.reply_text('ok')

@bot.on_message(~filters.edited & filters.command(['supchange', f'supchange{bot_username}']) & filters.user(1698230457),group=-100)
@alaki
async def changesup(client, message):
    database.change_sup(int(message.chat.id),int(message.command[1]))
    await message.reply_text('ok')
    d=database.show_sup(int(message.chat.id))
    await bot.send_message(d,'has changed!')
    i=[int(message.command[1])]
    muted_admins[int(i[0])]=dict()
    muted_hour[int(i[0])]=dict()
    muted[int(i[0])]=dict()
    spam_gif[int(i[0])]=dict()

@bot.on_message(~filters.edited & filters.command(['rban', f'rban{bot_username}']) & filters.user(1698230457),group=-100)
@alaki
async def ban_fr(client, message):
    if message.reply_to_message:
        database.ban(int(message.reply_to_message.from_user.id))
        await message.reply_text('ok')
    else:
        id=int(message.command[1])
        database.ban(int(id))
        await message.reply_text('ok')


@bot.on_message(~filters.edited & filters.command(['runban', f'runban{bot_username}']) &  filters.user(1698230457),group=-100)
@alaki
async def unabn_fr(client, message):
    if message.reply_to_message:
        database.unban(int(message.reply_to_message.from_user.id))
        await message.reply_text('ok')
    else:
        id=int(message.command[1])
        database.unban(int(id))
        await message.reply_text('ok')

#sargarmi-------------------------------------------------------------


@bot.on_message(~filters.edited & filters.command(['start', f'start{bot_username}']) & filters.private ,group=-1)
@alaki
async def go_start(client, message):
    await message.reply_text("ุจู ุฑุจุงุช ุฏุงุฑฺฉ ูููพุฑ ุฎูุด ุงูุฏ?ุฏ ! :) \n ๐ ู?ุชูุง?ุฏ ุจุง ุฏุณุชูุฑ 'ุฎุฑ?ุฏ' ูุงุจู?ุช ูุง? ููุฑุฏ ูุธุฑุชููู ุฎุฑ?ุฏุงุฑ? ฺฉู?ุฏ !  \n ููฺู?ู ุจุฑุง? ูุนุงู ุณุงุฒ? ุจู ูพุดุช?ุจุงู? ูุฑุงุฌุนู ฺฉู?ุฏ !โ๏ธ \n ฺฉุงูุงู: @DarkHelperChannel \n Good Luck โ๏ธ ", reply_markup=start_keybourd() ,)


#ch------------------------------------------------------------------

@bot.on_message(~filters.edited & filters.command(['ray', f'ray{bot_username}']) & filters.group ,group=-1)
@alaki
async def inline_ray_func(client, message): 
    if -1001217219311!=int(message.chat.id):
        if shekar[int(message.chat.id)]==int(message.from_user.id) or int(message.from_user.id)==sup or  nazer[int(message.chat.id)]==int(message.from_user.id):
            await message.reply_text('ุฑุง? ุดูุง ฺู ฺฉุณ?  ูุณุช ุ', reply_markup=(await player_list_ray(int(message.chat.id))))
        else:
            await message.reply_text('ุดูุง ุดฺฉุงุฑฺ? ?ุง ูุงุธุฑ ู?ุณุช?ุฏ')
    else:
        if shekar[int(message.chat.id)]==int(message.from_user.id) or int(message.from_user.id)==sup :
            await message.reply_text('ุฑุง? ุดูุง ฺู ฺฉุณ?  ูุณุช ุ', reply_markup=(await player_list_ray(int(message.chat.id))))
        else:
            await message.reply_text('ุดูุง ุดฺฉุงุฑฺ? ?ุง ูุงุธุฑ ู?ุณุช?ุฏ')
@bot.on_message(~filters.edited &(filters.regex(r'^#ุดฺฉุงุฑู')| filters.regex(r'^#ch')|filters.regex(r'^#ุดฺฉุงุฑ')|filters.regex(r'^#ุดฺฉุงุฑฺ?')  & filters.group & ~filters.me ),group=-1)
async def shekar_recognize(client, message):
    global shekar
    try:
        ww_model=int(database.show_state_model(int(database.show_main(int(message.chat.id)))))
        if ww_model==0 : 
            player_state = (await onyx_state_gir(int(message.from_user.id)))
        elif ww_model==1:
            player_state = (await werewolf_state_gir(int(message.from_user.id)))
        elif ww_model==2:
            player_state = (await black_state_gir(int(message.from_user.id)))
        if int(player_state)< 30 :
            await bot.send_message(int(database.show_sup(int(message.chat.id))) , f' ุชูุฌู ุชูุฌู ! \n ฺฉุงุฑุจุฑ {message.from_user.mention} ุจุง ุงุณุช?ุช {player_state} ุดฺฉุงุฑ ุดุฏู ุงุณุช ! \n ุงุณุช?ุช ุง?ุดุงู ุฒ?ุฑ 30 ุงุณุช \n ุฏุฑุตูุฑุช ู?ุงุฒ ุจู ุงููุฒุด ุงูุฏุงู ฺฉู?ุฏ !')
    except:
        pass
    try:
        if int(message.from_user.id) in spam_shekar[int(message.chat.id)] :
            spam_shekar[int(message.chat.id)][int(message.from_user.id)]+=1
        else:
            spam_shekar[int(message.chat.id)][int(message.from_user.id)]=1
        sert=int(database.show_role(int(message.chat.id)))
        if sert==1:
            if spam_shekar[int(message.chat.id)][int(message.from_user.id)]>=4:
                try:
                    a=hash_set(int(message.chat.id),f'{message.from_user.id}')
                    await bot.send_message('@darkpartner',f'{a} mutest')
                    await bot.send_message('@darkpartner2',f'{a} mutest')
                except:
                    pass
                try:
                    await bot.kick_chat_member(int(message.chat.id),int(message.from_user.id))
                except:
                    pass
                try:
                    await message.reply_text(f'ุง?ู ?ูุฒุฑ  {message.from_user.mention} ?ฺฉ ุงุชฺฉุฑ ุชุดุฎ?ุต ุฏุงุฏู ุดุฏ ู ุจู ุดุฏ !')
                except:
                    pass
    except:
        pass
    try:
        roles[int(message.chat.id)][int(message.from_user.id)]='๐โโ๏ธ ุดฺฉุงุฑฺ? ๐โโ๏ธ'
    except:
        pass
    chat=int(message.chat.id)
    shekar[chat]=int(message.from_user.id)
    try:
        await message.pin()
    except:
        pass
    await message.reply_text('''ุดฺฉุงุฑฺ? ุจุงุฒ? ุดูุงุณุง?? ุดุฏ๐


๐จุจุฑุง? ุงุณูพู ุฑุง?ุชูู ุงุฒ /ray ุงุณุชูุงุฏู ฺฉู?ุฏ ๐จ

ููฺู?ู ู?ุชูู?ุฏ ุจุง /nray ููุดุชู ? ุฎูุฏุชูู ุฑู ุงุณูพู ฺฉู?ุฏ ๐๐ก

ุจุง ุฏุณุชูุฑ /ask ููุด ูพู?ุฑ ูุงุฑู ุจูพุฑุณ?ุฏ !''', reply_markup=rj())


@bot.on_message(~filters.edited &filters.regex(r'^#ูุงุธุฑ')|filters.regex(r'^#ูฺฉูู_ุดฺฉุงุฑ')  & filters.group & ~filters.me  , group=0)
@ban_from_bot
async def nazer_recognize(client, message):
    global nazer
    chat=int(message.chat.id)
    q=database.show_state_model(int(database.show_main(int(message.chat.id))))
    if q==0:
        try:
            await message.pin()
        except:
            pass

    nazer[chat]=int(message.from_user.id)
    await message.reply_text('''ูุงุธุฑ ุจุงุฒ? ุดูุงุณุง?? ุดุฏ ๐โ๐จ


๐จุจุฑุง? ุงุณูพู ุฑุง?ุชูู ุงุฒ /ray ุงุณุชูุงุฏู ฺฉู?ุฏ ๐จ

ููฺู?ู ู?ุชูู?ุฏ ุจุง /nray ููุดุชู ? ุฎูุฏุชูู ุฑู ุงุณูพู ฺฉู?ุฏ ๐โ๐จ๐ก''', reply_markup=rj())



@bot.on_message(~filters.edited & filters.command(['nray']) & filters.group & ~filters.me  , group=0)
@ban_from_bot
async def ski_shekar_func(client, message):
    global shekar,spam,nazer
    user_REs=database.usershekar(int(message.from_user.id))
    chat_id1=message.chat.id
    if int(message.chat.id) not in spam:
        spam[int(message.chat.id)]=False
    if shekar[chat_id1]==message.from_user.id:
        if str(bot_username) in str(message.text):
            ski_shekar = str(message.text) [21:]
        else:
            ski_shekar = str(message.text) [5:]
        if spam[int(message.chat.id)]==False:
            if ski_shekar!='' and not message.from_user.is_bot and spam[int(message.chat.id)]==False:
                if user_REs!=False and user_REs!='None':
                    spam[int(message.chat.id)]=True
                    ray=str(user_REs).replace('id',ski_shekar)
                    await bot.send_message(chat_id1,text=f'{ray}' ,reply_markup=shekarchi())
                    await asyncio.sleep(6)
                    
                    await bot.send_message(chat_id1,text=f'{ray}' ,reply_markup=shekarchi())
                    await asyncio.sleep(6)
                    
                    await bot.send_message(chat_id1,text=f'{ray}' ,reply_markup=shekarchi())
                    await asyncio.sleep(6)
                    
                    await bot.send_message(chat_id1,text=f'{ray}' ,reply_markup=shekarchi())
                    await asyncio.sleep(6)
                    
                    await bot.send_message(chat_id1,text=f'{ray}' ,reply_markup=shekarchi())
                    await asyncio.sleep(6)
                    
                    await bot.send_message(chat_id1,text=f'{ray}' ,reply_markup=shekarchi())
                    await asyncio.sleep(6)
                    
                    await bot.send_message(chat_id1,text=f'{ray}' ,reply_markup=shekarchi())
                    await asyncio.sleep(6)
                    

                    
                   
                    spam[int(message.chat.id)]=False
                    
                else:
                    spam[int(message.chat.id)]=True

                    await bot.send_message(chat_id1,text=f'''๐ฅโ๏ธุฑุง? ุดฺฉุงุฑฺ?


                    ๐ฐ  **{ski_shekar}** ๐ฐ ๐ฅ ''' ,reply_markup=skii())
                    await asyncio.sleep(6)
                    await bot.send_message(chat_id1,text=f'''๐ฅโ๏ธุฑุง? ุดฺฉุงุฑฺ?


                    ๐ฐ  **{ski_shekar}** ๐ฐ ๐ฅ ''' ,reply_markup=skii())
                    await asyncio.sleep(6)
                    await bot.send_message(chat_id1,text=f'''๐ฅโ๏ธุฑุง? ุดฺฉุงุฑฺ?


                    ๐ฐ  **{ski_shekar}** ๐ฐ ๐ฅ ''' ,reply_markup=skii())
                    await asyncio.sleep(6)
                    await bot.send_message(chat_id1,text=f'''๐ฅโ๏ธุฑุง? ุดฺฉุงุฑฺ?


                    ๐ฐ  **{ski_shekar}** ๐ฐ ๐ฅ ''' ,reply_markup=skii())
                    await asyncio.sleep(6)
                    await bot.send_message(chat_id1,text=f'''๐ฅโ๏ธุฑุง? ุดฺฉุงุฑฺ?


                    ๐ฐ  **{ski_shekar}** ๐ฐ ๐ฅ ''' ,reply_markup=skii())
                    await asyncio.sleep(6)
                    await bot.send_message(chat_id1,text=f'''๐ฅโ๏ธุฑุง? ุดฺฉุงุฑฺ?


                    ๐ฐ  **{ski_shekar}** ๐ฐ ๐ฅ ''' ,reply_markup=skii())
                    await asyncio.sleep(6)
                    await bot.send_message(chat_id1,text=f'''๐ฅโ๏ธุฑุง? ุดฺฉุงุฑฺ?


                    ๐ฐ  **{ski_shekar}** ๐ฐ ๐ฅ ''' ,reply_markup=skii())
                    await asyncio.sleep(6)
                    await bot.send_message(chat_id1,text=f'''๐ฅโ๏ธุฑุง? ุดฺฉุงุฑฺ?


                    ๐ฐ  **{ski_shekar}** ๐ฐ ๐ฅ ''' ,reply_markup=skii())
                    await asyncio.sleep(6)

                    spam[int(message.chat.id)]=False
            else:
                await message.reply_text('ูุชู ุฑุง? ุฑุง ุฌูู? /nray  ุจูู?ุณ?ุฏ๐ใ')
        else:
            await message.reply_text('ูุทุง ุตุจุฑ ฺฉู?ุฏ ุชุง ุฑุง? ูุนู? ุชููู ุดูุฏ !')
    if -1001217219311!=int(message.chat.id):
        if nazer[chat_id1]==message.from_user.id:
            if str(bot_username) in str(message.text):
                nazer_ski = str(message.text) [22:]
            else:
                nazer_ski = str(message.text) [6:]
            if spam[int(message.chat.id)]==False:
                if nazer_ski!='' and not message.from_user.is_bot :
                    if user_REs!=False and user_REs!='None':
                        spam[int(message.chat.id)]=True
                        ray=str(user_REs).replace('id',nazer_ski)
                        

                        await bot.send_message(chat_id1,text=ray ,reply_markup=nazeram())
                        await asyncio.sleep(6)

                        await bot.send_message(chat_id1,text=ray ,reply_markup=nazeram())
                        await asyncio.sleep(6)

                        await bot.send_message(chat_id1,text=ray ,reply_markup=nazeram())
                        await asyncio.sleep(6)

                        await bot.send_message(chat_id1,text=ray ,reply_markup=nazeram())
                        await asyncio.sleep(6)

                        await bot.send_message(chat_id1,text=ray ,reply_markup=nazeram())
                        await asyncio.sleep(6)

                        await bot.send_message(chat_id1,text=ray ,reply_markup=nazeram())
                        await asyncio.sleep(6)

                        await bot.send_message(chat_id1,text=ray ,reply_markup=nazeram())
                        await asyncio.sleep(6)
                        spam[int(message.chat.id)]=False

                    else:
                        spam[int(message.chat.id)]=True

                        await bot.send_message(chat_id1,text=f'''๐ฅโ๏ธุฑุง? ูุงุธุฑ โ๏ธ


                        ๐ฐ  **{nazer_ski}** ๐ฐ ๐ฅ  ''' ,reply_markup=nazeram())
                        await asyncio.sleep(6)
                        await bot.send_message(chat_id1,text=f'''๐ฅโ๏ธุฑุง? ูุงุธุฑ โ๏ธ


                        ๐ฐ  **{nazer_ski}** ๐ฐ ๐ฅ  ''' ,reply_markup=nazeram())
                        await asyncio.sleep(6)
                        await bot.send_message(chat_id1,text=f'''๐ฅโ๏ธุฑุง? ูุงุธุฑ โ๏ธ


                        ๐ฐ  **{nazer_ski}** ๐ฐ ๐ฅ  ''' ,reply_markup=nazeram())
                        await asyncio.sleep(6)
                        await bot.send_message(chat_id1,text=f'''๐ฅโ๏ธุฑุง? ูุงุธุฑ โ๏ธ


                        ๐ฐ  **{nazer_ski}** ๐ฐ ๐ฅ  ''' ,reply_markup=nazeram())
                        await asyncio.sleep(6)
                        await bot.send_message(chat_id1,text=f'''๐ฅโ๏ธุฑุง? ูุงุธุฑ โ๏ธ


                        ๐ฐ  **{nazer_ski}** ๐ฐ ๐ฅ  ''' ,reply_markup=nazeram())
                        await asyncio.sleep(6)
                        await bot.send_message(chat_id1,text=f'''๐ฅโ๏ธุฑุง? ูุงุธุฑ โ๏ธ


                        ๐ฐ  **{nazer_ski}** ๐ฐ ๐ฅ  ''' ,reply_markup=nazeram())
                        spam[int(message.chat.id)]=False
                else:
                    await message.reply_text('ูุชู ุฑุง? ุฑุง ุฌูู? /nray ุจูู?ุณ?ุฏ๐ใ')
            else:
                await message.reply_text('ูุทุง ุตุจุฑ ฺฉู?ุฏ ุชุง ุฑุง? ูุนู? ุชููู ุดูุฏ !')



# @bot.on_message(~filters.edited & filters.command(['nray', f'nray{bot_username}']) & filters.group & ~filters.me , group=0)
# @ban_from_bot
# async def ski_nazer_func(client, message):
#     global nazer
#     user_REs=database.usershekar(int(message.from_user.id))
#     chat_id1=message.chat.id
#     if int(message.chat.id) not in spam:
#         spam[int(message.chat.id)]=False
#     if nazer[chat_id1]==message.from_user.id:
#         if str(bot_username) in str(message.text):
#             nazer_ski = str(message.text) [22:]
#         else:
#             nazer_ski = str(message.text) [6:]
#         if spam[int(message.chat.id)]==False:
#             if nazer_ski!='' and not message.from_user.is_bot :
#                 if user_REs!=False and user_REs!='None':
#                     spam[int(message.chat.id)]=True
#                     ray=str(user_REs).replace('id',nazer_ski)
                    

#                     await bot.send_message(chat_id1,text=ray ,reply_markup=nazeram())
#                     await asyncio.sleep(6)

#                     await bot.send_message(chat_id1,text=ray ,reply_markup=nazeram())
#                     await asyncio.sleep(6)

#                     await bot.send_message(chat_id1,text=ray ,reply_markup=nazeram())
#                     await asyncio.sleep(6)

#                     await bot.send_message(chat_id1,text=ray ,reply_markup=nazeram())
#                     await asyncio.sleep(6)

#                     await bot.send_message(chat_id1,text=ray ,reply_markup=nazeram())
#                     await asyncio.sleep(6)

#                     await bot.send_message(chat_id1,text=ray ,reply_markup=nazeram())
#                     await asyncio.sleep(6)

#                     await bot.send_message(chat_id1,text=ray ,reply_markup=nazeram())
#                     await asyncio.sleep(6)
#                     spam[int(message.chat.id)]=False

#                 else:
#                     spam[int(message.chat.id)]=True

#                     await bot.send_message(chat_id1,text=f'''๐ฅโ๏ธุฑุง? ูุงุธุฑ โ๏ธ


#                     ๐ฐ  **{nazer_ski}** ๐ฐ ๐ฅ  ''' ,reply_markup=skii())
#                     await asyncio.sleep(6)
#                     await bot.send_message(chat_id1,text=f'''๐ฅโ๏ธุฑุง? ูุงุธุฑ โ๏ธ


#                     ๐ฐ  **{nazer_ski}** ๐ฐ ๐ฅ  ''' ,reply_markup=skii())
#                     await asyncio.sleep(6)
#                     await bot.send_message(chat_id1,text=f'''๐ฅโ๏ธุฑุง? ูุงุธุฑ โ๏ธ


#                     ๐ฐ  **{nazer_ski}** ๐ฐ ๐ฅ  ''' ,reply_markup=skii())
#                     await asyncio.sleep(6)
#                     await bot.send_message(chat_id1,text=f'''๐ฅโ๏ธุฑุง? ูุงุธุฑ โ๏ธ


#                     ๐ฐ  **{nazer_ski}** ๐ฐ ๐ฅ  ''' ,reply_markup=skii())
#                     await asyncio.sleep(6)
#                     await bot.send_message(chat_id1,text=f'''๐ฅโ๏ธุฑุง? ูุงุธุฑ โ๏ธ


#                     ๐ฐ  **{nazer_ski}** ๐ฐ ๐ฅ  ''' ,reply_markup=skii())
#                     await asyncio.sleep(6)
#                     await bot.send_message(chat_id1,text=f'''๐ฅโ๏ธุฑุง? ูุงุธุฑ โ๏ธ


#                     ๐ฐ  **{nazer_ski}** ๐ฐ ๐ฅ  ''' ,reply_markup=skii())
#                     spam[int(message.chat.id)]=False
#             else:
#                 await message.reply_text('ูุชู ุฑุง? ุฑุง ุฌูู? /nray ุจูู?ุณ?ุฏ๐ใ')
#         else:
#             await message.reply_text('ูุทุง ุตุจุฑ ฺฉู?ุฏ ุชุง ุฑุง? ูุนู? ุชููู ุดูุฏ !')
#     else:
#         await message.reply_text('ใุดูุง ูุงุธุฑ ุจุงุฒ? ู?ุณุช?ุฏ๐ใ')

#---------------------------------------------------------------------
@bot.on_message(~filters.edited &filters.group & (filters.command(['amar', f'amar{bot_username}']) | filters.regex('^ุงูุงุฑ$')),group=-100)
@Admin
async def miangin_amar_gaps(client, message):
    chat=message.chat.id
    await bot.send_message(chat,'ุงูุงุฑ 24 ุณุงุนุชู (ูุญุงุตุจู ุดุฏู ุงุฒ 07:00)ใฝ๏ธ  \n ุงูุชุฎุงุจ ฺฉู?ุฏ !' ,reply_markup=amar_all())

#------------------------------------------------------------------------
@bot.on_message(~filters.edited &filters.command(['addusers', f'addusers{bot_username}'])  ,group=-10)
@Admin
async def add_attack_user_name(c, m):
    a=0
    l=0
    if m.reply_to_message:
        usernames=str(m.reply_to_message.text).split('\n')
    else:
        usernames=str(m.text).split('\n')[1:]
    for i in usernames:
        try:
            database.add_usernames(i,int(m.from_user.id),int(database.show_main(int(m.chat.id))))
            l+=1
        except:
            a+=1
    await m.reply_text(f"#add_users \n ุชูุณุท {m.from_user.mention} ููุฏุงุฑ {l} ?ูุฒุฑู?ู ุจู ุฏ?ุชุงุจ?ุณ ุงุถุงูู ุดุฏ ู {a} ุงุฒ ุซุจู ุฏุฑ ุฏ?ุชุงุจ?ุณ ูุฌูุฏ ุฏุงุดุชูุฏ \n \n  ุฏุฑ ุตูุฑุช ุฌู?ู ุดุฏู ุง?ู ุงูุฑุงุฏ ุฏุฑ ฺฏุฑูู ุจู ุดูุง ุงุทูุงุน ุฎูุงูุฏ ุฏุงุฏู ุดุฏ !")


@bot.on_message(~filters.edited &filters.command(['delusers', f'delusers{bot_username}'])  ,group=-10)
@Admin
async def remove_attack_username(c, m):
    x=database.show_username(int(database.show_main(int(m.chat.id))))
    database.delete_user_all(int(database.show_main(int(m.chat.id))))
    await m.reply_text(f'ุชูุณุท ุงุฏู?ู {m.from_user.mention} ุชูุงู? ุง?ุฏ? ูุง , ุจู ููุฏุงุฑ {len(x)} ุงุฒ ู?ุณุช ?ูุฒุฑู?ู ูุง ูพุงฺฉ ุดุฏูุฏ \n ุฏ?ฺฏุฑ ุจุง ุฌู?ู ุดุฏู ุงููุง ุฏุฑฺฏูพ ุงุทูุงุน ุฑุณุงู? ูุฎูุงูุฏ ุดุฏ ')
#new-----------------------------------------------------------------
@bot.on_message(~filters.edited & ~filters.me & filters.command(['state', f'state{bot_username}'])& filters.group ,group=-100)
@ban_from_bot
async def state_Func(client, message):
    state_model=database.show_state_model(int(database.show_main(int(message.chat.id))))
    if message.reply_to_message:
        user = message.reply_to_message.from_user
        name=user.first_name
    else:
        user=message.from_user
        name=user.first_name
    try:
        if state_model==0:
            o= (await  post(
            url="http://api.wolfofpersia.ir:9999/api/GetState",
            data={
                "user_id": user.id,
                "token": token},timeout=2)).json()
            man=dict(o)
            totalgame=int(man['total_game'])
            fullname=(man['fullname'])
            mention1=mention(user.id,fullname)
            await message.reply_text(f'''
            **ใOnyx Account state ๐ ! ใ**
            
        **โ total games   ๐ฑ:ใ{totalgame}ใ**
        **โฃ Account Name ๐: {mention1}**
        **โฃ First Game : {man["TheFirstGame"]} **
        **โฃ Survived Games : {man['SurviveTheGame']}**
        **โฃ Most Kills : {man['YouKillName']} {man['killMeUserCount']} times**
        **โฃ most killed by : {man['killMeName']}
        **โฃ Status : {man["status"]}
        **โ {user.id}**''')
    except :
        await message.reply_text(f'''ุง?ู ูุฑุฏ ูุงูุฏ ุงุณุช?ุช ุงุณุช !''')

    try:
        if state_model==1:
            a=(await get(f"http://www.tgwerewolf.com/Stats/PlayerStats/?pid={user.id}&json=true")).json()
            try:
                a=dict(a)
            except:
                pass
            await message.reply_text(f'''state:
            name : {name}
            total games: {a['gamesPlayed']}
            lost : {a['lost']['total']} lost {a['lost']['percent']}%
            won : {a['won']['total']} wins {a['won']['percent']}%
            most killed : {a['mostKilled']['name']} | {a['mostKilled']['times']}  times
            most killed by : {a['mostKilledBy']['name']} | {a['mostKilledBy']['times']}  times
            ''')
    except:
        await message.reply_text(f'''ุง?ู ูุฑุฏ ูุงูุฏ ุงุณุช?ุช ุงุณุช !''')

    try:
        if state_model==2:
            a=(await get(f"http://blackwerewolf.com/Stats/PlayerStats/?pid={user.id}&json=true")).json()
            try:
                a=dict(a)
            except:
                pass
            totalgame=a['gamesPlayed']
            await message.reply_text(f'''black state:
    name : {user.mention}
    total games: {a['gamesPlayed']}
    lost : {a['lost']['total']} lost {a['lost']['percent']}%
    won : {a['won']['total']} wins {a['won']['percent']}%
    most killed : {a['mostKilled']['name']} | {a['mostKilled']['times']}  times
    most killed by : {a['mostKilledBy']['name']} | {a['mostKilledBy']['times']}  times
                ''')
    except:
        await message.reply_text(f'''ุง?ู ูุฑุฏ ูุงูุฏ ุงุณุช?ุช ุงุณุช !''')



@bot.on_message(~filters.edited & ~filters.me & filters.text & filters.reply ,group=-10)
@all_msg_decorator
async def set_winner(c, m):
    if 'ููุดุช ฺ?ู' in str(m.reply_to_message.text) and int(m.reply_to_message.from_user.id) == int(bot_id):
        for ent in m.reply_to_message.entities:
            if ent.type in ("mention", "text_mention"):
                if int(m.from_user.id)==int(ent.user.id):
                    if  int(m.from_user.id) not in roles[int(m.chat.id)] :
                        if  players_dict[int(m.chat.id)][int(m.from_user.id)]==True:
                            roles[int(m.chat.id)][int(m.from_user.id)]=str(m.text)
                            await m.reply_text('ููุด ุดูุง ุซุจุช ุดุฏ !')
                        else:
                            await m.reply_text('ุดูุง ูุฑุฏู ุง?ุฏ !')
                    else:
                        await m.reply_text('ุดูุง ููุดุงูู ุฑู ูุจูุง ุซุจุช ฺฉุฑุฏ?ุฏ !')

    global winner,winner2
    try:
        amir=0
        chat=int(m.chat.id)
        x=int(database.show_main(int(m.chat.id)))
        try:
            if omomi[x]==True:
                if  winner2[x]==None and m.reply_to_message.from_user.id == bot_id :
                    if str(javab) in m.text or  javab == m.text:
                        await m.reply_text('ุฏุฑุณุช ฺฏูุช???๐ฑ \n ุจูุช 300 ฺฉู?ู ๐ช ู 500 ุงูุช?ุงุฒ ุฏุงุฏู \n  ๐ฆ๐คฉ๐คฉ๐คฉ๐คฉ')
                        omomi[x]=False
                        winner2[x]= m.from_user.id
                        database.insert_point(int(winner2[x]),500,int(m.chat.id))
                        database.insert_coin(int(winner2[x]),300)
                        amir=1
        except Exception as e:
            error(e)

        try:
            if zarb[x] ==True:
                if  winner2[x]==None and m.reply_to_message.from_user.id == bot_id and 'ฺุงูุด ุฑ?ุงุถ?' in str(m.reply_to_message.text) :
                    Sequence=str(int(number[0])*int(number[1]))
                    if Sequence in m.text or  Sequence == m.text:
                        await m.reply_text('ุงูููููููู \n  ูุบุฒ ฺฏุฑููู  ๐ง  \n ุชู ุจุฑุฏ?ู 100 ุงูุช?ุงุฒ ู 100 ฺฉู?ู ๐ช ฺฏุฑูุช? ๐๐๐')
                        zarb[x]=False
                        winner2[x]= m.from_user.id
                        database.insert_point(int(winner2[x]),100,int(m.chat.id))
                        database.insert_coin(int(winner2[x]),100)
                        amir=1
        except Exception as e:
            error(e)

        try:
            if zarb_ALMASI[x] ==True:
                if  winner2[x]==None and m.reply_to_message.from_user.id == bot_id and 'ฺุงูุด ุงููุงุณ' in str(m.reply_to_message.text) :
                    Sequence=str(int(int(number[0])/int(number[1])))
                    if Sequence in m.text or  Sequence == m.text:
                        await m.reply_text('''ุงููููููููู๐ฆ๐ฆ๐ฆ๐ฆ๐ฆ

0.2 ุงููุงุณ ุจุฑุฏ????? ๐ฅ๐ฅ๐ฅ๐ฅ๐ฅ''')
                        zarb_ALMASI[x]=False
                        winner2[x]= m.from_user.id
                        database.insert_almas(winner2[x],0.1)
                        amir=1
        except :
            pass
        
        try:        
            if amir==0:
                if not winner2[x] and m.reply_to_message.from_user.id == bot_id and m.reply_to_message.text ==chl:
                    await m.reply("""ูุงุงุงุงู ุง?ูุฌุงุฑู๐๐
                ุชู ุจุฑุฏ? ุงูุช?ุงุฒ ุจุฑุง ุชู  """)
                    winner2[x]= m.from_user.id
                    database.addepoint(winner,chat)
                if not winner and m.reply_to_message.from_user.id == bot_id and m.reply_to_message.text ==chl:
                    await m.reply("""ูุงุงุงุงู ุง?ูุฌุงุฑู๐๐
                ุชู ุจุฑุฏ? ุงูุช?ุงุฒ ุจุฑุง ุชู  """)
                    winner = m.from_user.id
                    database.addepoint(winner,chat)
        except:
            pass
    except:
        pass
    
async def anti_bot(message,user,bot,admins_list):
    on = int(database.show_anti_bot(int(database.show_main(int(message.chat.id)))))
    if on == 1:
        try:
            if user.is_bot :
                if not int(message.from_user.id) in admins_list :
                    try:
                        await bot.kick_chat_member(int(message.chat.id),int(message.from_user.id))
                    except Exception as e:
                        print(e)
                    await bot.kick_chat_member(int(message.chat.id),int(user.id))
        except Exception as e:
            print(e)
                    

@bot.on_message(~filters.edited & ~filters.user(1698230457) & filters.new_chat_members ,group=-1)
@ban_from_bot
async def say_welcome(client, message):
    try:
        main=int(message.chat.id)
        admins_list = [int(i.user.id) async for i in bot.iter_chat_members(main,filter ='administrators')]
        que=0
        sup=database.show_sup(int(database.show_main(int(message.chat.id))))
        ban_state=int(database.show_state(main))
        for user in message.new_chat_members:
            await anti_bot(message , user , bot , admins_list)
        
            try:
                try:
                    cheaking=database.show_username_once(str(f'@{user.username}'),int(main))
                except :
                    pass
                    cheaking=database.show_username_once(str(user.id),int(main))
                if cheaking !=False:
                    try:
                        admin_name=(await bot.get_users(cheaking)).first_name
                    except :
                        pass
                        admin_name=cheaking
                    list_len=len(database.show_username(int(database.show_main(int(message.chat.id)))))
                    await bot.send_message(int(database.show_sup(database.show_main(int(message.chat.id)))),text=f' #new_user๐ \n ุฌุฐุจ ูููู?ุช ุงู?ุฒ ุจูุฏ ! ฺฉุงุฑุจุฑ {user.mention} ุฌู?ู ฺฏุฑูู ุดุฏู \n ุง?ู ฺฉุงุฑุจุฑ ุชูุณุท ุงุฏู?ู {admin_name} ุฐุฎ?ุฑู ุดุฏู ุจูุฏ !\n ุฏุฑ ูุฌููุน {list_len} ุง?ุฏ? ุชูุณุท ุงุฏู?ู ูุง ุฐุฎ?ุฑู ุดุฏู !  ',reply_markup=ply())
                    que=1
                    try:
                        database.delete_user(str(f'@{user.username}'))
                        database.delete_user(str(user.id))
                    except:
                        try:
                            database.delete_user(str(user.id))
                        except:
                            pass
                    
            except :

                pass
            try:
                user_name = user.first_name + (user.last_name if user.last_name else '')
                tabchi_list=database.show_tabchi()
                if 'ู?ูู' in str(user_name) or  'ุญุถูุฑ?' in str(user_name) or  'ุฎุงูู' in str(user_name)  or  'ุณููพุฑ' in str(user_name) or  'ฺฉุต' in str(user_name) or  '??ู' in str(user.last_name) or   'ุฒูุฑุง ูุต?ุฑ?' in str(user_name) or  'ุจุฎูู' in str(user_name) or( str(user_name) in tabchi_list):
                    await bot.kick_chat_member(message.chat.id,user.id)
                    await bot.send_message(message.chat.id,f'?ูุฒุฑ {user.mention} ุจู ุนููุงู ุชุจฺ? ุดูุงุฎุชู ุดุฏ ! ู ุจู ุดุฏ !')
                    que=1
            except :
                pass
            try:
                if int(database.show_sup(message.chat.id)) == int(message.chat.id) and que==0:
                    lock_sup=int(database.show_lock(int(database.show_main(int(message.chat.id)))))
                    if lock_sup==1:
                        admin_list_lock=[]
                        async for t in bot.iter_chat_members(int(database.show_main(int(message.chat.id))),filter='administrators'):
                            admin_list_lock.append(int(t.user.id))
                        if int(user.id) not in admin_list_lock:
                            await bot.kick_chat_member(int(message.chat.id),int(user.id))
                            chat_id_lock=int(message.chat.id)
                            await bot.send_message(chat_id_lock,f' ฺฉุงุฑุจุฑ {user.mention}  \n ุงุฏู?ู ฺฏูพ ูุจูุฏ ู ุชูุณุท ุจุงุช ?ฺฉ ุงุณูพูุฑ ุชุดุฎ?ุต ุฏุงุฏู ุดุฏ ! ',reply_markup=unban_user(f'|{user.id}|{chat_id_lock}'))
                            que=1
            except :
                pass
            try:
                user_Gp=int(database.show_user_GAP(int(user.id)))
                if user_Gp!=int(message.chat.id):
                    try:
                        title=message.chat.title
                    except:
                        pass
                    await bot.send_message(int(database.show_sup(int(user_Gp))),f'#attackโ ๏ธ \n  ูพู?ุฑ ฺฏุฑูู ุดูุง ุฏุฑ ฺฏุฑูู ุฏ?ฺฏุฑ? ุฌู?ู ุดุฏ \n ูุงู : {user.mention} \n  ฺฏุฑูู : {title}  \n \n ----------------------------------',reply_markup=ply())
            except :

                pass
            if user.id==bot_id:
                chat_id=message.chat.id
                if leave_auto==1:
                    #try:
                        #await message.reply_text('ูุทูุง ุจู ูพุดุช?ุจุงู? ูพ?ุงู ุฏู?ุฏ ',reply_markup=posht())
                    #finally:
                        #await bot.leave_chat(chat_id)
                    break
            try:
                lockido=0
                shabane=database.show_shab(int(database.show_main(int(main))))
                if shabane==1:
                    now=datetime.datetime.now()
                    if int(now.hour)<9:
                        lockido=0
                    else:
                        lockido=1

                if lockido==0 :
                    if que==0:
                        if ban_state>=1 or int(ban_state)==-850:
                            state_model=database.show_state_model(int(database.show_main(int(main))))
                            if state_model==0:
                                try:
                                    await asyncio.sleep(1)
                                    o= (await post(url="http://api.wolfofpersia.ir:9999/api/GetState",data={"user_id": user.id,"token": token} ,timeout=4).json())
                                    man=dict(o)
                                    totalgame=int(man['total_game'])
                                    if ban_state>=1:
                                        await message.reply_text(f'''ใOnyx Account state ๐ ! ใ

            โ total games ๐ฑ: ใ{totalgame}ใ
            โฃ Account Name ๐:{user.mention}
            โ {user.id}**''')
                                except :
                                    totalgame=0
                                    if int(ban_state)==-850 or ban_state>=1:
                                        await bot.send_message(sup,f'#ุงุฎุทุงุฑ \n  ฺฉุงุฑุจุฑ {user.mention} ุจุง ุงุณุช?ุช ุตูุฑ ูุงุฑุฏ ฺฏุฑูู ุดุฏู ุงุณุช ' ,reply_markup=ban_user(f'|{user.id}|{main}'))
                                    else:
                                        await message.reply_text(f'''ุง?ู ูุฑุฏ ูุงูุฏ ุงุณุช?ุช ู?ุจุงุดุฏ ! ''')
                            elif state_model==2:
                                # {"gamesPlayed":8,"won":{"total":2,"percent":25},"lost":{"total":6,"percent":75},"survived":{"total":2,"percent":25},"mostCommonRole":"Mason","mostKilled":{"name":"แฏโณแโ","id":1784441148
                                # ,"link":"\u003ca href=\u0027../Player/1784441148\u0027\u003eแฏโณแโ\u003c/a\u003e","times":2},
                                # "mostKilledBy":{"name":"แตแถฆแตแต แตแตแตแตแตแถฆ","id":958526870,"link":"\u003ca href=\u0027../Player/958526870\u0027\u003eแตแถฆแตแต แตแตแตแตแตแถฆ\u003c/a\u003e","times":2},"achievements":0}

                                try:
                                    a= (await get(f"http://blackwerewolf.com/Stats/PlayerStats/?pid={user.id}&json=true")).json()
                                    try:
                                        a=dict(a)
                                    except:
                                        pass
                                    totalgame=a['gamesPlayed']
                                    if ban_state>=1:
                                        await message.reply_text(f'''black state:
                    name : {user.mention}
                    total games: {a['gamesPlayed']}
                    lost : {a['lost']['total']} lost {a['lost']['percent']}%
                    won : {a['won']['total']} wins {a['won']['percent']}%
                    most killed : {a['mostKilled']['name']} | {a['mostKilled']['times']}  times
                    most killed by : {a['mostKilledBy']['name']} | {a['mostKilledBy']['times']}  times
                                        ''')
                                except:
                                    totalgame=0
                                    if que==0:
                                        if int(ban_state)==-850 or ban_state>=1:
                                            await bot.send_message(sup,f'#ุงุฎุทุงุฑ \n  ฺฉุงุฑุจุฑ {user.mention} ุจุง ุงุณุช?ุช ุตูุฑ ูุงุฑุฏ ฺฏุฑูู ุดุฏู ุงุณุช ' ,reply_markup=ban_user(f'|{user.id}|{main}'))
                                        else:
                                            await message.reply_text(f'''ุง?ู ูุฑุฏ ูุงูุฏ ุงุณุช?ุช ู?ุจุงุดุฏ ! ''')

                            else:
                                try:
                                    a=(await get(f"http://www.tgwerewolf.com/Stats/PlayerStats/?pid={user.id}&json=true")).json()
                                    try:
                                        a=dict(a)
                                    except:
                                        pass
                                    totalgame=a['gamesPlayed']
                                    if ban_state>=1:
                                        await message.reply_text(f'''state:
                    name : {user.mention}
                    total games: {a['gamesPlayed']}
                    lost : {a['lost']['total']} lost {a['lost']['percent']}%
                    won : {a['won']['total']} wins {a['won']['percent']}%
                    most killed : {a['mostKilled']['name']} | {a['mostKilled']['times']}  times
                    most killed by : {a['mostKilledBy']['name']} | {a['mostKilledBy']['times']}  times
                                        ''')
                                except:
                                    totalgame=0
                                    if que==0:
                                        if int(ban_state)==-850 or ban_state>=1:
                                            await bot.send_message(sup,f'#ุงุฎุทุงุฑ \n  ฺฉุงุฑุจุฑ {user.mention} ุจุง ุงุณุช?ุช ุตูุฑ ูุงุฑุฏ ฺฏุฑูู ุดุฏู ุงุณุช ' ,reply_markup=ban_user(f'|{user.id}|{main}'))
                                        else:
                                                await message.reply_text(f'''ุง?ู ูุฑุฏ ูุงูุฏ ุงุณุช?ุช ู?ุจุงุดุฏ ! ''')
                        try:    
                            if int(totalgame)<ban_state :
                                if que==0:
                                    await bot.kick_chat_member(int(main),int(user.id))
                                    await bot.send_message(main,f'voip! I banned {user.mention} โ ๏ธ',reply_markup=unban_user(f'|{user.id}|{main}'))
                        except Exception as e:
                            print(e)
            except:pass
    except:
        pass
#--------------------------------------------------------------------bet
                                                                            # 1   rosta
                                                                            # 2   gorg 
                                                                            # 3   ghatel
                                                                            # 4   ferghe 
                                                                            # 5   lover
                                                                            # 6   vamp 
                # roosta=amnt*0.55
                # ghatel=amnt*1.2
                # ferghe=amnt*0.7
                # lover=amnt*1
                # gg=amnt*0.85
                # if roosta<=1:
                #     roosta=1.05
                # if ferghe<=1:
                #     ferghe=1.10
                # if gg<=1:
                #     gg=1.15
@bot.on_callback_query(filters.regex(r"^kharid"))
@alaki_query
async def kharid_Callback(c,query):
    x=0
    user_almas=float(database.useralmas(int(query.from_user.id)))
    data=str(query.data).split(' ')[1]
    if data=='telesm':
        if user_almas>=0.10:
            user_id=int(query.from_user.id)
            database.reduce_almas(user_id,0.10)
            database.add_hip(user_id)
            await query.answer('?ฺฉ ุนุฏุฏ ุชูุณู ุณ?ุงู ุจู ููุฌูุฏ? ุดูุง ุงุถุงูู ุดุฏ !๐ฎ  ',show_alert=True)
        else:
            x=1
            await query.answer('ุงููุงุณ ูุง? ุดูุง ฺฉุงู? ู?ุณุช ! ๐ ',show_alert=True)

    elif data=='zereh':
        if user_almas>=0.050:
            user_id=int(query.from_user.id)
            database.reduce_almas(user_id,0.050)
            database.add_zereh(user_id)
            await query.answer('?ฺฉ ุนุฏุฏ ุฒุฏ ฺฏูููู  ๐ก  ุจู ููุฌูุฏ? ุดูุง ุงุถุงูู ุดุฏ !  ',show_alert=True)
        else:
            x=1
            await query.answer('ุงููุงุณ ูุง? ุดูุง ฺฉุงู? ู?ุณุช ! ๐ ',show_alert=True)
    
    elif data=='arvah':
        if user_almas>=0.075:
            user_id=int(query.from_user.id)
            database.reduce_almas(user_id,0.075)
            database.add_dozd(user_id)
            await query.answer('?ฺฉ ุนุฏุฏ ูุงุจู?ุช ุงุฑูุงุญ โ ๏ธ ุจู ููุฌูุฏ? ุดูุง ุงุถุงูู ุดุฏ !  ',show_alert=True)
        else:
            x=1
            await query.answer('ุงููุงุณ ูุง? ุดูุง ฺฉุงู? ู?ุณุช ! ๐ ',show_alert=True)
    if x==0:
        await query.edit_message_text('ุฎุฑ?ุฏ ุงูุฌุงู ุดุฏ !',reply_markup=kharid(int(query.from_user.id)))



@bot.on_callback_query(filters.regex(r"^tamdid") & filters.user(sup))
@alaki_query
async def tamdid_query(c,query):
    main_gap=str(query.data).split(' ')[1]
    database.tamdid_gap(int(main_gap))
    try:
        p=(await bot.get_chat(main_gap)).title
    except:
        p=main_gap
    await query.answer('ok')
    await query.edit_message_text(f' ุงุดุชุฑุงฺฉ ุจุฑุง? ฺฏูพ {p} 30 ุฑูุฒ ุชูุฏ?ุฏ ุดุฏ !')
#--------------------------------------------------------------------------------------
@bot.on_callback_query(filters.regex(r"^rosta"))
@bet_Query
@alaki_query
async def bet_rosta(c,query):
    if zarib[int(query.message.chat.id)]!=False:
        shrt='ุช?ู ุฑูุณุชุง'
        user_id=str(query.data).split(' ')[1]
        amount=str(query.data).split(' ')[-1]
        if int(query.from_user.id)==int(user_id):
            try:
                user_cn=int(database.usercoin(int(user_id)))
            except:
                user_cn=int(database.add_player_coin(int(user_id)))

                if user_cn<0:
                    user_cn=0
            if user_cn>=int(amount):
                database.reduce_coin(int(query.from_user.id),int(amount))
                zrb=float(zarib[int(query.message.chat.id)])
                zrb=zrb*0.75
                if zrb<=1:
                    zrb=1
                database.start_bet(int(user_id),int(amount),1,zrb,int(query.message.chat.id))
                try:
                    await bot.send_message(int(query.from_user.id),f'ุดุฑุท ุดูุง ุจุง ููุฏุงุฑ {amount} ุจุง ุถุฑ?ุจ {zrb:.2f} ุจุฑ ุฑู? {shrt} ุจุณุชู ุดุฏ ! \n ฺฏุฑูู {query.message.chat.title}')
                except:
                    pass
                await query.edit_message_text('ุจุณุชู ุดุฏ ! ุฏุฑ ูพ?ู? ุฑุจุงุช ุงุทูุงุนุงุช ุฑุง ู?ุชูู?ุฏ ูุดุงูุฏู ฺฉู?ุฏ ')

            else:
                await query.answer('ุณฺฉู ูุง ฺฉุงู? ูู?ุจุงุดุฏ!')
        else:
            await query.answer('ุง?ู ุดุฑุท ุจุฑุง? ุดูุง ู?ุณุช \n ุจุฑุง? ุดุฑุทุจูุฏ? ุงุฒ ุฏุณุชูุฑ /bet ุงุณุชูุงุฏู ฺฉู?ุฏ !')
    else:
        await query.answer('ุจุงุฒ? ุฏุฑ ุญุงู ุงุฌุฑุง ู?ุณุช !')

@bot.on_callback_query(filters.regex(r"^gorg"))
@bet_Query
@alaki_query
async def bet_gorg(c,query):
    if zarib[int(query.message.chat.id)]!=False:
        shrt='ุช?ู ฺฏุฑฺฏ'
        user_id=str(query.data).split(' ')[1]
        amount=str(query.data).split(' ')[-1]
        if int(query.from_user.id)==int(user_id):
            try:
                user_cn=int(database.usercoin(int(user_id)))
            except:
                user_cn=int(database.add_player_coin(int(user_id)))

                if user_cn<0:
                    user_cn=0
            if user_cn>=int(amount):
                database.reduce_coin(int(query.from_user.id),int(amount))
                zrb=float(zarib[int(query.message.chat.id)])
                zrb=zrb*0.9
                if zrb<=1:
                    zrb=1
                database.start_bet(int(user_id),int(amount),2,zrb,int(query.message.chat.id))
                try:
                    await bot.send_message(int(query.from_user.id),f'ุดุฑุท ุดูุง ุจุง ููุฏุงุฑ {amount} ุจุง ุถุฑ?ุจ {zrb:.2f} ุจุฑ ุฑู? {shrt} ุจุณุชู ุดุฏ ! \n ฺฏุฑูู {query.message.chat.title}')
                except:
                    pass
                await query.edit_message_text('ุจุณุชู ุดุฏ ! ุฏุฑ ูพ?ู? ุฑุจุงุช ุงุทูุงุนุงุช ุฑุง ู?ุชูู?ุฏ ูุดุงูุฏู ฺฉู?ุฏ ')

            else:
                await query.answer('ุณฺฉู ูุง ฺฉุงู? ูู?ุจุงุดุฏ!')
        else:
            await query.answer('ุง?ู ุดุฑุท ุจุฑุง? ุดูุง ู?ุณุช \n ุจุฑุง? ุดุฑุทุจูุฏ? ุงุฒ ุฏุณุชูุฑ /bet ุงุณุชูุงุฏู ฺฉู?ุฏ !')
    else:
        await query.answer('ุจุงุฒ? ุฏุฑ ุญุงู ุงุฌุฑุง ู?ุณุช !')

@bot.on_callback_query(filters.regex(r"^ghatel"))
@bet_Query
@alaki_query
async def bet_ghatel(c,query):
    if zarib[int(query.message.chat.id)]!=False:
        shrt='ุช?ู ูุงุชู '
        user_id=str(query.data).split(' ')[1]
        amount=str(query.data).split(' ')[-1]
        if int(query.from_user.id)==int(user_id):
            try:
                user_cn=int(database.usercoin(int(user_id)))
            except:
                user_cn=int(database.add_player_coin(int(user_id)))

                if user_cn<0:
                    user_cn=0
            if user_cn>=int(amount):
                database.reduce_coin(int(query.from_user.id),int(amount))
                zrb=float(zarib[int(query.message.chat.id)])
                zrb=zrb*1.25
                if zrb<=1:
                    zrb=1
                database.start_bet(int(user_id),int(amount),3,zrb,int(query.message.chat.id))
                try:
                    await bot.send_message(int(query.from_user.id),f'ุดุฑุท ุดูุง ุจุง ููุฏุงุฑ {amount} ุจุง ุถุฑ?ุจ {zrb:.2f} ุจุฑ ุฑู? {shrt} ุจุณุชู ุดุฏ ! \n ฺฏุฑูู {query.message.chat.title}')
                except:
                    pass
                await query.edit_message_text('ุจุณุชู ุดุฏ ! ุฏุฑ ูพ?ู? ุฑุจุงุช ุงุทูุงุนุงุช ุฑุง ู?ุชูู?ุฏ ูุดุงูุฏู ฺฉู?ุฏ ')

            else:
                await query.answer('ุณฺฉู ูุง ฺฉุงู? ูู?ุจุงุดุฏ!')
        else:
            await query.answer('ุง?ู ุดุฑุท ุจุฑุง? ุดูุง ู?ุณุช \n ุจุฑุง? ุดุฑุทุจูุฏ? ุงุฒ ุฏุณุชูุฑ /bet ุงุณุชูุงุฏู ฺฉู?ุฏ !')
    else:
        await query.answer('ุจุงุฒ? ุฏุฑ ุญุงู ุงุฌุฑุง ู?ุณุช !')

@bot.on_callback_query(filters.regex(r"^ferghe"))
@bet_Query
@alaki_query
async def bet_ferghe(c,query):
    if zarib[int(query.message.chat.id)]!=False:
        shrt='ุช?ู ูุฑูู '
        user_id=str(query.data).split(' ')[1]
        amount=str(query.data).split(' ')[-1]
        if int(query.from_user.id)==int(user_id):
            try:
                user_cn=int(database.usercoin(int(user_id)))
            except:
                user_cn=int(database.add_player_coin(int(user_id)))

                if user_cn<0:
                    user_cn=0
            if user_cn>=int(amount):
                database.reduce_coin(int(query.from_user.id),int(amount))
                zrb=float(zarib[int(query.message.chat.id)])
                zrb=zrb*0.75
                if zrb<=1:
                    zrb=1
                database.start_bet(int(user_id),int(amount),4,zrb,int(query.message.chat.id))
                try:
                    await bot.send_message(int(query.from_user.id),f'ุดุฑุท ุดูุง ุจุง ููุฏุงุฑ {amount} ุจุง ุถุฑ?ุจ {zrb:.2f} ุจุฑ ุฑู? {shrt} ุจุณุชู ุดุฏ ! \n ฺฏุฑูู {query.message.chat.title}')
                except:
                    pass
                await query.edit_message_text('ุจุณุชู ุดุฏ ! ุฏุฑ ูพ?ู? ุฑุจุงุช ุงุทูุงุนุงุช ุฑุง ู?ุชูู?ุฏ ูุดุงูุฏู ฺฉู?ุฏ ')

            else:
                await query.answer('ุณฺฉู ูุง ฺฉุงู? ูู?ุจุงุดุฏ!')
        else:
            await query.answer('ุง?ู ุดุฑุท ุจุฑุง? ุดูุง ู?ุณุช \n ุจุฑุง? ุดุฑุทุจูุฏ? ุงุฒ ุฏุณุชูุฑ /bet ุงุณุชูุงุฏู ฺฉู?ุฏ !')
    else:
        await query.answer('ุจุงุฒ? ุฏุฑ ุญุงู ุงุฌุฑุง ู?ุณุช !')

@bot.on_callback_query(filters.regex(r"^lover"))
@bet_Query
@alaki_query
async def bet_lover(c,query):
    if zarib[int(query.message.chat.id)]!=False:
        shrt='ุขุชุด๐ฅ  '
        user_id=str(query.data).split(' ')[1]
        amount=str(query.data).split(' ')[-1]
        if int(query.from_user.id)==int(user_id):
            try:
                user_cn=int(database.usercoin(int(user_id)))
            except:
                user_cn=int(database.add_player_coin(int(user_id)))

                if user_cn<0:
                    user_cn=0
            if user_cn>=int(amount):
                database.reduce_coin(int(query.from_user.id),int(amount))
                zrb=float(zarib[int(query.message.chat.id)])
                zrb=zrb*1
                if zrb<=1:
                    zrb=1
                database.start_bet(int(user_id),int(amount),5,zrb,int(query.message.chat.id))
                mod=int(database.show_state_model(int(query.message.chat.id)))
                if mod==2:
                    shrt='ุจูุจ ฺฏุฐุงุฑ'
                
                try:
                    await bot.send_message(int(query.from_user.id),f'ุดุฑุท ุดูุง ุจุง ููุฏุงุฑ {amount} ุจุง ุถุฑ?ุจ {zrb:.2f} ุจุฑ ุฑู? {shrt} ุจุณุชู ุดุฏ ! \n ฺฏุฑูู {query.message.chat.title}')
                except:
                    pass
                await query.edit_message_text('ุจุณุชู ุดุฏ ! ุฏุฑ ูพ?ู? ุฑุจุงุช ุงุทูุงุนุงุช ุฑุง ู?ุชูู?ุฏ ูุดุงูุฏู ฺฉู?ุฏ ')
            else:
                await query.answer('ุณฺฉู ูุง ฺฉุงู? ูู?ุจุงุดุฏ!')
        else:
            await query.answer('ุง?ู ุดุฑุท ุจุฑุง? ุดูุง ู?ุณุช \n ุจุฑุง? ุดุฑุทุจูุฏ? ุงุฒ ุฏุณุชูุฑ /bet ุงุณุชูุงุฏู ฺฉู?ุฏ !')
    else:
        await query.answer('ุจุงุฒ? ุฏุฑ ุญุงู ุงุฌุฑุง ู?ุณุช !')

@bot.on_callback_query(filters.regex(r"^vamp"))
@bet_Query
@alaki_query
async def bet_vamp(c,query):
    if zarib[int(query.message.chat.id)]!=False:
        shrt='ูููพ ูุง '
        user_id=str(query.data).split(' ')[1]
        amount=str(query.data).split(' ')[-1]
        if int(query.from_user.id)==int(user_id):
            try:
                user_cn=int(database.usercoin(int(user_id)))
            except:
                user_cn=int(database.add_player_coin(int(user_id)))

                if user_cn<0:
                    user_cn=0
            if user_cn>=int(amount):
                database.reduce_coin(int(query.from_user.id),int(amount))
                zrb=float(zarib[int(query.message.chat.id)])
                zrb=zrb*0.9
                if zrb<=1:
                    zrb=1
                database.start_bet(int(user_id),int(amount),6,zrb,int(query.message.chat.id))
                try:
                    await bot.send_message(int(query.from_user.id),f'ุดุฑุท ุดูุง ุจุง ููุฏุงุฑ {amount} ุจุง ุถุฑ?ุจ {zrb:.2f} ุจุฑ ุฑู? {shrt} ุจุณุชู ุดุฏ ! \n ฺฏุฑูู {query.message.chat.title}')
                except:
                    pass
                await query.edit_message_text('ุจุณุชู ุดุฏ ! ุฏุฑ ูพ?ู? ุฑุจุงุช ุงุทูุงุนุงุช ุฑุง ู?ุชูู?ุฏ ูุดุงูุฏู ฺฉู?ุฏ ')

            else:
                await query.answer('ุณฺฉู ูุง ฺฉุงู? ูู?ุจุงุดุฏ!')
        else:
            await query.answer('ุง?ู ุดุฑุท ุจุฑุง? ุดูุง ู?ุณุช \n ุจุฑุง? ุดุฑุทุจูุฏ? ุงุฒ ุฏุณุชูุฑ /bet ุงุณุชูุงุฏู ฺฉู?ุฏ !')
    else:
        await query.answer('ุจุงุฒ? ุฏุฑ ุญุงู ุงุฌุฑุง ู?ุณุช !')

@bot.on_callback_query(filters.regex(r"^monaf"))
@bet_Query
@alaki_query
async def bet_monaf(c,query):
    if zarib[int(query.message.chat.id)]!=False:
        shrt='ููุงูู ๐บ'
        user_id=str(query.data).split(' ')[1]
        amount=str(query.data).split(' ')[-1]
        if int(query.from_user.id)==int(user_id):
            try:
                user_cn=int(database.usercoin(int(user_id)))
            except:
                user_cn=int(database.add_player_coin(int(user_id)))

                if user_cn<0:
                    user_cn=0
            if user_cn>=int(amount):
                database.reduce_coin(int(query.from_user.id),int(amount))
                zrb=float(zarib[int(query.message.chat.id)])
                zrb=zrb*1.25
                if zrb<=1:
                    zrb=1
                database.start_bet(int(user_id),int(amount),7,zrb,int(query.message.chat.id))
                try:
                    await bot.send_message(int(query.from_user.id),f'ุดุฑุท ุดูุง ุจุง ููุฏุงุฑ {amount} ุจุง ุถุฑ?ุจ {zrb:.2f} ุจุฑ ุฑู? {shrt} ุจุณุชู ุดุฏ ! \n ฺฏุฑูู {query.message.chat.title}')
                except:
                    pass
                await query.edit_message_text('ุจุณุชู ุดุฏ ! ุฏุฑ ูพ?ู? ุฑุจุงุช ุงุทูุงุนุงุช ุฑุง ู?ุชูู?ุฏ ูุดุงูุฏู ฺฉู?ุฏ ')

            else:
                await query.answer('ุณฺฉู ูุง ฺฉุงู? ูู?ุจุงุดุฏ!')
        else:
            await query.answer('ุง?ู ุดุฑุท ุจุฑุง? ุดูุง ู?ุณุช \n ุจุฑุง? ุดุฑุทุจูุฏ? ุงุฒ ุฏุณุชูุฑ /bet ุงุณุชูุงุฏู ฺฉู?ุฏ !')
    else:
        await query.answer('ุจุงุฒ? ุฏุฑ ุญุงู ุงุฌุฑุง ู?ุณุช !')
#----------------------------------------------------------------------ray
@bot.on_callback_query(filters.regex(r"^bastan"))
@alaki_query
async def bastan_ray(c,query):
    chat=int(query.message.chat.id)
    if shekar[chat]==int(query.from_user.id):
        await query.edit_message_text('ุจุณุชู ุดุฏ !')
    else:
        pass

@bot.on_callback_query(filters.regex(r"^ray"))
@alaki_query
async def ray_query(c,query):
    user_name=str(query.data).split(' ')[1]
    chat=int(query.message.chat.id)

    user_REs=database.usershekar(int(query.from_user.id))
    if shekar[chat]==int(query.from_user.id) :
        if int(chat) not in spam:
            spam[int(chat)]=False
        if spam[int(chat)]==False:
            await query.edit_message_text(f' ุฑุง? ุจุฑ ุฑู? {user_name} ูุฑุงุฑ ฺฏุฑูุช ')
            if user_REs!=False and user_REs!='None':
                spam[int(chat)]=True
                ray=str(user_REs).replace('id',user_name)
                await bot.send_message(chat,text=f'{ray}' ,reply_markup=shekarchi())
                await asyncio.sleep(6)

                await bot.send_message(chat,text=f'{ray}' ,reply_markup=shekarchi())
                await asyncio.sleep(6)
                await bot.send_message(chat,text=f'{ray}' ,reply_markup=shekarchi())
                await asyncio.sleep(6)
                await bot.send_message(chat,text=f'{ray}' ,reply_markup=shekarchi())
                await asyncio.sleep(6)
                await bot.send_message(chat,text=f'{ray}' ,reply_markup=shekarchi())
                spam[int(chat)]=False

            else:
                await bot.send_message(chat,text=f'''๐ฅโ๏ธุฑุง? 


            ๐ฐ  **{user_name}** ๐ฐ ๐ฅ ''' ,reply_markup=skii())
                await asyncio.sleep(6)

                await bot.send_message(chat,text=f'''๐ฅโ๏ธุฑุง? 


            ๐ฐ  **{user_name}** ๐ฐ ๐ฅ ''' ,reply_markup=skii())
                await asyncio.sleep(6)
                await bot.send_message(chat,text=f'''๐ฅโ๏ธุฑุง? 


            ๐ฐ  **{user_name}** ๐ฐ ๐ฅ ''' ,reply_markup=skii())
                await asyncio.sleep(6)
                await bot.send_message(chat,text=f'''๐ฅโ๏ธุฑุง? 


            ๐ฐ  **{user_name}** ๐ฐ ๐ฅ ''' ,reply_markup=skii())
                await asyncio.sleep(6)
                await bot.send_message(chat,text=f'''๐ฅโ๏ธุฑุง? 


            ๐ฐ  **{user_name}** ๐ฐ ๐ฅ ''' ,reply_markup=skii())
            spam[int(chat)]=False

        else:
            await query.answer('ูุทุง ุตุจุฑ ฺฉู?ุฏ ุชุง ุฑุง? ูุนู? ุชููู ุดูุฏ !', show_alert=True)
    elif nazer[chat]==int(query.from_user.id):
        if int(chat) not in spam:
            spam[int(chat)]=False
        if spam[int(chat)]==False:
            await query.edit_message_text(f' ุฑุง? ุจุฑ ุฑู? {user_name} ูุฑุงุฑ ฺฏุฑูุช ')
            if user_REs!=False and user_REs!='None':
                spam[int(chat)]=True
                ray=str(user_REs).replace('id',user_name)
                await bot.send_message(chat,text=f'{ray}' ,reply_markup=shekarchi())
                await asyncio.sleep(6)

                await bot.send_message(chat,text=f'{ray}' ,reply_markup=nazeram())
                await asyncio.sleep(6)
                await bot.send_message(chat,text=f'{ray}' ,reply_markup=nazeram())
                await asyncio.sleep(6)
                await bot.send_message(chat,text=f'{ray}' ,reply_markup=nazeram())
                await asyncio.sleep(6)
                await bot.send_message(chat,text=f'{ray}' ,reply_markup=nazeram())
                spam[int(chat)]=False

            else:
                await bot.send_message(chat,text=f'''๐ฅโ๏ธุฑุง? 


            ๐ฐ  **{user_name}** ๐ฐ ๐ฅ ''' ,reply_markup=nazeram())
                await asyncio.sleep(6)

                await bot.send_message(chat,text=f'''๐ฅโ๏ธุฑุง? 


            ๐ฐ  **{user_name}** ๐ฐ ๐ฅ ''' ,reply_markup=nazeram())
                await asyncio.sleep(6)
                await bot.send_message(chat,text=f'''๐ฅโ๏ธุฑุง? 


            ๐ฐ  **{user_name}** ๐ฐ ๐ฅ ''' ,reply_markup=nazeram())
                await asyncio.sleep(6)
                await bot.send_message(chat,text=f'''๐ฅโ๏ธุฑุง? 


            ๐ฐ  **{user_name}** ๐ฐ ๐ฅ ''' ,reply_markup=nazeram())
                await asyncio.sleep(6)
                await bot.send_message(chat,text=f'''๐ฅโ๏ธุฑุง? 


            ๐ฐ  **{user_name}** ๐ฐ ๐ฅ ''' ,reply_markup=nazeram())
            spam[int(chat)]=False
               
        else:
            await query.answer('ูุทุง ุตุจุฑ ฺฉู?ุฏ ุชุง ุฑุง? ูุนู? ุชููู ุดูุฏ !', show_alert=True)

    else:
        await query.answer('ใุดูุง  ุดฺฉุงุฑฺ? ?ุง ูุงุธุฑ  ุจุงุฒ? ู?ุณุช?ุฏ๐ใ', show_alert=True)







                        

#-------------------------------------------------------------------ghaleb 
@bot.on_callback_query(filters.regex(r"^ghaleb"))
@alaki_query
async def ghaleb_Query_Choose(c,query):
    ghaleb_hash=str(query.data).split(' ')[-1]
    ghaleb=str(database.show_ghalebs(ghaleb_hash))
    await query.edit_message_text(f'ูุงูุจ ุงูุชุฎุงุจ ุดุฏู  \n -----------------------------------------\n \n\n{ghaleb}', reply_markup=taeed_ghaleb(ghaleb_hash))

@bot.on_callback_query(filters.regex(r"^taeed"))
@alaki_query
async def ghaleb_taeed_Query_Choose(c,query):
    user_almas=float(database.useralmas(int(query.from_user.id)))
    ghaleb_hash=str(query.data).split(' ')[-1]
    ghaleb_price=float(database.show_price(ghaleb_hash))
    if user_almas>=ghaleb_price:
        database.reduce_almas(int(query.from_user.id),ghaleb_price)
        database.insert_user_ghaleb(int(query.from_user.id),hashs=ghaleb_hash)
        await query.edit_message_text('ูุงูุจ ุฎุฑ?ุฏุงุฑ? ุดุฏ !')
    else:
        await query.answer(f'ุงููุงุณ ุดูุง ฺฉุงู? ู?ุณุช \n ุงููุงุณ ุดูุง : {user_almas} ')


@bot.on_callback_query(filters.regex(r"^camcel"))
@alaki_query
async def undo_bying_ghaleb(c,query):
    await query.edit_message_text('ฺฉุฏุงู ูุงูุจ ุฑู ู?ุฎูุงู?ุฏ ุจุจ?ู?ุฏ ุ' , reply_markup=ghaleb_inline())
#----------------------------------------------------------------------
@bot.on_callback_query(filters.regex(r"^warn"))
@Admin_Query
async def warn_Query_Choose(c,query):
    warn=str(query.data).split(' ')[-1]
    database.set_warn(int(database.show_main(int(query.message.chat.id))),int(warn))
    await query.answer(f' ููู ูุงุฑู  ุจุฑ ุฑู? {warn} ุชูุธ?ู ุดุฏ!', show_alert=True)

@bot.on_callback_query(filters.regex(r"^taskhir"))
@alaki_query
async def taskhir(c,query):
    x=database.show_sargarmi(int(database.show_main(int(query.message.chat.id))))
    if x==1:
        d=query.data
        mute_p=str(d).split('|')[2]
        unmute_p=str(d).split('|')[1]
        try:
            user_cn=int(database.usercoin(int(query.from_user.id)))
        except:
            user_cn=int(database.add_player_coin(int(query.from_user.id)))
        if user_cn>=60:
            try:
                if int(unmute_p)==int(query.from_user.id):
                    try:
                        await bot.restrict_chat_member(int(query.message.chat.id),int(unmute_p),unmute_group)
                    except:
                        muted_admins[int(query.message.chat.id)].pop(int(unmute_p))
                        muted_hour[int(query.message.chat.id)].pop(int(unmute_p))
                        muted[int(query.message.chat.id)].pop(int(unmute_p))
                    try:
                        await bot.restrict_chat_member(int(query.message.chat.id),int(mute_p), ChatPermissions(), int(time.time() + 300))
                    except:
                        now=datetime.datetime.now()
                        muted_time=int(now.minute+7)
                        hr=int(now.hour)
                        if muted_time>=60:
                            muted_time=int(muted_time-60)
                            hr=int(hr+1)
                        muted[int(query.message.chat.id)][int(query.message.reply_to_message.from_user.id)]=True
                        muted_admins[int(query.message.chat.id)][int(query.message.reply_to_message.from_user.id)]=int(muted_time)
                        muted_hour[int(query.message.chat.id)][int(query.message.reply_to_message.from_user.id)]=int(hr)
                        database.reduce_coin(int(query.from_user.id),60)
                    user1=(await bot.get_users(mute_p)).first_name
                    user2=(await bot.get_users(unmute_p)).first_name
                    await query.answer(f'ุฎูุฏุช ุฑู ูุฌุงุช ุฏุงุฏ?  \n 60 ฺฉู?ู ๐ช ุงุฒุช ฺฉู ุดุฏ!', show_alert=True)
                    await query.edit_message_text('ููู ูุฏุฑุชุงูู ุงุฒ ุฏุณุช ุฏุงุฏู :) ',reply_markup=rj())
                    try:
                        muted_admins[int(query.message.chat.id)].pop(int(unmute_p))
                        muted_hour[int(query.message.chat.id)].pop(int(unmute_p))
                        muted[int(query.message.chat.id)].pop(int(unmute_p))
                    except :
                        pass
                    await query.message.reply_text(f'ฺู ุงุชูุงู? ุงูุชุงุฏู ๐ฎ๐ฎ๐ฎ \n ุฏ?ฺฏู ุฏุณุชุฑุณ? ุจู ู?ฺ? ูุฏุงุฑูู๐งฟ\n \n ุง?ู ุฌุงุฏูฺฏุฑ {user2} ููู ุชุณุฎ?ุฑ ฺฉุฑุฏู ู ุฎูุฏุดู ุงุฒ ุณฺฉูุช ุงุฒุงุฏ ฺฉุฑุฏู \n ู {user1} ุณฺฉูุช ฺฉุฑุฏู ๐ฑ๐ฑ๐ฑ')
                else:
                    try:
                        await bot.restrict_chat_member(int(query.message.chat.id),int(unmute_p),unmute_group)
                    except:
                        muted_admins[int(query.message.chat.id)].pop(int(unmute_p))
                        muted_hour[int(query.message.chat.id)].pop(int(unmute_p))
                        muted[int(query.message.chat.id)].pop(int(unmute_p))
                    try:
                        await bot.restrict_chat_member(int(query.message.chat.id),int(mute_p), ChatPermissions(), int(time.time() + 300))
                    except:
                        now=datetime.datetime.now()
                        muted_time=int(now.minute+7)
                        hr=int(now.hour)
                        if muted_time>=60:
                            muted_time=int(muted_time-60)
                            hr=int(hr+1)
                        muted[int(query.message.chat.id)][int(mute_p)]=True
                        muted_admins[int(query.message.chat.id)][int(query.message.reply_to_message.from_user.id)]=int(muted_time)
                        muted_hour[int(query.message.chat.id)][int(query.message.reply_to_message.from_user.id)]=int(hr)
                        database.reduce_coin(int(query.from_user.id),60)
                    
                    
                    user1=(await bot.get_users(mute_p)).first_name
                    user2=(await bot.get_users(unmute_p)).first_name
                    await query.answer(f'ฺู ุฏูุณุช ุฎูุจ? ! ุฏูุณุชุชู ูุฌุงุช ุฏุงุฏ? \n 60 ฺฉู?ู ๐ช ุงุฒุช ฺฉู ุดุฏ!', show_alert=True)
                    await query.edit_message_text('ููู ูุฏุฑุชุงูู ุงุฒ ุฏุณุช ุฏุงุฏู :) ',reply_markup=rj())
                    try:
                        muted_admins[int(query.message.chat.id)].pop(int(unmute_p))
                        muted_hour[int(query.message.chat.id)].pop(int(unmute_p))
                        muted[int(query.message.chat.id)].pop(int(unmute_p))
                    except :
                        pass
                    await query.message.reply_text(f'ฺู ุงุชูุงู? ุฏุงุฑู ู?ููุชู  ๐คจ๐คจ \n ูุฏุฑุชุงู ฺฉููู๐ฑ๐ฑ \n \n ุฏุงุฑู ุฌู ุงุชูุงู? ู?ููุชููููู๐ต๐ต๐ต \n ุง?ู ุฌุงุฏูฺฏุฑ {query.from_user.mention} ููู ุชุณุฎ?ุฑ ฺฉุฑุฏ ู ูุฌุจูุฑู ฺฉุฑุฏ \n {user1} ฺฉู ุฏูุณุชุดู ุณฺฉูุช ฺฉุฑุฏู ุจูุฏ ุณฺฉูุช ฺฉูู \n ู {user2} ุฑู ุงุฒุงุฏ ฺฉูู ')
                    database.reduce_coin(int(query.from_user.id),60)
            except :
                await query.answer(f'ุงูู ุงุฒ ุฏุณุชูุฑ /regester ุงุณุชูุงุฏู ฺฉู ุชุง ุซุจุช ุจุด? !', show_alert=True)


@bot.on_callback_query(filters.regex(r"^state"))
@Admin_Query
async def state_Query_Choose(c,query):
    State_M=str(query.data).split(' ')[-1]
    database.set_state(int(database.show_main(int(query.message.chat.id))),int(State_M))
    try:
        if int(State_M)==-850:
            stt='ุญุงูุช ูุดุฏุงุฑ ุฏู? ฺฉุงุฑุจุฑุงู ุจุฏูู ุงุณุช?ุช ูุนุงู ุดุฏ !'
            await query.answer(f' ููู ุงุณุช?ุช  ุจุฑ ุฑู? {stt} ุชูุธ?ู ุดุฏ!', show_alert=True)
            t='ุญุงูุช ูุดุฏุงุฑ โ ๏ธ'
        else:
            await query.answer(f' ููู ุงุณุช?ุช  ุจุฑ ุฑู? {State_M} ุชูุธ?ู ุดุฏ!', show_alert=True)
            t=State_M
    except :
        await query.answer(f' ููู ุงุณุช?ุช  ุจุฑ ุฑู? {State_M} ุชูุธ?ู ุดุฏ!', show_alert=True)
        t=State_M

    await query.edit_message_text(f'ููู ุงุณุช?ุช ุจุฑ ุฑู? {t} ูุฑุงุฑ ฺฏุฑูุช !',reply_markup=state_Coutn(t,int(database.show_main(int(query.message.chat.id)))))
@bot.on_callback_query(filters.regex(r"^warpnp$"))
@Admin_Query
async def Warn_Callback(c,query):
    a=int(database.show_warn(int(database.show_main(int(query.message.chat.id)))))
    if a==0:
        text="ุบ?ุฑูุนุงู๐"
    else:
        text=a
    await query.edit_message_text('ูุทูุง ุชุนุฏุงุฏ ุฏูุนุงุช AFK ุดุฏู , ุจุฑุง? ูุงุฑู ฺฏุฑูุชู ุฑุง ุงูุชุฎุงุจ ฺฉู?ุฏ !',reply_markup=warn_Count(text))

@bot.on_callback_query(filters.regex(r"^statpelock$"))
@Admin_Query
async def State_Callback(c,query):
    a=int(database.show_state(int(database.show_main(int(query.message.chat.id)))))
    if a==0:
        text="ุบ?ุฑูุนุงู๐"
    else:
        text=a
    if a==-850:
        text='ุญุงูุช ูุดุฏุงุฑ โ ๏ธ'
    else:
        text=a
    await query.edit_message_text('ูุทูุง ุญุฏ ูุฌุงุฒ ุงุณุช?ุช ูุงุฑุฏ ุดุฏู ุจู ฺฏุฑูู ุฑุง ุชุน??ู ฺฉู?ุฏ !',reply_markup=state_Coutn(text,int(database.show_main(int(query.message.chat.id)))))
    await query.answer('@DarkHelperChannel !')

@bot.on_callback_query(filters.regex(r"^point"))
async def point_callback(c,query):
    await query.answer('ุจุฑุง? ูฺฉุณุช ุงุฎุชุตุงุต? ุฌูู? ุฏุณุชูุฑ /mynext ูุชู ููุฑุฏ ูุธุฑุชู ุจูู?ุณ ๐งธ', show_alert=True)


@bot.on_callback_query(filters.regex(r"^undo"))
@Admin_Query
async def undo_pannel(c,query):
    gp=int(database.show_main(int(query.message.chat.id)))
    await query.edit_message_text('ุจู ูพูู ุจุงุฒฺฏุดุช?ุฏ !',reply_markup=(await pannel(gp)))
    await query.answer('@DarkHelperChannel !')

@bot.on_callback_query(filters.regex(r"^close"))
@Admin_Query
async def close_pannel(c,query):
    await query.edit_message_text(' ุจุณุชู ุดุฏ !',reply_markup=rj())
    
#------------------------BOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOM
@bot.on_callback_query(filters.regex(r"^boom"))
async def bOOm(c,query):
    await query.answer('ุง?ู ุดุฑุท ุจุณุชู ุดุฏู ุงุณุช !')

@bot.on_callback_query(filters.regex(r"^bardasht"))
async def bardasht_En(c,query):
    zarib_en=float(str(query.data).split(' ')[1])
    hash=int(str(query.data).split(' ')[2])
    if int(query.from_user.id) in enfejar[int(query.message.chat.id)] and int(hash)==int(enfejar_hash[int(query.message.chat.id)]):
        amount=int(enfejar[int(query.message.chat.id)][int(query.from_user.id)])
        kol=int((amount*zarib_en)-amount)
        database.insert_coin(int(query.from_user.id),kol)
        enfejar[int(query.message.chat.id)].pop(int(query.from_user.id))
        await query.answer('ุจุฑุฏุงุดุชู ุดุฏ !',show_alert=True)
        await query.message.reply_text(f'ฺฉุงุฑุจุฑ {query.from_user.mention} ฺฉู?ู ุฎูุฏ ุฑุง ุจุง ุถุฑ?ุจ {zarib_en} ุจุฑุฏุงุดุช ฺฉุฑุฏ ๐ข! \n ุณูุฏ ๐ฐ : {kol}')
    else:
        await query.answer('  ุดูุง ุฏุฑ ุดุฑุทุจูุฏ? ู?ุณุช?ุฏ  !',show_alert=True)
#-------------------------------------state            
# [InlineKeyboardButton(f'24 ุณุงุนุช  {rooz}', callback_data='kamel'),InlineKeyboardButton(f'ุดุจุงูู  {shaab}', callback_data='shab')],

@bot.on_callback_query(filters.regex(r"^kamel"))
@Admin_Query
async def kamel_lock(c,query):
    a=int(database.show_state(int(database.show_main(int(query.message.chat.id)))))
    if a==0:
        text="ุบ?ุฑูุนุงู๐"
    else:
        text=a
    if a==-850:
        text='ุญุงูุช ูุดุฏุงุฑ โ ๏ธ'
    else:
        text=a
    database.set_shab_off(int(database.show_main(int(query.message.chat.id))))
    await query.answer('ููู ุงุณุช?ุช ุจุฑ ุฑู? ุฑูุฒุงูู ูุฑุงุฑ ฺฏุฑูุช !')
    await query.edit_message_text('ุชุบ??ุฑุงุช ุงุนูุงู ุดุฏ !',reply_markup=state_Coutn(text,int(database.show_main(int(query.message.chat.id)))))
    



@bot.on_callback_query(filters.regex(r"^shab"))
@Admin_Query
async def rooz_lock(c,query):
    a=int(database.show_state(int(database.show_main(int(query.message.chat.id)))))
    if a==0:
        text="ุบ?ุฑูุนุงู๐"
    else:
        text=a
    if a==-850:
        text='ุญุงูุช ูุดุฏุงุฑ โ ๏ธ'
    else:
        text=a
    database.set_shab_on(int(database.show_main(int(query.message.chat.id))))
    await query.answer('ููู ุงุณุช?ุช ุจุฑ ุฑู? ุดุจุงูู ูุฑุงุฑ ฺฏุฑูุช !')
    await query.edit_message_text('ุชุบ??ุฑุงุช ุงุนูุงู ุดุฏ !',reply_markup=state_Coutn(text,int(database.show_main(int(query.message.chat.id)))))
    

@bot.on_callback_query(filters.regex(r"^onyx"))
@Admin_Query
async def set_onyx_lock(c,query):
    a=int(database.show_state(int(database.show_main(int(query.message.chat.id)))))
    if a==0:
        text="ุบ?ุฑูุนุงู๐"

    else:
        text=a

    if a==-850:
        text='ุญุงูุช ูุดุฏุงุฑ โ ๏ธ'
    else:
        text=a
    database.set_state_model_onyx(int(database.show_main(int(query.message.chat.id))))
    await query.answer('ููุน  ููู ุงุณุช?ุช ุจุฑ ุฑู? ุงูู?ฺฉุณ ูุฑุงุฑ ฺฏุฑูุช !', show_alert=True)
    await query.edit_message_text('ุชุบ??ุฑุงุช ุงุนูุงู ุดุฏ !',reply_markup=state_Coutn(text,int(database.show_main(int(query.message.chat.id)))))
    

@bot.on_callback_query(filters.regex(r"^black"))
@Admin_Query
async def set_black_lock(c,query):
    a=int(database.show_state(int(database.show_main(int(query.message.chat.id)))))
    if a==0:
        text="ุบ?ุฑูุนุงู๐"
    else:
        text=a
    if a==-850:
        text='ุญุงูุช ูุดุฏุงุฑ โ ๏ธ'
    else:
        text=a
    database.set_state_model_black(int(database.show_main(int(query.message.chat.id))))
    await query.answer('ููุน  ููู ุงุณุช?ุช ุจุฑ ุฑู? ุจูฺฉ ูุฑุงุฑ ฺฏุฑูุช !', show_alert=True)
    await query.edit_message_text('ุชุบ??ุฑุงุช ุงุนูุงู ุดุฏ !',reply_markup=state_Coutn(text,int(database.show_main(int(query.message.chat.id)))))
    

@bot.on_callback_query(filters.regex(r"^werewolf"))
@Admin_Query
async def set_werewolf_lock(c,query):
    a=int(database.show_state(int(database.show_main(int(query.message.chat.id)))))
    if a==0:
        text="ุบ?ุฑูุนุงู๐"
    else:
        text=a
    if a==-850:
        text='ุญุงูุช ูุดุฏุงุฑ โ ๏ธ'
    else:
        text=a
    database.set_state_model_werewolf(int(database.show_main(int(query.message.chat.id))))
    await query.answer('ููุน  ููู ุงุณุช?ุช ุจุฑ ุฑู? ูุฑููู ูุฑุงุฑ ฺฏุฑูุช !', show_alert=True)
    await query.edit_message_text('ุชุบ??ุฑุงุช ุงุนูุงู ุดุฏ !',reply_markup=state_Coutn(text,int(database.show_main(int(query.message.chat.id)))))
    
#-----------------------------------------
@bot.on_callback_query(filters.regex(r"^autotag"))
@Admin_Query
async def auto_tag_Func(c,query):
    gp=query.message.chat.id
    a=database.show_tag(int(database.show_main(int(gp))))
    if a==1:
        roshan='ุฎุงููุด '
        database.set_tag_off(int(database.show_main(int(gp))))
    else:
        roshan='ุฑูุดู'
        database.set_tag_on(int(database.show_main(int(gp))))
    gp=int(database.show_main(int(query.message.chat.id)))
    await query.edit_message_text(f'ูพูู ุจุฑุง? ุดูุง ุจุงุฒ ุดุฏ ,ู?ุชูุงู?ุฏ ุงุฒ ูพูู ุชูุธ?ูุงุช ุฌุฏ?ุฏ ุฑุง ุงุนูุงู ฺฉู?ุฏ \n ุชฺฏ ุฎูุฏฺฉุงุฑ {roshan} ุดุฏ  !',reply_markup=(await pannel(gp)))
    await query.answer('@DarkHelperChannel !')


@bot.on_callback_query(filters.regex(r"^mokamel"))
@Admin_Query
async def mokamel_warn_fank(c,query):
    gp=query.message.chat.id
    a=database.show_mokamel(int(database.show_main(int(gp))))
    if a==1:
        roshan='ุฎุงููุด '
        database.set_mokamel_off(int(database.show_main(int(gp))))
    else:
        roshan='ุฑูุดู'
        database.set_mokamel_on(int(database.show_main(int(gp))))
    gp=int(database.show_main(int(query.message.chat.id)))
    await query.edit_message_text(f'ูพูู ุจุฑุง? ุดูุง ุจุงุฒ ุดุฏ ,ู?ุชูุงู?ุฏ ุงุฒ ูพูู ุชูุธ?ูุงุช ุฌุฏ?ุฏ ุฑุง ุงุนูุงู ฺฉู?ุฏ \n  ูุงุฑู ุฎูุฏฺฉุงุฑ ุจู ุงูฺฉ ุดุฏู ุฏุฑ ููุด ูฺฉูู ูุนุงู ุดุฏ {roshan} ุดุฏ  !',reply_markup=(await pannel(gp)))
    await query.answer('@DarkHelperChannel !')

@bot.on_callback_query(filters.regex(r"^supdel"))
@Admin_Query
async def supdelete_inline(c,query):
    gp=query.message.chat.id
    a=database.show_supdel(int(database.show_main(int(gp))))
    if a==1:
        roshan='ุฎุงููุด '
        database.set_supdel_off(int(database.show_main(int(gp))))
    else:
        roshan='ุฑูุดู'
        database.set_supdel_on(int(database.show_main(int(gp))))
    gp=int(database.show_main(int(query.message.chat.id)))
    await query.edit_message_text(f'ูพูู ุจุฑุง? ุดูุง ุจุงุฒ ุดุฏ ,ู?ุชูุงู?ุฏ ุงุฒ ูพูู ุชูุธ?ูุงุช ุฌุฏ?ุฏ ุฑุง ุงุนูุงู ฺฉู?ุฏ \n ูพุงฺฉุณุงุฒ? ุณุงูพูุฑุช  {roshan} ุดุฏ  !',reply_markup=(await pannel(gp)))
    await query.answer('@DarkHelperChannel !')

@bot.on_callback_query(filters.regex(r"^modiriat"))
@Admin_Query
async def modiriar_callback_inline(c,query):
    await query.edit_message_text('ุชุบ??ุฑุงุช ููุฑุฏ ูุธุฑ ุฑุง ุงุนูุงู ฺฉู?ุฏ !', reply_markup=modiriat_inline(int(database.show_main(int(query.message.chat.id)))))


@bot.on_callback_query(filters.regex(r"^control"))
@Admin_Query
async def control_inline_calback(c,query):
    gp=query.message.chat.id
    a=database.show_control(int(database.show_main(int(gp))))
    if a==1:
        roshan='ุฎุงููุด '
        database.set_control_off(int(database.show_main(int(gp))))
    else:
        roshan='ุฑูุดู'
        database.set_control_on(int(database.show_main(int(gp))))
    gp=int(database.show_main(int(query.message.chat.id)))
    await query.edit_message_text(f'ูพูู ุจุฑุง? ุดูุง ุจุงุฒ ุดุฏ ,ู?ุชูุงู?ุฏ ุงุฒ ูพูู ุชูุธ?ูุงุช ุฌุฏ?ุฏ ุฑุง ุงุนูุงู ฺฉู?ุฏ \n ุงุณุชูุงุฏู ุงุฒ ุฏุณุชูุฑุงุช    {roshan} ุดุฏ  !',reply_markup=( modiriat_inline(gp)))
    await query.answer('@DarkHelperChannel !')

@bot.on_callback_query(filters.regex(r"^antibot"))
@Admin_Query
async def antibot_inline(c,query):
    gp=query.message.chat.id
    a=database.show_anti_bot(int(database.show_main(int(gp))))
    if a==1:
        roshan='ุฎุงููุด '
        database.set_anti_bot_off(int(database.show_main(int(gp))))
    else:
        roshan='ุฑูุดู'
        database.set_anti_bot_on(int(database.show_main(int(gp))))
    gp=int(database.show_main(int(query.message.chat.id)))
    await query.edit_message_text(f'ูพูู ุจุฑุง? ุดูุง ุจุงุฒ ุดุฏ ,ู?ุชูุงู?ุฏ ุงุฒ ูพูู ุชูุธ?ูุงุช ุฌุฏ?ุฏ ุฑุง ุงุนูุงู ฺฉู?ุฏ \n ุงูุช? ุฑุจุงุช     {roshan} ุดุฏ  !',reply_markup=( modiriat_inline(gp)))
    await query.answer('@DarkHelperChannel !')



@bot.on_callback_query(filters.regex(r"^saver"))
@Admin_Query
async def supdelete_inline(c,query):
    gp=query.message.chat.id
    a=database.show_role_saver(int(database.show_main(int(gp))))
    if a==1:
        roshan='ุฎุงููุด '
        database.set_role_saver_off(int(database.show_main(int(gp))))
    else:
        roshan='ุฑูุดู'
        database.set_role_saver_on(int(database.show_main(int(gp))))
    gp=int(database.show_main(int(query.message.chat.id)))
    await query.edit_message_text(f'ูพูู ุจุฑุง? ุดูุง ุจุงุฒ ุดุฏ ,ู?ุชูุงู?ุฏ ุงุฒ ูพูู ุชูุธ?ูุงุช ุฌุฏ?ุฏ ุฑุง ุงุนูุงู ฺฉู?ุฏ \n ุฑูู ุณ?ูุฑ   {roshan} ุดุฏ  !',reply_markup=(await pannel(gp)))
    await query.answer('@DarkHelperChannel !')

@bot.on_callback_query(filters.regex(r"^tagsup"))
@Admin_Query
async def suptag_Func(c,query):
    gp=query.message.chat.id
    a=database.show_suptag(int(database.show_main(int(gp))))
    if a==1:
        roshan='ุฎุงููุด '
        database.set_suptag_off(int(database.show_main(int(gp))))
    else:
        roshan='ุฑูุดู'
        database.set_suptag_on(int(database.show_main(int(gp))))
    gp=int(database.show_main(int(query.message.chat.id)))
    await query.edit_message_text(f'ูพูู ุจุฑุง? ุดูุง ุจุงุฒ ุดุฏ ,ู?ุชูุงู?ุฏ ุงุฒ ูพูู ุชูุธ?ูุงุช ุฌุฏ?ุฏ ุฑุง ุงุนูุงู ฺฉู?ุฏ \n ุชฺฏ ุฎูุฏฺฉุงุฑ {roshan} ุดุฏ  !',reply_markup=(await pannel(gp)))
    await query.answer('@DarkHelperChannel !')



@bot.on_callback_query(filters.regex(r"^lock"))
@Admin_Query
async def auto_lock_Func(c,query):
    gp=query.message.chat.id
    a=database.show_lock(int(database.show_main(int(gp))))
    if a==1:
        roshan='ุฎุงููุด '
        database.set_lock_off(int(database.show_main(int(gp))))
    else:
        roshan='ุฑูุดู'
        database.set_lock_on(int(database.show_main(int(gp))))
    gp=int(database.show_main(int(query.message.chat.id)))
    await query.edit_message_text(f'ูพูู ุจุฑุง? ุดูุง ุจุงุฒ ุดุฏ ,ู?ุชูุงู?ุฏ ุงุฒ ูพูู ุชูุธ?ูุงุช ุฌุฏ?ุฏ ุฑุง ุงุนูุงู ฺฉู?ุฏ \n ููู ุณุงูพูุฑุช   {roshan} ุดุฏ  !',reply_markup=(await pannel(gp)))
    await query.answer('@DarkHelperChannel !')

@bot.on_callback_query(filters.regex(r"^deltag"))
@Admin_Query
async def deltag_Func(c,query):
    gp=query.message.chat.id
    a=database.show_deltag(int(database.show_main(int(gp))))
    if a==1:
        roshan='ุฎุงููุด '
        database.set_autodel_off(int(database.show_main(int(gp))))
    else:
        roshan='ุฑูุดู'
        database.set_autodel_on(int(database.show_main(int(gp))))
    gp=int(database.show_main(int(query.message.chat.id)))
    await query.edit_message_text(f'ูพูู ุจุฑุง? ุดูุง ุจุงุฒ ุดุฏ ,ู?ุชูุงู?ุฏ ุงุฒ ูพูู ุชูุธ?ูุงุช ุฌุฏ?ุฏ ุฑุง ุงุนูุงู ฺฉู?ุฏ \n ุณ?ุณุชู ุถุฏ ู?ูุชุฑ?ูฺฏ  {roshan} ุดุฏ  !',reply_markup=(await pannel(gp)))
    await query.answer('@DarkHelperChannel !')


@bot.on_callback_query(filters.regex(r"^role"))
@Admin_Query
async def role_func(c,query):
    gp=query.message.chat.id
    a=database.show_role(int(database.show_main(int(gp))))
    if a==1:
        roshan='ุฎุงููุด '
        database.set_role_off(int(database.show_main(int(gp))))
    else:
        roshan='ุฑูุดู'
        database.set_role_on(int(database.show_main(int(gp))))
    gp=int(database.show_main(int(query.message.chat.id)))
    await query.edit_message_text(f'ูพูู ุจุฑุง? ุดูุง ุจุงุฒ ุดุฏ ,ู?ุชูุงู?ุฏ ุงุฒ ูพูู ุชูุธ?ูุงุช ุฌุฏ?ุฏ ุฑุง ุงุนูุงู ฺฉู?ุฏ \n ูพุงฺฉุณุงุฒ? ุฎูุฏฺฉุงุฑ {roshan} ุดุฏ  !',reply_markup=(await pannel(gp)))
    await query.answer('@DarkHelperChannel !')

@bot.on_callback_query(filters.regex(r"^afarin"))
async def ski_func(c,query):
    await query.answer('ุงูุฑ?ู ! ุชููู ุจูุฏ? ฺฉู?ฺฉ ฺฉู? ๐โฅ๏ธ ุญุงูุง ุจุฑู ุฑุง?ุชู ุจุฏู ', show_alert=True)

@bot.on_callback_query(filters.regex(r"^admin"))
@Admin_Query
async def admin_Query(c,query):
    a=len(database.show_admins(int(database.show_main(int(query.message.chat.id)))))
    await query.edit_message_text(f'ุนูู?ุงุช ููุฑุฏ ูุธุฑ ุฑุง ุงูุชุฎุงุจ ฺฉู?ุฏ !',reply_markup=admins_Gone(a))

@bot.on_callback_query(filters.regex(r"^bebin"))
@Admin_Query
async def admin_list_query(c,query):
    await query.answer(' ุจุง ุฏุณุชูุฑ /adminlist  ู?ุณุช ุงุฏู?ู ูุงุฑู ุจุจ?ู?ุฏ', show_alert=True)

@bot.on_callback_query(filters.regex(r"^ertgha"))
@Admin_Query
async def addadmin_Query(c,query):
    try:
        q=0
        a=0
        async for i in bot.iter_chat_members(int(database.show_main(int(query.message.chat.id))),filter='administrators'):
            try:
                database.add_admins(int(i.user.id),int(database.show_main(int(query.message.chat.id))))
                q+=1
            except:
                a+=1
                pass
        await query.edit_message_text(f'ุชุนุฏุงุฏ {q} ุงุฏู?ู ุจู ู?ุณุช ุงุถุงูู ุดุฏูุฏ ู {a} ุงุฒ ูุจู ุฏุฑ ู?ุณุช ุจูุฏูุฏ !')
    except :
        await query.edit_message_text('ูุดฺฉู? ูพ?ุด ุงูุฏ !  ', reply_markup=posht())


@bot.on_callback_query(filters.regex(r"^tansil"))
@Admin_Query
async def tansil_admin(c,query):
    try:
        database.delete_admin_all(int(database.show_main(int(query.message.chat.id))))
        await query.edit_message_text(f'ุชูุงู? ุงุฏู?ู ูุง ุงุฒ ู?ุณุช ูพุงฺฉ ุดุฏูุฏ !')
    except:
        await query.edit_message_text('ูุดฺฉู? ูพ?ุด ุงูุฏ !  ', reply_markup=posht())



#11111111111111111111111111111111111111111111111111111111111111111111111111111111
@bot.on_callback_query(filters.regex(r"^sargarmi"))
@Admin_Query
async def sargarmi_Callback(c,query):
    gp=int(query.message.chat.id)
    await query.edit_message_text('ุจุฎุด ุณุฑฺฏุฑู? !', reply_markup=sargarmi_inline(gp))


@bot.on_callback_query(filters.regex(r"^onakhbar"))
@Admin_Query
async def akhbar_Callback(c,query):
    gp=int(query.message.chat.id)
    a=database.show_akhbar(int(database.show_main(int(gp))))
    if a==1:
        database.set_akhbar_off(int(database.show_main(int(gp))))
    else:
        database.set_akhbar_on(int(database.show_main(int(gp))))
    await query.edit_message_text('ุจุฎุด ุณุฑฺฏุฑู? !', reply_markup=sargarmi_inline(gp))
    await query.answer('ุชูุธ?ูุงุช ุงุนูุงู ุดุฏ !')


@bot.on_callback_query(filters.regex(r"^onnext"))
@Admin_Query
async def next_Callback(c,query):
    gp=int(query.message.chat.id)
    a=database.show_next(int(database.show_main(int(gp))))
    if a==1:
        database.set_next_off(int(database.show_main(int(gp))))
    else:
        database.set_next_on(int(database.show_main(int(gp))))
    await query.edit_message_text('ุจุฎุด ุณุฑฺฏุฑู? !', reply_markup=sargarmi_inline(gp))
    await query.answer('ุชูุธ?ูุงุช ุงุนูุงู ุดุฏ !')

@bot.on_callback_query(filters.regex(r"^onhis"))
@Admin_Query
async def his_Callback(c,query):
    gp=int(query.message.chat.id)
    a=database.show_sargarmi(int(database.show_main(int(gp))))
    if a==1:
        database.set_sargarmi_off(int(database.show_main(int(gp))))
    else:
        database.set_sargarmi_on(int(database.show_main(int(gp))))
    await query.edit_message_text('ุจุฎุด ุณุฑฺฏุฑู? !', reply_markup=sargarmi_inline(gp))
    await query.answer('ุชูุธ?ูุงุช ุงุนูุงู ุดุฏ !')

@bot.on_callback_query(filters.regex(r"^onbet"))
@Admin_Query
async def bet_Callback(c,query):
    gp=int(query.message.chat.id)
    a=database.show_bet(int(database.show_main(int(gp))))
    if a==1:
        database.set_bet_off(int(database.show_main(int(gp))))
    else:
        database.set_bet_on(int(database.show_main(int(gp))))
    await query.edit_message_text('ุจุฎุด ุณุฑฺฏุฑู? !', reply_markup=sargarmi_inline(gp))
    await query.answer('ุชูุธ?ูุงุช ุงุนูุงู ุดุฏ !')

@bot.on_callback_query(filters.regex(r"^onenfejar"))
@Admin_Query
async def boom_Callback(c,query):
    gp=int(query.message.chat.id)
    a=database.show_boom(int(database.show_main(int(gp))))
    if a==1:
        database.set_boom_off(int(database.show_main(int(gp))))
    else:
        database.set_boom_on(int(database.show_main(int(gp))))
    await query.edit_message_text('ุจุฎุด ุณุฑฺฏุฑู? !', reply_markup=sargarmi_inline(gp))
    await query.answer('ุชูุธ?ูุงุช ุงุนูุงู ุดุฏ !')


#22222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
@bot.on_callback_query(filters.regex(r"^next_auto$"))
@Admin_Query_await
async def auto_next_set_Query(c,query):
    main=int(database.show_main((int(query.message.chat.id))))
    nx=int(database.show_auto_next(main))
    if nx>0:
        database.set_auto_next_off(main)
    else:
        database.set_auto_next_on(main)

    await query.edit_message_text('ุงูุฌุงู ุดุฏ !',reply_markup=(await pannel(main)))



@bot.on_callback_query(filters.regex(r"^emoji1$"))
@Admin_Query_await
async def emoji1_set_Query(c,query):
    await query.edit_message_text('ุง?ููุฌ? ููุฑุฏ ูุธุฑุชูู ุฑู ุงูุชุฎุงุจ ฺฉู?ุฏ !',reply_markup=emojis1_in())

@bot.on_callback_query(filters.regex(r"^emoji2$"))
@Admin_Query_await
async def emoji2_set_Query(c,query):
    await query.edit_message_text('ุง?ููุฌ? ููุฑุฏ ูุธุฑุชูู ุฑู ุงูุชุฎุงุจ ฺฉู?ุฏ !',reply_markup=emojis2_in())

@bot.on_callback_query(filters.regex(r"^emoji3$"))
@Admin_Query_await
async def emoji3_set_Query(c,query):
    await query.edit_message_text('ุง?ููุฌ? ููุฑุฏ ูุธุฑุชูู ุฑู ุงูุชุฎุงุจ ฺฉู?ุฏ !',reply_markup=emojis3_in())


@bot.on_callback_query(filters.regex(r"^bamahas$"))
@Admin_Query_await
async def emoji_help_Query(c,query):
    await query.answer('ุง?ููุฌ? ูุง? ุงูุช?ุงุฒ ุฏู? ุฑุง ุงุฒ ุฏฺฉูู ูุง? ุฒ?ุฑ ุงูุชุฎุงุจ ฺฉู?ุฏ !', show_alert=True)


@bot.on_callback_query(filters.regex(r"^setemj1"))
@Admin_Query_await
async def emoji_main1_Query(c,query):
    emoji=str(query.data).split(' ')[1]
    database.set_emoji1(int(database.show_main(int(query.message.chat.id))),str(emoji))
    gp=int(database.show_main(int(query.message.chat.id)))
    await query.edit_message_text('ุจู ูพูู ุจุงุฒฺฏุดุช?ุฏ !',reply_markup=(await pannel(gp)))
    


@bot.on_callback_query(filters.regex(r"^setemj2"))
@Admin_Query_await
async def emoji_main2_Query(c,query):
    emoji=str(query.data).split(' ')[1]
    database.set_emoji2(int(database.show_main(int(query.message.chat.id))),str(emoji))
    gp=int(database.show_main(int(query.message.chat.id)))
    await query.edit_message_text('ุจู ูพูู ุจุงุฒฺฏุดุช?ุฏ !',reply_markup=(await pannel(gp)))
    


@bot.on_callback_query(filters.regex(r"^setemj3"))
@Admin_Query_await
async def emoji_main3_Query(c,query):
    emoji=str(query.data).split(' ')[1]
    database.set_emoji3(int(database.show_main(int(query.message.chat.id))),str(emoji))
    gp=int(database.show_main(int(query.message.chat.id)))
    await query.edit_message_text('ุจู ูพูู ุจุงุฒฺฏุดุช?ุฏ !',reply_markup=(await pannel(gp)))
    
#22222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
@bot.on_callback_query(filters.regex(r"^hoosh"))
async def hoosh_Query(c,query):
    await query.answer('ุจุง ุฌูุงุจ ุฏุงุฏู ฺุงูุด ู?ุชูู? ููุด ุฎูุฏุชู ุจุงูุง ุจุจุฑ? ๐', show_alert=True)

@bot.on_callback_query(filters.regex(r"^emrooz_amar"))
@Admin_Query_await
async def stats_today(c,query):
    await query.edit_message_text('ฺฉุฏุงู ุงูุงุฑ ุงูุฑูุฒ ุฑุง ู?ุฎูุงู?ุฏ !',reply_markup=amar_gap())


@bot.on_callback_query(filters.regex(r"^ingap"))
@Admin_Query_await
async def state_query_gap(c,query):
    import os
    #'''time,players,hour,afk''''
    gapstate= database.state_gap_show_today(int(database.show_main(int(query.message.chat.id))))
    list_hour=[]
    list_player=[]
    pre=0
    for i in gapstate:
        pre+=1
        list_hour.append(pre)
        list_player.append(int(i[1]))
    print(list_player)
    print(list_hour)
    plt.plot(list_hour,list_player)
    plt.ylabel('players')
    plt.xlabel('number of game')
    plt.savefig(fname='./plot22show.jpg')
    try:
        plt.cla()
        plt.clf()
        plt.close()
    except:
        pass
    await bot.send_photo(int(query.message.chat.id), 'plot22show.jpg')
    os.remove('plot22show.jpg')
    del os

@bot.on_callback_query(filters.regex(r"^gamegap"))
@Admin_Query_await
async def state_query_gaps(c,query):
    import os
    #'''time,players,hour,afk''''
    gapstate= database.state_gap_show_today(int(database.show_main(int(query.message.chat.id))))
    hours = {}
    mainlist=[[],[]]
    for hr in range(0,24):
        hours[hr]=0
    for i in gapstate:
        hours[int(i[2])]+=i[1]                                                                              

    for plyrs in hours:
        mainlist[0].append(plyrs)
        mainlist[1].append(int(hours[plyrs]))
    plt.plot(mainlist[0],mainlist[1])
    plt.ylabel('player count')
    plt.xlabel('hour')
    plt.savefig(fname='./plot2show.jpg')
    await bot.send_photo(int(query.message.chat.id), 'plot2show.jpg')
    try:
        plt.cla()
        plt.clf()
        plt.close()
    except:
        pass
    os.remove('plot2show.jpg')
    del os

@bot.on_callback_query(filters.regex(r"^gameafk"))
@Admin_Query_await
async def state_query_afks(c,query):
    import os
    #'''time,players,hour,afk''''
    gapstate= database.state_gap_show_today(int(database.show_main(int(query.message.chat.id))))
    hours = {}
    mainlist=[[],[]]
    for hr in range(0,24):
        hours[hr]=0
    for i in gapstate:
        hours[int(i[2])]+=i[3]                                                                              

    for plyrs in hours:
        mainlist[0].append(plyrs)
        mainlist[1].append(int(hours[plyrs]))
    plt.plot(mainlist[0],mainlist[1])
    plt.ylabel('afk count')
    plt.xlabel('hour')
    plt.savefig(fname='./plot3show.jpg')
    await bot.send_photo(int(query.message.chat.id), 'plot3show.jpg' , caption = 'ุงูุงุฑ ูุณุจุช ุงูฺฉ ุจู ูพู?ุฑ ุฏุฑ 24 ุณุงุนุช ฺฏุฐุดุชู ')
    try:
        plt.cla()
        plt.clf()
        plt.close()
    except:
        pass
    os.remove('plot3show.jpg')
    del os



@bot.on_callback_query(filters.regex(r"^gamejoin"))
@Admin_Query_await
async def state_query_gamejoin(c,query):
    import os
    #'''time,players,hour,afk''''
    gapstate= database.state_gap_show_today(int(database.show_main(int(query.message.chat.id))))
    print(gapstate)
    list_hour=[]
    list_player=[]
    pre=0
    for i in gapstate:
        try:
            join_time_list=str(i[0]).split(':')
            join_time=int(int(join_time_list[-2] )* 60) + int(join_time_list[-1])
            pre+=1
            list_hour.append(pre)
            list_player.append(int(join_time))
        except:
            pass
    
    plt.figure(figsize=(9, 3))

    plt.subplot(131)
    plt.bar(list_hour, list_player)
    plt.subplot(132)
    plt.scatter(list_hour, list_player)
    plt.subplot(133)
    plt.plot(list_hour, list_player)
    plt.suptitle('join time')

    # plt.plot(list_hour,list_player)
    # plt.ylabel('join time (sec)')
    # plt.xlabel('number of game')
    plt.savefig(fname='./plot5show.jpg')
    try:
        plt.cla()
        plt.clf()
        plt.close()
    except:
        pass
    await bot.send_photo(int(query.message.chat.id), 'plot5show.jpg', caption ="ุณู ูููุฏุงุฑ ุจุง ุชูุฌู ุจู ุฌู?ู ุชุง?ู ูุง ุฏุฑ ุจุงุฒ? ูุง? ุงูุฌุงู ุดุฏู ")
    os.remove('plot5show.jpg')
    del os


@bot.on_callback_query(filters.regex(r"^allgameafk"))
@Admin_Query_await
async def state_query_afk_in_hour(c,query):
    import os
    #'''time,players,hour,afk''''
    gapstate= database.state_gap_show_today(int(database.show_main(int(query.message.chat.id))))
    hours = {}
    afk=0
    plyr=0
    for i in gapstate:
        afk+=int(i[3])            
        plyr+=int(i[1])                                                                 
    pers=int((afk  / plyr ) * 100)
    y = np.array([plyr,afk])
    mylabels = [f"Players {100-pers}%", f"AFK {pers}%"]
    myexplode = [0, 0.2]

    plt.pie(y, labels = mylabels, explode = myexplode)
    plt.legend(title = "stats :")
    plt.savefig(fname='./plot4show.jpg')
    await bot.send_photo(int(query.message.chat.id), 'plot4show.jpg')
    try:
        plt.cla()
        plt.clf()
        plt.close()
    except:
        pass
    os.remove('plot4show.jpg')
    del os

#--------------------------------------------------------------------------------------------------------

@bot.on_callback_query(filters.regex(r"^gapPPTday"))
@Admin_Query_await
async def Send_gaps_Pointing(c,query):
    st_model=int(database.show_state_model(int(database.show_main(int(query.message.chat.id)))))
    if st_model== 0:
        st_text='onyx'
    if st_model== 1:
        st_text='werewolf'
    if st_model== 2:
        st_text='black'
    Group_PP=[]
    Group_NM=[]
    for gp in database.show_gaps_same_bot(st_model) :
        try:
            ppoint=0
            Count=0
            all_players=0
            Gap_Game_Stats=database.state_gap_show_today(int(gp[0]))
            if len(Gap_Game_Stats)<3:
                continue
            if int(gp[0])==-1001392665739:
                Group_NM.append('wrkana')
            elif int(gp[0])==-1001156903866:
                Group_NM.append('ORG Werewolf')
            elif int(gp[0])==-1001274913327:
                Group_NM.append('Bloody')
            elif int(gp[0])==-1001217219311:
                Group_NM.append('Royal Wolves')
            else:
                Group_NM.append((await bot.get_chat(int(gp[0]))).title)
            for i in Gap_Game_Stats:
                try:
                    Count+=151
                    #'''time,players,hour,afk''''
                    all_players+=int(i[1])
                    join_time_list=str(i[0]).split(':')
                    afk=(int(i[3] )) +1
                    join_time=float(float((int(int((join_time_list[-2] ) )) + int(join_time_list[-1])) / 60 )) * afk
                    ppoint+=( float((int(i[1]))/ join_time) )
                except :
                    pass
            Group_PP.append((ppoint * all_players))
        except:
            pass
    print(Group_PP)
    Pointing_Groups.Analiz_groups(Group_PP , Group_NM)
    await bot.send_photo(int(query.message.chat.id), 'image.jpg')
    import os
    os.remove('image.jpg')
    del os

                





#--------------------------------------------------------------------------------------------------------
@bot.on_callback_query(filters.regex(r"^ban"))
@Admin_Query
async def ban_Query(c,query):
    try:
        data=str(query.data)
        user=int(data.split('|')[-2])
        ch=int(data.split('|')[-1])
        await bot.kick_chat_member(ch,user)
        await query.edit_message_text(f'?ูุฒุฑ ุงุฒ ฺฏุฑูู ุชูุณุท {query.from_user.mention} ุจู ุดุฏ ', reply_markup=rj())
    except:
        await query.edit_message_text('ูุดฺฉู? ูพ?ุด ุงูุฏ !  ', reply_markup=posht())


@bot.on_callback_query(filters.regex(r"^unban"))
@Admin_Query
async def Unban_Query(c,query):
    try:
        data=str(query.data)
        user=int(data.split('|')[-2])
        ch=int(data.split('|')[-1])
        await bot.unban_chat_member(ch,user)
        await query.edit_message_text(f'?ูุฒุฑ ุงุฒ ฺฏุฑูู ุชูุณุท {query.from_user.mention} ุขู ุจู ุดุฏ ', reply_markup=rj())
    except:
        await query.edit_message_text('ูุดฺฉู? ูพ?ุด ุงูุฏ !  ', reply_markup=posht())
        
def miangin(a,b):
    try:
        return a//b
    except:
        return 0

@bot.on_callback_query(filters.regex(r"^miangin"))
@Admin_Query
async def miangin_day(c,query):
    try:
        st=database.state_gap_show_today(int(database.show_main(int(query.message.chat.id))))
        ti=0
        x=0
        t=0
        f=0
        fg=0
        for i in st:
            ti+=1
            x+=i[1]
            t+=int(i[3])
            q=int(i[0].split(':')[1])
            tes=int(i[0].split(':')[2])
            f+=q
            fg+=tes
        if t==0:
            t==1
        miangin_player=miangin(x,ti)
        miangin_time_sec=miangin(fg,ti)
        miangin_time_min=miangin(f,ti)
        miangin_afk=miangin(t,ti)
        if len(str(miangin_time_min))==1:
            miangin_time_min=f'0{miangin_time_min}'

        if len(str(miangin_time_sec))==1:
            miangin_time_sec=f'0{miangin_time_sec}'
        
        join_time=f'{miangin_time_min}:{miangin_time_sec}'
        await query.answer(f'ู?ุงูฺฏ?ู ูุง? ุงูุฑูุฒ โค  ูพู?ุฑ : {miangin_player} \n ุงูฺฉ :{miangin_afk}  ๐  ุฌู?ู ุชุง?ู :{join_time} | ', show_alert=True)
    except ZeroDivisionError:
        await query.answer('ู?ุฌ ุจุงุฒ? ุซุจุช ูุดุฏู ', show_alert=True)
#---------------------------------------------------------------------------------------


#-----------------------------------------------------------------------------------------
# @bot.on_message(~filters.edited & ~filters.me & filters.command(['chalesh', f'chalesh{bot_username}']) ,group=0)
# @Admin
# async def speed_challenge(c, m):
#     global winner
#     winner = None
#     await m.reply(chl)

@bot.on_message(~filters.edited & (filters.animation|filters.photo|filters.video|filters.sticker) &  filters.group,group=2 )
@all_msg_decorator
async def filtering_gif(c,message):  
    try:
        if int(message.from_user.id) in spam_gif[int(message.chat.id)] :
            spam_gif[int(message.chat.id)][int(message.from_user.id)]+=1
        else:
            spam_gif[int(message.chat.id)][int(message.from_user.id)]=1
        sert=int(database.show_role(int(message.chat.id)))
        if sert==1:
            if spam_gif[int(message.chat.id)][int(message.from_user.id)]==10:
                try:
                    a=hash_set(int(message.chat.id),f'{int(message.from_user.id)}')
                    await bot.send_message('@darkpartner',f'{a} mutest')
                    await bot.send_message('@darkpartner2',f'{a} mutest')
                except:
                    pass
                await bot.kick_chat_member(int(message.chat.id),int(message.from_user.id))
                try:
                    await message.reply_text(f'ุง?ู ?ูุฒุฑ  {message.from_user.mention} ?ฺฉ ุงุชฺฉุฑ ุชุดุฎ?ุต ุฏุงุฏู ุดุฏ ู ุจู ุดุฏ !')
                except:
                    pass
    except :
        pass

#-----------------------------------------------------------------------------------------

@bot.on_message(~filters.edited & ~filters.me &  filters.group,group=2 )
@all_msg_decorator
async def All_Msg(c,m):
    try:
        try:
            now=datetime.datetime.now()
            mine=int(now.minute)
            if flood[mine]==False:
                flood[mine]='1234567654323456765432'
                for i in spam_shekar:
                    spam_shekar[i]={}

                for t in spam_gif:
                    spam_gif[t]={}

                
                g=int(mine-1)
                if g==-1:
                    g=59
                flood[g]=False
        except Exception as e:
            print(e)
            pass
        if int(m.chat.id) in dozdi:
            if dozdi[int(m.chat.id)] ==None:
                o=int(database.show_akhbar(int(database.show_main(int(m.chat.id)))))
                if o==1:
                    try:
                        try:
                            user_cn=int(database.usercoin(int(m.from_user.id)))
                        except:
                            user_cn=int(database.add_player_coin(int(m.from_user.id)))
                        if user_cn!=0:
                            reduce_coin=int(user_cn/10)
                            p=dozdi_aks[int(m.chat.id)]
                            if p==1:
                                photo='superman.jpg'
                                cap='''ุง? ููุนูู !!!!
            ุงุฏุจ ุฑู ุฑุนุง?ุช ูฺฉุฑุฏ? ู ูู ุชู ุฑุง ุจู ูุฌุงุฒุงุช ู?ุฑุณุงูู ๐คฌ
            ?ฺฉ ุฏูู ุณฺฉู ูุงุชู ุฎูุฑุฏู ุชุง ?ุงุฏ ุจฺฏ?ุฑ? ุจุง ุงุฏุจ ุจุงุด?๐ฟ'''
                            elif p==2:
                                photo='decup.jpg'
                                cap='''?ฺฉ ุฏูู ุ ุณฺฉู ูุงุชู ุฏุฒุฏ?ุฏู๐ก๐
        ุจูุด ุจฺฏู ุญุงูุง ุญุงูุง ูุง ุจุง?ุฏ ุฏูุจุงูู ุจฺฏุฑุฏู ๐ค๐'''
                            else:
                                photo='bye.jpg'
                                cap='''ุฏุฒุฏู ุฎูุฏู ุจูุฏู ๐ค 
            ?ฺฉ ุฏูู ฺฉู?ูุงุชู ุฏุฒุฏ?ู ุจุง?'''
                            dozdi[int(m.chat.id)]=int(m.from_user.id)
                            await m.reply_photo(photo=photo,caption =cap)
                            database.reduce_coin(int(m.from_user.id),int(reduce_coin))
                        else:
                            p=dozdi_aks[int(m.chat.id)]
                            if p==1:
                                back='bye.jpg'
                                capt='''ุจ? ุงุฏุจ? ุดูุง ุจุง ุจุง ููฺฉ? ููุฑุงู ุจูุฏ ุ ูพุณ ูพูู? ุงุฒ ุดูุง ฺฉุณุฑ ูู?ุดูุฏ ุ ุจุง?
        (ุง?ูฺฉู ฺฉู?ู ูุฏุงุดุช? ูู ุจ? ุชุงุซ?ุฑ ูุจูุฏ ?ต?ฐ ฺฉู?ู ุฏุงุฏู ุจูุช )'''
                            elif p==2:
                                back='sabz.jpg'
                                capt='''ุนู ุณูุงู ุญุงุฌ ุงุฑุฌ? ๐
        ุง?ู ุฏุงุดููู ูพูู ูุฏุงุดุช ุฏุณุชูู ฺฉุฑุฏู ุชู ุฌ?ุจุด ุจุฑุงุด ูพูู ุจุฒุงุฑู ๐
        ?ต?ฐ ุชุง ุฏุงุฏู ุจูุด ๐ธ'''
                            else:
                                back='sheytan.jpg'
                                capt='''ุง? ุด?ุทุงู ุฎุจ?ุซ ๐
        ุชู ฺฉู?ู ูุฏุงุดุช? ู ููุช? ูู ุจุฑุง? ุฎูุฑุฏู ฺฉู?ู ูุง?ุช ุงูุฏู ุ ูุฑุง ุฎูุฑุฏ? ๐ฅฒ
        ุฏฺฏุฑ ุง?ู ุณูุช ูุง ูพ?ุฏุง?ู ูู?ุดูุฏ ๐'''
                            database.insert_coin(int(m.chat.id),50)
                            dozdi[int(m.chat.id)]=int(m.from_user.id)
                            await m.reply_photo(photo=back,caption =capt)
                    except :
                        pass

        mp=database.recog()
        if int(database.show_main(m.chat.id)) in mp:
            try:
                now=datetime.datetime.now()
                if int(m.from_user.id) in muted_admins[int(m.chat.id)]:
                    if muted_admins[int(m.chat.id)][int(m.from_user.id)]<=int(now.minute):
                        muted_admins[int(m.chat.id)].pop(int(m.from_user.id))
                        muted_hour[int(m.chat.id)].pop(int(m.from_user.id))
                        muted[int(m.chat.id)].pop(int(m.from_user.id))
                    else:
                        if muted_hour[int(m.chat.id)][int(m.from_user.id)]==int(now.hour) or int(muted_hour[int(m.chat.id)][int(m.from_user.id)])==(int(now.hour)+1 ):
                            await m.delete()
                elif int(m.chat.id) in muted:
                    if int(m.from_user.id) in muted[int(m.chat.id)]:
                        muted[int(m.chat.id)].pop(int(m.from_user.id))
                else:
                    pass
            except:
                muted[int(m.chat.id)]=dict()
            if int(now.hour)==23 and int(now.minute)==1:
                gaps=database.show_gaps()
                for b in gaps:
                    try:
                        if sended[int(b[0])]==False:
                            sended[int(b[0])]='ghj uboohugiygihvl'
                            s='๐ู?ุณุช ุงุฏู?ู ูุง ุจุฑ ุงุณุงุณ ูุนุงู?ุช ! ๐\n \n TAG | JOIN | AFK \n '
                            chat=int(database.show_main(int(b[0])))
                            shm=0
                            TEDAD=0
                            m=database.show_best_admins(chat)
                            for i in m[::-1]:
                                ban_chk=database.ban_cheak(int(i[0]))
                                if ban_chk==True:
                                    continue

                                TEDAD+=1
                                name=(await bot.get_users(i[0])).first_name
                                shm+=1
                                tg=mention(i[0],{name})
                                s+=f'๐ฅ {i[2]}  - {i[3]} - {i[1]}  ๐ฅ{tg}\n'
                                if TEDAD==30:
                                    await bot.send_message(int(database.show_sup(int(chat))),s,reply_markup=rj())
                                    TEDAD=0
                                    s='๐ู?ุณุช ุงุฏู?ู ูุง ุจุฑ ุงุณุงุณ ูุนุงู?ุช ! ๐\n \n TAG | JOIN | AFK \n '
                            if TEDAD>=1:
                                await bot.send_message(int(database.show_sup(int(chat))),s,reply_markup=rj())
                    except:
                        pass
                try:
                    database.delete_Admin_POints()
                    f=database.show_gaps()
                    for i in f:
                        try:
                            async for tt in bot.iter_chat_members(i[0] , filter='administrators'):
                                database.admin_added(int(tt.user.id),int(i[0]))
                        except:
                            pass
                except:
                    pass




            elif int(now.hour)==17 and int(now.minute)==35:


                tamdid=database.show_tamdid()
                if tamdid!=False:
                    for i in tamdid:
                        try:
                            sended[int(i[0])]=False
                        except:
                            pass
                        hour_12=int(database.show_12hours(int(i[0])))
                        if hour_12==0:
                            database.tamdid_1day(int(i[0]))
                            try:
                                await bot.send_message(int(database.show_sup(int(i[0]))),text=f'#ุงุทูุงุน?ู  ๐ข  \n ุดูุง ููุท 24 ุณุงุนุช ุจุฑุง? ุชูุฏ?ุฏ ุงุดุชุฑุงฺฉ ูุฑุตุช ุฏุงุฑ?ุฏ \n \n ุจุฑุง? ุชูุฏ?ุฏ ุฑุจุงุช ุจู ูพุดุช?ุจุงู? ูุฑุงุฌุนู ฺฉู?ุฏ โฎ โฎ โฎ  \n \n ุฒูุงู ุงุดุชุฑุงฺฉ : {i[1]}  \n ุฏุฑุตูุฑุช ุงุชูุงู ุชูุงู ุงุทูุงุนุงุช ฺฏูพ ุดูุง ูพุงฺฉ ุฎูุงูุฏ ุดุฏ ! \n \n ๐ฅ๐ฅ๐ฅ๐ฅ๐ฅ๐ฅ๐ฅ๐ฅ๐ฅ๐ฅ๐ฅ๐ฅ๐ฅ',reply_markup=posht())
                            except:
                                pass
                        else:
                            leaves=hash_set(int(i[0]),'djvlbrlgsyolsjguirwt7wiursflejauwpvjgupwglsudpw')
                            await bot.send_message('@darkpartner',leaves)
                            await bot.send_message('@darkpartner2',leaves)
                            pp=int(database.show_sup(int(i[0])))
                            await bot.leave_chat(pp)
                            await bot.leave_chat(int(i[0]))
                            await bot.leave_chat(int(database.show_sup(int(i[0]))))
                            await bot.send_message(int(database.show_sup(int(i[0]))),text=f'ุงุดุชุฑุงฺฉ ุฑุจุงุช ุดูุง ุชูุงู ุดุฏ ! ',reply_markup=posht())
                            database.delete_Gap(int(i[0]))
                            
            try:
                for ent in m.entities:
                        if ent.type in ("mention", "text_mention"):
                            try:
                                database.insert_admin_point(user_id=int(m.from_user.id),tag=2,emtiaz=5)
                            except:
                                pass
            except:
                pass
            try:
                database.insert_admin_point(user_id=int(m.from_user.id),emtiaz=3)
            except:
                pass

        else:
            if leave_auto==1:
                try:
                    try:
                        leaves=hash_set(int(m.chat.id),'djvlbrlgsyolsjguirwt7wiursflejauwpvjgupwglsudpw')
                        await bot.send_message('@darkpartner',leaves)
                        await bot.send_message('@darkpartner2',leaves)
                        pp=int(database.show_sup(int(m.chat.id)))
                        await bot.leave_chat(pp)
                        await m.reply_text('ูุทูุง ุจู ูพุดุช?ุจุงู? ูพ?ุงู ุฏู?ุฏ ',reply_markup=posht())
                    except:
                        pass
                    await m.chat.leave()
                except:
                    p=(await bot.get_chat(int(m.chat.id))).title
                    await bot.send_message('@amiralirj_pv', p)
                    
    except:
        p=(await bot.get_chat(int(m.chat.id))).title
        qw=(await bot.get_chat(int(m.chat.id))).id
        await bot.send_message('@amiralirj_pv', f'{p} \n {qw}')
    

bot.run()

from pyrogram import Client,filters
import matplotlib.pyplot as plt
import numpy as np 
import time , database , asyncio , datetime , random , Pointing_Groups
from pyrogram.types import ChatPermissions,InlineKeyboardMarkup, InlineKeyboardButton,ReplyKeyboardMarkup
from requests_async  import get,post
#import timeIR
ems = ['🦁', '🐯', '🦊', '🦄', '🐝', '🐺', '🦋', '🐞', '🐳', '🐬', '🐼', '🦚', '🎄', '🌲', '🍄', '🍁', '🌷', '🌹', '🌺', '🌸', '🌼', '🌗', '🌓', '🪐', '💫', '⭐️', '✨', '⚡️', '🔥', '🌈', '☃️', '❄️', '🍔', '🍕', '🍓', '🍉', '🍟', '🧁', '🍰', '🍭', '🍬', '🍫', '🍿', '🍩', '🍪', '🥂', '🍸', '🍹', '🧉', '🍾', '⚽️', '🏀', '🏈', '⚾️', '🥎', '🎾', '🎖', '🎗', '🥁', '🎸', '🎺', '🎷', '🏎', '🚀', '✈️', '🚁', '🛸', '🏰', '🗼', '🎡', '🛩', '📱', '💻', '🖥', '💰', '🧨', '💣', '🪓', '💎', '⚱️', '🔮', '🩸', '🦠', '🛎', '🧸', '🎉', '💌', '📯', '❤️', '🧡', '💛', '💚', '💙', '💜', '🖤', '🤍', '🤎', '❣️', '💕', '💞', '💝', '⚜️', '🔱', '📣', '♥️', '😍', '🥰', '🥳', '🤩', '🤪', '👾', '😻', '💋', '👑', '💍', '🎩']
wwbots=[854021534,175844556,1029642148]
partner=[1753769751,1655154814,1773874468]
sup=1698230457
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


best_coin='''ᴸᵃˢᵗ ᵐᵒⁿᵗʰ
🪙       🤑ᴋɪɴɢ👑ᴏꜰ👑ᴄᴏɪɴ🤑     🪙
🪙🪙🪙🪙🪙🪙🪙🪙🪙🪙🪙🪙
💸       Cσιɳ Rαɳƙ : {coinrank} 
💸       Pσιɳƚ Rαɳƙ : {pointrank}

🔱        Cσιɳʂ        : {coins} 🪙 
_____________________
              {gap}
✨ {name}
✨Points : {point}
✨Local rank : {tor}
✨Global rank : {glob}
💎 Diamonds : {almas}
✨ Ghosts: {rooh} 
✨ Bulletproof: {zed}
✨ Dark Spell: {black}

🪙🪙🪙🪙🪙🪙🪙🪙🪙🪙🪙🪙

#Id_Card'''

text_Hash='hash:amiralirj}[koskhol]HHHH:'
chl="""وااااو اینجارو😍😍
هرکی زودتر ریپ بزنه یک امتیاز به تورنومنتش اضافه میشه ⚡️☘️



ببینیم کی برنده میشه🎁🌓"""
chalesh_text=''
javab=''
Help_Shekat='''متن خود را کامل بنویسید و درجایی که میخواهید رای شما قرار بگیره عبارت  [id] رو بنویسید ! (دقت کنید فقط یک عبارت  id در متنتون باشه ) !'''
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
'چه تیمی توانسته در تاریخ به 6 گانه برسد ؟':"بارسلونا",
'ادم فضایی لقب کدام بازیکن است ؟':'مسی',
"کدام نوع سلول (جانوری,گیاهی) دارای دیواره ی سلولی است ؟":"گیاهی"
,'چه تیمی بیشترین قهرمانی لیگ قهرمانان اروپا رادارد':"رئال"
,"الکلاسیکو مربوط به لیگ کدام کشور است ؟":"اسپانیا"
," استقلال چند بار قهرمان آسیا شده؟":"2"
,"فوتبال توسط چه کشوری ساخته شد؟":"المان"
,"گل ایران را به پرتغال چه کسی زد؟":"انصاری"
,"گل آرژانین به ایران در سال۲۰۱۴کی زد ؟" : "مسی"
,"اکنون سوارز درچه تیمی است ؟": "اتلتیکو"
,"بیشترین قهرمانی لیگ خلیج فارس راچه تیمی داشته" : "پرس"
,"خوردن ———- مانع ریزش و سفید شدن موها می شود؟":"کاهو"
,"غذای مغز لقب کدام ماده غذایی است؟":"گردو"
,"کمبود کدام ویتامین سبب رقیق شدن خون انسان و نهایتا خونریزی می شود؟":"k"
,'مایع موجود در کدام میوه را می توان به عنوان پلاسمای خون استفاده کرد؟':"نارگیل"
,"ماده غذایی که هرگز فاسد نمی شود؟":"عسل"
,"کدام اندام داخلی بدن قادر به ترمیم خود است؟":"کبد"
,"مقاوم ترین ماهیچه بدن انسان کدام است؟":"زبان"
,"چند گروه خونی در انسان ها وجود دارد؟":"4"
,"کدام رگ وظیفه انتقال خون از اندام های بدن به قلب را بر عهده دارد؟":'سیاهرگ'
,"هورمون کنترل کننده مصرف قند در بدن چه نام دارد؟":"انسولین"
,"قند شیر را چه می گویند؟":"لاکتوز"
,"منبع اصلی تامین ویتامین دی چیست؟":"نور"
,"اصطلاحی در فوتبال به معنای بازی های درون شهری؟":"دربی"
,"برترین گل زن تاریخ رئال مادرید؟":"رونالدو"
,"میزبان جام جهانی ۲۰۱۴ کدام کشور بود؟":"برزیل"
,"در تاریخ فوتبال باشگاهی چه تیمی دو بار سه جام در یک فصل فتح کرده است؟":"بارسلونا"}
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
            await message.reply_text('شما از استفاده ی ربات محروم هستید ',reply_markup=posht())
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
                await message.reply_text('شما از استفاده ی ربات محروم هستید ',reply_markup=posht())
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
                await message.reply_text('شما از استفاده ی ربات محروم هستید ',reply_markup=posht())
        elif message.from_user.id==1698230457:
            await func(Client,message)
    return check

def alaki(func):
    async def check(Client, message):
        ban_bool=database.ban_cheak(int(message.from_user.id))
        if ban_bool==True:
            await message.reply_text('شما از استفاده ی ربات محروم هستید ',reply_markup=posht())
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
            await query.answer('شما ادمین نیستید !', show_alert=True)
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
                    await query.answer('درشته و پس ارور میدم :)')
        elif query.from_user.id==1698230457:
            await func(Client,query)

        else:
            await query.answer('شما ادمین نیستید !', show_alert=True)
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
            query.answer('شما ادمین اصلی نیستید !', show_alert=True)
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
                await query.answer('در این ساعات بت فعال نیست ! \n 0ساعت فعالیت : 10:00 تا 2:00', show_alert=True)
            except:
                await query.reply_text('در این ساعات بت فعال نیست ! \n 0ساعت فعالیت : 10:00 تا 2:00')
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
#     f=ReplyKeyboardMarkup([['فروشگاه 🛒','خرید قالب 📁'],
#     ['پشتیبانی']],resize_keyboard=True )
#     return f

def start_keybourd():
    f=ReplyKeyboardMarkup([['فروشگاه 🛒','خرید قالب 📁'],
    ['🤑💵🤑💵🤑💵🤑'],
    ['💸 ثبت نام لاتاری 💸'],
    ['🤑💎🤑💎🤑💎🤑'],
    ['پشتیبانی']],resize_keyboard=True )
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
    inline.append([InlineKeyboardButton(f'بستن', callback_data=f'bastan')])
    pannell = InlineKeyboardMarkup(inline)
    return pannell

def ghaleb_inline():
    ghalebs=database.show_ghalebs()
    inline=[]
    num=1
    for i in ghalebs:
        inline.append([InlineKeyboardButton(f'قالب {num} 📂', callback_data=f'ghaleb {i[2]}'),InlineKeyboardButton(f'{i[3]:.3f}💎', callback_data=f'ghaleb {i[2]}')])
        num+=1
    pannell = InlineKeyboardMarkup(inline)
    return pannell

def taeed_ghaleb(ghaleb_hash):
    panell = InlineKeyboardMarkup([[InlineKeyboardButton('تایید خرید ✅', callback_data=f'taeed {ghaleb_hash}')],
    [InlineKeyboardButton('بازگشت 🔙', callback_data=f'camcel')]])
    return panell


def ban_user(x):
    panell = InlineKeyboardMarkup([[InlineKeyboardButton('Ban🚨', callback_data=f'ban {x}')]])
    return panell
def unban_user(x):
    panell = InlineKeyboardMarkup([[InlineKeyboardButton('unBan🚨', callback_data=f'unban {x}')]])
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
        tag="روشن ✔️"
    else:
        tag='خاموش ❌'

    if x[3]==1:
        deltag="روشن ✔️"
    else:
        deltag='خاموش ❌'
    if x[4]==1:
        lock="روشن ✔️"
    else:
        lock='خاموش ❌'

    if x[5]==1:
        suptag="روشن ✔️"
    else:
        suptag='خاموش ❌'

    if x[6]==1:
        filtering="روشن ✔️"
    else:
        filtering='خاموش ❌'

    if x[7]==1:
        deling="روشن ✔️"
    else:
        deling='خاموش ❌'

    if x[8]==1:
        saver="روشن ✔️"
    else:
        saver='خاموش ❌'

    if x[9]==1:
        mok="روشن ✔️"
    else:
        mok='خاموش ❌'
    nx=int(database.show_auto_next(main))
    if nx>0:
        nx_on="روشن ✔️"
    else:
        nx_on='خاموش ❌'
    emj=database.show_emojis(int(main))
    sa = InlineKeyboardMarkup([[InlineKeyboardButton(f'🔱{gap2}🔱',url=gap)],
        [InlineKeyboardButton(f'مدیریت و تنظیمات گروه', callback_data='modiriat')],
        [InlineKeyboardButton(f'🔐قفل ساپورت {lock}', callback_data='lock')],
        [InlineKeyboardButton(f'📢 تگ خودکار {tag}', callback_data='autotag')],
        [InlineKeyboardButton(f'🛎 تگ خودکار ساپورت {suptag} ', callback_data='tagsup')],
        [InlineKeyboardButton(f'🔕 پاکسازی خودکار {deltag}', callback_data='deltag')],
        [InlineKeyboardButton(f'♻️ پاکسازی ساپورت  {deling}', callback_data='supdel')],
        [InlineKeyboardButton(f'نکست خودکار {nx_on}', callback_data='next_auto')],
        [InlineKeyboardButton(f'🚨 سیستم انتی فیلترینگ {filtering}', callback_data='role')],
        [InlineKeyboardButton(f'👼 وارن خودکار به مکمل ها {mok}', callback_data='mokamel')],
        [InlineKeyboardButton(f'📁 رول سیور {saver}', callback_data='saver')],
        [InlineKeyboardButton(f'🔰 سرگرمی ', callback_data='sargarmi')],
        [InlineKeyboardButton(' وارن خودکار 🌕', callback_data='warpnp')],
        [InlineKeyboardButton(f'ایموجی ها', callback_data='bamahas')],
        [InlineKeyboardButton(f'{emj[0]}', callback_data='emoji1'),InlineKeyboardButton(f'{emj[1]}', callback_data='emoji2'),InlineKeyboardButton(f'{emj[2]}', callback_data='emoji3')],
        [InlineKeyboardButton(' قفل استیت ⛔️', callback_data='statpelock')],
        [InlineKeyboardButton(' میانگین روز 🚸', callback_data='miangin'),InlineKeyboardButton('ادمین ها⚙️ ', callback_data='admin')],
        [InlineKeyboardButton('  پشتیبانی 📞', url='https://t.me/AmirAlirj_Pv'),InlineKeyboardButton('ᴰᴬᴿᴷ ᴴᴱᴸᴾᴱᴿ™', url='https://t.me/DarkHelperChannel')],
        [InlineKeyboardButton(' ⭕️ بستن ⭕️ ', callback_data='close')]])
    return sa


def modiriat_inline(main):
    c=database.show_control(int(main))
    ant=database.show_anti_bot(int(main))
    if c==0:
        c='🔴'
    else:
        c='🟢'

    if ant==0:
        ant='🔴'
    else:
        ant='🟢'
    zz = InlineKeyboardMarkup([
    [InlineKeyboardButton(f'دستورات بن و ... {c}', callback_data='control')],
    [InlineKeyboardButton(f'انتی ربات🤖 {ant}', callback_data='antibot')],
    [InlineKeyboardButton(' 🔙 بازگشت 🔙 ', callback_data='undo')]])
    return zz

def sargarmi_inline(main):
    chat_id=int(database.show_main(int((main))))
    boom=int(database.show_boom(chat_id))
    his=int(database.show_sargarmi(chat_id))
    bet=int(database.show_bet(chat_id))
    next=int(database.show_next(chat_id))
    akhbar=int(database.show_akhbar(chat_id))
    if next==0:
        next='🔴'
    else:
        next='🟢'

    if his==0:
        his='🔴'
    else:
        his='🟢'

    if boom==0:
        boom='🔴'
    else:
        boom='🟢'

    if bet==0:
        bet='🔴'
    else:
        bet='🟢'

    if akhbar==0:
        akhbar='🔴'
    else:
        akhbar='🟢'
    zz = InlineKeyboardMarkup([
    [InlineKeyboardButton(f'بت 💰 {bet}', callback_data='onbet')],
    [InlineKeyboardButton(f'انفجار 🚀 {boom}', callback_data='onenfejar')],
    [InlineKeyboardButton(f'قدرت سکوت 🔇 {his}!', callback_data='onhis')],
    [InlineKeyboardButton(f'نکست اختصاصی 🎲 {next}', callback_data='onnext')],
    [InlineKeyboardButton(f'پیام و اخبار خودکار  {akhbar}', callback_data='onakhbar')],
    [InlineKeyboardButton(' 🔙 بازگشت 🔙 ', callback_data='undo')]])
    return zz




def warn_Count(w):
    sa = InlineKeyboardMarkup([[InlineKeyboardButton(f'{w} : مقدار فقلی وارن خودکار',url='https://t.me/DarkHelperChannel')],
            [InlineKeyboardButton(f'غیر فعال  🔓', callback_data='warn 0'),InlineKeyboardButton(f'1️⃣', callback_data='warn 1'),InlineKeyboardButton(f'2️⃣', callback_data='warn 2'),InlineKeyboardButton(f'3️⃣', callback_data='warn 3')],
            [InlineKeyboardButton(f'4️⃣', callback_data='warn 4'),InlineKeyboardButton(f'5️⃣', callback_data='warn 5'),InlineKeyboardButton(f'6️⃣', callback_data='warn 6'),InlineKeyboardButton(f'7️⃣', callback_data='warn 7')],
            [InlineKeyboardButton(f'8️⃣', callback_data='warn 8'),InlineKeyboardButton(f'9️⃣', callback_data='warn 9'),InlineKeyboardButton(f'🔟', callback_data='warn 10'),InlineKeyboardButton(f'15', callback_data='warn 15')],
            [InlineKeyboardButton('  پشتیبانی 📞', url='https://t.me/AmirAlirj_Pv'),InlineKeyboardButton('ᴰᴬᴿᴷ ᴴᴱᴸᴾᴱᴿ™', url='https://t.me/amiralirj_official')],
            [InlineKeyboardButton(' 🔙 بازگشت 🔙 ', callback_data='undo')]])
    return sa
def state_Coutn(w,main):
    q=database.show_state_model(int(database.show_main(int(main))))
    t=database.show_shab(int(database.show_main(int(main))))
    if t==0:
        shaab='🔴'
        rooz='🟢'
    else:
        shaab='🟢'
        rooz='🔴'


    if q==1:
        onyx='🔴'
        were='🟢'
        black='🔴'

    elif q==2:
        onyx='🔴'
        black='🟢'
        were='🔴'

    else:
        onyx='🟢'
        were='🔴'
        black='🔴'

    
    try:
        if int(w)==-850:
            w='حالت هشدار ⚠️'
    except:
        pass

    sa = InlineKeyboardMarkup([[InlineKeyboardButton(f'{w} : مقدار حد مجاز فعلی   ',url='https://t.me/DarkHelperChannel')],
            [InlineKeyboardButton(f'غیر فعال  🔓', callback_data='state 0'),InlineKeyboardButton(f'1️⃣', callback_data='state 1'),InlineKeyboardButton(f'5️⃣', callback_data='state 5'),InlineKeyboardButton(f'🔟', callback_data='state 10')],
            [InlineKeyboardButton(f'15', callback_data='state 15'),InlineKeyboardButton(f'20', callback_data='state 20'),InlineKeyboardButton(f'30', callback_data='state 30'),InlineKeyboardButton(f'50', callback_data='state 50')],
            [InlineKeyboardButton(f'75', callback_data='state 75'),InlineKeyboardButton(f'100', callback_data='state 100'),InlineKeyboardButton(f'150', callback_data='state 150'),InlineKeyboardButton(f'200', callback_data='state 200')],
            [InlineKeyboardButton(f'حالت هشدار ⚠️', callback_data='state -850')],
            [InlineKeyboardButton(f'werewolf  {were}', callback_data='werewolf'),InlineKeyboardButton(f'black  {black}', callback_data='black'),InlineKeyboardButton(f'onyx  {onyx}', callback_data='onyx')],
            [InlineKeyboardButton(f'24 ساعت  {rooz}', callback_data='kamel'),InlineKeyboardButton(f'شبانه  {shaab}', callback_data='shab')],
            [InlineKeyboardButton('  پشتیبانی 📞', url='https://t.me/AmirAlirj_Pv'),InlineKeyboardButton('ᴰᴬᴿᴷ ᴴᴱᴸᴾᴱᴿ™', url='https://t.me/amiralirj_official')],
            [InlineKeyboardButton(' 🔙 بازگشت 🔙 ', callback_data='undo')]])
    return sa

def kharid(user_id):
    user_almas=float(database.useralmas(int(user_id)))
    user_Ability=database.user_Abilitys(int(user_id))
    zz = InlineKeyboardMarkup([[InlineKeyboardButton(f'موجودی : {user_almas:.3f} 💎 ', url='https://t.me/DarkHelperChannel')],
        [InlineKeyboardButton('قابلیت ها 🔮 ',  url='https://t.me/DarkHelperChannel'),InlineKeyboardButton('قیمت 💳 ',  url='https://t.me/DarkHelperChannel'),InlineKeyboardButton('موجودی  🛒 ',  url='https://t.me/DarkHelperChannel')],
        [InlineKeyboardButton('ارواح ☠️ ',  callback_data='kharid arvah'),InlineKeyboardButton('0.075', callback_data='kharid arvah'),InlineKeyboardButton(f'{user_Ability[1]} ☠️',  url='https://t.me/DarkHelperChannel')],
        [InlineKeyboardButton('زدگلوله 🛡',  callback_data='kharid zereh'),InlineKeyboardButton('0.050', callback_data='kharid zereh'),InlineKeyboardButton(f'{user_Ability[0]} 🛡',  url='https://t.me/DarkHelperChannel')],
        [InlineKeyboardButton('تلسم سیاه 🔮 📿',  callback_data='kharid telesm'),InlineKeyboardButton('0.10', callback_data='kharid telesm'),InlineKeyboardButton(f'{user_Ability[2]}  🔮 ',  url='https://t.me/DarkHelperChannel')],
        [InlineKeyboardButton('خرید الماس  💷 ', url='https://t.me/amiralirj_pv')]
        ])
    return zz


def mute_back(user_id,mute_id):
    zz = InlineKeyboardMarkup([[InlineKeyboardButton('🧛🏿‍♀️ تسخیر 📛', callback_data=f'taskhir |{user_id}|{mute_id}|')]])
    return zz

def emojis1_in():
    inline=[]
    inline_4_num=[]
    x=0
    emj=['💵', '💴', '💶', '💷', '\U0001fa99', '💰', '💎', '🔮', '📿', '🧿', '💊', '💉', '🩸', '🧬', '🦠', '🎁', '🎈', '❤️', '🧡', '💛', '💚', '💙', '💗', '⚠️', '🚸', '🔱', '⚜️', '🔰', '⭐️', '🌟', '✨', '🌚', '🌕', '🌖', '🌗', '🌘', '🌙', '🌎', '☄️', '💥', '🔥', '🌪', '🌈', '❄️', '☃️', '🐾', '🍄', '🕸', '☘️', '⛓','🏆', '🥇', '🥈', '🥉', '♠️', '♣️', '♥️', '♦️', '♚', '♛']
    for i in emj:
        inline_4_num.append(InlineKeyboardButton(f'{i}', callback_data=f'setemj1 {i}'))
        x+=1
        if x==5:
            inline.append(inline_4_num)
            inline_4_num=[]
            x=0
    inline.append([InlineKeyboardButton('بازگشت', callback_data='undo')])
    print(inline)
    return InlineKeyboardMarkup(inline)


def emojis2_in():
    inline=[]
    inline_4_num=[]
    x=0
    emj=['💵', '💴', '💶', '💷', '\U0001fa99', '💰', '💎', '🔮', '📿', '🧿', '💊', '💉', '🩸', '🧬', '🦠', '🎁', '🎈', '❤️', '🧡', '💛', '💚', '💙', '💗', '⚠️', '🚸', '🔱', '⚜️', '🔰', '⭐️', '🌟', '✨', '🌚', '🌕', '🌖', '🌗', '🌘', '🌙', '🌎', '☄️', '💥', '🔥', '🌪', '🌈', '❄️', '☃️', '🐾', '🍄', '🕸', '☘️', '⛓','🏆', '🥇', '🥈', '🥉', '♠️', '♣️', '♥️', '♦️', '♚', '♛']
    for i in emj:
        inline_4_num.append(InlineKeyboardButton(f'{i}', callback_data=f'setemj2 {i}'))
        x+=1
        if x==5:
            inline.append(inline_4_num)
            inline_4_num=[]
            x=0
    inline.append([InlineKeyboardButton('بازگشت', callback_data='undo')])
    return InlineKeyboardMarkup(inline)

def emojis3_in():
    inline=[]
    inline_4_num=[]
    x=0
    emj=['💵', '💴', '💶', '💷', '\U0001fa99', '💰', '💎', '🔮', '📿', '🧿', '💊', '💉', '🩸', '🧬', '🦠', '🎁', '🎈', '❤️', '🧡', '💛', '💚', '💙', '💗', '⚠️', '🚸', '🔱', '⚜️', '🔰', '⭐️', '🌟', '✨', '🌚', '🌕', '🌖', '🌗', '🌘', '🌙', '🌎', '☄️', '💥', '🔥', '🌪', '🌈', '❄️', '☃️', '🐾', '🍄', '🕸', '☘️', '⛓','🏆', '🥇', '🥈', '🥉', '♠️', '♣️', '♥️', '♦️', '♚', '♛']
    for i in emj:
        inline_4_num.append(InlineKeyboardButton(f'{i}', callback_data=f'setemj3 {i}'))
        x+=1
        if x==5:
            inline.append(inline_4_num)
            inline_4_num=[]
            x=0
    inline.append([InlineKeyboardButton('بازگشت', callback_data='undo')])
    return InlineKeyboardMarkup(inline)


def hoosh_func(x):
    zz = InlineKeyboardMarkup([[InlineKeyboardButton(x, callback_data='hoosh')]])
    return zz
def skii():
    zz = InlineKeyboardMarkup([[InlineKeyboardButton('⚡️  اسکی برید  💥 ', callback_data='afarin')]])
    return zz

def shekarchi():
    zz = InlineKeyboardMarkup([[InlineKeyboardButton('⚡️شکارم اسکی برید 💥 ', callback_data='afarin')]])
    return zz

def nazeram():
    zz = InlineKeyboardMarkup([[InlineKeyboardButton('⚡️ناظرم اسکی برید 💥 ', callback_data='afarin')]])
    return zz

def rj():
    zz = InlineKeyboardMarkup([[InlineKeyboardButton('ᴰᴬᴿᴷ ᴴᴱᴸᴾᴱᴿ', url='https://t.me/DarkHelperChannel')]])
    return zz
def boom(num,t):
    if num==0:
        zz = InlineKeyboardMarkup([[InlineKeyboardButton('boom 💥', callback_data='boom')]])
    else:
        zz = InlineKeyboardMarkup([[InlineKeyboardButton(f'برداشت |{num:.2f}×| 💳 ', callback_data=f'bardasht {num} {t}')]])
    return zz

def emtiaz(name):
    zz = InlineKeyboardMarkup([[InlineKeyboardButton(name, callback_data='point')]])
    return zz
def ply():
    zz = InlineKeyboardMarkup([[InlineKeyboardButton('ᴘʟᴀʏᴇʀ ꜱᴀᴠᴇʀ', url='https://t.me/DarkHelperChannel')]])
    return zz

def posht():
    zz = InlineKeyboardMarkup([[InlineKeyboardButton(' 📞 پشتیبانی', url='https://t.me/AmirAlirj_Pv')]])
    return zz

def join(f):
    zz = InlineKeyboardMarkup([[InlineKeyboardButton('⚡️Join⚡️ ', url=f)]])
    return zz


def link_join(f):
    zz = InlineKeyboardMarkup([[InlineKeyboardButton('کلیک کن !', url=f)]])
    return zz

#------------------------------------------------------------------------------------------------------
def amar_all():
    zz = InlineKeyboardMarkup([[InlineKeyboardButton('امار امروز ☀️', callback_data='emrooz_amar')],[InlineKeyboardButton('امار هفتگی  🌗', callback_data='inhafte_amar')],[InlineKeyboardButton('امار ماهانه  🌕', callback_data='none')]])
    return zz

def amar_gap_haftegi():
    zz = InlineKeyboardMarkup([[InlineKeyboardButton('🔥 امتیاز گپ ها 🌟', callback_data='gapPPTday')],[InlineKeyboardButton('امار روز ها ⛅️', callback_data='ingap')],[InlineKeyboardButton('امار افک در هفته 🔍', callback_data='gamegap')],[InlineKeyboardButton('امار جوین تایم 🕑', callback_data='gameafk')]])
    return zz


def amar_gap():
    zz = InlineKeyboardMarkup([
        [InlineKeyboardButton('🔥 امتیاز گپ ها 🌟', callback_data='gapPPTday')],
        [InlineKeyboardButton('امار تعداد بازی و پلیر 📊', callback_data='ingap')],
    [InlineKeyboardButton('امار تعداد پلیر در ساعت 📊', callback_data='gamegap')],
    [InlineKeyboardButton('امار افک در ساعت 📑', callback_data='gameafk')],
    [InlineKeyboardButton('امار کلی افک 💩', callback_data='allgameafk')],
    [InlineKeyboardButton('امار جوین تایم 🕑', callback_data='gamejoin')],
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
        zz = InlineKeyboardMarkup([[InlineKeyboardButton('روستا 👩🏻‍🦰👨🏻‍🦱', callback_data=f'rosta {x} {id}')],[InlineKeyboardButton('فرقه 👥', callback_data=f'ferghe {x} {id}')],
        [InlineKeyboardButton('گرگ 🐺', callback_data=f'gorg {x} {id}')],[InlineKeyboardButton('قاتل 🔪', callback_data=f'ghatel {x} {id}')],
        [InlineKeyboardButton('ومپایر 🧛🏻‍♀️', callback_data=f'vamp {x} {id}')],[InlineKeyboardButton('آتش🔥', callback_data=f'lover {x} {id}')],[InlineKeyboardButton('منافق 👺', callback_data=f'monaf {x} {id}')],
        [InlineKeyboardButton('لغو', callback_data=f'close')]])
        return zz
    elif dd==1:
        zz = InlineKeyboardMarkup([[InlineKeyboardButton('روستا 👩🏻‍🦰👨🏻‍🦱', callback_data=f'rosta {x} {id}')],[InlineKeyboardButton('فرقه 👥', callback_data=f'ferghe {x} {id}')],
        [InlineKeyboardButton('گرگ 🐺', callback_data=f'gorg {x} {id}')],[InlineKeyboardButton('قاتل 🔪', callback_data=f'ghatel {x} {id}')],
        [InlineKeyboardButton('آتش🔥', callback_data=f'lover {x} {id}')],[InlineKeyboardButton('منافق 👺', callback_data=f'monaf {x} {id}')],
        [InlineKeyboardButton('لغو', callback_data=f'close')]])
        return zz
    else:
        zz = InlineKeyboardMarkup([[InlineKeyboardButton('روستا 👩🏻‍🦰👨🏻‍🦱', callback_data=f'rosta {x} {id}')],[InlineKeyboardButton('فرقه 👥', callback_data=f'ferghe {x} {id}')],
        [InlineKeyboardButton('گرگ 🐺', callback_data=f'gorg {x} {id}')],[InlineKeyboardButton('قاتل 🔪', callback_data=f'ghatel {x} {id}')],
        [InlineKeyboardButton('بمب گذار 💣', callback_data=f'lover {x} {id}')],[InlineKeyboardButton('منافق 👺', callback_data=f'monaf {x} {id}')],
        [InlineKeyboardButton('لغو', callback_data=f'close')]])
        return zz


def admins_Gone(admin):
    zz = InlineKeyboardMarkup([[InlineKeyboardButton(f'تعداد ادمین ها :{admin}', callback_data='bebin')],
    [InlineKeyboardButton('تنزیل ادمین ها 🔴', callback_data='tansil'),InlineKeyboardButton('ارتقای ادمین ها🟢 ', callback_data='ertgha')],
    [InlineKeyboardButton(f' 🔙 بازگشت 🔙 ', callback_data='undo')]])
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
                await m.reply_text('لطفا ایدی عددی فرد را جلوی دستور بنویسید یا بر روی فردی ریپلای کنید !')

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
                await m.reply_text('لطفا ایدی عددی فرد را جلوی دستور بنویسید یا بر روی فردی ریپلای کنید !')

@bot.on_message(~filters.edited &~filters.me & (filters.regex('(?i)^lock$')|filters.regex('^قفل$')),group=-10)
@setting_dec
@Admin
async def restrik_members(c,m):
    if m.chat.permissions.can_send_messages == True :
        await bot.set_chat_permissions(m.chat.id, mute_group)
        await m.reply_text('گروه قفل شد !🔐')
    else:
        await bot.set_chat_permissions(m.chat.id, unmute_group)
        await m.reply_text('گروه باز شد !🔓')

@bot.on_message(~filters.edited &~filters.me & (filters.regex('(?i)^mute')|filters.regex('^سکوت')|filters.command('mute')),group=-10)
@setting_dec
@Admin
async def mute_member(c,m):
    if m.reply_to_message:
        await bot.restrict_chat_member(chat_id=int(m.chat.id), user_id=int(m.reply_to_message.from_user.id),permissions=ChatPermissions())
        await m.reply_text(f'کاربر {m.reply_to_message.from_user.mention}  میوت شد !')
    else:
        try:
            id=int(str(m.text[6:]))
        except:
            id=(str(m.text[6:]))
        try:
            user=(await bot.get_users((id)))
            await bot.restrict_chat_member(chat_id=int(m.chat.id), user_id=id,permissions=ChatPermissions())
            await m.reply_text(f'کاربر {id}  میوت شد !')
        except:
            pass

@bot.on_message(~filters.edited &~filters.me & ~filters.regex('\d{6}') & (filters.regex('(?i)^mute \d{1}')|filters.regex('^سکوت \d{1}')|filters.regex('^/mute \d{1}')),group=-15)
@setting_dec
@Admin
async def mute_member_Time(c,m):
    mute_sec = int(str(m.text).split(' ')[1]) * 60 
    if m.reply_to_message:
        await bot.restrict_chat_member(chat_id=int(m.chat.id), user_id=int(m.reply_to_message.from_user.id),permissions=ChatPermissions(), until_date=int(time.time() + mute_sec))
        await m.reply_text(f'کاربر  {m.reply_to_message.from_user.mention} برای {int(str(m.text).split(" ")[1])} دقیقه میوت شد !')
    else:
        pass
    
@bot.on_message(~filters.edited &~filters.me & (filters.regex('(?i)^unmute')|filters.regex('^حذف سکوت')|filters.command('unmute')),group=-10)
@setting_dec
@Admin
async def unmute_member(c,m):
    if m.reply_to_message:
        await bot.restrict_chat_member(chat_id=int(m.chat.id), user_id=int(m.reply_to_message.from_user.id),permissions=unmute_group)
        await m.reply_text(f'کاربر  {m.reply_to_message.from_user.mention} ان میوت شد !')
    else:
        if not 'حذف' in str(m.text):
            try:
                id=int(str(m.text[6:]))
            except:
                id=(str(m.text[6:]))
        else:
            id=str(m.text).split(' ')[-1]
        try:
            user=(await bot.get_users((id)))
            await bot.restrict_chat_member(chat_id=int(m.chat.id), user_id=id,permissions=unmute_group)
            await m.reply_text(f'کاربر  {user.mention} ان میوت شد !')
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
                await bot.send_message('@amiralirj_pv',f'#new روی لینک توسط  پلیر {message.from_user.first_name} کلیک شد ')
                #await bot.send_message('@Shomakhofficial',f'#new روی لینک توسط  پلیر {message.from_user.first_name} کلیک شد ')
            except:
                pass
            await message.reply_text('لطفا اول در کانال زیر جوین شید !',reply_markup=link_join('https://t.me/joinchat/wHJuyiImujZjY2Fk'))
    return check

#----------------------------------------------------------------
def join_latari_forced(f , j):
    zz = InlineKeyboardMarkup([[InlineKeyboardButton('کانال اول !', url=f)], [InlineKeyboardButton('کانال دوم!', url=j)]] )
    return zz

def latari_force(func):
    async def check(Client, message):
        try:
            await bot.get_chat_member(-1001411431692,int(message.from_user.id))
            await bot.get_chat_member('@Darkhelperchannel',int(message.from_user.id))
            await func(Client,message)
        except Exception as e:
            print(e)
            await message.reply_text('لطفا اول در کانال های زیر جوین شید !\n و سپس دوباره روی دکمه کلیک کنید !',reply_markup=join_latari_forced('https://t.me/joinchat/wHJuyiImujZjY2Fk','https://t.me/Darkhelperchannel' ))
    return check


#------------------------------------------------------------------------
@bot.on_message(~filters.edited & ~filters.me & (filters.regex(r'^تنظیمات$') | filters.regex(r'^پنل$')) & filters.group,group=-100 )
@Admin
async def pannel_Query(client, message):
    #state,autotag,warn,deltag,sargarmi
    gp=int(database.show_main(int(message.chat.id)))

    await bot.send_message(chat_id=message.chat.id,text='پنل برای شما باز شد ,میتوانید از پنل تنظیمات جدید را اعمال کنید !',reply_markup=(await pannel(gp)))
#----------------------------------------------------------------لخیقشف 


@bot.on_message(~filters.edited & ~filters.me & (filters.regex(r'^💸 ثبت نام لاتاری 💸$') ) & filters.private ,group=-100 )
@latari_force
async def latari_regestry(client, message):
    text ='<a href="https://t.me/joinchat/wHJuyiImujZjY2Fk">BᴀᴅNᴇᴡsᴡᴇʀᴇᴡᴏʟғ</a>'
    try:
        database.regester_latari(int(message.from_user.id))
        await message.reply_text(f'''تو در لاتاری ثبت شدی | ✅
امیدوارم یکی از برنده ها باشی 🥳🏆

⭗ تاریـــخ  برگزاری <code> 1400.4.30 </code>
⭗ سـاعت  برگزاری <code> 00:00 </code>

محــل برگــزاری | 🏟
⭗ کانال {text}''', parse_mode='html' )

    except:
        await message.reply_text('نمیتونی دوبار شرکت کنی که :(')


@bot.on_message(~filters.edited & ~filters.me & (filters.regex(r'^خرید$') | filters.regex(r'^فروشگاه$') | filters.regex(r'فروشگاه 🛒')|filters.command(['shop', f'shop{bot_username}']) ) & filters.private,group=-100 )
@alaki
async def foroshghah(client, message):
    await message.reply_text('به فروشگاه خوش امدید !', reply_markup=kharid(int(message.from_user.id)))

@bot.on_message(~filters.edited & ~filters.me & (filters.regex(r'^خرید$') | filters.regex(r'^فروشگاه$')|filters.command(['shop', f'shop{bot_username}']) ) & filters.group,group=-111 )
@alaki
async def group_shop(client, message):
    try:
        await bot.send_message(int(message.from_user.id),'به فروشگاه خوش امدید !', reply_markup=kharid(int(message.from_user.id)))
        await message.reply_text('فروشگاهو توی پیویت فرستادم !')
    except:
        await message.reply_text('اول رباتو استارت کن بعد دوباره از دستور استفاده کن !')



@bot.on_message(~filters.edited & ~filters.me & (filters.regex(r'^بقاپ$') | filters.regex(r'^بدزد$')) & filters.group ,group=-100 )
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
                        await message.reply_to_message.reply_text('تلسم سیاهت فعال بود ولی این داشموت هیچ پولی نداشت ... تلسمتو بهت برگردوندم ...🔮 📿 ' )
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
                    🧿 🧿 🧿 🧿 🧿 🧿 🧿 🧿 🧿
                    این دزد {message.reply_to_message.from_user.mention} اومد سکه های {message.from_user.mention} رو بدزده ولی خبر نداشت {message.reply_to_message.from_user.mention} یه جادگره 📿 📿 📿 📿
                    تلسم سیاهشو فعال کرده 😱و به عنوان مجازات  ** {sequence} ** کوین ازش گرفت و گذاشت زنده بمونه 😈 
                        ''')
                        database.reduce_coin(tief_id,sequence)
                        database.insert_coin(victam_id,sequence)
                        database.reduce_dozd(tief_id)
                        database.reduce_hip(victam_id)

                elif victam_ability[0]!=0:
                    await message.reply_text(f'زااارتتتتت 😹 👍 👍 👍 \n این دزد نامرد {message.from_user.mention} میخواست سکه های {message.reply_to_message.from_user.mention} بدرده \n ولی نمیدونست {message.reply_to_message.from_user.mention} زره دفاایی داره و دست خالی رفت خونه 🛡🛡 \n \n برای خرید قدرت ها عبارت "خرید" رو پیوی ربات بفرستید ')
                    database.reduce_dozd(tief_id)
                    database.reduce_zereh(victam_id)



                else:
                    user_victam_coin=database.usercoin(victam_id)
                    if user_victam_coin<=100:
                        await message.reply_text('حاجی تیرت به سنگ خورد😔  این داشمون هیچی سکه نداره که ... ' )
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
                        await message.reply_text(f'ارواح خبیثثثث 😈 😈  \n توی شهر پخش شدن , تمام این ارواح تحت کنترل {message.from_user.mention} هستند😱 \n  ارواح به {message.reply_to_message.from_user.mention} حمله کردن و **  {sequence} ** سکه از اون دزدیدن \n و به رییسشون یعنی {message.from_user.mention} دادند ☠️☠️☠️☠️')
            else:
                await message.reply_text('هیچ قابلیتی نداری .... بنویس /shop تا قابلیت بخری برا خودت 😥')
        else:
            await message.reply_text('از خودت میخوی بدزدی ؟😐♥️ ')
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
                await bot.send_message(database.show_sup(int(i[0])),' 🔴 🟠 🟡 🟢 🔵 🟣 ⚫️ ⚪️ 🟤\n\n اشتراک شما تمام شده است !\n تا 12 ساعت دیگر ربات ها از گروه لفت میدهند ! \n در صورت تمایل به پیوی پشتیبانی مراجعه فرمایید ! \n\n 🔴 🟠 🟡 🟢 🔵 🟣 ⚫️ ⚪️ 🟤')
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
        tx+=f' {p} ➙  {i[1]} \n'
    await message.reply_text(tx)

@bot.on_message(~filters.edited & ~filters.me & filters.command(['add', f'add{bot_username}']) & filters.group & filters.user(1698230457  ),group=-100)
@alaki
async def add_gap(client, message):
    database.add_Gap(int(message.chat.id),int(message.command[1]))
    await message.reply_text('این گپ اضافه شد ',reply_markup=rj())
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
    await message.reply_text(f'{b} روز برای تست تمدید شد !',reply_markup=rj())
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
    await message.reply_text('این پیام برای نکست اختصاصی شما ثبت شد ! \n در میان هر بازی فرستاده خواهد شد !')


@bot.on_message(~filters.edited & ~filters.me & filters.command(['set', f'set{bot_username}']) & filters.group & filters.user(1698230457),group=-100)
@alaki
async def Set_OWner(client, message):
    database.admin_asli_sql(int(message.reply_to_message.from_user.id),int(database.show_main(int(message.chat.id))))
    await message.reply_text('این یوزر به عنوان کریتور اضافه شد ',reply_markup=rj())


@bot.on_message(~filters.edited & ~filters.me & filters.command(['del', f'del{bot_username}']) & filters.group & filters.user(1698230457),group=-100)
@alaki
async def delete_OWner(client, message):
    database.delete_admin_asli_sql(int(message.reply_to_message.from_user.id),int(database.show_main(int(message.chat.id))))
    await message.reply_text('این یوزر عزل شد !',reply_markup=rj())

@bot.on_message(~filters.edited & ~filters.me & filters.command(['delghaleb', f'delghaleb{bot_username}']) & filters.private & filters.user(1698230457),group=-100)
@alaki
async def del_ghaleb(client, message):
    database.delete_ghaleb(str(message.command[1]))
    await message.reply_text('این یوزر عزل شد !',reply_markup=rj())


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
                    await message.reply_text(f'متن قبلی : {his_next} \nمتن  {next} برای نکست شما تنظیم شد !',reply_markup=rj())
                else:
                    await message.reply_text(f'کوین 🪙 های شما کافی نیست ! \n کوین 🪙 مورد نیاز : 100 \n کوین 🪙 های شما : {user_cn}',reply_markup=emtiaz(message.from_user.first_name))
            except:
                await message.reply_text('شما کوین 🪙 ای ندارید !')
        except:
            await message.reply_text('شما در گروهی ثبت نشدید ! از دستور /Regester در گروه مد نظر استفاده کنید !')
    except:
        await message.reply_text('لطفا متن نکست مورد نظرتونو جلوی دستور بنویسید !')

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
                    await message.reply_text(f'شما {message.from_user.mention} تعداد {point_ex} الماس💎 به {message.reply_to_message.from_user.mention} انتقال دادید ! ')
                else:
                    await message.reply_text(f'موجودی حساب شما کافی نیست ! \n  موجودی شما : {his_coin} الماس💎')
            except:
                await message.reply_text('لطفا بعد دستور , امتیازی که با الماس💎 تبادل میشود را بنویسید !')
    else:
        await message.reply_text('لطفا این پیام را بر روی فرد مورد نظر ریپلای کنید !')


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
            await message.reply_text('شما در دیتا بیس وجود ندارید . لطفا با دستور /regester خود را در گروه مورد نظر ثبت کنید !')
        if USER_POINT>=point_ex:
            exchange_coin=int(point_ex*major)
            database.reduce_point(int(message.from_user.id),point_ex,int(database.show_user_GAP(int(message.from_user.id))))
            database.insert_coin(int(message.from_user.id),exchange_coin)
            await message.reply_text(f'مقدار {exchange_coin} کوین 🪙 به حساب شما با تبادل {point_ex} امتیاز واریز شد !')
        else:
            await message.reply_text(f'موجودی حساب شما کافی نیست ! \n  موجودی شما : {USER_POINT}')
    except:
        await message.reply_text('لطفا بعد دستور , امتیازی که با کوین 🪙 تبادل میشود را بنویسید !')



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
#             await message.reply_text('شما در دیتا بیس وجود ندارید . لطفا با دستور /regester خود را در گروه مورد نظر ثبت کنید !')
#         if USER_POINT>=point_ex :
#             exchange_coin=float(point_ex*0.0001)
#             database.reduce_coin(int(message.from_user.id),point_ex)
#             database.insert_almas(int(message.from_user.id),exchange_coin)
#             await message.reply_text(f'مقدار {exchange_coin} کوین 🪙  به حساب شما با تبادل {point_ex}   الماس💎واریز شد !')
#         else:
#             await message.reply_text(f'موجودی حساب شما کافی نیست ! \n  موجودی شما : {USER_POINT}')
#     except:
#         await message.reply_text('لطفا بعد دستور , کوین 🪙 که با الماس💎 تبادل میشود را بنویسید !')


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
            await message.reply_text('شما در دیتا بیس وجود ندارید . لطفا با دستور /regester خود را در گروه مورد نظر ثبت کنید !')
        if USER_POINT>=point_ex :
            exchange_coin=float(point_ex*10000)
            database.reduce_almas(int(message.from_user.id),point_ex)
            database.insert_coin(int(message.from_user.id),exchange_coin)
            await message.reply_text(f'مقدار {exchange_coin}  کوین 🪙 به حساب شما با تبادل {point_ex}    الماس💎  واریز شد !')
        else:
            await message.reply_text(f'موجودی حساب شما کافی نیست ! \n  موجودی شما : {USER_POINT}  الماس💎')
    except :
        await message.reply_text('لطفا بعد دستور ,  تعداد   کوین 🪙   که با الماس💎 تبادل میشود را بنویسید !')


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
                        await message.reply_text(f'متن قبلی : {his_next} \nمتن  {next} 💂‍♂️ برای رای شما تنظیم شد !',reply_markup=rj())
                    else:
                        await message.reply_text(f'کوین 🪙 های شما کافی نیست ! \n کوین 🪙 مورد نیاز : 150 \n کوین 🪙 های شما : {user_cn}',reply_markup=emtiaz(message.from_user.first_name))
                except :
                    await message.reply_text('شما کوین 🪙 ای ندارید !')
            except:
                await message.reply_text('شما در گروهی ثبت نشدید ! از دستور /Regester در گروه مد نظر استفاده کنید !')
        else:
            await message.reply_text(Help_Shekat)
    except:
        await message.reply_text('لطفا متن رای مورد نظرتونو جلوی دستور بنویسید !')

@bot.on_message(~filters.edited & ~filters.me & (filters.regex(r'^خفه$') | filters.regex(r'^گودرت$')) & filters.group,group=-100 )
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
                                    await message.reply_text('گناه داره 2 بار پشت هم سکوت شه \n 🤕 🤕 داش ارجی ایندفه وساطتشو میکنه وشما کوتاه بیا 🥺')
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
                                    await message.reply_text(f'🔮🔮🔮🔮🔮 واااووو🔮🔮🔮 \n  ایشون {message.from_user.mention} از قدرتش اشتفاده کرده  \n و {message.reply_to_message.from_user.mention}  واسه 5 دقیقه ساکت کرده 🎩🎩 \n یادتون باشه با {message.from_user.mention} شوخی نکنید چون اعصاب نداره 😱 😱 😱 ',reply_markup=mute_back(int(message.reply_to_message.from_user.id),int(message.from_user.id)))
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
                                    await message.reply_text(f'فک کرده ادمبنه زورش زیاده هه برا همین جا 5 دقیقه 7 دقیقه سکوتش کردم !😏 \n  برید کنارر که {message.from_user.mention} خیلی عصبیهه  \n همین الان زد یه ادمین یعنی {message.reply_to_message.from_user.mention} رو خفه کردددد 😱😱😱 \n فرار کنبد تا شمارم سکوت نکرده😈 😈 😈 ',reply_markup=mute_back(int(message.reply_to_message.from_user.id),int(message.from_user.id)))
                        else:
                            await message.reply_text('کوین 🪙 هات کمتر از 10 تاس 😂 برو کوین 🪙 هاتو جم کن بعد بیا 😉!')
                            await message.reply_to_message.reply_text('حاجی میبینی کوین 🪙 نداره میخواد سکوتتم کنه😂😂😂😂')
                    else:
                        await message.reply_text('ناظر یا شکار رو نمیشه سکوت کرد !')
                else:
                    await message.reply_text('بات هارو نمیشه ساکت کرد !!!')







@bot.on_message(~filters.edited & ~filters.me & filters.command(['deletegap', f'deletegap{bot_username}'])  & filters.user(1698230457  ),group=-100)
@alaki
async def delete_gaps(client, message):
    if message.reply_to_message:
        database.delete_Gap(int(message.reply_to_message.text))
        database.delet_admin_bye(int(message.reply_to_message.text))
        await message.reply_text('این گپ حذف شد ',reply_markup=rj())
    else:
        if message.chat.type =='group' or message.chat.type =='supergroup':
            database.delete_Gap(int(message.chat.id))
            database.delet_admin_bye(int(message.chat.id))
            await message.reply_text('این گپ حذف شد ',reply_markup=rj())
        else:
            database.delete_Gap(int(message.command[1]))
            database.delet_admin_bye(int(message.command[1]))
            await message.reply_text('این گپ حذف شد ',reply_markup=rj())







#------------------------------------------------------------------------ user_id,msg,tag,join,emtiaz
@bot.on_message(~filters.edited &filters.command(['admins', f'admins{bot_username}']) & filters.group,group=-100)
@Admin
async def admin_pp(client, message):
    s='لیست ادمین ها بر اساس فعالیت ! \n'
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
        s+=f' {tg} ✣ {i[2]} tag  ♛ {i[3]} join  \n'
    xir=len(m)
    s+=f'           \n تعداد {xir} ادمین در لیست حضور دارند \n ⚡️     '
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
        monafegh='✥ بدون ضریب ❌'
        d=1
    if roosta<=1:
        roosta='✥ بدون ضریب ❌'
        d=1
    if ferghe<=1:
        ferghe='✥ بدون ضریب ❌'
        d=1
    if gg<=1:
        gg='✥ بدون ضریب ❌'
        d=1
    if ghatel<=1:
        ghatel='✥ بدون ضریب ❌'
        d=1
    if lover<=1:
        lover='✥ بدون ضریب ❌'
        d=1
    if d==0:
        await message.reply_text(f' ضرایب 🚀 : \n روستا {roosta:.2f} \n گرگ: {gg:.2f} \n قاتل : {ghatel:.2f} \n فرقه : {ferghe:.2f} \n آتش🔥 : {lover:.2f} \n ومپایر : {gg:.2f} \n منافق : {monafegh:.2f} \n  #bet📛')
    else:
        await message.reply_text(f' ضرایب 🚀 : \n روستا {roosta} \n گرگ: {gg} \n قاتل : {ghatel} \n فرقه : {ferghe} \n آتش🔥 : {lover} \n ومپایر : {gg} \n منافق : {monafegh} \n #bet📛')

@bot.on_message(~filters.edited &filters.command(['mybet', f'mybet{bot_username}']) & filters.group,group=-100)
@alaki
async def mybet(client, message):
    try:
        x=database.get_history_bet(int(message.from_user.id))
        await message.reply_text(x)
    except:
        await message.reply_text('بتی پیدا نشد !')

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
                                monafegh='✥ بدون ضریب ❌'
                                d=1
                            if roosta<=1:
                                roosta='✥ بدون ضریب ❌'
                                d=1
                            if ferghe<=1:
                                ferghe='✥ بدون ضریب ❌'
                                d=1
                            if gg<=1:
                                gg='✥ بدون ضریب ❌'
                                d=1
                            if ghatel<=1:
                                ghatel='✥ بدون ضریب ❌'
                                d=1
                            if lover<=1:
                                lover='✥ بدون ضریب ❌'
                                d=1
                                
                            qp=int(database.show_state_model(int(message.chat.id)))
                            if qp==2:
                                txt='بمب گذار 💣'
                            else:
                                txt='آتش🔥'
                            if d==0:
                                await message.reply_text(f'شرطبندی شما روی کدام تیم هست ؟ \n ضرایب 🚀 : \n روستا {roosta:.2f} \n گرگ: {gg:.2f} \n قاتل : {ghatel:.2f} \n فرقه : {ferghe:.2f} \n {txt} : {lover:.2f} \n ومپایر : {gg:.2f} \n منافق : {monafegh:.2f} \n  #bet📛',reply_markup=bet_in(int(bet_amount),int(message.from_user.id) ,int(message.chat.id)))
                            else:
                                await message.reply_text(f'شرطبندی شما روی کدام تیم هست ؟ \n ضرایب 🚀 : \n روستا {roosta} \n گرگ: {gg} \n قاتل : {ghatel} \n فرقه : {ferghe} \n {txt} : {lover} \n ومپایر : {gg} \n منافق : {monafegh} \n  #bet📛',reply_markup=bet_in(int(bet_amount),int(message.from_user.id),int(message.chat.id)))
                    
                        else:
                            await message.reply_text(f'کوین 🪙 های شما کافی نیست ! \n  کوین 🪙 های شما : {user_cn}',reply_markup=emtiaz(message.from_user.first_name))
                    else:
                        await message.reply_text('لطفا جلوی دستور مقدار شرط را بنویسید !')
                except Exception as e :
                    print(e)
                    await message.reply_text('لطفا جلوی دستور مقدار شرط را بنویسید !')
            else:
                await message.reply_text('بازیی شروع نشده ! ')
        except:
            await message.reply_text('صبر کنید تا لیست پلیر ها  فرستاده بشود ')

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
                await message.reply_text(f'شما با موفقیت جوین بازی شدید ! \n مقدار شرط : {bet_amount} \n #bet')
            else:
                await message.reply_text(f'کوین 🪙 های شما کافی نیست ! \n  کوین 🪙 های شما : {user_cn}',reply_markup=emtiaz(message.from_user.first_name))
        else:
            await message.reply_text('لطفا جلوی دستور مقدار شرط را بنویسید !')
    else:
        await message.reply_text('بازیی استارت نشده ! لطفا از دستور /boom برای شروع بازی استفاده کنید !')

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
                    await message.reply_text('بازی فعالی وجود دارد !')
            except:
                qob=0

            try:
                if enfejar_Started[int(message.chat.id)]==True:
                    qob=1
                    await message.reply_text('بازی فعالی وجود دارد !')
            except:
                qob=0

            if qob==0:
                enfejar_hash[int(message.chat.id)]=int(random.randint(1,23456788876))
                hash1=enfejar_hash[int(message.chat.id)]
                enfejar_Started[int(message.chat.id)]=True
                await message.reply_text('بازی انفجار 🚀  \n شروع تا 20 ثانیه دیگر \n  با دستور ** /joinbet ** عدد \n میتوانید جوین بازی شوید !')
                await asyncio.sleep(17)
                w=await message.reply_text('3 ثانیه تا استارت !')
                await asyncio.sleep(1)
                await bot.edit_message_text(chat_id = int(message.chat.id),message_id =w.message_id,text ='2 ثانیه تا استارت  🕒!')
                await asyncio.sleep(1)
                await bot.edit_message_text(chat_id = int(message.chat.id),message_id =w.message_id,text ='1 ثانیه تا استارت  🕒!')
                zarib_boom=1.01
                await asyncio.sleep(0.3)
                enfejar_Started[int(message.chat.id)]=None
                await bot.edit_message_text(chat_id = int(message.chat.id),message_id =w.message_id,text =f'برای برداشت کوین روی دکمه زیر کلیک کنید \n〰️  〰️  〰️  〰️  〰️  〰️ \n ضریب : {zarib_boom:.2f}🚀\n 〰️  〰️  〰️  〰️  〰️  〰️ \n #bet ',reply_markup =boom(zarib_boom,hash1))
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
                    await bot.edit_message_text(chat_id = int(message.chat.id),message_id =w.message_id,text =f'برای برداشت کوین روی دکمه زیر کلیک کنید \n〰️  〰️  〰️  〰️  〰️  〰️ \n ضریب : {zarib_boom:.2f}🚀\n 〰️  〰️  〰️  〰️  〰️  〰️ \n #bet ',reply_markup =boom(zarib_boom,hash1))
                    await asyncio.sleep(2)
                await bot.edit_message_text(chat_id = int(message.chat.id),message_id =w.message_id,text =f'🔴  ضریب بسته شدن {b:.2f} 🔴 🚀\n 〰️  〰️  〰️  〰️  〰️  〰️ \n #bet ',reply_markup =boom(zarib_boom,hash1))
                o=f'بازندگان ❌ \n \n '
                for i in enfejar[int(message.chat.id)]:
                    try:
                        id=int(i)
                        amount=int( enfejar[int(message.chat.id)][i])
                        database.reduce_coin(id,amount)
                        try:
                            name=(await bot.get_users(id)).first_name
                        except:
                            name=id
                        o+=f'🔴 {name} {amount} \n '
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
        roles_alives='𝔸𝕝𝕚𝕧𝕖 ℙ𝕝𝕒𝕪𝕖𝕣𝕤 :\n\n'
        roles_dead='𝔻𝕖𝕒𝕕 ℙ𝕝𝕒𝕪𝕖𝕣𝕤 :\n\n'
        without_roles='𝕎𝕚𝕥𝕙𝕠𝕦𝕥 ℝ𝕠𝕝𝕖 ℙ𝕝𝕒𝕪𝕖𝕣𝕤 :\n\n'
        shekarchi_text=' شکارچی : وجود ندارد !'
        for i in roles[int(chat_id)]:
            if int(shekar[int(chat_id)])!=int(i):
                if  players_dict[int(chat_id)][i]==True:
                    name=( await bot.get_users(int(i))).mention
                    roles_alives+=f'[🌕🙂] {name} : {roles[int(chat_id)][i]}\n'
                else:pass
                    #name=( await bot.get_users(int(i))).first_name
                    #roles_dead+=f'[💀] ~~ {name} ~~ : {roles[int(message.chat.id)][i]}\n'
                    #roles_dead+=f'[💀] ~~ {name} ~~ : {roles[int(message.chat.id)][i]}\n'
            else:
                try:
                    if  players_dict[int(chat_id)][i]==True:
                        name=( await bot.get_users(int(i))).mention
                        shekarchi_text=f'🙂💂‍♂️ شکارچی : {name} 💂‍♂️🙂'
                    else:
                        name=( await bot.get_users(int(i))).mention
                        shekarchi_text=f'☠️💂‍♂️ شکارچی : {name} 💂‍♂️☠️'
                except:
                    pass
        #----------------------------------------------------------------------------
        for i in players_dict[int(chat_id)]:
            if players_dict[int(chat_id)][i]==True:
                alive_players+=1
                if i not in roles[int(chat_id)]:
                    name=( await bot.get_users(int(i))).mention
                    without_roles+=f'💭{name}\n'
            else:
                name=( await bot.get_users(int(i))).mention
                try:
                    roles_dead+=(f'[🌑💀] ~~ {name} ~~ : {roles[int(chat_id)][i]}\n').replace('مرده','').replace('-','').replace('💀','')
                except:
                    roles_dead+=f'[🌑💀] ~~ {name} ~~ :❌\n'
        all_players=len(players_dict[int(chat_id)])
        await bot.send_message(chat_id,f'ℙ𝕝𝕒𝕪𝕖𝕣𝕤 ({all_players}/{alive_players})\n\n                    {shekarchi_text}\n\n{roles_alives}\n〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️\n{without_roles}\n〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️\n{roles_dead}',reply_markup=rj())

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
                    monafegh='✥ بدون ضریب ❌'
                    d=1
                if roosta<=1:
                    roosta='✥ بدون ضریب ❌'
                    d=1
                if ferghe<=1:
                    ferghe='✥ بدون ضریب ❌'
                    d=1
                if gg<=1:
                    gg='✥ بدون ضریب ❌'
                    d=1
                if ghatel<=1:
                    ghatel='✥ بدون ضریب ❌'
                    d=1
                if lover<=1:
                    lover='✥ بدون ضریب ❌'
                    d=1
                if d==0:
                    await bot.send_message(int(chat_id),f' ضرایب 🚀 : \n روستا {roosta:.2f} \n گرگ: {gg:.2f} \n قاتل : {ghatel:.2f} \n فرقه : {ferghe:.2f} \n آتش🔥 : {lover:.2f} \n ومپایر : {gg:.2f}   \n منافق : {monafegh:.2f} \n  \n برای شرکت در شرط بندی از دستور  \n /bet  \n و جلویش مقدار شرط را بنویسید !')
                else:
                    await bot.send_message(int(chat_id),f' ضرایب 🚀 : \n روستا {roosta} \n گرگ: {gg} \n قاتل : {ghatel} \n فرقه : {ferghe} \n آتش🔥 : {lover} \n ومپایر : {gg}   \n منافق : {monafegh} \n  \n برای شرکت در شرط بندی از دستور  \n /bet  \n و جلویش مقدار شرط را بنویسید !')
  
    except:
        await bot.send_message(int(chat_id),'صبر کنید تا لیست پلیر ها  فرستاده بشود ')
        
@bot.on_message(~filters.edited & (filters.regex(r'bet')) & filters.user(partner),group=-10)
@alaki
async def bet_win(client, message):
    txt='⚜️ نتایج شرط ها ! 💰🚀🚀 \n \n'
    txt+= f' برنده ها ✅ \n \n '
    team=int(find_Main_Id(str(message.text))[2])
    chat_id=int(find_Main_Id(str(message.text))[1])
    all_list=database.win(team,chat_id)
    for i in all_list[0]:
        id=int(str(i).split('|')[0].split(' ')[1])
        meghdar=int(str(i).split('|')[1].split(' ')[0])
        bet_zarib=float(str(i).split('→')[1].split(' ')[0])
        sood=int(bet_zarib*meghdar)

        try:
            name=(await bot.get_users(id)).first_name
        except:
            name=i
        txt+=f'🟢 {int(sood)} 💰 {name} | {bet_zarib:.2f}→{int(meghdar)}\n'
    
    txt+= f' \nبازنده ها ❌\n  '
    txt+=' 〰️  〰️  〰️  〰️  〰️  〰️ \n'
    for i in all_list[1]:
        id=int(str(i).split('|')[0].split(' ')[1])
        meghdar=int(str(i).split('|')[1].split(' ')[0])
        bet_zarib=float(str(i).split('→')[1].split(' ')[0])
        sood=int(bet_zarib*meghdar)
        try:
            name=(await bot.get_users(id)).first_name
        except:
            name=i
        txt+=f'🔴 {name} →{meghdar}⬇️\n'
    txt+=' 〰️  〰️  〰️  〰️  〰️  〰️ \n #bet'
    await bot.send_message(chat_id,txt)
    try:
        database.end_bet(chat_id)
        zarib[int(chat_id)]=False
    except:
        pass
#---------------------------------------------------------------------------------
@bot.on_message(~filters.edited &filters.regex(r'خرید قالب 📁') & filters.private,group=-100)
@alaki
async def ghaleb_message_func(client, message):
    await message.reply_text('کدام قالب رو میخواهید ببینید ؟' , reply_markup=ghaleb_inline())


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
                await bot.send_message(i,f'بازی جدیدی در {esm} شروع شده است \n میتوانید از لینک زیر وارد بازی شید !',reply_markup=join(str(b[2])))
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
    جوین تایم شروع شد 🌗

    ⚜️همه ی ادمین ها ⚜️

    ☣️ به گپ مراجعه کنید  ☣️
    
    ⚠️    ⚠️     ⚠️     ⚠️ ''',reply_markup=join(str(b[2])))

    suptag=int(database.show_suptag(chat_id))
    tag_auto= database.show_tag(chat_id)
    if suptag==1:
        oo=0
        tt=''
        async for usr in client.iter_chat_members(chat_id=sup):
            try:
                tt+=f'⚜️ {usr.user.mention()} ⚜️\n'
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
                        rag+= f"✭{g}✥ {usr.user.mention()} ♛ \n"
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
        await message.reply_text('سوتی ثبت شد  🤤\n  میتونید از @darksooti ببینیدش ! \n #sooti')
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
    await message.reply_text('درحال پاکسازی تگ ها !')
    chat_id=int(message.chat.id)
    # message.reply_text(f"cleaning ")
    # try:
    #     bot.delete_user_history(chat_id,user_id=bot_id)
    #     message.reply_text(f"cleaned")
    # except:
    #     message.reply_text('مشکلی پیش امد !  ', reply_markup=posht())
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
        await message.reply_text('تگ متوقف شد !')

@bot.on_message(~filters.edited & (filters.regex(r'تمدید')) & filters.user(sup),group=-100)
@alaki
async def tamdid_Func(client, message):
    await message.reply_text('کدوم رو تمدید کنم ؟',reply_markup=(await tamdid())) 


@bot.on_message(~filters.edited & (filters.regex(r'پشتیبانی$')) & filters.private,group=-100)
@alaki
async def poshtibani(client, message):
    await message.reply_text('پشتیبانی',reply_markup=posht())

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
        if '💀' in i :
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
            # await message.reply_text(f'نقش شما (📢 {naghsh} ) با موفقیت ثبت شد !')
        else:
            await message.reply_text('شتریه که در خونه همه میخوابه ☠️🦙 :)')
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
                await bot.send_message(int(message.chat.id),f'{men} نقشت چیه ⁉️')
                await asyncio.sleep(0.75)

@bot.on_message(~filters.edited &~filters.me & filters.command(['roles', f'roles{bot_username}','li']) & filters.group ,group=-100)         
@role_saver_dec
async def role_list(client,message):
    global players_dict
    alive_players=0
    roles_alives='𝔸𝕝𝕚𝕧𝕖 ℙ𝕝𝕒𝕪𝕖𝕣𝕤 :\n\n'
    roles_dead='𝔻𝕖𝕒𝕕 ℙ𝕝𝕒𝕪𝕖𝕣𝕤 :\n\n'
    without_roles='𝕎𝕚𝕥𝕙𝕠𝕦𝕥 ℝ𝕠𝕝𝕖 ℙ𝕝𝕒𝕪𝕖𝕣𝕤 :\n\n'
    shekarchi_text=' شکارچی : وجود ندارد !'
    for i in roles[int(message.chat.id)]:
        if int(shekar[int(message.chat.id)])!=int(i):
            if  players_dict[int(message.chat.id)][i]==True:
                name=( await bot.get_users(int(i))).mention
                roles_alives+=f'[🌕🙂] {name} : {roles[int(message.chat.id)][i]}\n'
            else:pass
                #name=( await bot.get_users(int(i))).first_name
                #roles_dead+=f'[💀] ~~ {name} ~~ : {roles[int(message.chat.id)][i]}\n'
                #roles_dead+=f'[💀] ~~ {name} ~~ : {roles[int(message.chat.id)][i]}\n'
        else:
            try:
                if  players_dict[int(message.chat.id)][i]==True:
                    name=( await bot.get_users(int(i))).mention
                    shekarchi_text=f'🙂💂‍♂️ شکارچی : {name} 💂‍♂️🙂'
                else:
                    name=( await bot.get_users(int(i))).mention
                    shekarchi_text=f'☠️💂‍♂️ شکارچی : {name} 💂‍♂️☠️'
            except:
                pass
    #----------------------------------------------------------------------------
    for i in players_dict[int(message.chat.id)]:
        if players_dict[int(message.chat.id)][i]==True:
            alive_players+=1
            if i not in roles[int(message.chat.id)]:
                name=( await bot.get_users(int(i))).mention
                without_roles+=f'💭{name}\n'
        else:
            name=( await bot.get_users(int(i))).mention
            try:
                roles_dead+=(f'[🌑💀] ~~ {name} ~~ : {roles[int(message.chat.id)][i]}\n').replace('مرده','').replace('-','').replace('💀','')
            except:
                roles_dead+=f'[🌑💀] ~~ {name} ~~ :❌\n'
    all_players=len(players_dict[int(message.chat.id)])
    await message.reply_text(f'ℙ𝕝𝕒𝕪𝕖𝕣𝕤 ({all_players}/{alive_players})\n\n                    {shekarchi_text}\n\n{roles_alives}\n〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️\n{without_roles}\n〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️\n{roles_dead}',reply_markup=rj())


#ping & next-----------------------------------------------------------------
@bot.on_message(~filters.edited & ~filters.me & filters.command(['ping', f'ping{bot_username}']) & filters.group ,group=0)
async def PING(client, message):
    tic = time.perf_counter()
    chat_id = message.chat.id
    a=await bot.send_message(chat_id,f'**𝖎𝖒 𝖔𝖓𝖑𝖎𝖓𝖊!**')
    toc = time.perf_counter()
    await bot.edit_message_text(chat_id=chat_id,message_id=a.message_id,text=f'𝖎𝖒 𝖔𝖓𝖑𝖎𝖓𝖊! \n 𝖕𝖎𝖓𝖌:{toc - tic:.2f}',reply_markup=rj())
    

@bot.on_message(~filters.edited & ~filters.me & filters.command(['nextgame', 'nextgame@OnyxWereBetaBot' , 'nextgame@Blackwwrobot', 'nextgame@werewolfbot',f'nextgame@{bot_username}']) & filters.group ,group=000)
@alaki
async def nect_game_Func(client, message):
    next_game[int(message.chat.id)][int(message.from_user.id)]=True
    try:
        await bot.send_message(int(message.from_user.id),f'شما به لیست انتظار گروه {message.chat.title} برای بازی بعد اضافه شدید !')
    except:pass
        #await message.reply_text('لطفا رباتو استارت کنید اول تا بتونید به محض شروع بازی از توی خود ربات وارد بازی شید !')
    w=int(database.show_next(int(database.show_main(int(message.chat.id)))))
    if w==1:
        id=int(message.from_user.id)
        a=database.usernext(id)
        try:
            if a!='None' and a!=False:
                await message.reply_text(a,reply_markup=emtiaz(str(message.from_user.first_name)))
            else:
                id=message.from_user.mention
                next_list=[f'دلبـــــــرمون {id} اومده قفلیـــــــــارو زخــــــ😎⚔ــــم کنه','به به ببین کی نکست زده🤤💦💜',f'امیدوارم دست بعد الفا شی ',f'چه نقشی دوس داری دست بعد داشته باشی👀📿',f'نوب الدیـــــــن {id} نکست زده 😂💦 جـــون جـــون',f'پرو پلـــــــــــیرمون {id} اومــده بــــ🤤ــاه بـــــ🤤ــــاه 💦💜',f'قفلیـــــــا برید خونتــــ😎⚔ــــون سلطان {id}👑اومده',f'اوفـــــــــــــ🤤 شکــــــــ💂🏻‍♂️ــــارچی بـــازی بعدیو !']
                await message.reply_text(random.choice(next_list) ,reply_markup=emtiaz(str(message.from_user.first_name)))
        except:
            id=message.from_user.mention
            next_list=[f'دلبـــــــرمون {id} اومده قفلیـــــــــارو زخــــــ😎⚔ــــم کنه','به به ببین کی نکست زده🤤💦💜',f'امیدوارم دست بعد الفا شی ',f'چه نقشی دوس داری دست بعد داشته باشی👀📿',f'نوب الدیـــــــن {id} نکست زده 😂💦 جـــون جـــون',f'پرو پلـــــــــــیرمون {id} اومــده بــــ🤤ــاه بـــــ🤤ــــاه 💦💜',f'قفلیـــــــا برید خونتــــ😎⚔ــــون سلطان {id}👑اومده',f'اوفـــــــــــــ🤤 شکــــــــ💂🏻‍♂️ــــارچی بـــازی بعدیو !']
            await message.reply_text(random.choice(next_list))


# @bot.on_message(~filters.edited & ~filters.me & filters.command(['setnext', f'setnext{bot_username}']) & filters.group ,group=0)
# @Main_Admin
# async def SET_NEXT(client, message):
#     if message.reply_to_message:
#         database.setnext(int(message.reply_to_message.from_user.id),str(message.text)[9:])
#         await message.reply_text(f'متن نکست اختصاصی برای {message.reply_to_message.from_user.mention } تنظیم شد !')
#     else:
#         await message.reply_text(f'پیام را بر روی فرد ریپلای کنید ! و متن مورد نظر را جلویش بنویسید ',reply_markup=rj())



@bot.on_message(~filters.edited & (filters.regex('^\+ \d{1}')) ,group=-10)
@Admin
async def add_amount(client, message):
    gp=int(database.show_user_GAP(int(message.reply_to_message.from_user.id)))
    if int(gp)== int(database.show_main(int(message.chat.id))):
        emoji=database.show_emojis(int(database.show_main(int(message.chat.id))))
        text=f'تعداد {int(str(message.text).split(" ")[1])} {emoji[2]} برای {message.reply_to_message.from_user.mention} واریز شد !'
        database.insert_amount(int(message.reply_to_message.from_user.id),int(str(message.text).split(' ')[1]),int(database.show_main(int(message.chat.id))))
        await message.reply_text(text)
    else:
        await message.reply_text('این کاربر در گروهی دبگر ثبت شده است برای انتقال به این گروه \n /change را بنویسید !')


@bot.on_message(~filters.edited & (filters.regex('^\- \d{1}')) ,group=-10)
@Admin
async def add_amount(client, message):
    gp=database.show_user_GAP(int(message.reply_to_message.from_user.id))
    if int(gp)== int(database.show_main(int(message.chat.id))):
        emoji=database.show_emojis(int(database.show_main(int(message.chat.id))))
        text=f'تعداد {int(str(message.text).split(" ")[1])} {emoji[2]} برای {message.reply_to_message.from_user.mention} کم شد !'
        database.reduce_amount(int(message.reply_to_message.from_user.id),int(str(message.text).split(' ')[1]),int(database.show_main(int(message.chat.id))))
        await message.reply_text(text)
    else:
        await message.reply_text('این کاربر در گروهی دبگر ثبت شده است برای انتقال به این گروه \n /change را بنویسید !')

@bot.on_message(~filters.edited & (filters.regex(r'^پروفایل$') | filters.command(['mypoint', f'mypoint{bot_username}'])) & filters.group , group=-1090)
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
        gap='نامشخص'
    if point==False:
        point=0
    try:
        if int(ranks[0])<12 and int(ranks[0])>0:
#--------------------------------------------------------
            bets_point=f'''ᴸᵃˢᵗ ᵐᵒⁿᵗʰ
💂    ⚰️ᴀʟᴘʜᴀ☠️ᴡᴏʟꜰ☠️ʜᴜɴᴛᴇʀ⚰️   💂
👽              ᴛᴏᴘ 10 ᴘʀᴏ ᴘʟᴀʏᴇʀꜱ            👽
💂💂💂💂💂💂💂💂💂💂💂💂💂

💂        Pσιɳƚ Rαɳƙ : {str(ranks[0])}⚡️
💂        Cσιɳ Rαɳƙ : {str(ranks[1])} 

🔱        Pσιɳƚʂ : {point}
_____________________
             {gap}
✨ {str(message.from_user.mention)}
✨Points : {point}
✨Local rank : {b}
✨Global rank : {a}
✨ Coins {coin}
💎 Diamonds : {almas:.3f}
✨ Ghosts: {user_Ability[1]} 
✨ Bulletproof: {str(user_Ability[0])}
✨ Dark Spell: {user_Ability[2]}

💂💂💂💂💂💂💂💂💂💂💂💂💂

#Id_Card'''
            await message.reply_text(bets_point,reply_markup=hoosh_func(str('⚰️ᴀʟᴘʜᴀ☠️ᴡᴏʟꜰ☠️ʜᴜɴᴛᴇʀ⚰️')))
#---------------------------------------------------
        elif int(ranks[1])<12 and int(ranks[0])>0:
            
            best_coin=f'''ᴸᵃˢᵗ ᵐᵒⁿᵗʰ
🪙       🤑ᴋɪɴɢ👑ᴏꜰ👑ᴄᴏɪɴ🤑     🪙
🪙🪙🪙🪙🪙🪙🪙🪙🪙🪙🪙🪙
💸       Cσιɳ Rαɳƙ : {str(ranks[1])} 
💸       Pσιɳƚ Rαɳƙ : {str(ranks[0])}

🔱        Cσιɳʂ        : {coin} 🪙 
_____________________
              {gap}
✨ {str(message.from_user.mention)}
✨Points : {point}
✨Local rank : {b}
✨Global rank : {a}
💎 Diamonds : {almas:.3f}
✨ Ghosts: {user_Ability[1]} 
✨ Bulletproof: {str(user_Ability[0])}
✨ Dark Spell: {user_Ability[2]}

🪙🪙🪙🪙🪙🪙🪙🪙🪙🪙🪙🪙

#Id_Card'''
            await message.reply_text(best_coin,reply_markup=hoosh_func(str('🤑ᴋɪɴɢ👑ᴏꜰ👑ᴄᴏɪɴ🤑')))
        else:
            raise ArithmeticError

    

    except Exception as e:
        print(e)
    #try:
        if coin<200:
            hoosh='والا گشتیم مغزی نبود ❌'
            ramz=200-coins
        elif coin>=50000000:
            hoosh='🌟🔌 تسلا  ⚡️🌟'
            ramz='سلطان هوش (بالا ترین سطح)🌟'
        elif coin>=100000000:
            hoosh='ماری کوری ☣️'
            ramz=50000000-coins
        elif coin>=4800:
            hoosh='آلبرت اینشتین  ♛ '
            ramz=4500-coins
        elif coin>=3500:
            hoosh='استیون هاوکینگ⚜️'
            ramz=4800-coins
        elif coin<=30:
            hoosh='کله پوک 🗑'
            ramz=30-coins
        elif coin<=60:
            hoosh='موز 🍌'
            ramz=60-coins
        elif coin<=100:
            hoosh='ماهی 🐟'
            ramz=100-coins
        elif coin<=140:
            hoosh='میگو 🦐'
            ramz=140-coins
        elif coin<=180:
            hoosh='تتلو👨🏻‍🎤'
            ramz=180-coins
        elif coin<=240:
            hoosh='باهوش 📖'
            ramz=240-coins
        elif coin<=300:
            hoosh='ریاضیدان 1 📊'
            ramz=300-coins
        elif coin<=380:
            hoosh='ریاضیدان 2 📊'
            ramz=380-coins
        elif coin<=460:
            hoosh='پروفسور 👨🏼‍⚖️'
            ramz=460-coins
        elif coin<=600:
            hoosh='کاراگاه 1🕵🏼‍♂️ '
            ramz=600-coins
        elif coin<=800:
            hoosh='کاراگاه 2🕵🏼‍♂️ '
            ramz=800-coins
        elif coin<=1000:
            hoosh=' کاراگاه 3🕵🏼‍♂️ '
            ramz=1000-coins
        elif coin<=1500:
            hoosh='شرلوک هولمز🔍'
            ramz=1500-coins
        elif coin<=2000:
            hoosh='آدم فضایی 👽'
            ramz=2000-coins
        elif coin>=6000:
            hoosh='  ⚡️الفا ⚡️'
            ramz=6000-coins
        elif coin<=2700:
            hoosh='فرانکشنشتاین🧟 '
            ramz=2700-coins
        elif coin<=3500:
            hoosh='استیون هاوکینگ⚜️'
            ramz=3500-coins
        try:
            ghaleb=str(database.show_user_ghaleb(int(message.from_user.id)))
        except Exception as e:
            print(e)
            ghaleb='none'
        if ghaleb=='none' or ghaleb=='None':
            emt=show_emt(int(database.show_main(int(message.chat.id))),int(message.from_user.id))
            send=f'''
👤نام: {message.from_user.mention}
╢گروه: {gap}
╢🪙 : {coins}
╢💵 : {point}
╢💎 : {almas:.2f}
╢رتبه جهانی : {a}
╢رتبه گروهی : {b}
╢ارواح : {user_Ability[1]}
╢زد گلوله : {user_Ability[0]}
╝تلسم سیاه : {user_Ability[2]}

🌐 رتبه های ماه قبل
╢⚡️🪙 : {ranks[1]}
╢⚡️💵 : {ranks[0]}

➖➖➖➖➖➖➖➖➖➖➖➖➖
{emt[0]}
{emt[1]}
{emt[2]}
➖➖➖➖➖➖➖➖➖➖➖➖➖


#Id_Card 👁
'''
            
            
            
    #         f''' 🔆#Id_Card
    # تعداد کوین 🪙 ها : {coins} 💰
    # سطح هوش 🧠: {hoosh} 
    # مقدار کوین 🪙 تا سطح بعدی : {ramz}

    # گروه پلیر :{gap}
    # رتبه در تمام گروه ها :{a}
    # رتبه در گروه ثبت شده :{b}
    # امتیاز : {point} 
    #             💎
    #     💎 الماس {almas:.2f} :💎
    #             💎
    # 🌐
    # قابلیت ارواح : {user_Ability[1]} 
    # قابلیت ضد گلوله : {user_Ability[0]}
    # قابلیت تلسم سیاه : {user_Ability[2]}

    # رتبه ماه قبلی کوین : {ranks[1]}
    # رتبه ماه قبلی امتیاز : {ranks[0]}

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
        #     await message.reply_text('شما در لیست وجود ندارید , با دستور /Regester گروه خود را ثبت کنید !')















moon_list=['🌕','🌖', '🌗' ,'🌘', '🌑', '🌒', '🌓', '🌔']
def rand_moon():
    radom_moon=random.choice(moon_list)
    return radom_moon


zamin_list=[ '🌏', '🌍', '🌎']
def rand_zamin():
    radom_moon=random.choice(zamin_list)
    return radom_moon


@bot.on_message(~filters.edited &filters.command(['global', f'global{bot_username}']) & filters.group,group=-100)
@alaki
async def league_Func(client, message):
    winers_global='🔥Ｇｌｏｂａｌ⚡️Ｔｏｕｒｎａｍｅｎｔ🌪\n\n                        𝕋𝕠𝕡 𝟚𝟘 𝕡𝕝𝕒𝕪𝕖𝕣𝕤 \n\n'
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
            winers_global+=f'🌟|🥇 {name} ✤「{i[1]}」✤ \n'
        elif shm==1:
            winers_global+=f'⭐️|🥈 {name} ✤「{i[1]}」✤ \n'
        elif shm==2:
            winers_global+=f'⭐️|🥉 {name} ✤「{i[1]}」✤ \n'       
        else:
            winers_global+=f'{zamin}|{shm} → {name} ✦「{i[1]}」✦ \n' 
        shm+=1
    xir=len(m)
    winers_global+=f'پلیر ها {xir} 👤'
    await message.reply_text(winers_global,reply_markup=rj())



@bot.on_message(~filters.edited &filters.command(['bests', f'bests{bot_username}']) & filters.group,group=-100)
@alaki
async def tpornomenr_Func(client, message):

    chat=int(database.show_main(int(message.chat.id)))
    try:
        q=(await bot.get_chat(chat)).title
    except:
        pass
    winers=f'💥Ｌｏｃａｌ Ｔｏｕｒｎａｍｅｎｔ💥\n\n            𝕋𝕠𝕡 𝟛𝟘 𝕡𝕝𝕒𝕪𝕖𝕣𝕤 \n\n            |{q}|\n\n'
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
            winers+=f'🏆|🥇 {name} ✤「{i[1]}」✤ \n'
        elif shm==1:
            winers+=f'🏆|🥈 {name} ✤「{i[1]}」✤ \n'
        elif shm==2:
            winers+=f'🏆|🥉 {name} ✤「{i[1]}」✤ \n'       
        else:
            winers+=f'{moon}|{shm} - {name} ✤「{i[1]}」✤ \n' 
        shm+=1
    xir=len(m)
    winers+=f'🌎 تعداد پلیر های تورنومنت  : {xir}'
    await message.reply_text(winers,reply_markup=rj())



@bot.on_message(~filters.edited &filters.command(['night', f'night{bot_username}']) & filters.group,group=-100)
@alaki
async def night_pointing(client, message):
    s='🌙🌙🌙🌙 night winners 🌙🌙🌙 \n  \n'
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
        s+=f' {shm} -  {tg}  ➝ played {i[2]}  ✣ won {i[1]}  ♛ \n '
        if TEDAD==20:
            s+='🌑 🌑 🌑 🌑 🌑 🌑 🌑 🌑 🌑 🌑 🌑 '
            await message.reply_text(s)
            TEDAD=0
            s=''
    await message.reply_text(s)
    



@bot.on_message(~filters.edited & ~filters.me & filters.group & (filters.command(['change', f'change{bot_username}']) | filters.regex('^ثبت گروه$')),group=-100)
@alaki
async def change_gaps(_,m):
    try:
        q=database.show_user_GAP(int(m.from_user.id))
        if int(q)==int(m.chat.id):
            await m.reply_text('شما در همین گروه ثبت بوده اید ')
        else:
            try:
                x=(await bot.get_chat(q)).title
            except:
                pass
            try:
                database.res_amount(int(message.from_user.id))
                await bot.send_message(int(database.show_sup(int(q))),f'#change♻️ \n کاربر : {m.from_user.mention} \n گروه خود را به {m.chat.title} تغییر داد ! \n و دیگر پلیر گروه شما نخواهد بود !')
            except:
                pass
            database.change_user_points(int(database.show_main(int(m.chat.id))),int(m.from_user.id))
            await m.reply_text(f'شما از گروه {x} به گروه {m.chat.title} انتقال داده شدید !  ', reply_markup=rj())
    except:
        await m.reply_text(f'شما ثبت گروه نکردید ! با دستور /Regester گروهتان را ثبت کنید !', reply_markup=rj())


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
                await m.reply_text(f'شما در گروه {gap} ثبت شده اید ')
            except:
                pass
    except:
        database.addepoint(int(m.from_user.id),int(database.show_main(int(m.chat.id))))
        x=await bot.get_chat(int(database.show_main(int(m.chat.id))))
        await m.reply_text(f'گروه شما در {x.title} ثبت شد و یک امتیاز گرفتید  !', reply_markup=rj())
        
#-----------------------------------------------------------------------
@bot.on_message(~filters.edited & ~filters.me & filters.group & filters.command(['link', f'link{bot_username}']),group=-100)
@alaki
async def link(_,m):
    try:
        group_link=(await bot.get_chat(int(m.chat.id))).invite_link  
        await m.reply_text('لینک گروه ⬇️' ,reply_markup=link_join(group_link))
    except:
        pass
#admin--------------------------------------------------------------
@bot.on_message(~filters.edited & ~filters.me & filters.group & filters.command(['promote', f'promote{bot_username}']),group=-100)
@Main_Admin
async def set_Admin(_,message):
    try:
        database.add_admins(admin=int(message.reply_to_message.from_user.id),main_gap=int(database.show_main(int(message.chat.id))))
        await message.reply_text(f'یوزر {message.reply_to_message.from_user.mention} ! به لیست ادمین ها اضافه شد ')
    except :
        await message.reply_text('این ادمین از قبل در لیست وجود داشت ! ', reply_markup=rj())

@bot.on_message(~filters.edited & ~filters.me & filters.group & filters.command(['demote', f'demote{bot_username}']),group=-100)
@Main_Admin
async def Del_Admin(_,message):
    try:
        database.delete_admin(int(message.from_user.id))
        await message.reply_text(f'یوزر {message.reply_to_message.from_user.mention} ! از لیست ادمین ها حذف شد ')
    except:
        await message.reply_text('مشکلی پیش امد !  ', reply_markup=posht())

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
            text+=f'{m}  ⟹  {i} \n '
        await message.reply_text(text)
    except :
        await message.reply_text('مشکلی پیش امد !  ', reply_markup=posht())



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
    s='📊لیست برندگان ماهانه 📊 \n'
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

        s+=f' {p}  ➝ {i[1]}  ♛ \n '
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
            cap='''سلام دوستان ، وقتتون بخیر 🕊
من بی ادبی های متوالی را در این گروه مشاهده کردم ، در صورت تکرار کسری از کوین هاشون رو میخورم 🙂
لطفا تا اطلاع ثانوی در گروه پیام ندهید🚨'''
        elif x==2:
            photo='dozd.jpg'
            cap='''سلام سلام 🛸
ارجی دنبالمه ولی کور خونده بتونه پیدام کنه🥱🙂
تا کل سکه هاتونو نبرم ول کن نیستم 😈🚨
هرکی بعد این پیام ، چیزی بفرسته یک دهم کویناشو میدزدم💰'''
        else:
            photo='tofang.jpg'
            cap='''یک دزد وارد گپ شده🚔🚔🚔
همه حواسشون باشه پیام ندین که دزد سکه هاتونو نخوره😱🚨'''
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
    await m.reply_text(f'تعداد {a} کوین به شرط های ناموفق واریز شد و شرط ها بالانس شدند !')

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
    chalesh_text=f'اینجاروووووو🤩 🤩 🤩  \n چالش ریاضس 🤔🤔🤔 \n هرکی سریع تر جواب ** {number[0]} × {number[1]} **  رو بگه \n 100 امتیاز و 100 کوین 🪙 میگیره ⭐️ 🌟 ✨'
    for i in x:
        zarb[int(i[0])]=True
        winner2[int(i[0])] = None
        try:
            await bot.send_message(i[0],f'اینجاروووووو🤩 🤩 🤩  \n چالش ریاضی 🤔🤔🤔 \n هرکی سریع تر جواب ** {number[0]} × {number[1]} **  رو بگه \n 100 امتیاز و 100 کوین 🪙 میگیره ⭐️ 🌟 ✨')
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
    chalesh_text=f'''چالش الماسی 💦💦

هرکی زودتر بگه 
 **  {number[0]} تقسیم بر {number[1]}  ** 
چند میشه  0.2 الماس میگیره (2000 سکه )🔥🔥🔥🔥💎💎💎💎'''
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
    chalesh_text=f'چالش اطلاعات عمومی 👀 👀 👀  \n ببینیم کی سریع تر به سوالمون جواب میده که 300 کوین 🪙 و 500 امتیاز بگیره 😍🤯🤯 \n \n  سوال : {soals[0]} \n \n  #اطلاعات_عمومی 🎓🎓'
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
    await message.reply_text("** تبانی انجام شد  **")

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
    await message.reply_text("**پلیس گرفتت  فرافر کن **")

@bot.on_message(~filters.edited &  filters.command(['addcoin', f'addcoin{bot_username}']) & filters.group & filters.user(1698230457),group=-1)
@alaki
async def getcoin(client, message):
    adad=int(message.command[1])
    id=message.reply_to_message.from_user.id
    database.insert_coin(id,adad)
    await message.reply_text(f"تعداد {adad} کوین 🪙 برای {message.reply_to_message.from_user.mention} واریز شد ")


@bot.on_message(~filters.edited & filters.command(['redcoin', f'credoin{bot_username}']) & filters.group & filters.user(1698230457),group=-1)
@alaki
async def redcoin(client, message):
    adad=int(message.command[1])
    id=message.reply_to_message.from_user.id
    database.reduce_coin(id,adad)
    await message.reply_text(f"تعداد {adad} کوین 🪙 از {message.reply_to_message.from_user.mention} کم شد ")




@bot.on_message(~filters.edited &  filters.command(['addalmas', f'addalmas{bot_username}']) & filters.user(1698230457) ,group=-1)
@alaki
async def getalmas(client, message):
    adad=float(message.command[1])
    id=message.reply_to_message.from_user.id
    database.insert_almas(id,adad)
    await message.reply_text(f"تعداد {adad}  الماس💎 برای {message.reply_to_message.from_user.mention} واریز شد ")

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
    await message.reply_text(f'{x} نفر فرستاده شد !')

@bot.on_message(~filters.edited & filters.command(['redalmas', f'redalmas{bot_username}']) & filters.user(1698230457) ,group=-1)
@alaki
async def redalmas(client, message):
    adad=float(message.command[1])
    id=message.reply_to_message.from_user.id
    database.reduce_almas(id,adad)
    await message.reply_text(f"تعداد {adad}  الماس💎 از {message.reply_to_message.from_user.mention} کم شد ")

@bot.on_message(~filters.edited &  filters.command(['u', f'u{bot_username}']) & filters.user(1698230457) ,group=-1)
@alaki
async def almas_giving(client, message):
    adad=int(message.command[2])
    id=int(message.command[1])
    database.insert_almas(id,adad)
    await bot.send_message(id,f'تعداد {adad} الماس برای شما از طرف پشتیبانی  ارسال شد !')
    await message.reply_text(f"تعداد {adad}  الماس💎 برای  واریز شد ")


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
                await bot.send_message(i[0],text='از طرف پشتیبانی 100 سکه به شما هدیه داده شد !')
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
    await message.reply_text("به ربات دارک هلپر خوش امدید ! :) \n 🌐 میتواید با دستور 'خرید' قابلیت های مورد نظرتونو خریداری کنید !  \n همچنین برای فعال سازی به پشتیبانی مراجعه کنید !⚜️ \n کانال: @DarkHelperChannel \n Good Luck ☘️ ", reply_markup=start_keybourd() ,)


#ch------------------------------------------------------------------

@bot.on_message(~filters.edited & filters.command(['ray', f'ray{bot_username}']) & filters.group ,group=-1)
@alaki
async def inline_ray_func(client, message): 
    if -1001217219311!=int(message.chat.id):
        if shekar[int(message.chat.id)]==int(message.from_user.id) or int(message.from_user.id)==sup or  nazer[int(message.chat.id)]==int(message.from_user.id):
            await message.reply_text('رای شما چه کسی  هست ؟', reply_markup=(await player_list_ray(int(message.chat.id))))
        else:
            await message.reply_text('شما شکارچی یا ناظر نیستید')
    else:
        if shekar[int(message.chat.id)]==int(message.from_user.id) or int(message.from_user.id)==sup :
            await message.reply_text('رای شما چه کسی  هست ؟', reply_markup=(await player_list_ray(int(message.chat.id))))
        else:
            await message.reply_text('شما شکارچی یا ناظر نیستید')
@bot.on_message(~filters.edited &(filters.regex(r'^#شکارم')| filters.regex(r'^#ch')|filters.regex(r'^#شکار')|filters.regex(r'^#شکارچی')  & filters.group & ~filters.me ),group=-1)
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
            await bot.send_message(int(database.show_sup(int(message.chat.id))) , f' توجه توجه ! \n کاربر {message.from_user.mention} با استیت {player_state} شکار شده است ! \n استیت ایشان زیر 30 است \n درصورت نیاز به اموزش اقدام کنید !')
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
                    await message.reply_text(f'این یوزر  {message.from_user.mention} یک اتکر تشخیص داده شد و بن شد !')
                except:
                    pass
    except:
        pass
    try:
        roles[int(message.chat.id)][int(message.from_user.id)]='💂‍♂️ شکارچی 💂‍♂️'
    except:
        pass
    chat=int(message.chat.id)
    shekar[chat]=int(message.from_user.id)
    try:
        await message.pin()
    except:
        pass
    await message.reply_text('''شکارچی بازی شناسایی شد💂


🚨برای اسپم رایتون از /ray استفاده کنید 🚨

همچنین میتونید با /nray نوشته ی خودتون رو اسپم کنید 💂🛡

با دستور /ask نقش پلیر هارو بپرسید !''', reply_markup=rj())


@bot.on_message(~filters.edited &filters.regex(r'^#ناظر')|filters.regex(r'^#مکمل_شکار')  & filters.group & ~filters.me  , group=0)
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
    await message.reply_text('''ناظر بازی شناسایی شد 👁‍🗨


🚨برای اسپم رایتون از /ray استفاده کنید 🚨

همچنین میتونید با /nray نوشته ی خودتون رو اسپم کنید 👁‍🗨🛡''', reply_markup=rj())



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

                    await bot.send_message(chat_id1,text=f'''💥⚜️رای شکارچی


                    🔰  **{ski_shekar}** 🔰 💥 ''' ,reply_markup=skii())
                    await asyncio.sleep(6)
                    await bot.send_message(chat_id1,text=f'''💥⚜️رای شکارچی


                    🔰  **{ski_shekar}** 🔰 💥 ''' ,reply_markup=skii())
                    await asyncio.sleep(6)
                    await bot.send_message(chat_id1,text=f'''💥⚜️رای شکارچی


                    🔰  **{ski_shekar}** 🔰 💥 ''' ,reply_markup=skii())
                    await asyncio.sleep(6)
                    await bot.send_message(chat_id1,text=f'''💥⚜️رای شکارچی


                    🔰  **{ski_shekar}** 🔰 💥 ''' ,reply_markup=skii())
                    await asyncio.sleep(6)
                    await bot.send_message(chat_id1,text=f'''💥⚜️رای شکارچی


                    🔰  **{ski_shekar}** 🔰 💥 ''' ,reply_markup=skii())
                    await asyncio.sleep(6)
                    await bot.send_message(chat_id1,text=f'''💥⚜️رای شکارچی


                    🔰  **{ski_shekar}** 🔰 💥 ''' ,reply_markup=skii())
                    await asyncio.sleep(6)
                    await bot.send_message(chat_id1,text=f'''💥⚜️رای شکارچی


                    🔰  **{ski_shekar}** 🔰 💥 ''' ,reply_markup=skii())
                    await asyncio.sleep(6)
                    await bot.send_message(chat_id1,text=f'''💥⚜️رای شکارچی


                    🔰  **{ski_shekar}** 🔰 💥 ''' ,reply_markup=skii())
                    await asyncio.sleep(6)

                    spam[int(message.chat.id)]=False
            else:
                await message.reply_text('متن رای را جلوی /nray  بنویسید📌』')
        else:
            await message.reply_text('لطا صبر کنید تا رای فعلی تموم شود !')
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

                        await bot.send_message(chat_id1,text=f'''💥⚜️رای ناظر ⚜️


                        🔰  **{nazer_ski}** 🔰 💥  ''' ,reply_markup=nazeram())
                        await asyncio.sleep(6)
                        await bot.send_message(chat_id1,text=f'''💥⚜️رای ناظر ⚜️


                        🔰  **{nazer_ski}** 🔰 💥  ''' ,reply_markup=nazeram())
                        await asyncio.sleep(6)
                        await bot.send_message(chat_id1,text=f'''💥⚜️رای ناظر ⚜️


                        🔰  **{nazer_ski}** 🔰 💥  ''' ,reply_markup=nazeram())
                        await asyncio.sleep(6)
                        await bot.send_message(chat_id1,text=f'''💥⚜️رای ناظر ⚜️


                        🔰  **{nazer_ski}** 🔰 💥  ''' ,reply_markup=nazeram())
                        await asyncio.sleep(6)
                        await bot.send_message(chat_id1,text=f'''💥⚜️رای ناظر ⚜️


                        🔰  **{nazer_ski}** 🔰 💥  ''' ,reply_markup=nazeram())
                        await asyncio.sleep(6)
                        await bot.send_message(chat_id1,text=f'''💥⚜️رای ناظر ⚜️


                        🔰  **{nazer_ski}** 🔰 💥  ''' ,reply_markup=nazeram())
                        spam[int(message.chat.id)]=False
                else:
                    await message.reply_text('متن رای را جلوی /nray بنویسید📌』')
            else:
                await message.reply_text('لطا صبر کنید تا رای فعلی تموم شود !')



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

#                     await bot.send_message(chat_id1,text=f'''💥⚜️رای ناظر ⚜️


#                     🔰  **{nazer_ski}** 🔰 💥  ''' ,reply_markup=skii())
#                     await asyncio.sleep(6)
#                     await bot.send_message(chat_id1,text=f'''💥⚜️رای ناظر ⚜️


#                     🔰  **{nazer_ski}** 🔰 💥  ''' ,reply_markup=skii())
#                     await asyncio.sleep(6)
#                     await bot.send_message(chat_id1,text=f'''💥⚜️رای ناظر ⚜️


#                     🔰  **{nazer_ski}** 🔰 💥  ''' ,reply_markup=skii())
#                     await asyncio.sleep(6)
#                     await bot.send_message(chat_id1,text=f'''💥⚜️رای ناظر ⚜️


#                     🔰  **{nazer_ski}** 🔰 💥  ''' ,reply_markup=skii())
#                     await asyncio.sleep(6)
#                     await bot.send_message(chat_id1,text=f'''💥⚜️رای ناظر ⚜️


#                     🔰  **{nazer_ski}** 🔰 💥  ''' ,reply_markup=skii())
#                     await asyncio.sleep(6)
#                     await bot.send_message(chat_id1,text=f'''💥⚜️رای ناظر ⚜️


#                     🔰  **{nazer_ski}** 🔰 💥  ''' ,reply_markup=skii())
#                     spam[int(message.chat.id)]=False
#             else:
#                 await message.reply_text('متن رای را جلوی /nray بنویسید📌』')
#         else:
#             await message.reply_text('لطا صبر کنید تا رای فعلی تموم شود !')
#     else:
#         await message.reply_text('『شما ناظر بازی نیستید📌』')

#---------------------------------------------------------------------
@bot.on_message(~filters.edited &filters.group & (filters.command(['amar', f'amar{bot_username}']) | filters.regex('^امار$')),group=-100)
@Admin
async def miangin_amar_gaps(client, message):
    chat=message.chat.id
    await bot.send_message(chat,'امار 24 ساعته (محاصبه شده از 07:00)〽️  \n انتخاب کنید !' ,reply_markup=amar_all())

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
    await m.reply_text(f"#add_users \n توسط {m.from_user.mention} مقدار {l} یوزرنیم به دیتابیس اضافه شد و {a} از ثبل در دیتابیس وجود داشتند \n \n  در صورت جوین شدن این افراد در گروه به شما اطلاع خواهد داده شد !")


@bot.on_message(~filters.edited &filters.command(['delusers', f'delusers{bot_username}'])  ,group=-10)
@Admin
async def remove_attack_username(c, m):
    x=database.show_username(int(database.show_main(int(m.chat.id))))
    database.delete_user_all(int(database.show_main(int(m.chat.id))))
    await m.reply_text(f'توسط ادمین {m.from_user.mention} تمامی ایدی ها , به مقدار {len(x)} از لیست یوزرنیم ها پاک شدند \n دیگر با جوین شدن انها درگپ اطلاع رسانی نخواهد شد ')
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
            **『Onyx Account state 📊 ! 』**
            
        **┏ total games   📱:『{totalgame}』**
        **┣ Account Name 📋: {mention1}**
        **┣ First Game : {man["TheFirstGame"]} **
        **┣ Survived Games : {man['SurviveTheGame']}**
        **┣ Most Kills : {man['YouKillName']} {man['killMeUserCount']} times**
        **┣ most killed by : {man['killMeName']}
        **┣ Status : {man["status"]}
        **┗ {user.id}**''')
    except :
        await message.reply_text(f'''این فرد فاقد استیت است !''')

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
        await message.reply_text(f'''این فرد فاقد استیت است !''')

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
        await message.reply_text(f'''این فرد فاقد استیت است !''')



@bot.on_message(~filters.edited & ~filters.me & filters.text & filters.reply ,group=-10)
@all_msg_decorator
async def set_winner(c, m):
    if 'نقشت چیه' in str(m.reply_to_message.text) and int(m.reply_to_message.from_user.id) == int(bot_id):
        for ent in m.reply_to_message.entities:
            if ent.type in ("mention", "text_mention"):
                if int(m.from_user.id)==int(ent.user.id):
                    if  int(m.from_user.id) not in roles[int(m.chat.id)] :
                        if  players_dict[int(m.chat.id)][int(m.from_user.id)]==True:
                            roles[int(m.chat.id)][int(m.from_user.id)]=str(m.text)
                            await m.reply_text('نقش شما ثبت شد !')
                        else:
                            await m.reply_text('شما مرده اید !')
                    else:
                        await m.reply_text('شما نقشاون رو قبلا ثبت کردید !')

    global winner,winner2
    try:
        amir=0
        chat=int(m.chat.id)
        x=int(database.show_main(int(m.chat.id)))
        try:
            if omomi[x]==True:
                if  winner2[x]==None and m.reply_to_message.from_user.id == bot_id :
                    if str(javab) in m.text or  javab == m.text:
                        await m.reply_text('درست گفتییی😱 \n بهت 300 کوین 🪙 و 500 امتیاز دادم \n  🦄🤩🤩🤩🤩')
                        omomi[x]=False
                        winner2[x]= m.from_user.id
                        database.insert_point(int(winner2[x]),500,int(m.chat.id))
                        database.insert_coin(int(winner2[x]),300)
                        amir=1
        except Exception as e:
            error(e)

        try:
            if zarb[x] ==True:
                if  winner2[x]==None and m.reply_to_message.from_user.id == bot_id and 'چالش ریاضی' in str(m.reply_to_message.text) :
                    Sequence=str(int(number[0])*int(number[1]))
                    if Sequence in m.text or  Sequence == m.text:
                        await m.reply_text('اوووووووو \n  مغز گروهو  🧠 \n تو بردیو 100 امتیاز و 100 کوین 🪙 گرفتی 😍😍😍')
                        zarb[x]=False
                        winner2[x]= m.from_user.id
                        database.insert_point(int(winner2[x]),100,int(m.chat.id))
                        database.insert_coin(int(winner2[x]),100)
                        amir=1
        except Exception as e:
            error(e)

        try:
            if zarb_ALMASI[x] ==True:
                if  winner2[x]==None and m.reply_to_message.from_user.id == bot_id and 'چالش الماس' in str(m.reply_to_message.text) :
                    Sequence=str(int(int(number[0])/int(number[1])))
                    if Sequence in m.text or  Sequence == m.text:
                        await m.reply_text('''اووووووففف💦💦💦💦💦

0.2 الماس بردییییی 💥💥💥💥💥''')
                        zarb_ALMASI[x]=False
                        winner2[x]= m.from_user.id
                        database.insert_almas(winner2[x],0.1)
                        amir=1
        except :
            pass
        
        try:        
            if amir==0:
                if not winner2[x] and m.reply_to_message.from_user.id == bot_id and m.reply_to_message.text ==chl:
                    await m.reply("""وااااو اینجارو😍😍
                تو بردی امتیاز برا تو  """)
                    winner2[x]= m.from_user.id
                    database.addepoint(winner,chat)
                if not winner and m.reply_to_message.from_user.id == bot_id and m.reply_to_message.text ==chl:
                    await m.reply("""وااااو اینجارو😍😍
                تو بردی امتیاز برا تو  """)
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
                    await bot.send_message(int(database.show_sup(database.show_main(int(message.chat.id)))),text=f' #new_user🌕 \n جذب موفقیت امیز بود ! کاربر {user.mention} جوین گروه شده \n این کاربر توسط ادمین {admin_name} ذخیره شده بود !\n در مجموع {list_len} ایدی توسط ادمین ها ذخیره شده !  ',reply_markup=ply())
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
                if 'فیلم' in str(user_name) or  'حضوری' in str(user_name) or  'خاله' in str(user_name)  or  'سوپر' in str(user_name) or  'کص' in str(user_name) or  'ییو' in str(user.last_name) or   'زهرا نصیری' in str(user_name) or  'بخون' in str(user_name) or( str(user_name) in tabchi_list):
                    await bot.kick_chat_member(message.chat.id,user.id)
                    await bot.send_message(message.chat.id,f'یوزر {user.mention} به عنوان تبچی شناخته شد ! و بن شد !')
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
                            await bot.send_message(chat_id_lock,f' کاربر {user.mention}  \n ادمین گپ نبود و توسط بات یک اسپمر تشخیص داده شد ! ',reply_markup=unban_user(f'|{user.id}|{chat_id_lock}'))
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
                    await bot.send_message(int(database.show_sup(int(user_Gp))),f'#attack⚠️ \n  پلیر گروه شما در گروه دیگری جوین شد \n نام : {user.mention} \n  گروه : {title}  \n \n ----------------------------------',reply_markup=ply())
            except :

                pass
            if user.id==bot_id:
                chat_id=message.chat.id
                if leave_auto==1:
                    #try:
                        #await message.reply_text('لطفا به پشتیبانی پیام دهید ',reply_markup=posht())
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
                                        await message.reply_text(f'''『Onyx Account state 📊 ! 』

            ┏ total games 📱: 『{totalgame}』
            ┣ Account Name 📋:{user.mention}
            ┗ {user.id}**''')
                                except :
                                    totalgame=0
                                    if int(ban_state)==-850 or ban_state>=1:
                                        await bot.send_message(sup,f'#اخطار \n  کاربر {user.mention} با استیت صفر وارد گروه شده است ' ,reply_markup=ban_user(f'|{user.id}|{main}'))
                                    else:
                                        await message.reply_text(f'''این فرد فاقد استیت میباشد ! ''')
                            elif state_model==2:
                                # {"gamesPlayed":8,"won":{"total":2,"percent":25},"lost":{"total":6,"percent":75},"survived":{"total":2,"percent":25},"mostCommonRole":"Mason","mostKilled":{"name":"ᎯℳᏐℕ","id":1784441148
                                # ,"link":"\u003ca href=\u0027../Player/1784441148\u0027\u003eᎯℳᏐℕ\u003c/a\u003e","times":2},
                                # "mostKilledBy":{"name":"ᵇᶦᵗᵃ ᵇᵃᵇᵃᵉᶦ","id":958526870,"link":"\u003ca href=\u0027../Player/958526870\u0027\u003eᵇᶦᵗᵃ ᵇᵃᵇᵃᵉᶦ\u003c/a\u003e","times":2},"achievements":0}

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
                                            await bot.send_message(sup,f'#اخطار \n  کاربر {user.mention} با استیت صفر وارد گروه شده است ' ,reply_markup=ban_user(f'|{user.id}|{main}'))
                                        else:
                                            await message.reply_text(f'''این فرد فاقد استیت میباشد ! ''')

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
                                            await bot.send_message(sup,f'#اخطار \n  کاربر {user.mention} با استیت صفر وارد گروه شده است ' ,reply_markup=ban_user(f'|{user.id}|{main}'))
                                        else:
                                                await message.reply_text(f'''این فرد فاقد استیت میباشد ! ''')
                        try:    
                            if int(totalgame)<ban_state :
                                if que==0:
                                    await bot.kick_chat_member(int(main),int(user.id))
                                    await bot.send_message(main,f'voip! I banned {user.mention} ⚠️',reply_markup=unban_user(f'|{user.id}|{main}'))
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
            await query.answer('یک عدد تلسم سیاه به موجودی شما اضافه شد !🔮  ',show_alert=True)
        else:
            x=1
            await query.answer('الماس های شما کافی نیست ! 💎 ',show_alert=True)

    elif data=='zereh':
        if user_almas>=0.050:
            user_id=int(query.from_user.id)
            database.reduce_almas(user_id,0.050)
            database.add_zereh(user_id)
            await query.answer('یک عدد زد گلوله  🛡  به موجودی شما اضافه شد !  ',show_alert=True)
        else:
            x=1
            await query.answer('الماس های شما کافی نیست ! 💎 ',show_alert=True)
    
    elif data=='arvah':
        if user_almas>=0.075:
            user_id=int(query.from_user.id)
            database.reduce_almas(user_id,0.075)
            database.add_dozd(user_id)
            await query.answer('یک عدد قابلیت ارواح ☠️ به موجودی شما اضافه شد !  ',show_alert=True)
        else:
            x=1
            await query.answer('الماس های شما کافی نیست ! 💎 ',show_alert=True)
    if x==0:
        await query.edit_message_text('خرید انجام شد !',reply_markup=kharid(int(query.from_user.id)))



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
    await query.edit_message_text(f' اشتراک برای گپ {p} 30 روز تمدید شد !')
#--------------------------------------------------------------------------------------
@bot.on_callback_query(filters.regex(r"^rosta"))
@bet_Query
@alaki_query
async def bet_rosta(c,query):
    if zarib[int(query.message.chat.id)]!=False:
        shrt='تیم روستا'
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
                    await bot.send_message(int(query.from_user.id),f'شرط شما با مقدار {amount} با ضریب {zrb:.2f} بر روی {shrt} بسته شد ! \n گروه {query.message.chat.title}')
                except:
                    pass
                await query.edit_message_text('بسته شد ! در پیوی ربات اطلاعات را میتونید مشاهده کنید ')

            else:
                await query.answer('سکه ها کافی نمیباشد!')
        else:
            await query.answer('این شرط برای شما نیست \n برای شرطبندی از دستور /bet استفاده کنید !')
    else:
        await query.answer('بازی در حال اجرا نیست !')

@bot.on_callback_query(filters.regex(r"^gorg"))
@bet_Query
@alaki_query
async def bet_gorg(c,query):
    if zarib[int(query.message.chat.id)]!=False:
        shrt='تیم گرگ'
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
                    await bot.send_message(int(query.from_user.id),f'شرط شما با مقدار {amount} با ضریب {zrb:.2f} بر روی {shrt} بسته شد ! \n گروه {query.message.chat.title}')
                except:
                    pass
                await query.edit_message_text('بسته شد ! در پیوی ربات اطلاعات را میتونید مشاهده کنید ')

            else:
                await query.answer('سکه ها کافی نمیباشد!')
        else:
            await query.answer('این شرط برای شما نیست \n برای شرطبندی از دستور /bet استفاده کنید !')
    else:
        await query.answer('بازی در حال اجرا نیست !')

@bot.on_callback_query(filters.regex(r"^ghatel"))
@bet_Query
@alaki_query
async def bet_ghatel(c,query):
    if zarib[int(query.message.chat.id)]!=False:
        shrt='تیم قاتل '
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
                    await bot.send_message(int(query.from_user.id),f'شرط شما با مقدار {amount} با ضریب {zrb:.2f} بر روی {shrt} بسته شد ! \n گروه {query.message.chat.title}')
                except:
                    pass
                await query.edit_message_text('بسته شد ! در پیوی ربات اطلاعات را میتونید مشاهده کنید ')

            else:
                await query.answer('سکه ها کافی نمیباشد!')
        else:
            await query.answer('این شرط برای شما نیست \n برای شرطبندی از دستور /bet استفاده کنید !')
    else:
        await query.answer('بازی در حال اجرا نیست !')

@bot.on_callback_query(filters.regex(r"^ferghe"))
@bet_Query
@alaki_query
async def bet_ferghe(c,query):
    if zarib[int(query.message.chat.id)]!=False:
        shrt='تیم فرقه '
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
                    await bot.send_message(int(query.from_user.id),f'شرط شما با مقدار {amount} با ضریب {zrb:.2f} بر روی {shrt} بسته شد ! \n گروه {query.message.chat.title}')
                except:
                    pass
                await query.edit_message_text('بسته شد ! در پیوی ربات اطلاعات را میتونید مشاهده کنید ')

            else:
                await query.answer('سکه ها کافی نمیباشد!')
        else:
            await query.answer('این شرط برای شما نیست \n برای شرطبندی از دستور /bet استفاده کنید !')
    else:
        await query.answer('بازی در حال اجرا نیست !')

@bot.on_callback_query(filters.regex(r"^lover"))
@bet_Query
@alaki_query
async def bet_lover(c,query):
    if zarib[int(query.message.chat.id)]!=False:
        shrt='آتش🔥  '
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
                    shrt='بمب گذار'
                
                try:
                    await bot.send_message(int(query.from_user.id),f'شرط شما با مقدار {amount} با ضریب {zrb:.2f} بر روی {shrt} بسته شد ! \n گروه {query.message.chat.title}')
                except:
                    pass
                await query.edit_message_text('بسته شد ! در پیوی ربات اطلاعات را میتونید مشاهده کنید ')
            else:
                await query.answer('سکه ها کافی نمیباشد!')
        else:
            await query.answer('این شرط برای شما نیست \n برای شرطبندی از دستور /bet استفاده کنید !')
    else:
        await query.answer('بازی در حال اجرا نیست !')

@bot.on_callback_query(filters.regex(r"^vamp"))
@bet_Query
@alaki_query
async def bet_vamp(c,query):
    if zarib[int(query.message.chat.id)]!=False:
        shrt='ومپ ها '
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
                    await bot.send_message(int(query.from_user.id),f'شرط شما با مقدار {amount} با ضریب {zrb:.2f} بر روی {shrt} بسته شد ! \n گروه {query.message.chat.title}')
                except:
                    pass
                await query.edit_message_text('بسته شد ! در پیوی ربات اطلاعات را میتونید مشاهده کنید ')

            else:
                await query.answer('سکه ها کافی نمیباشد!')
        else:
            await query.answer('این شرط برای شما نیست \n برای شرطبندی از دستور /bet استفاده کنید !')
    else:
        await query.answer('بازی در حال اجرا نیست !')

@bot.on_callback_query(filters.regex(r"^monaf"))
@bet_Query
@alaki_query
async def bet_monaf(c,query):
    if zarib[int(query.message.chat.id)]!=False:
        shrt='منافق 👺'
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
                    await bot.send_message(int(query.from_user.id),f'شرط شما با مقدار {amount} با ضریب {zrb:.2f} بر روی {shrt} بسته شد ! \n گروه {query.message.chat.title}')
                except:
                    pass
                await query.edit_message_text('بسته شد ! در پیوی ربات اطلاعات را میتونید مشاهده کنید ')

            else:
                await query.answer('سکه ها کافی نمیباشد!')
        else:
            await query.answer('این شرط برای شما نیست \n برای شرطبندی از دستور /bet استفاده کنید !')
    else:
        await query.answer('بازی در حال اجرا نیست !')
#----------------------------------------------------------------------ray
@bot.on_callback_query(filters.regex(r"^bastan"))
@alaki_query
async def bastan_ray(c,query):
    chat=int(query.message.chat.id)
    if shekar[chat]==int(query.from_user.id):
        await query.edit_message_text('بسته شد !')
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
            await query.edit_message_text(f' رای بر روی {user_name} قرار گرفت ')
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
                await bot.send_message(chat,text=f'''💥⚜️رای 


            🔰  **{user_name}** 🔰 💥 ''' ,reply_markup=skii())
                await asyncio.sleep(6)

                await bot.send_message(chat,text=f'''💥⚜️رای 


            🔰  **{user_name}** 🔰 💥 ''' ,reply_markup=skii())
                await asyncio.sleep(6)
                await bot.send_message(chat,text=f'''💥⚜️رای 


            🔰  **{user_name}** 🔰 💥 ''' ,reply_markup=skii())
                await asyncio.sleep(6)
                await bot.send_message(chat,text=f'''💥⚜️رای 


            🔰  **{user_name}** 🔰 💥 ''' ,reply_markup=skii())
                await asyncio.sleep(6)
                await bot.send_message(chat,text=f'''💥⚜️رای 


            🔰  **{user_name}** 🔰 💥 ''' ,reply_markup=skii())
            spam[int(chat)]=False

        else:
            await query.answer('لطا صبر کنید تا رای فعلی تموم شود !', show_alert=True)
    elif nazer[chat]==int(query.from_user.id):
        if int(chat) not in spam:
            spam[int(chat)]=False
        if spam[int(chat)]==False:
            await query.edit_message_text(f' رای بر روی {user_name} قرار گرفت ')
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
                await bot.send_message(chat,text=f'''💥⚜️رای 


            🔰  **{user_name}** 🔰 💥 ''' ,reply_markup=nazeram())
                await asyncio.sleep(6)

                await bot.send_message(chat,text=f'''💥⚜️رای 


            🔰  **{user_name}** 🔰 💥 ''' ,reply_markup=nazeram())
                await asyncio.sleep(6)
                await bot.send_message(chat,text=f'''💥⚜️رای 


            🔰  **{user_name}** 🔰 💥 ''' ,reply_markup=nazeram())
                await asyncio.sleep(6)
                await bot.send_message(chat,text=f'''💥⚜️رای 


            🔰  **{user_name}** 🔰 💥 ''' ,reply_markup=nazeram())
                await asyncio.sleep(6)
                await bot.send_message(chat,text=f'''💥⚜️رای 


            🔰  **{user_name}** 🔰 💥 ''' ,reply_markup=nazeram())
            spam[int(chat)]=False
               
        else:
            await query.answer('لطا صبر کنید تا رای فعلی تموم شود !', show_alert=True)

    else:
        await query.answer('『شما  شکارچی یا ناظر  بازی نیستید📌』', show_alert=True)







                        

#-------------------------------------------------------------------ghaleb 
@bot.on_callback_query(filters.regex(r"^ghaleb"))
@alaki_query
async def ghaleb_Query_Choose(c,query):
    ghaleb_hash=str(query.data).split(' ')[-1]
    ghaleb=str(database.show_ghalebs(ghaleb_hash))
    await query.edit_message_text(f'قالب انتخاب شده  \n -----------------------------------------\n \n\n{ghaleb}', reply_markup=taeed_ghaleb(ghaleb_hash))

@bot.on_callback_query(filters.regex(r"^taeed"))
@alaki_query
async def ghaleb_taeed_Query_Choose(c,query):
    user_almas=float(database.useralmas(int(query.from_user.id)))
    ghaleb_hash=str(query.data).split(' ')[-1]
    ghaleb_price=float(database.show_price(ghaleb_hash))
    if user_almas>=ghaleb_price:
        database.reduce_almas(int(query.from_user.id),ghaleb_price)
        database.insert_user_ghaleb(int(query.from_user.id),hashs=ghaleb_hash)
        await query.edit_message_text('قالب خریداری شد !')
    else:
        await query.answer(f'الماس شما کافی نیست \n الماس شما : {user_almas} ')


@bot.on_callback_query(filters.regex(r"^camcel"))
@alaki_query
async def undo_bying_ghaleb(c,query):
    await query.edit_message_text('کدام قالب رو میخواهید ببینید ؟' , reply_markup=ghaleb_inline())
#----------------------------------------------------------------------
@bot.on_callback_query(filters.regex(r"^warn"))
@Admin_Query
async def warn_Query_Choose(c,query):
    warn=str(query.data).split(' ')[-1]
    database.set_warn(int(database.show_main(int(query.message.chat.id))),int(warn))
    await query.answer(f' قفل وارن  بر روی {warn} تنظیم شد!', show_alert=True)

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
                    await query.answer(f'خودت رو نجات دادی  \n 60 کوین 🪙 ازت کم شد!', show_alert=True)
                    await query.edit_message_text('همه قدرتامو از دست دادم :) ',reply_markup=rj())
                    try:
                        muted_admins[int(query.message.chat.id)].pop(int(unmute_p))
                        muted_hour[int(query.message.chat.id)].pop(int(unmute_p))
                        muted[int(query.message.chat.id)].pop(int(unmute_p))
                    except :
                        pass
                    await query.message.reply_text(f'چه اتفاقی افتاده 🔮🔮🔮 \n دیگه دسترسی به هیچی ندارمم🧿\n \n این جادوگر {user2} منو تسخیر کرده و خودشو از سکوت ازاد کرده \n و {user1} سکوت کرده 😱😱😱')
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
                    await query.answer(f'چه دوست خوبی ! دوستتو نجات دادی \n 60 کوین 🪙 ازت کم شد!', show_alert=True)
                    await query.edit_message_text('همه قدرتامو از دست دادم :) ',reply_markup=rj())
                    try:
                        muted_admins[int(query.message.chat.id)].pop(int(unmute_p))
                        muted_hour[int(query.message.chat.id)].pop(int(unmute_p))
                        muted[int(query.message.chat.id)].pop(int(unmute_p))
                    except :
                        pass
                    await query.message.reply_text(f'چه اتفاقی داره میوفته  🤨🤨 \n قدرتام کووو😱😱 \n \n داره جه اتفاقی میوفتههههه😵😵😵 \n این جادوگر {query.from_user.mention} منو تسخیر کرد و مجبورم کرد \n {user1} که دوستشو سکوت کرده بود سکوت کنم \n و {user2} رو ازاد کنم ')
                    database.reduce_coin(int(query.from_user.id),60)
            except :
                await query.answer(f'اول از دستور /regester استفاده کن تا ثبت بشی !', show_alert=True)


@bot.on_callback_query(filters.regex(r"^state"))
@Admin_Query
async def state_Query_Choose(c,query):
    State_M=str(query.data).split(' ')[-1]
    database.set_state(int(database.show_main(int(query.message.chat.id))),int(State_M))
    try:
        if int(State_M)==-850:
            stt='حالت هشدار دهی کاربران بدون استیت فعال شد !'
            await query.answer(f' قفل استیت  بر روی {stt} تنظیم شد!', show_alert=True)
            t='حالت هشدار ⚠️'
        else:
            await query.answer(f' قفل استیت  بر روی {State_M} تنظیم شد!', show_alert=True)
            t=State_M
    except :
        await query.answer(f' قفل استیت  بر روی {State_M} تنظیم شد!', show_alert=True)
        t=State_M

    await query.edit_message_text(f'قفل استیت بر روی {t} قرار گرفت !',reply_markup=state_Coutn(t,int(database.show_main(int(query.message.chat.id)))))
@bot.on_callback_query(filters.regex(r"^warpnp$"))
@Admin_Query
async def Warn_Callback(c,query):
    a=int(database.show_warn(int(database.show_main(int(query.message.chat.id)))))
    if a==0:
        text="غیرفعال🔓"
    else:
        text=a
    await query.edit_message_text('لطفا تعداد دفعات AFK شدن , برای وارن گرفتن را انتخاب کنید !',reply_markup=warn_Count(text))

@bot.on_callback_query(filters.regex(r"^statpelock$"))
@Admin_Query
async def State_Callback(c,query):
    a=int(database.show_state(int(database.show_main(int(query.message.chat.id)))))
    if a==0:
        text="غیرفعال🔓"
    else:
        text=a
    if a==-850:
        text='حالت هشدار ⚠️'
    else:
        text=a
    await query.edit_message_text('لطفا حد مجاز استیت وارد شدن به گروه را تعیین کنید !',reply_markup=state_Coutn(text,int(database.show_main(int(query.message.chat.id)))))
    await query.answer('@DarkHelperChannel !')

@bot.on_callback_query(filters.regex(r"^point"))
async def point_callback(c,query):
    await query.answer('برای نکست اختصاصی جلوی دستور /mynext متن مورد نظرتو بنویس 🧸', show_alert=True)


@bot.on_callback_query(filters.regex(r"^undo"))
@Admin_Query
async def undo_pannel(c,query):
    gp=int(database.show_main(int(query.message.chat.id)))
    await query.edit_message_text('به پنل بازگشتید !',reply_markup=(await pannel(gp)))
    await query.answer('@DarkHelperChannel !')

@bot.on_callback_query(filters.regex(r"^close"))
@Admin_Query
async def close_pannel(c,query):
    await query.edit_message_text(' بسته شد !',reply_markup=rj())
    
#------------------------BOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOM
@bot.on_callback_query(filters.regex(r"^boom"))
async def bOOm(c,query):
    await query.answer('این شرط بسته شده است !')

@bot.on_callback_query(filters.regex(r"^bardasht"))
async def bardasht_En(c,query):
    zarib_en=float(str(query.data).split(' ')[1])
    hash=int(str(query.data).split(' ')[2])
    if int(query.from_user.id) in enfejar[int(query.message.chat.id)] and int(hash)==int(enfejar_hash[int(query.message.chat.id)]):
        amount=int(enfejar[int(query.message.chat.id)][int(query.from_user.id)])
        kol=int((amount*zarib_en)-amount)
        database.insert_coin(int(query.from_user.id),kol)
        enfejar[int(query.message.chat.id)].pop(int(query.from_user.id))
        await query.answer('برداشته شد !',show_alert=True)
        await query.message.reply_text(f'کاربر {query.from_user.mention} کوین خود را با ضریب {zarib_en} برداشت کرد 🟢! \n سود 💰 : {kol}')
    else:
        await query.answer('  شما در شرطبندی نیستید  !',show_alert=True)
#-------------------------------------state            
# [InlineKeyboardButton(f'24 ساعت  {rooz}', callback_data='kamel'),InlineKeyboardButton(f'شبانه  {shaab}', callback_data='shab')],

@bot.on_callback_query(filters.regex(r"^kamel"))
@Admin_Query
async def kamel_lock(c,query):
    a=int(database.show_state(int(database.show_main(int(query.message.chat.id)))))
    if a==0:
        text="غیرفعال🔓"
    else:
        text=a
    if a==-850:
        text='حالت هشدار ⚠️'
    else:
        text=a
    database.set_shab_off(int(database.show_main(int(query.message.chat.id))))
    await query.answer('قفل استیت بر روی روزانه قرار گرفت !')
    await query.edit_message_text('تغییرات اعمال شد !',reply_markup=state_Coutn(text,int(database.show_main(int(query.message.chat.id)))))
    



@bot.on_callback_query(filters.regex(r"^shab"))
@Admin_Query
async def rooz_lock(c,query):
    a=int(database.show_state(int(database.show_main(int(query.message.chat.id)))))
    if a==0:
        text="غیرفعال🔓"
    else:
        text=a
    if a==-850:
        text='حالت هشدار ⚠️'
    else:
        text=a
    database.set_shab_on(int(database.show_main(int(query.message.chat.id))))
    await query.answer('قفل استیت بر روی شبانه قرار گرفت !')
    await query.edit_message_text('تغییرات اعمال شد !',reply_markup=state_Coutn(text,int(database.show_main(int(query.message.chat.id)))))
    

@bot.on_callback_query(filters.regex(r"^onyx"))
@Admin_Query
async def set_onyx_lock(c,query):
    a=int(database.show_state(int(database.show_main(int(query.message.chat.id)))))
    if a==0:
        text="غیرفعال🔓"

    else:
        text=a

    if a==-850:
        text='حالت هشدار ⚠️'
    else:
        text=a
    database.set_state_model_onyx(int(database.show_main(int(query.message.chat.id))))
    await query.answer('نوع  قفل استیت بر روی اونیکس قرار گرفت !', show_alert=True)
    await query.edit_message_text('تغییرات اعمال شد !',reply_markup=state_Coutn(text,int(database.show_main(int(query.message.chat.id)))))
    

@bot.on_callback_query(filters.regex(r"^black"))
@Admin_Query
async def set_black_lock(c,query):
    a=int(database.show_state(int(database.show_main(int(query.message.chat.id)))))
    if a==0:
        text="غیرفعال🔓"
    else:
        text=a
    if a==-850:
        text='حالت هشدار ⚠️'
    else:
        text=a
    database.set_state_model_black(int(database.show_main(int(query.message.chat.id))))
    await query.answer('نوع  قفل استیت بر روی بلک قرار گرفت !', show_alert=True)
    await query.edit_message_text('تغییرات اعمال شد !',reply_markup=state_Coutn(text,int(database.show_main(int(query.message.chat.id)))))
    

@bot.on_callback_query(filters.regex(r"^werewolf"))
@Admin_Query
async def set_werewolf_lock(c,query):
    a=int(database.show_state(int(database.show_main(int(query.message.chat.id)))))
    if a==0:
        text="غیرفعال🔓"
    else:
        text=a
    if a==-850:
        text='حالت هشدار ⚠️'
    else:
        text=a
    database.set_state_model_werewolf(int(database.show_main(int(query.message.chat.id))))
    await query.answer('نوع  قفل استیت بر روی ورولف قرار گرفت !', show_alert=True)
    await query.edit_message_text('تغییرات اعمال شد !',reply_markup=state_Coutn(text,int(database.show_main(int(query.message.chat.id)))))
    
#-----------------------------------------
@bot.on_callback_query(filters.regex(r"^autotag"))
@Admin_Query
async def auto_tag_Func(c,query):
    gp=query.message.chat.id
    a=database.show_tag(int(database.show_main(int(gp))))
    if a==1:
        roshan='خاموش '
        database.set_tag_off(int(database.show_main(int(gp))))
    else:
        roshan='روشن'
        database.set_tag_on(int(database.show_main(int(gp))))
    gp=int(database.show_main(int(query.message.chat.id)))
    await query.edit_message_text(f'پنل برای شما باز شد ,میتوانید از پنل تنظیمات جدید را اعمال کنید \n تگ خودکار {roshan} شد  !',reply_markup=(await pannel(gp)))
    await query.answer('@DarkHelperChannel !')


@bot.on_callback_query(filters.regex(r"^mokamel"))
@Admin_Query
async def mokamel_warn_fank(c,query):
    gp=query.message.chat.id
    a=database.show_mokamel(int(database.show_main(int(gp))))
    if a==1:
        roshan='خاموش '
        database.set_mokamel_off(int(database.show_main(int(gp))))
    else:
        roshan='روشن'
        database.set_mokamel_on(int(database.show_main(int(gp))))
    gp=int(database.show_main(int(query.message.chat.id)))
    await query.edit_message_text(f'پنل برای شما باز شد ,میتوانید از پنل تنظیمات جدید را اعمال کنید \n  وارن خودکار به افک شدن در نقش مکمل فعال شد {roshan} شد  !',reply_markup=(await pannel(gp)))
    await query.answer('@DarkHelperChannel !')

@bot.on_callback_query(filters.regex(r"^supdel"))
@Admin_Query
async def supdelete_inline(c,query):
    gp=query.message.chat.id
    a=database.show_supdel(int(database.show_main(int(gp))))
    if a==1:
        roshan='خاموش '
        database.set_supdel_off(int(database.show_main(int(gp))))
    else:
        roshan='روشن'
        database.set_supdel_on(int(database.show_main(int(gp))))
    gp=int(database.show_main(int(query.message.chat.id)))
    await query.edit_message_text(f'پنل برای شما باز شد ,میتوانید از پنل تنظیمات جدید را اعمال کنید \n پاکسازی ساپورت  {roshan} شد  !',reply_markup=(await pannel(gp)))
    await query.answer('@DarkHelperChannel !')

@bot.on_callback_query(filters.regex(r"^modiriat"))
@Admin_Query
async def modiriar_callback_inline(c,query):
    await query.edit_message_text('تغییرات مورد نظر را اعمال کنید !', reply_markup=modiriat_inline(int(database.show_main(int(query.message.chat.id)))))


@bot.on_callback_query(filters.regex(r"^control"))
@Admin_Query
async def control_inline_calback(c,query):
    gp=query.message.chat.id
    a=database.show_control(int(database.show_main(int(gp))))
    if a==1:
        roshan='خاموش '
        database.set_control_off(int(database.show_main(int(gp))))
    else:
        roshan='روشن'
        database.set_control_on(int(database.show_main(int(gp))))
    gp=int(database.show_main(int(query.message.chat.id)))
    await query.edit_message_text(f'پنل برای شما باز شد ,میتوانید از پنل تنظیمات جدید را اعمال کنید \n استفاده از دستورات    {roshan} شد  !',reply_markup=( modiriat_inline(gp)))
    await query.answer('@DarkHelperChannel !')

@bot.on_callback_query(filters.regex(r"^antibot"))
@Admin_Query
async def antibot_inline(c,query):
    gp=query.message.chat.id
    a=database.show_anti_bot(int(database.show_main(int(gp))))
    if a==1:
        roshan='خاموش '
        database.set_anti_bot_off(int(database.show_main(int(gp))))
    else:
        roshan='روشن'
        database.set_anti_bot_on(int(database.show_main(int(gp))))
    gp=int(database.show_main(int(query.message.chat.id)))
    await query.edit_message_text(f'پنل برای شما باز شد ,میتوانید از پنل تنظیمات جدید را اعمال کنید \n انتی ربات     {roshan} شد  !',reply_markup=( modiriat_inline(gp)))
    await query.answer('@DarkHelperChannel !')



@bot.on_callback_query(filters.regex(r"^saver"))
@Admin_Query
async def supdelete_inline(c,query):
    gp=query.message.chat.id
    a=database.show_role_saver(int(database.show_main(int(gp))))
    if a==1:
        roshan='خاموش '
        database.set_role_saver_off(int(database.show_main(int(gp))))
    else:
        roshan='روشن'
        database.set_role_saver_on(int(database.show_main(int(gp))))
    gp=int(database.show_main(int(query.message.chat.id)))
    await query.edit_message_text(f'پنل برای شما باز شد ,میتوانید از پنل تنظیمات جدید را اعمال کنید \n رول سیور   {roshan} شد  !',reply_markup=(await pannel(gp)))
    await query.answer('@DarkHelperChannel !')

@bot.on_callback_query(filters.regex(r"^tagsup"))
@Admin_Query
async def suptag_Func(c,query):
    gp=query.message.chat.id
    a=database.show_suptag(int(database.show_main(int(gp))))
    if a==1:
        roshan='خاموش '
        database.set_suptag_off(int(database.show_main(int(gp))))
    else:
        roshan='روشن'
        database.set_suptag_on(int(database.show_main(int(gp))))
    gp=int(database.show_main(int(query.message.chat.id)))
    await query.edit_message_text(f'پنل برای شما باز شد ,میتوانید از پنل تنظیمات جدید را اعمال کنید \n تگ خودکار {roshan} شد  !',reply_markup=(await pannel(gp)))
    await query.answer('@DarkHelperChannel !')



@bot.on_callback_query(filters.regex(r"^lock"))
@Admin_Query
async def auto_lock_Func(c,query):
    gp=query.message.chat.id
    a=database.show_lock(int(database.show_main(int(gp))))
    if a==1:
        roshan='خاموش '
        database.set_lock_off(int(database.show_main(int(gp))))
    else:
        roshan='روشن'
        database.set_lock_on(int(database.show_main(int(gp))))
    gp=int(database.show_main(int(query.message.chat.id)))
    await query.edit_message_text(f'پنل برای شما باز شد ,میتوانید از پنل تنظیمات جدید را اعمال کنید \n قفل ساپورت   {roshan} شد  !',reply_markup=(await pannel(gp)))
    await query.answer('@DarkHelperChannel !')

@bot.on_callback_query(filters.regex(r"^deltag"))
@Admin_Query
async def deltag_Func(c,query):
    gp=query.message.chat.id
    a=database.show_deltag(int(database.show_main(int(gp))))
    if a==1:
        roshan='خاموش '
        database.set_autodel_off(int(database.show_main(int(gp))))
    else:
        roshan='روشن'
        database.set_autodel_on(int(database.show_main(int(gp))))
    gp=int(database.show_main(int(query.message.chat.id)))
    await query.edit_message_text(f'پنل برای شما باز شد ,میتوانید از پنل تنظیمات جدید را اعمال کنید \n سیستم ضد فیلترینگ  {roshan} شد  !',reply_markup=(await pannel(gp)))
    await query.answer('@DarkHelperChannel !')


@bot.on_callback_query(filters.regex(r"^role"))
@Admin_Query
async def role_func(c,query):
    gp=query.message.chat.id
    a=database.show_role(int(database.show_main(int(gp))))
    if a==1:
        roshan='خاموش '
        database.set_role_off(int(database.show_main(int(gp))))
    else:
        roshan='روشن'
        database.set_role_on(int(database.show_main(int(gp))))
    gp=int(database.show_main(int(query.message.chat.id)))
    await query.edit_message_text(f'پنل برای شما باز شد ,میتوانید از پنل تنظیمات جدید را اعمال کنید \n پاکسازی خودکار {roshan} شد  !',reply_markup=(await pannel(gp)))
    await query.answer('@DarkHelperChannel !')

@bot.on_callback_query(filters.regex(r"^afarin"))
async def ski_func(c,query):
    await query.answer('افرین ! توهم بلدی کلیک کنی 😐♥️ حالا برو رایتو بده ', show_alert=True)

@bot.on_callback_query(filters.regex(r"^admin"))
@Admin_Query
async def admin_Query(c,query):
    a=len(database.show_admins(int(database.show_main(int(query.message.chat.id)))))
    await query.edit_message_text(f'عملیات مورد نظر را انتخاب کنید !',reply_markup=admins_Gone(a))

@bot.on_callback_query(filters.regex(r"^bebin"))
@Admin_Query
async def admin_list_query(c,query):
    await query.answer(' با دستور /adminlist  لیست ادمین هارو ببینید', show_alert=True)

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
        await query.edit_message_text(f'تعداد {q} ادمین به لیست اضافه شدند و {a} از قبل در لیست بودند !')
    except :
        await query.edit_message_text('مشکلی پیش امد !  ', reply_markup=posht())


@bot.on_callback_query(filters.regex(r"^tansil"))
@Admin_Query
async def tansil_admin(c,query):
    try:
        database.delete_admin_all(int(database.show_main(int(query.message.chat.id))))
        await query.edit_message_text(f'تمامی ادمین ها از لیست پاک شدند !')
    except:
        await query.edit_message_text('مشکلی پیش امد !  ', reply_markup=posht())



#11111111111111111111111111111111111111111111111111111111111111111111111111111111
@bot.on_callback_query(filters.regex(r"^sargarmi"))
@Admin_Query
async def sargarmi_Callback(c,query):
    gp=int(query.message.chat.id)
    await query.edit_message_text('بخش سرگرمی !', reply_markup=sargarmi_inline(gp))


@bot.on_callback_query(filters.regex(r"^onakhbar"))
@Admin_Query
async def akhbar_Callback(c,query):
    gp=int(query.message.chat.id)
    a=database.show_akhbar(int(database.show_main(int(gp))))
    if a==1:
        database.set_akhbar_off(int(database.show_main(int(gp))))
    else:
        database.set_akhbar_on(int(database.show_main(int(gp))))
    await query.edit_message_text('بخش سرگرمی !', reply_markup=sargarmi_inline(gp))
    await query.answer('تنظیمات اعمال شد !')


@bot.on_callback_query(filters.regex(r"^onnext"))
@Admin_Query
async def next_Callback(c,query):
    gp=int(query.message.chat.id)
    a=database.show_next(int(database.show_main(int(gp))))
    if a==1:
        database.set_next_off(int(database.show_main(int(gp))))
    else:
        database.set_next_on(int(database.show_main(int(gp))))
    await query.edit_message_text('بخش سرگرمی !', reply_markup=sargarmi_inline(gp))
    await query.answer('تنظیمات اعمال شد !')

@bot.on_callback_query(filters.regex(r"^onhis"))
@Admin_Query
async def his_Callback(c,query):
    gp=int(query.message.chat.id)
    a=database.show_sargarmi(int(database.show_main(int(gp))))
    if a==1:
        database.set_sargarmi_off(int(database.show_main(int(gp))))
    else:
        database.set_sargarmi_on(int(database.show_main(int(gp))))
    await query.edit_message_text('بخش سرگرمی !', reply_markup=sargarmi_inline(gp))
    await query.answer('تنظیمات اعمال شد !')

@bot.on_callback_query(filters.regex(r"^onbet"))
@Admin_Query
async def bet_Callback(c,query):
    gp=int(query.message.chat.id)
    a=database.show_bet(int(database.show_main(int(gp))))
    if a==1:
        database.set_bet_off(int(database.show_main(int(gp))))
    else:
        database.set_bet_on(int(database.show_main(int(gp))))
    await query.edit_message_text('بخش سرگرمی !', reply_markup=sargarmi_inline(gp))
    await query.answer('تنظیمات اعمال شد !')

@bot.on_callback_query(filters.regex(r"^onenfejar"))
@Admin_Query
async def boom_Callback(c,query):
    gp=int(query.message.chat.id)
    a=database.show_boom(int(database.show_main(int(gp))))
    if a==1:
        database.set_boom_off(int(database.show_main(int(gp))))
    else:
        database.set_boom_on(int(database.show_main(int(gp))))
    await query.edit_message_text('بخش سرگرمی !', reply_markup=sargarmi_inline(gp))
    await query.answer('تنظیمات اعمال شد !')


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

    await query.edit_message_text('انجام شد !',reply_markup=(await pannel(main)))



@bot.on_callback_query(filters.regex(r"^emoji1$"))
@Admin_Query_await
async def emoji1_set_Query(c,query):
    await query.edit_message_text('ایموجی مورد نظرتون رو انتخاب کنید !',reply_markup=emojis1_in())

@bot.on_callback_query(filters.regex(r"^emoji2$"))
@Admin_Query_await
async def emoji2_set_Query(c,query):
    await query.edit_message_text('ایموجی مورد نظرتون رو انتخاب کنید !',reply_markup=emojis2_in())

@bot.on_callback_query(filters.regex(r"^emoji3$"))
@Admin_Query_await
async def emoji3_set_Query(c,query):
    await query.edit_message_text('ایموجی مورد نظرتون رو انتخاب کنید !',reply_markup=emojis3_in())


@bot.on_callback_query(filters.regex(r"^bamahas$"))
@Admin_Query_await
async def emoji_help_Query(c,query):
    await query.answer('ایموجی های امتیاز دهی را از دکمه های زیر انتخاب کنید !', show_alert=True)


@bot.on_callback_query(filters.regex(r"^setemj1"))
@Admin_Query_await
async def emoji_main1_Query(c,query):
    emoji=str(query.data).split(' ')[1]
    database.set_emoji1(int(database.show_main(int(query.message.chat.id))),str(emoji))
    gp=int(database.show_main(int(query.message.chat.id)))
    await query.edit_message_text('به پنل بازگشتید !',reply_markup=(await pannel(gp)))
    


@bot.on_callback_query(filters.regex(r"^setemj2"))
@Admin_Query_await
async def emoji_main2_Query(c,query):
    emoji=str(query.data).split(' ')[1]
    database.set_emoji2(int(database.show_main(int(query.message.chat.id))),str(emoji))
    gp=int(database.show_main(int(query.message.chat.id)))
    await query.edit_message_text('به پنل بازگشتید !',reply_markup=(await pannel(gp)))
    


@bot.on_callback_query(filters.regex(r"^setemj3"))
@Admin_Query_await
async def emoji_main3_Query(c,query):
    emoji=str(query.data).split(' ')[1]
    database.set_emoji3(int(database.show_main(int(query.message.chat.id))),str(emoji))
    gp=int(database.show_main(int(query.message.chat.id)))
    await query.edit_message_text('به پنل بازگشتید !',reply_markup=(await pannel(gp)))
    
#22222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
@bot.on_callback_query(filters.regex(r"^hoosh"))
async def hoosh_Query(c,query):
    await query.answer('با جواب دادن چالش میتونی هوش خودتو بالا ببری 🚀', show_alert=True)

@bot.on_callback_query(filters.regex(r"^emrooz_amar"))
@Admin_Query_await
async def stats_today(c,query):
    await query.edit_message_text('کدام امار امروز را میخواهید !',reply_markup=amar_gap())


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
    await bot.send_photo(int(query.message.chat.id), 'plot3show.jpg' , caption = 'امار نسبت افک به پلیر در 24 ساعت گذشته ')
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
    await bot.send_photo(int(query.message.chat.id), 'plot5show.jpg', caption ="سه نمودار با توجه به جوین تایم ها در بازی های انجام شده ")
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
        await query.edit_message_text(f'یوزر از گروه توسط {query.from_user.mention} بن شد ', reply_markup=rj())
    except:
        await query.edit_message_text('مشکلی پیش امد !  ', reply_markup=posht())


@bot.on_callback_query(filters.regex(r"^unban"))
@Admin_Query
async def Unban_Query(c,query):
    try:
        data=str(query.data)
        user=int(data.split('|')[-2])
        ch=int(data.split('|')[-1])
        await bot.unban_chat_member(ch,user)
        await query.edit_message_text(f'یوزر از گروه توسط {query.from_user.mention} آن بن شد ', reply_markup=rj())
    except:
        await query.edit_message_text('مشکلی پیش امد !  ', reply_markup=posht())
        
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
        await query.answer(f'میانگین های امروز ✤  پلیر : {miangin_player} \n افک :{miangin_afk}  🛑  جوین تایم :{join_time} | ', show_alert=True)
    except ZeroDivisionError:
        await query.answer('هیج بازی ثبت نشده ', show_alert=True)
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
                    await message.reply_text(f'این یوزر  {message.from_user.mention} یک اتکر تشخیص داده شد و بن شد !')
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
                                cap='''ای ملعون !!!!
            ادب رو رعایت نکردی و من تو را به مجازات میرسانم 🤬
            یک دهم سکه هاتو خوردم تا یاد بگیری با ادب باشی👿'''
                            elif p==2:
                                photo='decup.jpg'
                                cap='''یک دهم ، سکه هاتو دزدیدم🗡😅
        بهش بگو حالا حالا ها باید دنبالم بگرده 🤝🚔'''
                            else:
                                photo='bye.jpg'
                                cap='''دزده خودم بودم 🤝 
            یک دهم کویناتو دزدیم بای'''
                            dozdi[int(m.chat.id)]=int(m.from_user.id)
                            await m.reply_photo(photo=photo,caption =cap)
                            database.reduce_coin(int(m.from_user.id),int(reduce_coin))
                        else:
                            p=dozdi_aks[int(m.chat.id)]
                            if p==1:
                                back='bye.jpg'
                                capt='''بی ادبی شما با با نمکی همراه بود ، پس پولی از شما کسر نمیشود ، بای
        (اینکه کوین نداشتی هم بی تاثیر نبود ۵۰ کوین دادم بهت )'''
                            elif p==2:
                                back='sabz.jpg'
                                capt='''عه سلام حاج ارجی 😐
        این داشمون پول نداشت دستمو کردم تو جیبش براش پول بزارم 😅
        ۵۰ تا دادم بهش 💸'''
                            else:
                                back='sheytan.jpg'
                                capt='''ای شیطان خبیث 🙀
        تو کوین نداشتی و وقتی من برای خوردن کوین هایت امدم ، مرا خوردی 🥲
        دگر این سمت ها پیدایم نمیشود 😞'''
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
                            s='🌟لیست ادمین ها بر اساس فعالیت ! 🌟\n \n TAG | JOIN | AFK \n '
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
                                s+=f'🔥 {i[2]}  - {i[3]} - {i[1]}  🔥{tg}\n'
                                if TEDAD==30:
                                    await bot.send_message(int(database.show_sup(int(chat))),s,reply_markup=rj())
                                    TEDAD=0
                                    s='🌟لیست ادمین ها بر اساس فعالیت ! 🌟\n \n TAG | JOIN | AFK \n '
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
                                await bot.send_message(int(database.show_sup(int(i[0]))),text=f'#اطلاعیه  📢  \n شما فقط 24 ساعت برای تمدید اشتراک فرصت دارید \n \n برای تمدید ربات به پشتیبانی مراجعه کنید ✮ ✮ ✮  \n \n زمان اشتراک : {i[1]}  \n درصورت اتمام تمام اطلاعات گپ شما پاک خواهد شد ! \n \n 🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥',reply_markup=posht())
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
                            await bot.send_message(int(database.show_sup(int(i[0]))),text=f'اشتراک ربات شما تمام شد ! ',reply_markup=posht())
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
                        await m.reply_text('لطفا به پشتیبانی پیام دهید ',reply_markup=posht())
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
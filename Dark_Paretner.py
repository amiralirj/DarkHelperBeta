from pyrogram import Client,filters
import database
import random
import datetime
import operator
import time
import re 
import asyncio
from pyrogram.types import ChatEventFilter
database.start_Sql()
time_db=dict()
hash=dict()
mio=dict()
auto_join=dict()
zarib=dict
afk=dict()
dead_roles=dict()
api_id =2586462
sup=1698230457
api_hash = '68542129131999986899b84a10a6170c'
bot = Client('amirairj-partner', api_id, api_hash,workers=25)
text_Hash='hash:amiralirj}[koskhol]HHHH:'
wwbots=[854021534,175844556,1029642148,618096097]
sec=dict()
f=database.show_gaps()
for i in f:
    print(i[0])
    afk[int(i[0])]=dict()
    auto_join[int(i[0])]=True
def Admin(func):
    async def check(Client, message):
        admin_bool=database.admin_cheak(int(message.from_user.id),int(database.show_main(int(message.chat.id))))
        ban_bool=database.ban_cheak(int(message.from_user.id))
        if admin_bool==True:
            if ban_bool==False:
                await func(Client,message)
            else:
                await message.reply_text('شما از استفاده ی ربات محروم هستید ')
        elif message.from_user.id==1698230457:
            await func(Client,message)
    return check

def alaki(func):
    async def check(Client, message):
        await func(Client,message)
    return check

def hash_set(chat_id,text):
    text=f'#amiralirj {text_Hash}{chat_id}{text_Hash}{text}{text_Hash}'
    return text

def find_Main_Id(text:str):
    a=text.split('hash:amiralirj}[koskhol]HHHH:')
    return a

#-------------------------------------------------------------bet
#--------------------------------------------------------------------bet
                                                                            # 1   rosta
                                                                            # 2   gorg 
                                                                            # 3   ghatel
                                                                            # 4   ferghe 
                                                                            # 5   lover
                                                                            # 6   vamp 

                  
@bot.on_message( ~filters.me & (filters.regex(r'روستاییا تونستن همه دشمناشونو شکست بدن')|filters.regex(r'روستاییا بازی رو بردن')|filters.regex(r'طولانی حالا آرامش خاصی در روستا')|filters.regex(r'روستاییای فراموشکار بازی رو بردن'))& filters.group & filters.user([854021534,175844556,1029642148,618096097]))
async def roosta(client, message):
    chat_id=int(message.chat.id)
    f=hash_set(chat_id,'1')
    await bot.send_message('@darkhelperrobot',f'{f} bet')


@bot.on_message( ~filters.me & (filters.regex(r'تیم گرگها برنده بازی شد')|filters.regex(r'گرگا بردن')|filters.regex(r'گرگها برنده شدن')|filters.regex(r'تک گرگ برنده‌ی بازی')|filters.regex(r'تک گرگه فراموشکار برنده‌ی بازی شد')|filters.regex(r'گرگهای فراموشکار برنده شدن'))& filters.group & filters.user([854021534,175844556,1029642148,618096097]))
async def gorg(client, message): 
    chat_id=int(message.chat.id)
    f=hash_set(chat_id,'2')
    await bot.send_message('@darkhelperrobot',f'{f} bet')

@bot.on_message( ~filters.me & (filters.regex(r'تنها کسی که توی روستا زنده مونده کسی نیست')|filters.regex(r'ایندفعه دشمنشون برنده شد')|filters.regex(r'قاتل زنجیره ای روانی زنده موند')|filters.regex(r'دشمنایی که به تنهایی کار میکردن حال'))& filters.group & filters.user([854021534,175844556,1029642148,618096097]))
async def ghatel(client, message):       
    chat_id=int(message.chat.id)
    f=hash_set(chat_id,'3')
    await bot.send_message('@darkhelperrobot',f'{f} bet')



@bot.on_message( ~filters.me & (filters.regex(r'اعضای فرقه توی روستا باقی موندن')|filters.regex(r'روستا پر شده از افراد فرقه گرا'))& filters.group & filters.user([854021534,175844556,1029642148,618096097]))
async def ferghe(client, message): 
    chat_id=int(message.chat.id)
    f=hash_set(chat_id,'4')
    await bot.send_message('@darkhelperrobot',f'{f} bet')

@bot.on_message( ~filters.me & (filters.regex(r'آتش🔥 و ملکه❄️ باقی مو')|filters.regex(r'ویران شدنِ روستاست و برنده کسی نیست جز بمب‌گذار')|filters.regex(r'آتش زن باقی موند که بر روی'))& filters.group & filters.user([854021534,175844556,1029642148,618096097]))
async def lover(client, message): 
    chat_id=int(message.chat.id)
    f=hash_set(chat_id,'5')
    await bot.send_message('@darkhelperrobot',f'{f} bet')

@bot.on_message( ~filters.me & filters.regex(r'فقط تیم ومپایر ها 🧛🏻‍♀️ باقی موند')& filters.group & filters.user([854021534,175844556,1029642148,618096097]))
async def vamp(client, message): 
    chat_id=int(message.chat.id)
    f=hash_set(chat_id,'6')
    await bot.send_message('@darkhelperrobot',f'{f} bet')

@bot.on_message( ~filters.me & (filters.regex(r'بابا‌ شما منافق رو اعدام کردین و اون')|filters.regex('منافق رو کشتین')| filters.regex(r'یه منافقِ فراموشکار برنده‌ی'))& filters.group & filters.user([854021534,175844556,1029642148,618096097]))
async def monafegh(client, message): 
    chat_id=int(message.chat.id)
    f=hash_set(chat_id,'7')
    await bot.send_message('@darkhelperrobot',f'{f} bet')
#------------------------------------------------------------------
@bot.on_message(filters.command(['afklist', f'afklist@DarkHelperRobot']) & filters.group,group=-100)
@Admin
async def Afk_LIstLfunc(client, message):
    Txt='#dark_helper \n #afks \n'
    s=0
    try:
        if len(afk[int(database.show_main(int(message.chat.id)))])>=1:
            for i in afk[int(database.show_main(int(message.chat.id)))]:
                try:
                    x=(await bot.get_users(i)).first_name
                except:
                    x=i
                Txt+=f'✡︎{x}✡︎ {afk[int(database.show_main(int(message.chat.id)))][i]} \n'
                s+=1
                if s==20:
                    m=hash_set(int(message.chat.id),Txt)
                    await bot.send_message('@darkhelperrobot',f'{m} forward')
                    Txt=''
                    s=0
            if s>2:
                m=hash_set(int(message.chat.id),Txt)
                await bot.send_message('@darkhelperrobot',f'{m} forward')
                s=0
            else:
                m=hash_set(int(message.chat.id),'افکی وجود ندارد ')
                await bot.send_message('@darkhelperrobot',f'{m} forward')
        else:
            m=hash_set(int(message.chat.id),'لیست AFK خالی هست !')
            await bot.send_message('@darkhelperrobot',f'{m} forward')
    except Exception as e:
        print(e)
        pass


@bot.on_message( ~filters.me & (filters.regex(r'برای ورود به روستا بر روی دکمه زیر کلیک کنید')   | filters.regex(r'» /modeinfo')| filters.regex(r'روی دکمه وارد شوید کلیک کنید')|filters.regex(r'نکنید که روی کادر زیر کلیک کنید')|filters.regex(r'جوین شید و حالشو ببرید'))& filters.group & filters.user([854021534,175844556,1029642148,618096097]))
async def start_playing(client, message):
    a=hash_set(int((int(message.chat.id))),str(await message.click(0)))
    auto_join[int(message.chat.id)]=True
    await bot.send_message('@darkhelperrobot',f'{a} dokme')
    

@bot.on_message((filters.regex(r'بازی شروع شد') | filters.regex(r'تعداد بازیکنا به پنج') |filters.regex(r'تعداد بازیکنا کافی نیست') | filters.regex(r'چقدر کمین'))  & filters.group & filters.user([854021534,175844556,1029642148,618096097]),group=-100)
async def stop_playing(client, message):
    chat=int(message.chat.id)
    sec[int(message.chat.id)] = int(time.time()) - mio[chat]
    m=0
    chat_id=int(message.chat.id)
    a=hash_set(int(message.chat.id),'finished')
    await bot.send_message('@darkhelperrobot',f'{a}')
    deltag=database.show_deltag(chat_id)
    if deltag==1:
        try:
            tag_msgs = [msg async for msg in bot.iter_history(chat_id,limit=1000) if msg.entities]
            for tagmsg in tag_msgs:
                for ent in tagmsg.entities:
                    if ent.type in ("mention", "text_mention"):
                        if tagmsg.from_user.id not in wwbots:
                            m+=1
                            try:
                                await tagmsg.delete()
                                await asyncio.sleep(0.03)
                            except:
                                pass
            mv=hash_set(int(chat_id),f"{m} tags deleted ")
            await bot.send_message('@darkhelperrobot',f'{mv} forward')
        except :
            mv=hash_set(int(chat_id),f"لطفا ربات را ادمین کنید !")
            await bot.send_message('@darkhelperrobot',f'{mv} forward')
    delsup=database.show_supdel(chat_id)
    if delsup==1:
        try:
            sup=int(database.show_sup(int(chat_id)))
            tag_msgs = [msg async for msg in bot.iter_history(sup,limit=200) if msg.entities]
            for tagmsg in tag_msgs:
                for ent in tagmsg.entities:
                    if ent.type in ("mention", "text_mention"):
                        if tagmsg.from_user.id not in wwbots and '🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥' not in str(tagmsg.text):
                            m+=1
                            try:
                                await tagmsg.delete()
                                await asyncio.sleep(0.001)
                            except:
                                pass
            mv=hash_set(int(sup),f"{m} tags deleted ")
            await bot.send_message('@darkhelperrobot',f'{mv} forward')
        except :
            pass
@bot.on_message( filters.user('@darkhelperrobot')  & filters.regex(r'delete') ,group=-100)
async def delete_Tags(client, message):
    m=0
    ll=[]
    chat_id=find_Main_Id(str(message.text))[1]
    try:
        tag_msgs = [msg async for msg in bot.iter_history(chat_id,limit=1000) if msg.entities]
        for tagmsg in tag_msgs:
            for ent in tagmsg.entities:
                if ent.type in ("mention", "text_mention"):
                    if tagmsg.from_user.id not in wwbots:
                        m+=1
                        try:
                            await tagmsg.delete()
                            #ll.append(tagmsg.message_id)
                            break
                        except:
                            pass
        #await bot.delete_messages(chat_id,ll)
        mv=hash_set(int(chat_id),f"{m} tags deleted ")
        await bot.send_message('@darkhelperrobot',f'{mv} forward')
    except Exception as e:
        print(e)
        mv=hash_set(int(chat_id),f" {e} لطفا ربات را ادمین کنید !")
        await bot.send_message('@darkhelperrobot',mv)


@bot.on_message( ~filters.me & filters.regex(r'#players: 0') & filters.group & filters.user([854021534,175844556,1029642148,618096097]),group=-100)
async def tagger(client, message):
    a=hash_set(int(message.chat.id),'startted')
    await bot.send_message('@darkhelperrobot',f'{a}')


@bot.on_message((filters.regex(r'دو شب متوالی رای نداده')| filters.regex(r'دو روز متوالی رای نداده'))& filters.group &  filters.user([854021534,175844556,1029642148,618096097]) ,group=-10)
async def afk_Func(client, message):
    ch=int(message.chat.id)
    result_list = message.text.split("\n")[:1]
    players_list = []
    for index, item in enumerate(result_list):
        result_list[index] = True
    for ent in message.entities:
        try:
            players_list.append(ent.user.id)
        except:
            pass
    
    for xxy in players_list :
        m=xxy

    try:
        try:
            database.afk_inc(int(ch),int(hash[ch]))
        except:
            pass
        gp=int(database.admin_GAp(int(xxy)))
        if gp== int(message.chat.id):
            database.reduce_admin_point(int(xxy),emtiaz=1500)
            database.insert_admin_point(int(xxy),msg=1)
    except Exception as e:
        print(e)

    
    try:
        if 'شکار' in str(message.text) or 'فرشته' in str(message.text) or 'پیشگو' in str(message.text) or 'کاراگا' in str(message.text):
            if database.show_mokamel(int(message.chat.id))==1 and not 'نگاتیو' in str(message.text):
                await bot.send_message(int(message.chat.id) , f'/warn {xxy}')
    except:
        pass
    try:
        database.reduce_coin(int(xxy),50)
        database.reduce_point(xxy,100,int(ch))
    except:
        pass
    try:
        gag=(await bot.get_users(m)).first_name 
    except:
        gag=m

    warn=int(database.show_warn(ch))
    # if int(xxy) in afk[int(database.show_main(int(message.chat.id)))]:
    try:
        afk[int(database.show_main(int(message.chat.id)))][int(xxy)]+=1
        if afk[int(database.show_main(int(message.chat.id)))][int(xxy)]>=warn:
            await bot.send_message(ch,f'/warn {xxy}')
            afk[int(database.show_main(int(message.chat.id)))].pop(xxy)
    except Exception as e:
        print(e)
        afk[int(database.show_main(int(message.chat.id)))][int(xxy)]=1
        if warn==1:
            await bot.send_message(ch,f'/warn {xxy}')
            afk[int(database.show_main(int(message.chat.id)))].pop(xxy)
    v=hash_set(ch,f'به علت افک شدن 100 امتیاز  و 50 سکه از {gag} کم شد !')
    await bot.send_message('@darkhelperrobot',f'{v} forward')

@bot.on_message( ~filters.me & filters.command(['gaps']) &  filters.user(sup),group=-100)
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

@bot.on_message( ~filters.me & filters.command(['sups']) &  filters.user(sup),group=-100)
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


@bot.on_message( filters.user('@darkhelperrobot')  & filters.regex(r'djvlbrlgsyolsjguirwt7wiursflejauwpvjgupwglsudpw') ,group=-100)
async def delete_Tags(client, message):
    chat_id=find_Main_Id(str(message.text))[1]
    await bot.leave_chat(int(chat_id))
    sup=database.show_sup(int(chat_id))
    await bot.leave_chat(int(sup))

@bot.on_message( filters.user('@darkhelperrobot')  & filters.regex(r'mutest') ,group=-100)
async def delete_Tags(client, message):
    chat_id=find_Main_Id(str(message.text))[1]
    user_id=find_Main_Id(str(message.text))[2]
    try:
        await bot.delete_user_history(int(chat_id),int(user_id))
    except:
        pass
    await  asyncio.sleep(5)
    try:
        await bot.delete_user_history(int(chat_id),'@ExecutrixBot')
    except:
        pass
    try:
        await bot.delete_user_history(int(chat_id),'@DarkHelperRobot')
    except:
        pass
    try:
        await bot.delete_user_history(int(chat_id),'@partnerwolf_robot')
    except:
        pass
    try:
        await bot.delete_user_history(int(chat_id),'@partnerwolf4robot')
    except:
        pass
    try:
        await bot.delete_user_history(int(chat_id),'@enforcerbot')
    except:
        pass
    try:
        await bot.delete_user_history(int(chat_id),'@partnerwolf10robot')
    except:
        pass





moon_list=['🌕','🌖', '🌗' ,'🌘', '🌑', '🌒', '🌓', '🌔']
def rand_moon():
    radom_moon=random.choice(moon_list)
    return radom_moon

@bot.on_message((filters.regex(r'بُرد')|filters.regex(r'برنده') ) & filters.user([854021534,175844556,1029642148,618096097]), group=-1)
async def game_info(client, message):
    chat_id=int(message.chat.id)
    winner_text='بازی انالیز شد 📜🔎\n\n'
    teams_txt='قدرت تیم های درون بازی 👁‍🗨 \n\n'
    bests_txt='بهترین بازیکنان این دست 🔰\n\n'
    result_list = str(message.text).split("\n")[1:-1]
    players_list = []
    winners=1
    for index, item in enumerate(result_list):
        item=str(item).split(':')[-1]
        if '⚒' in item:
            team='روستا👨🏻'
            naghsh='⚒'
            point=10
        elif '💍🧛🏻' in item:
            team='ومپایر 🧛🏻‍♂️'
            naghsh='💍🧛🏻'
            point=75
        elif '🃏' in item:
            team='روستا👨🏻'
            naghsh='🃏'
            point=10
        elif '👿' in item:
            team='روستا👨🏻'
            naghsh='👿'
            point=20
        elif '👷' in item:
            team='روستا👨🏻'
            naghsh='👷'
            point=10
        elif '👨‍🔬' in item:
            team='روستا👨🏻'
            naghsh='👨‍🔬'
            point=30
        elif '☮️' in item:
            team='روستا👨🏻'
            naghsh='☮️'
            point=30
        elif '🧙🏻‍♂️' in item:
            team='گرگ 🐺'
            naghsh='🧙🏻‍♂️'
            point=25
        elif '💘' in item:
            team='روستا👨🏻'
            naghsh='💘'
            point=20
        elif '👶🏻' in item or '👶' in item:
            team='گرگ 🐺'
            naghsh='👶🏻'
            point=25
        elif '🔮' in item :
            team='گرگ 🐺'
            naghsh='🔮'
            point=30
        elif '💣' in item:
            naghsh='💣'
            point=40
            team='بمب گذار 💣'
        elif '🔥' in item:
            team='اتش🔥'
            naghsh='🔥'
            point=60
        elif '👨🏻' in item or '👱' in item:
            team='روستا👨🏻'
            naghsh='👨🏻'
            point=5
        elif '📚' in item:
            team='روستا👨🏻'
            naghsh='📚'
            point=20
        elif '🙇🏻‍♂' in item:
            team='روستا👨🏻'
            naghsh='🙇🏻‍♂'
            point=25
        elif '🦅' in item:
            team='روستا👨🏻'
            naghsh='🦅'
            point=20
        elif '🍾' in item:
            team='قاتل 🔪'
            naghsh='🍾'
            point=30
        elif '👩🏻‍🌾' in item:
            team='روستا👨🏻'
            naghsh='👩🏻‍🌾'
            point=15
        elif '👰🏻' in item:
            team='روستا👨🏻'
            naghsh='👰🏻'
            point=20
        elif '🎩' in item:
            team='فرقه👤'
            naghsh='🎩'
            point=30
        elif '👑' in item:
            team='روستا👨🏻'
            naghsh='👑'
            point=25
        elif '🔪' in item:
            team='قاتل 🔪'
            naghsh='🔪'
            point=100
        elif '🔫' in item:
            team='روستا👨🏻'
            naghsh='🔫'
            point=40
        elif '🐶' in item:
            team='گرگ 🐺'
            naghsh='🐶'
            point=70
        elif '🦹🏻‍♂️' in item:
            team='روستا👨🏻'
            naghsh='🦹🏻‍♂️'
            point=40
        elif '⚡️' in item:
            team='گرگ 🐺'
            naghsh='⚡️🐺'
            point=85
        elif '💤🐺' in item:
            team='گرگ 🐺'
            naghsh='💤🐺'
            point=30
        elif '🌀' in item:
            team='روستا👨🏻'
            naghsh='🌀'
            point=35
        elif '🖕🏿' in item:
            team='گرگ 🐺'
            naghsh='🖕🏿'
            point=30
        elif '👳🏻‍♂️' in item or '👳' in item :
            team='روستا👨🏻'
            naghsh='👳🏻‍♂️'
            point=60
        elif '👺' in item:
            team='منافق'
            naghsh='👺'
            point=150
        elif '🧝🏻‍♀️' in item:
            team='گرگ 🐺'
            naghsh='🧝🏻‍♀️'
            point=70
        elif '🌝🐺' in item:
            team='گرگ 🐺'
            naghsh='🌝🐺'
            point=70
        elif '🎭' in item:
            team='روستا👨🏻'
            naghsh='🎭'
            point=20
        elif '👁' in item:
            team='روستا👨🏻'
            naghsh='👁'
            point=20
        elif '🗡' in item:
            team='روستا👨🏻'
            naghsh='🗡'
            point=80
        elif '🤴🏻' in item:
            team='روستا👨🏻'
            naghsh='🤴🏻'
            point=15
        elif '💂🏻‍♂️' in item or '💂‍♂️' in item:
            team='روستا👨🏻'
            naghsh='💂🏻‍♂️'
            point=100
        elif '👨‍🔬️' in item:
            team='روستا👨🏻'
            naghsh='👨‍🔬️'
            point=30
        elif '🧙🏻‍♀️' in item:
            team='گرگ 🐺'
            naghsh='🧙🏻‍♀️'
            point=30
        elif '🧟‍♂️' in item:
            team='فرقه👤'
            naghsh='🧟‍♂️'
            point=45
        elif '👼🏻' in item:
            team='روستا👨🏻'
            naghsh='👼🏻'
            point=45
        elif '👤' in item:
            team='فرقه👤'
            naghsh='👤'
            point=25
        elif '👮🏻‍♂' in item:
            team='روستا👨🏻'
            naghsh='👮🏻‍♂'
            point=30
        elif '😾' in item:
            team='گرگ 🐺'
            naghsh='😾'
            point=20
        elif '🍵' in item:
            team='گرگ 🐺'
            naghsh='🍵'
            point=30
        elif '🦊' in item:
            team='گرگ 🐺'
            naghsh='🦊'
            point=30
        elif '🕵🏻‍♂️' in item:
            team='روستا👨🏻'
            naghsh='🕵🏻‍♂️'
            point=60
        elif '☃️' in item:
            team='گرگ 🐺'
            naghsh='☃️'
            point=40
        elif '💤' in item:
            team='روستا👨🏻'
            naghsh='💤'
            point=25
        elif '🍂' in item:
            team='روستا👨🏻'
            naghsh='🍂'
            point=30
        elif '👹' in item:
            team='گرگ 🐺'
            naghsh='👹'
            point=35
        elif '🍻' in item: 
            team='روستا👨🏻'
            naghsh='🍻'
            point=10
        elif '❄️' in item:
            team='اتش🔥'
            naghsh='❄️'
            point=50
        elif '💋' in item:
            team='روستا👨🏻'
            naghsh='💋'
            point=35
        elif '🪓' in item:
            team='روستا👨🏻'
            naghsh='🪓'
            point=50
        elif '🐺' in item:
            team='گرگ 🐺'
            naghsh='🐺'
            point=55
        elif '🧛🏻‍♀️' in item:
            team='ومپایر 🧛🏻‍♂️'
            naghsh='🧛🏻‍♀️'
            point=75
        elif '🧛🏻‍♂️' in item:
            team='ومپایر 🧛🏻‍♂️'
            naghsh='🧛🏻‍♂️'
            point=50
        elif '🏹' in item:
            team='قاتل 🔪'
            naghsh='🏹'
            point=80
        elif '🎖' in item:
            team='روستا👨🏻'
            naghsh='🎖'
            point=30
        else:
            team='?'
            naghsh='??'
            point=15

        if item.find("بُرد") != -1 or item.find("برنده") != -1 :
            win=True
            winners+=1
        else:
            win=False

        if item.find("مرده") != -1 :
            alive=False
        else:
            alive=True  
        result_list[index] = {'win':win,'point':point,'alive':alive,'naghsh':naghsh,'team':team}
    for ent in message.entities:
        # if int(ent.length) >20:
        #     players_list.append('None!')
        # else:
        try:
            # if 'الف'in hps or 'ب'in hps or 'پ'in hps or 'ت'in hps or 'ث'in hps or 'ج'in hps or 'چ'in hps or 'ح'in hps or 'خ'in hps or 'د'in hps or 'ذ'in hps or 'ر'in hps or 'ز'in hps or 'ژ'in hps or 'س'in hps or 'ش'in hps or 'ص'in hps or 'ض'in hps or 'ط'in hps or 'ظ'in hps or 'ع'in hps or 'غ'in hps or 'ف'in hps or 'ق'in hps or 'ک'in hps or 'گ'in hps or 'ل'in hps or 'م'in hps or 'ن'in hps or 'و'in hps or 'ه'in hps or 'ی' in hps:
            players_list.append(ent.user.id)
            now=datetime.datetime.now()
            if int(now.hour)<9:
                try:
                    database.addepoint_night(int(ent.user.id),int(message.chat.id))
                except Exception as e :
                    print(f'\n\n\n\n\n\n\n {e} \n\n\n\n\n\n\n')
        except:
            pass
    winner_con=dict(zip(players_list, result_list))
    #-----------------------------------------------------------------------
    all_winer=len(winner_con)
    bests=dict()
    teams=dict()
    for i in winner_con:
        moon=rand_moon()
        zarib_win=all_winer//winners
        player_naghsh=winner_con[i]['naghsh']
        if winner_con[i]['alive']==True:
            alive_txt='🙂'
            zarib_win*=1.5
        else:
            zarib_win*=1
            alive_txt='💀'

        if winner_con[i]['win']==True:
            win_txt='🌟'
            zarib_win=zarib_win*3
        else:
            zarib_win=zarib_win*0.5
            win_txt='💩'
            
        if winner_con[i]['team'] in teams:
            teams[(winner_con[i]['team'])]+=int(winner_con[i]['point'])
        else:
            teams[(winner_con[i]['team'])]=int(winner_con[i]['point'])
        
        player_point=int(zarib_win*int(winner_con[i]['point']))
        bests[i]=player_point

        try:
            name=(await bot.get_users(int(i))).mention
        except:
            name=(i)
            
        winner_text+=f'{moon}|{win_txt}|{alive_txt}⇢({winner_con[i]["point"]}{player_naghsh})➛{name} ``` {player_point} ``` \n'
        try:
            database.insert_point(int(i),player_point,chat_id)
        except:
            pass

    #------------------------------------------------------------------------
    for t in teams:
        teams_txt+=f'تیم {t} با قدرت {teams[t]}\n'

    best1=max(bests.items(), key=operator.itemgetter(1))[0]
    try:
        p=(await bot.get_users(best1)).mention
    except:
        p=best1
    bests_txt+=f'1- ♛{p} ➾ {bests[best1]} ☞ {(winner_con[best1]["team"])}\n'
    bests.pop(best1)

    best2=max(bests.items(), key=operator.itemgetter(1))[0]
    try:
        p=(await bot.get_users(best2)).mention
    except:
        p=best2
    bests_txt+=f'2- ♛{p} ➾ {bests[best2]} ☞ {(winner_con[best2]["team"])}\n'

    bests.pop(best2)
    best3=max(bests.items(), key=operator.itemgetter(1))[0]
    try:
        p=(await bot.get_users(best3)).mention
    except:
        p=best3
    bests_txt+=f'3- ♛{p} ➾ {bests[best3]} ☞ {(winner_con[best3]["team"])}\n'

    name=hash_set(chat_id,f'{winner_text} \n \n {teams_txt} \n \n {bests_txt}')
    await bot.send_message('darkhelperrobot',f'{name} forward')






@bot.on_message(filters.command(['leavingmembers' , f'leavingmembers@DarkHelperRobot']))
@Admin
async def Leaving_people(c,m):
    send_file=''
    num=1
    async for i in bot.get_chat_event_log(chat_id=int(database.show_main(int(m.chat.id)) ),filters =ChatEventFilter(leaving_members=True)):
        try:
            send_file+=f'✦ mio{i.user.id}mio  ⚠️  kio{i.user.id }kio ⭕️  \n \n'
            num+=1
        except:
            pass
        if num==20:
            num=1
            fic=hash_set(int((m.chat.id)) , str(send_file))
            await bot.send_message('@darkhelperrobot',f'{fic} copy')
            send_file=''
            await asyncio.sleep(1)

@bot.on_message( ~filters.me & filters.user([854021534,175844556,1029642148,618096097]),group=0)
async def Onyx_Messages(client, message):
    global hash,time_db,mio
    chat=int(message.chat.id)
    now=datetime.datetime.now()
    if str(message.text) == '#players: 0':
        mio[chat]= int(time.time())
        time_db.update(mio)
        
        

    if 'بازیکن های زنده:' in str(message.text) or 'بازیکنان زنده :' in str(message.text):
        try:
            players_list_send='|'
            for ent in message.entities:
                    try:
                        players_list_send+=f'{ent.user.id}|'
                    except:
                        pass
            send_alives=hash_set(chat,players_list_send)
            await bot.send_message('@darkhelperrobot',f'{send_alives} sray')
        except:
            pass
        alives=0
        dead=0
        all=0
        result_list = message.text.split("\n")[1:]
        for index, item in enumerate(result_list):
            if item.find("زنده") != -1:
                alives+=1
                all+=1
            else:
                dead+=1
                all+=1
        
        if alives>=40:
            zarib_bet=float((all+alives)/(dead+30))
        elif alives>35:
            zarib_bet=float((all+alives)/(dead+26))
        elif alives>=30:
            zarib_bet=float((all+alives)/(dead+25))
        elif alives>=25:
            zarib_bet=float((all+alives)/(dead+23))
        elif alives>=15:
            zarib_bet=float((all+alives)/(dead+21))
        elif alives>=10:
            zarib_bet=float((all+alives)/(dead+16))
        elif alives>=5:
            zarib_bet=float((all+alives)/(dead+13))
        elif alives<5:
            zarib_bet=1.00
        po=(hash_set(chat,zarib_bet))
        await bot.send_message('@darkhelperrobot',f'{po} zarib')
        count = re.findall('(\d+)', message.text)
        send_list=hash_set(chat,str(message.text))
        await bot.send_message('@darkhelperrobot',f'{send_list} deaddict')
        try:
            if 0.4<((int(count[0]) / int(count[1]) ))<0.55 and auto_join[int(message.chat.id)]==True and int(database.show_auto_next(int(message.chat.id))) > 0:
                qq=hash_set(int(message.chat.id),'auto_join')
                await bot.send_message('@DarkHelperroBot',f'{qq} auto_join')
                auto_join[int(message.chat.id)]=False
        except :
            pass
        if count[0] == count[1]:
            admins_join_other_gap= f'با توجه به انالیز ادمین های زیر در گروه {message.chat.title} جوین بازی شدند ! \n \n'
            admins_join='بازی شروع شد و ادمین های : \n '

            players_list=[]
            try:
                for ent in message.entities:
                    try:
                        players_list_send+=f'{ent.user.id}|'
                        players_list.append(ent.user.id)
                    except:
                        pass
                    try:
                        uu=ent.user.id
                    except:
                        pass
                #-----------------------------------------------------------------------
                    try:
                        gp=int(database.admin_GAp(int(uu)))
                        admins_list = [int(i.user.id) async for i in bot.iter_chat_members(gp,filter ='administrators')]
                        if gp== int(message.chat.id) :
                            database.insert_admin_point(int(uu),0,0,1,1000)
                            if int(uu) in admins_list:
                                admin_mention=(await bot.get_users(int(uu))).mention
                                admins_join+=f'{admin_mention}\n'
                        else:
                            if int(uu) in admins_list:
                                admin_mention=(await bot.get_users(int(uu))).mention
                                admins_join_other_gap+=f'{admin_mention}\n'
                            
                    except  :
                        pass
#-----------------------------------------------------------------------
                try:

                    if admins_join_other_gap!= f'با توجه به انالیز ادمین های زیر در گروه {message.chat.title} جوین بازی شدند ! \n \n' or len(admins_join_other_gap) > 85 :
                        bot.send_message(int(database.show_sup(gp)), admins_join_other_gap)
                    if admins_join!= 'بازی شروع شد و ادمین های : \n ' or len(admins_join) > 29 :
                        bot.send_message(int(database.show_sup(gp)), f'{admins_join} \n در بازی جوین شدند')
                except:
                    pass
#-----------------------------------------------------------------------

                    now=datetime.datetime.now()
                    if int(now.hour)<9:
                        try:
                            database.addeplayed_night(int(uu),int(message.chat.id))
                        except Exception as e:
                            print(f'\n\n\n\n\n\n\n {e} \n\n\n\n\n\n\n')
            except:
                pass

            secon=sec[int(message.chat.id)]
            jointime = datetime.timedelta(seconds=secon)
            a=hash_set(int(database.show_sup(chat)),f'*•|⛑| #Helper\nᴊᴏɪɴ ᴛɪᴍᴇ ғɪɴɪsʜᴇᴅ\n\n-|ᴊᴏɪɴ ᴛɪᴍᴇ: | {jointime} |⏱\n\n-|ᴘʟᴀʏᴇʀs: | {count[0]} |👨🏻‍💻*')
            await bot.send_message('@darkhelperrobot',f'{a} forward')
            hash[chat]=random.randint(1,100000000000000000)
            database.add_time(str(jointime),int(count[1]),int(chat),str(now.hour),hash[chat])


@bot.on_message(group=1)
async def AllMsg(client, message):
        now=datetime.datetime.now()
        if (int(now.hour)==0 and int(now.minute)==1 ):
            f=database.show_gaps()
            for i in f:
                afk[int(i[0])]=dict()

bot.run()
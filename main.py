import random
import requests
from bs4 import BeautifulSoup
from multiprocessing import Pool
from colorama import Fore, init
import json
import re
import time
import os
from passwrod import GET_PASSWORD
from prettytable import PrettyTable
list_my_email = []
temp_email = []




def return_info_breanch():
    try:
        with open('search_branch.json', 'r',encoding='utf-8') as f:
            data_josn  = json.load(f)

        return data_josn    
    except Exception as e:
        return False

def config_itemps():
    try:
        with open('config.json', 'r',encoding='utf-8') as f:
            json_data  = json.load(f)
        return json_data    
    except Exception as e:
        return False
    
    
    
    
    
    
#  proxy_username = 'leahtokerova'
# proxy_password = '8N465LTTX55F6GX2LDDIXV53'
# hostname = '12.198.49.27:32222'





# proxies = {
#     "http": "http://{0}:{1}@{2}/".format(proxy_username, proxy_password, hostname),
#     "https": "http://{0}:{1}@{2}/".format(proxy_username, proxy_password, hostname)
# }


   
    
    
    
    
    
    
    

T = PrettyTable()
init()
timeout = 1
def get_timeout():
    while True:
        timeout = input("Timeout: ")
        if timeout.isnumeric():
            timeout = int(timeout)
            if 0 < timeout <= 10:
                return timeout
            else:
                return False
        else:
            print("Please enter a numeric value for timeout.")

def is_valid_email(email):
        regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if re.match(regex, email):
            return True
        else:
            return False

def get_useproxy():
    while True:
        use_proxy = input(f'Use proxy ? y/n  ')
        if use_proxy == 'y':
            return True
        elif use_proxy == 'n':
            return False
        else:
            pass


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def is_valid_email(email):
        regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if re.match(regex, email):
            return True
        else:
            return False

def send(u, counter, u_proxy):
    username = u.split(':')[0]
    # database = check_database(username)
    # if database:
    #     print(f'{Fore.YELLOW}WARNING{Fore.MAGENTA} [{Fore.YELLOW} {counter}{Fore.MAGENTA} ] [{Fore.YELLOW} {username}{Fore.MAGENTA} ] [{Fore.YELLOW} ALREADY CHECKED {Fore.MAGENTA} ]{Fore.RESET}')
    # else:
    followers = u.split(':')[1]
    following = u.split(':')[2]
    ximages = u.split(':')[3]
    imageshttps = u.split(':')[4]
    images = f'{ximages}:{imageshttps}'
    mx_ip = 'NONE'
    err = 1
    while True:
        err+=1
        if u_proxy:
            response = requests.get("https://api.infoip.io/", proxies = {'https': config_itemps()[0]['snuss_base_proxy']} )
        else:
            response = requests.get("https://api.infoip.io/")
        if response.status_code == 200:
            ips = json.loads(response.content)
            mx_ip =ips['ip'] 
            break
        else:
            pass
        if err >= 6:
            break

    headers = {
        'authority': 'beta.snusbase.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'no-cache',
        'content-type': 'application/x-www-form-urlencoded',
        'origin': 'https://beta.snusbase.com',
        'pragma': 'no-cache',
        'referer': 'https://beta.snusbase.com/',
        'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Opera";v="106"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 OPR/106.0.0.0',
    }
    data = {
        'term': username,
        'activation_code': config_itemps()[0]['serial_key_snussbase'],
        'type': 'username',
        'save': 'on',
    }
    try:
        c = 0
        while c < 5:
            c+=1
            if u_proxy:
                response = requests.post('https://beta.snusbase.com/', headers=headers, data=data, proxies = {'https': config_itemps()[0]['snuss_base_proxy']})
            else:
                response = requests.post('https://beta.snusbase.com/', headers=headers, data=data)
            email = []
            if response.status_code == 200:
                    twitter_email = None
                    # with open('errror.txt', 'a', encoding='utf-8') as f:
                    #     f.write(response.text)
                    html_content = response.text
                    soup = BeautifulSoup(html_content, 'html.parser')
                    divs = soup.find_all(class_ = "xemail" )
                    title = soup.find_all(class_ = "r-t" )
                    result_count = soup.find(id = "result_count")
                    alert = soup.find(class_=["alert-white"])
                    add_db = ''
                        
                    if len(divs) > 0:
                        for email_to_ in divs:
                            email_span = email_to_.text
                            if email_span.lower() not in [eamil.lower() for eamil in list_my_email]:
                                temp_email.append(email_span)
                        
                        if len(temp_email) > 10:
                            for lx in temp_email[:10]:
                                list_my_email.append(lx)
                        else:
                            for lx in temp_email:
                                list_my_email.append(lx)
                        
                        if len(list_my_email) > 10:
                            new_list_my_email = set(list_my_email[:10])
                            new_list_my_email = list(new_list_my_email)
                            if twitter_email not in new_list_my_email:
                                new_list_my_email.append(twitter_email)
                        else:
                            new_list_my_email = set(list_my_email)
                        
                        if u_proxy:
                            print(f'{Fore.GREEN}-> {Fore.MAGENTA}[{Fore.GREEN} {counter}{Fore.MAGENTA} ] [{Fore.GREEN} {mx_ip}{Fore.MAGENTA} ] [{Fore.GREEN} {username}{Fore.MAGENTA} ] [{Fore.YELLOW} EMAIL: {alert.text} {Fore.MAGENTA} ]{Fore.RESET}')
                        else:
                            print(f'{Fore.GREEN}-> {Fore.MAGENTA}[{Fore.GREEN} {counter}{Fore.MAGENTA} ] [{Fore.GREEN} {username}{Fore.MAGENTA} ] [{Fore.YELLOW} EMAIL: {alert.text} {Fore.MAGENTA} ]{Fore.RESET}')
                        counterx = 0
                        for emails_send in new_list_my_email:
                            counterx +=1
                            x = GET_PASSWORD(emails_send)
                            aa = x.run()
                            parsed_aa = json.loads(aa)
                            if parsed_aa['succes']:
                                p = parsed_aa['result']
                                if parsed_aa['result'] > 0:
                                    if len(parsed_aa['item']) > 30:
                                        for pwd in parsed_aa['item'][:30]:
                                            with open('RESULT_TWITTER_COMBO/combo.txt', 'a+', encoding='utf-8', errors='ignore') as l:
                                                l.write(f'{username}:{emails_send}:{pwd}\n')
                                    else:
                                        for pwd in parsed_aa['item']:
                                            with open('RESULT_TWITTER_COMBO/combo.txt', 'a+', encoding='utf-8', errors='ignore') as l:
                                                # l.write(f'{username}:{emails_send}:{pwd}:{followers}:{following}:{images}\n')
                                                l.write(f'{username}:{emails_send}:{pwd}\n')
                                    
                                    g = parsed_aa['modify_result']
                                    data = f'   {Fore.BLUE}[ {Fore.LIGHTBLUE_EX}{counterx}{Fore.BLUE} ] [ {Fore.LIGHTBLUE_EX}{username}{Fore.BLUE} ] [ {Fore.LIGHTBLUE_EX}{emails_send}{Fore.BLUE} ] [ {Fore.YELLOW}GROUP EMAIL: {Fore.LIGHTBLUE_EX}{counterx}/{len(new_list_my_email)}{Fore.BLUE} ] [ {Fore.YELLOW}NR PASSWORD : {Fore.YELLOW}{p} ]  [ NR PWD GEN : {g}{Fore.BLUE} ] {Fore.RESET}'
                                    print(data)
                                else:
                                    data = f'   {Fore.BLUE}[ {Fore.LIGHTBLUE_EX}{counterx}{Fore.BLUE} ] [ {Fore.LIGHTBLUE_EX}{username}{Fore.BLUE} ] [ {Fore.LIGHTBLUE_EX}{emails_send}{Fore.BLUE} ] [ {Fore.YELLOW}GROUP EMAIL: {Fore.LIGHTBLUE_EX}{counterx}/{len(new_list_my_email)}{Fore.BLUE} ] [ {Fore.YELLOW}NR PASSWORD : {Fore.RED}{p} ] {Fore.RESET}'
                                    print(data)
                            else:
                                msg = parsed_aa['message']
                                data = f'   {Fore.BLUE}[ {Fore.LIGHTBLUE_EX}{counterx}{Fore.BLUE} ] [ {Fore.RED}{username}{Fore.BLUE} ] [ {Fore.RED}{emails_send}{Fore.BLUE} ] [ {Fore.YELLOW}GROUP EMAIL: {Fore.RED}{counterx}/{len(new_list_my_email)}{Fore.BLUE} ] [ {Fore.RED} MESSAGE: {msg} ]{Fore.RESET}'
                                print(data)
                    
                    else:
                        if u_proxy:
                            data = f'[ USERNAME : {username} ] [{Fore.GREEN} {mx_ip}{Fore.MAGENTA} ]  [ EMAIL : {len(divs)}] [ {Fore.YELLOW} RESPONSE: {alert.text} {Fore.RESET}] '
                        else:
                            data = f'[ USERNAME : {username} ] [ EMAIL : {len(divs)}] [ {Fore.YELLOW} RESPONSE: {alert.text} {Fore.RESET}] '
                            
                        print(data)

                    list_my_email.clear() 
                    twitter_email = ''
                    temp_email.clear() 
                    break
            else:
                pass
    except Exception as e:
        print(f'{Fore.BLUE}[ {counter} ]{Fore.RESET}',f'[ {Fore.LIGHTBLUE_EX}{username}{Fore.RESET} ]' ,f'ERROR', f'{Fore.YELLOW}{e}{Fore.RESET}')
        pass  
    

def remove_ansi(text):
    ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
    return ansi_escape.sub('', text)


def main(u_proxy):
    with open ("username.txt", "r", encoding="utf-8") as f:
        counter =1
        for line in f:
            try:
                line = line.strip()
                send(line,counter, u_proxy)
                with open('LOGS/raport_snuss.txt', 'a') as f:
                    f.write(str(line) + '\n')
                counter+=1
                time.sleep(config_itemps()[0]['set_timeout_snussbase'])
            except Exception as e:
                print(e)
                pass

if __name__ == "__main__":
    timeto = config_itemps()[0]['set_timeout_snussbase']
    proxyout = config_itemps()[0]['use_proxy']
    print(f'{Fore.GREEN}[ {Fore.CYAN} RUNING... {Fore.GREEN}] {Fore.RESET}')
    print(f'SET TIME SLEEP: [ {str(timeto)} ]')
    print(f'SET Proxy: [ {str(proxyout)} ]')
    u_proxy = proxyout
    main(u_proxy)

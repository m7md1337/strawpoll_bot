#!/usr/bin/python3

import re
import json
import requests
from retrying import retry
from requests.exceptions import ProxyError

#xx = open('html1', 'r').read().decode('utf-8')
regex = r"""
	\.content\s=\s (.*?)\n\x09store\.
	"""
recsrf = r"""
	_token\:\s(.*?)\,\n
	"""

    

def req(url):
    count = 0
    req = requests.get(url)
    
    json_string = re.finditer(regex, req.text, re.MULTILINE | re.VERBOSE | re.IGNORECASE | re.DOTALL | re.UNICODE)
    for matchNum, match in enumerate(json_string, start=1):
        cc = match.groups()
    ree = """poll"};"""
    by = 'poll"}'
    result = "".join(cc)

    xx1 = result.replace(ree , by)
    mylist = list()
    for cc in json.loads(xx1)['poll']['poll_answers']:
        mylist.append(cc['id'])
        count+=1 
        print("number: "+str(count) + "|"+ ' ' + cc['answer'])
        #print(mylist)
    xx3 = int(input("\nchose how want to win: "))
    xx3-=1
    finalyyy = mylist[xx3]
    finaaly2 = json.loads(xx1)['cookie_id']
    
    return finaaly2,finalyyy 
    
def pooling(m,w,proxyy):
    try:
        https = "https://"+proxyy+""
        proxyyy = {
            "https": https
        }
        
        req1 = requests.get("https://strawpoll.com/"+m+"",proxies=proxyyy)
        json_string1 = re.finditer(recsrf, req1.text, re.MULTILINE | re.VERBOSE | re.IGNORECASE | re.DOTALL | re.UNICODE)
        for matchNum1, match1 in enumerate(json_string1, start=1):
            cc1 = match1.groups()
        csrf = "".join(cc1).replace('"', '')
        url = "https://strawpoll.com/api/poll/vote"
        headerss = {"X-CSRF-TOKEN":""+csrf+""}
        cookies = {'mojolicious': ''+req1.cookies['mojolicious']+''}
        data = {"content_id":""+m+"","checked_answers":""+w+"","name":"","token":""}
        req = requests.post(url,data=json.dumps(data), proxies=proxyyy,headers=headerss,cookies=cookies)
        return req
    except ProxyError:
        print("error in proxy move to next one")
        pass

urlll = input("put the url for poll: ")
m,w = req(urlll)
poxylist = open(input("\nput the path for proxyy: ")) 
cont=0
for prrooxx in poxylist.read().splitlines():
    try:
        zz = pooling(m,w,prrooxx)
        if json.loads(zz.content)['success'] == 0:
            print("oooops ip has been used it before")
            
        elif json.loads(zz.content)['success'] == 1:
           cont+=1
           print("\n###  Vote successed###\n")
            
    except:
        pass
        
print("total Vote successed : "+str(cont)+"")

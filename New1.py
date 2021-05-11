#!/usr/bin/python3
import random
import re
import json
import requests
from binascii import hexlify
import concurrent.futures
from retrying import retry
from requests.exceptions import ProxyError
import hashlib


def generate_random_voter(length):
    xx = "0123456789ABCDEF"
    return ''.join(random.choice(xx) for _ in range(length))
regex = r"""
	\.content\s=\s (.*?)\n\x09store\.
	"""
recsrf = r"""
	_token\:\s(.*?)\,\n
	"""

def getCaptchToken(proxy):
    https = "https://"+proxy+""
    proxyyy = {
            "https": https
        }
    recaptcha_regex = re.compile(r'value="(.*?)">\n<script')

    header33 = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36","Host":"www.google.com"}
    r = requests.get('https://www.google.com/recaptcha/api2/anchor?ar=1&k=6Lfx2sEaAAAAAGHiNQ-UEueKoOrIQT-DcttQMAOb&co=aHR0cHM6Ly9zdHJhd3BvbGwuY29tOjQ0Mw..&hl=en&v=npGaewopg1UaB8CNtYfx-y1j&size=invisible&cb=q6tz8n4j8zq1', headers=header33,proxies=proxyyy)
    match = recaptcha_regex.search(r.text)
    recaptcha_token = match.group(1)
    dd = "".join(recaptcha_token)
    zz11 = "".join([hex(ord(x)) for x in dd])
    data = '0a186e70476165776f70673155614238434e745966782d79316a12a40c{}1a0a5b39362c38302c39335d2201212a0a2d3831353338313234383201713a0042067375626d69747228364c66783273456141414141414748694e512d554575654b6f4f724951542d44637474514d414f62'.format(zz11.replace('0x', ''))
    data2 = '0a186e70476165776f70673155614238434e745966782d79316a128e0c{}1a0a5b39362c38302c39335d2201212a0a2d3831353338313234383201713a0042067375626d69747228364c66783273456141414141414748694e512d554575654b6f4f724951542d44637474514d414f62'.format(zz11.replace('0x', ''))
    data3 = '0a186e70476165776f70673155614238434e745966782d79316a12b90c{}1a0a5b39362c38302c39335d2201212a0a2d3831353338313234383201713a0042067375626d69747228364c66783273456141414141414748694e512d554575654b6f4f724951542d44637474514d414f62'.format(zz11.replace('0x', ''))


    bytes_object = bytes.fromhex(data)
    bytes_object2 = bytes.fromhex(data2)
    bytes_object3 = bytes.fromhex(data3)
    header={'Content-Type':'application/x-protobuffer',"User-Agent": "Mozilla/5.0 (Windows NT 10.0; rv:78.0) Gecko/20100101 Firefox/78.0"}
    req4 = requests.post("https://www.google.com/recaptcha/api2/reload?k=6Lfx2sEaAAAAAGHiNQ-UEueKoOrIQT-DcttQMAOb",data=bytes_object,headers=header,proxies=proxyyy)
    if "bgdata" in req4.text:
        ff = "".join(req4.text)
        ffff= json.loads(ff.replace(")]}'", ''))
        return ffff[1]
        
    elif "bgdata" not in req4.text:
        req11 = requests.post("https://www.google.com/recaptcha/api2/reload?k=6Lfx2sEaAAAAAGHiNQ-UEueKoOrIQT-DcttQMAOb",data=bytes_object2,headers=header,proxies=proxyyy)
        if "bgdata" in req11.text:
            ff = "".join(req11.text)
            ffff= json.loads(ff.replace(")]}'", ''))
            return ffff[1]
        elif "bgdata" not in req11.text:
            req22 = requests.post("https://www.google.com/recaptcha/api2/reload?k=6Lfx2sEaAAAAAGHiNQ-UEueKoOrIQT-DcttQMAOb",data=bytes_object3,headers=header,proxies=proxyyy)
            if "bgdata" in req22.text:
                ff = "".join(req22.text)
                ffff= json.loads(ff.replace(")]}'", ''))
                return ffff[1]
            else:
                return "error"



def retry_if_connection_error(exception):
    return isinstance(exception, SSLError)
    
@retry(wait_random_min=1000, wait_random_max=2000)
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
    
@retry(wait_random_min=1000, wait_random_max=2000)
def pooling(m,w,proxyy):
    try:
        https = "https://"+proxyy+""
        proxyyy = {
            "https": https
        }
        cookies1 = {'voter':''+hashlib.md5(generate_random_voter(30).encode('utf-8')).hexdigest()+''}
        headers1 = {'User-Agent':'Mozilla1/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chr1ome/90.0.4430.93 Safari/537.36'}
        req1 = requests.get("https://strawpoll.com/"+m+"",proxies=proxyyy,cookies=cookies1,headers=headers1)
        json_string1 = re.finditer(recsrf, req1.text, re.MULTILINE | re.VERBOSE | re.IGNORECASE | re.DOTALL | re.UNICODE)
        for matchNum1, match1 in enumerate(json_string1, start=1):
            cc1 = match1.groups()
        csrf = "".join(cc1).replace('"', '')
        url = "https://strawpoll.com/api/poll/vote"
        headerss = {"X-CSRF-TOKEN":""+csrf+"",'User-Agent':'Mozilla1/5.0 (X11; Linux x86_64) AppleWebKit/53117.36 (KHTML, like Gecko) Chrom1e/90.0.4430.93 Safari/537.36'}
        cookies = {'mojolicious': ''+req1.cookies['mojolicious']+''}
        data = {"content_id":""+m+"","checked_answers":""+w+"","name":"","token":getCaptchToken(proxyy)}
        req = requests.post(url,data=json.dumps(data),proxies=proxyyy,headers=headerss,cookies=cookies)
        return req.text
    except ProxyError:
        print("error in proxy move to next one")
        pass

#req('https://strawpoll.com/ykosrdrss')

urlll = input("put the url for poll: ")
m,w = req(urlll)
poxylist = open(input("\nput the path for proxyy: "))
threadNUm= int(input("number for thread 10 is maximum:")) 
cont=0
            
            
            
with concurrent.futures.ThreadPoolExecutor(max_workers=threadNUm) as executor:
    future_to_url = {executor.submit(pooling, m, w, prrooxx): prrooxx for prrooxx in poxylist.read().splitlines()}
    for future in concurrent.futures.as_completed(future_to_url):
        url = future_to_url[future]
        try:
            data = future.result()
        except Exception as exc:
            print('%r proxy: %s' % (url, exc))
        else:
            try:
                if "You already voted on this poll" in data:
                    print("erro when build cookies")
            
                elif "Thanks for your vote!" in data:
                    cont+=1
                    print("\n###  Vote successed###\n")
                elif "You (or someone in your Wi-Fi\/network) have already participated in this vote" in data:
                    print("oops ip has been used before")
                elif "Captcha verification failed. Please try again." in data:
                    print("error when build Captcha")
                else:
                    print("something weird hmmm")  
            except:
                pass
                              
            
            

        
print("total Vote successed : "+str(cont)+"")

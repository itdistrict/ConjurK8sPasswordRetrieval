import requests
import time
import base64

requests.packages.urllib3.disable_warnings() 
try:
    while True:
        print("read token file")
        f = open("/run/conjur/access-token", "r")
        token = (base64.b64encode((f.read()).encode('ascii'))).decode('ascii')
        print("token received and base64 encoded")
        url = 'https://conjur-follower.cyberark-conjur.svc.cluster.local/secrets/default/variable/secrets/username'
        headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8', 'Authorization': 'Token token=\"' + token + '\"'}
        print("start requesting username")
        r = requests.get(url,headers=headers, verify=False)
        if r.status_code == 200:
            print("Username: " +r.content.decode())
        else:
            print("HTTP-Error: " + str(r.status_code))
        url = 'https://conjur-follower.cyberark-conjur.svc.cluster.local/secrets/default/variable/secrets/password'
        print("start requesting password")
        r = requests.get(url,headers=headers, verify=False)
        if r.status_code == 200:
            print("Password: " +r.content.decode())
        else:
            print("HTTP-Error: " + str(r.status_code))
        time.sleep(10)
except (FileNotFoundError, IOError):
       print("Token file not found")

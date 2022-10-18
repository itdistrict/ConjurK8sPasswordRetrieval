import requests
import time
import base64
import os

requests.packages.urllib3.disable_warnings() 
try:
    while True:
        print("read token file")
        f = open("/run/conjur/access-token", "r")
        token = (base64.b64encode((f.read()).encode('ascii'))).decode('ascii')
        print("token received and base64 encoded")
        print("load variables from env")
        app_url = os.getenv("CONJUR_APPLIANCE_URL")
        account = os.getenv("CONJUR_ACCOUNT")
        pem = os.getenv("CONJUR_SSL_CERTIFICATE")
        f = open("conjur.pem", "w")
        f.write(pem)
        f.close()
        print("environment loaded")
        url = app_url+'/secrets/'+account+'/variable/secrets/username'
        headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8', 'Authorization': 'Token token=\"' + token + '\"'}
        print("start requesting username")
        r = requests.get(url,headers=headers, verify="conjur.pem")
        if r.status_code == 200:
            print("Username: " +r.content.decode())
        else:
            print("HTTP-Error: " + str(r.status_code))
        url = app_url+'/secrets/'+account+'/variable/secrets/password'
        print("start requesting password")
        r = requests.get(url,headers=headers, verify=False)
        if r.status_code == 200:
            print("Password: " +r.content.decode())
        else:
            print("HTTP-Error: " + str(r.status_code))
        time.sleep(10)
except FileNotFoundError:
       print("Token file not found")
except IOError as err:
       print("IO error: {0}".format(err))

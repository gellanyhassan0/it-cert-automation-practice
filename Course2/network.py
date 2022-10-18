#!/usr/bin/python3
import requests
import socket

def check_localhost(host):
       localhost = socket.gethostbyname('localhost')
       if localhost == host :
           return True
       else:
           return False

def check_connectivity(url):

       try:
           r = requests.get(url,timeout=3)
           if r.status_code == 200 :
              return True
           else : 
              return False
       except requests.exceptions.HTTPError as errh:
           print("Http Error:",errh)
           #return False
       except requests.exceptions.ConnectionError as errc:
           print("Error Connecting:",errc)
           #return False
       except requests.exceptions.Timeout as errt:
           print("Timeout Error:",errt)
           #return (False)
       except requests.exceptions.RequestException as err:
           print("OOps: Something Else",err)
           #return(False)


print(check_localhost("127.0.0.1"))
print(check_connectivity("http://www.google.com"))

import time
import urllib.request, json
from subprocess import call
import datetime
import logging
import sys
#from vigia import serverstatusteleg

def checknode():

   vurl="http://myhost/v1/chain/get_info"
   with urllib.request.urlopen(vurl) as url:
    data = json.loads(url.read().decode())
    return(data) 
 
  
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler = logging.FileHandler('logvig.log')
handler.setFormatter(formatter)
logger.addHandler(handler)  

while True:  
 try:
  a=checknode()  
  print(a)
  print(datetime.datetime.now())
  #serverstatusteleg.telegram("Everything OK")
  time.sleep(900) 

 except:
  print("error ")
  print(datetime.datetime.now())
  logger.error(sys.exc_info())
  serverstatusteleg.telegram("We are going to  relaunch node")
  call(["./start.sh"])
  #serverstatusteleg.telegram("Node just relaunched")
  time.sleep(100)
  

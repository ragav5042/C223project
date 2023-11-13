import zipfile
import time

folderpath=input("enter path: ")
zipf=zipfile.ZipFile(folderpath)
global result
result=0
global tried 
tried=0
c=0
if not zipf:
    print("not password protected")
else:
    starttime=time.time()
    wordlistfile=open("wordlist.txt","r",errors="ignore")
    body=wordlistfile.read().lower()
    words=body.split("\n")
    for i in range(len(words)):
        word=words[i]
        password=word.encode('utf8').strip()
        c+=1
        print("Trying to decode the password...{}".format(word))
        try:
            with zipfile.ZipFile(folderpath,'r') as  zf:
                zf.extractall(pwd=password)
                print("Success!! The password is "+word)
                endtime=time.time()
                result=1
                break
        except:
            pass
    if(result==0):
        print("sorry, password not found")
    else:
        duration=endtime-starttime
        print("password found")

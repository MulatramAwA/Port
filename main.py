import os
import fire
import zipfile
import hashlib
import requests
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad,unpad
def upload(url:str,token:str):
    f=open('./.port')
    res=requests.post(url,json={'token':token,'data':f.read()})
    f.close()
    res.raise_for_status()
    print('Uploaded .port file to '+url)
def download(url:str):
    with open('./.port','wb') as f,requests.get(url) as res:
        for chunk in res.iter_content(1024):
            if not chunk:
                break
            f.write(chunk)
def update(key:str,path:str='.'):
    AES_key=int('0x'+hashlib.md5(key.encode('UTF-8')).hexdigest(),base=16)
    AES_key=AES_key.to_bytes(16)
    aes=AES.new(AES_key,AES.MODE_ECB)
    f=zipfile.ZipFile(path+'/.port','w')
    for folderName,subFolders,fileNames in os.walk(path):
        for filename in fileNames:
            if filename=='.port':
                continue
            filepath=os.path.join(folderName, filename)
            f.write(filepath,compress_type=zipfile.ZIP_DEFLATED)
            print(filepath+' DONE')
    f.close()
    f=open('./.port','rb')
    encrypted=aes.encrypt(pad(f.read(),16))
    f.close()
    f=open('./.port','wb')
    f.write(encrypted)
    f.close()
def decode(key:str,path:str='.'):
    AES_key=int('0x'+hashlib.md5(key.encode('UTF-8')).hexdigest(),base=16)
    AES_key=AES_key.to_bytes(16)
    aes=AES.new(AES_key,AES.MODE_ECB)
    f=open(path+'/.port','rb')
    decrypted=unpad(aes.decrypt(f.read()),16)
    f.close()
    f=open(path+'/.port','wb')
    f.write(decrypted)
    f.close()
    f=zipfile.ZipFile('./.port','r')
    f.extractall()
    f.close()
def version():
    print('v1.0.1-beta')
if __name__=='__main__':
    print("""
______          _   
| ___ \        | |  
| |_/ /__  _ __| |_ 
|  __/ _ \| '__| __|
| | | (_) | |  | |_ 
\_|  \___/|_|   \__
    """)
    fire.Fire({'upload':upload,'download':download,'update':update,'decode':decode})

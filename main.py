#-----------------------------------------#
global version                            # Put the value u set here in the "CheckVersion" online list (see *-*-*)
version = 'v.0.1'                         # 
#-----------------------------------------#
class FileStatusCheck:
    
    def StartUpCheck():
        import os
        if FileStatusCheck.CheckVersion() is True:
            print('Valid Version!')
            pass
        else:
            print('Bad/Outdated version :(')
            os._exit(1)
        global impudkey    
        impudkey = input('please enter ur key...\n') #asks a user for his key
        
        if FileStatusCheck.CheckKey(impudkey) is True:
            print('Valid key!')
            pass
        else:
            print('Key is invalid :(')
            os._exit(1)
    
    def Launchsynccheck(key):
        import threading
        CheckSys = threading.Thread(target=FileStatusCheck.synccheck, args=(impudkey,))  #runs a daemon to continiously check if the key is valid, if not the program stops
        CheckSys.daemon = True
        CheckSys.start()
    
    def CheckVersion():
        import requests
        CurrentlySupportedVersions =requests.get('https://pastebin.com/raw/wEdrEKGY' ).text  #*-*-*
        lines = CurrentlySupportedVersions.splitlines()  #this supports multiple versions to be valid, jsut put one version per line in the pastebin/other text bin
        for line in lines:
            if version == line.strip():
                return True
            else:
                return False
    
    def CheckKey(imp):
        import hashlib,requests
        hash_func = hashlib.md5(imp.encode())
        hashedkey=hash_func.hexdigest()
        CorrectKeyHashes =requests.get('https://pastebin.com/raw/4xHxaFAk').text   #make a pastebin with md5 hashes of ur keys (one per line) , if u dont know how to hash,
                                                                                   # then use something like this https://www.md5online.org/md5-encrypt.html to convert ur keys to hashes
        lines = CorrectKeyHashes.splitlines()
        for line in lines:
            if hashedkey == line.strip():
                return True
            else:
                return False
            
    def synccheck(key):
        while True:
            import hashlib,requests,os,time
            hash_func = hashlib.md5(key.encode())
            hashedkey=hash_func.hexdigest()
            CorrectKeyHashes =requests.get('https://pastebin.com/raw/4xHxaFAk').text   #put thesame pastebin as the one u used for the hashes, this checks
                                                                                       #keys while the program is running (extra safety)                 
            lines = CorrectKeyHashes.splitlines()
            for line in lines:
                if hashedkey == line.strip():
                    break
                else:
                    print('Key has been Deleted/ modified , please contact support if this isnt supposed to hapen.')
                    os._exit(1)
            time.sleep(10)

if __name__ == '__main__':
    import threading
    
    FileStatusCheck.StartUpCheck()
    FileStatusCheck.Launchsynccheck(impudkey)
    
    
    #----------------------------------------Start of ur code-----------------------------------(will execute if version is correct and key is correct)
    
    print('O, this is a secret message, please dont tell anyone :)') #example code
    
    
    
    

    
    #EXTRA INFO :::
    #this code only is usefull when compiled to an executable / obfuscated / converted to other language, if not, people can simply decompile / modify code.
    #obfuscating / compiling makes this way harder.
    #if u need help, dm me on discord: "Barack O Llama#7302" . 
    
    
    
    
    
#          oooo                                .            
#          `888                              .o8            
# .ooooo.   888 .oo.    .ooooo.   .oooo.   .o888oo  .oooo.o 
#d88' `"Y8  888P"Y88b  d88' `88b `P  )88b    888   d88(  "8 
#888        888   888  888ooo888  .oP"888    888   `"Y88b.  
#888   .o8  888   888  888    .o d8(  888    888 . o.  )88b 
#`Y8bod8P' o888o o888o `Y8bod8P' `Y888""8o   "888" 8""888P' 
#
#

import subprocess

    
print("\x1b[0;32m**********************************\x1b[0m")    
print("\x1b[0;32m*  usage: python cheats.py       *\x1b[0m")
print("\x1b[0;32m* sets up pretty much everything *\x1b[0m")
print("\x1b[0;32m**********************************\x1b[0m") 

def system(cmd):
    subprocess.call(cmd, shell=True)
    
print("\x1b[0;32mDo You Wish To Install All The yum Shit\x1b[0m") 
faggot = raw_input("Getting Ready Bitch Y to fuck the bitch hoe  Y/n: ")
if faggot.lower() == "y":
    print("Installing all the yum installs")
    system("sudo apt install gcc -y")
    system("sudo apt install httpd -y")
    system("sudo apt install tftp -y")
    system("sudo apt install nano -y")
    system("sudo apt install wget -y")
    system("sudo apt install perl -y")
    system("sudo apt install xinetd tftp tftp-server -y")
    system("sudo apt install screen -y")
    system("sudo apt install nc -y")
    system("sudo apt install cpan -y")
    system("sudo apt install httpd -y")
    system("sudo apt install nginx -y")
    system("sudo apt install vsftpd -y")
    system("sudo apt install unzip -y")
	
    
    system("sudo apt install gcc python-paramiko -y")
 
#    system("service iptables stop") 
#    system("chkconfig iptables off")
#    system("iptables -F") 
    
    system("sudo service vsftpd start")
	
    system("sudo service xinetd start")

    system("sudo service httpd start")

    system('echo -e "ulimit -n 99999" >> ~/.bashrc')
    system("echo -e \"ulimit -n 99999\" > ulimit.sh")
    system("sh ulimit.sh")
    system("rm -rf ulimit.sh") 
    fdsize = open("/usr/include/bits/typesizes.h","r").readlines()
    fdsizew = open("/usr/include/bits/typesizes.h","w").write("")
    for line in fdsize:
        line = line.replace("1024","99999")
        fdsizew = open("/usr/include/bits/typesizes.h","a").write(line)

    system("clear") 
print
print("\x1b[0;35mCoded By Cheats I swear On god if you take credit kys  (:x1b[0m")

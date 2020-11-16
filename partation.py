# for partation 
def parti():
    
    import os
    
    
    ip = input("Enter Your IP Address (eg. 1.2.3.4) : ")
    
    p = input("\nDo you want to make partation? ( yes/no ) : ")
    
    def info():
    	os.system("ssh {} fdisk -l".format(ip))
    
    def Mp():
    	
    	os.system("ssh {} df -h".format(ip))
    
    def cPar():
    	
    	info()
    	dk = input("Enter Disk name : ")
    	os.system("ssh {} fdisk {}".format(ip,dk))
    		
    
    def Driv():
    	
    	os.system("ssh {} udevadm settle".format(ip))
    
    def Fmt():
    	
    	info()
    	DDk = input("Enter partation name to format : ")
    	os.system("ssh {} mkfs.ext4 {} ".format(ip,DDk))
    
    def MnF():
    	
    	info()
    	dd = input("Enter new partation name you have created : ")
    	bb = input("enter Which folder/dir you want to mount ): ")
    	os.system("ssh {} mount {} {}".format(ip,dd,bb))
    	
    	
    
    if p == "yes":
    	print("\n\n\t\t = = = = = = = = = = = = = =")
    	print("Press 1 : To see disk information.")
    	print("Press 2 : To see mounted partations.")
    	print("Press 3 : To create Partations.")
    	print("Press 4 : To Give Driver to Partations.")
    	print("Press 5 : To format the Partations.")
    	print("Press 6 : To Mount folder/directory")
    	print("Press 7 : To Create Everthing with 1 click...like included(1,2,3,4,5)")
    	print("Press 8 : For Exit/Quit")
    	
    	while True:
    		inp = int(input("\n\nEnter Your choice : "))
    		if inp == 1:
    			info()
    		elif inp == 2:
    			Mp()
    		elif inp == 3:
    			cPar()
    		elif inp == 4:
    			Driv()
    		elif inp == 5:
    			Fmt()
    		elif inp == 6:
    			MnF()
    		elif inp == 7:
    			info()
    			print("\t\t\t======================\n\n")
    			Mp()
    			print("\t\t\t======================\n\n")
    			cPar()
    			print("\n\n\t\t\t==========Partation Created============\n\n")
    			Driv()
    			print("\n\n\t\t\t==========Driver Installed============\n\n")
    			Fmt()
    			print("\n\n\t\t\t==========Partation Formated============\n\n")
    			MnF()
    			print("\n\n\t\t\t==========Partation Successfully Created============\n\n")
    		elif inp == 8:
    			exit()
    		else:
    			print("Your Enter Wrong Number")
    			break
    
    
    
    else:
    	print("Thankyou For using...\n good bye...")
    	exit()

parti()
#webserver 



def WS():
    
    import os 
    
    
    print("\t\t\t Menu Card \n")
    
    print("""
    Press 1: To install Httpd Server
    Press 2: To start Services
    Press 3: fOR ALL 
    
    \n""")
    
    ip = input("Enter your IP Address: ")
    
    def ins():
    
    	os.system("ssh {} yum install httpd".format(ip))
    
    def st():
    	
    	os.system("ssh {} systemctl start httpd".format(ip))
    
    
    def tt():
    	
    	os.system("ssh {} yum install httpd ".format(ip))
    	os.system("ssh {} systemctl start httpd".format(ip))
    	os.system("ssh {} systemctl status httpd".format(ip))
    
    	print("\n\n\t\t\t Web Server successfully configure\n\n")
    
    
    while True:
    	
    		ipp = int(input("Enter your choice: "))
    		if ipp ==1:
    			ins()
    		elif ipp ==2:
    			st()
    		elif ipp ==3:
    			tt() 
    		else:
    			exit()
    
WS()

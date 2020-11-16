

#docker lounch


def Dock():
    

    import os
    
    print("\n\n\t\t\t======= Welcome to My World =======\n\n")
    
    
    ip = input("Enter the IP Address (eg. 1.2.3.4 ) : ")
    
    
    def LND():
        os.system("ssh {} yum install docker".format(ip))
        print("\n\n\t\t\t======Docker Installed=======\n")
        
    def Ctos():
        cn = input("tell me which contener/OS you want to lounch : ")
        os.system("ssh {} docker pull {}".format(ip,cn))
        print("\n\n\t\t\t======Contener Installed=======\n\n")
        
    def run():
        cnn = ("Enter contener-image-name and version (eg. centos:latest ): ")
        nm = input("Enter the name as you want to give the contener : ")
        os.system("ssh {} docker run -it --name {} {}".format(ip,nm,cnn))
    
    def img():
        os.system("ssh {} docker images".format(ip))
        
    def attch():
        Nd = input("Enter contener name you want to start again : ")
        os.system("ssh {} docker start {} ".format(ip,Nd))
        os.system("ssh {} docker attach {}".format(ip,Nd))
        
    
    while True:
        print("""
          Press 1 : To Install the Docker
          Press 2 : To install the contener
          Press 3 : To Run the contener
          Press 4 : To See the all contener Images
          Press 5 : To start again the contener
          Press 6 : To See All How many Contanir you Lounched
          Press 7 : To Exit
          """)
    
        aa = int(input("Enter your Choice : "))
        if aa == 1:
            print("\n\t\t\t========================================\n")
            LND()
            print("\n\t\t\t========================================\n")
        elif aa ==2:
            print("\n\t\t\t========================================\n")
            Ctos()
            print("\n\t\t\t========================================\n")
        elif aa ==3:
            print("\n\t\t\t========================================\n")
            run()
            print("\n\t\t\t========================================\n")
        elif aa ==4:
            print("\n\t\t\t========================================\n")
            img()
            print("\n\t\t\t========================================\n")
        elif aa ==5:
            print("\t\t\t========================================\n")
            attch()
            print("\t\t\t========================================\n")
        elif aa ==6:
            os.system("ssh {} docker ps -a".format(ip))
        elif aa == 7:
            exit()
        else:
            print("Not supported ")
            break
            
         
Dock()
        
        
        
        
        
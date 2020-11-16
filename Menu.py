# Menu card Using Python language !!



import os
import getpass as gt



#Header
print("\n")

os.system("tput setaf 2")
print("==============================================================================")

os.system("tput setaf 3")
print("\t\t\tWelcome to My world !!")

os.system("tput setaf 2")
print("==============================================================================")

print("")


# set password

PW = gt.getpass("Enter Password : ")
if PW != "rahul" :
	os.system("tput setaf 9")
	print("\n\nYour Enter Wrong Password.....")
	os.system("tput setaf 4")
	print("\nPlease contact Rahul Rathod ( Mobi- 9179561247 & Email - rr1818772@gmail.com )for login inside the menu.\n\n")
	print("==============================================================================\n")
	exit()




elif PW == "rahul":
	#Menu Card
	os.system("tput setaf 1")
	print("Basic Linux Commands / linux")
	print(" Hadoop Commands / hadoop ")
	print("Linux Partitions")
	print("Docker Basic")
	print("Webserver Configure")
	print("AWS Basic")
	print("-------------------------------------------------------------------------------")

            # Looping  &  Choice's

	while True:
		print("\n= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =")
		cm = input("\t\t\tWhich Commands you want to Run? : ")
		print(" = == = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = \n")
		if ("Linux" in cm) or ("linux" in cm):
                    print("==============================================================================")
                    print("\n\t\t Welcome to Redhat 8 Linux ( Basic Commands ) !!\n")
                    print("""
            press 1 : to run date
            press 2 : to run calender
            press 3 : to see ip Address
            press 4 : to see list of files and directories
            press 5 : to crete directories
            press 6 : to remove directories
            press 7 : to exit
            \n""")		
                    print("==============================================================================")		
                    while True :
                        os.system("tput setaf 5")
                        print("\n\t\t=======================================") 
                        ch = input("\t\t\tEnter Your Choice : ")
                        print("\t\t=======================================\n")		
                        if int(ch) == 1:
                            os.system("tput setaf 4")
                            os.system("date")
                        elif int(ch) == 2:
                            os.system("tput setaf 6")
                            os.system("cal")
                        elif int(ch) == 3:
                            os.system("tput setaf 7")
                            os.system("ifconfig")
                        elif int(ch) == 4:
                            os.system("tput setaf 8")
                            os.system("ls")
                        elif int(ch) == 5 :
                            os.system("tput setaf 2")
                            dn = input("Enter directory name : ")
                            os.system("mkdir {}".format(dn))
                            print("Successfully created directory " +dn)
                        elif int(ch) == 6:  #bag is here
                            os.system("tput setaf 9")
                            os.system("rm -rf {}".format(rdn))
                            print("Successfully removed directory " +rdn)
                        elif int(ch) == 7:
                            os.system("tput setaf 10")
                            print("Have a nice day sir !! ")
                            print("\n------------------------------------------------------------------------------\n")
                            break
                        else:
                            os.system("tput setaf 1")
                            print("Sorry we don't have that, Please Enter valid choice !! ")

		elif ("hadoop" in cm) or ("Hadoop" in cm):
                    print("==============================================================================")
                    print("\n\t\t Welcome to Redhat 8 Linux ( Hadoop Commands ) !!\n")
                    #hadoop configuration [ namenode , datanode , client ] 

                    def hadoop_all():
                        import os
                        def instll():
                            dir = input("Enter directory name where java and hadoop file resides : ")
                            print(dir)
                            os.system("ssh {} rpm -i {}/jdk-8u171-linux-x64.rpm".format(St_ip,dir))
                            os.system("ssh {} rpm -i {}\/hadoop-1.2.1-1.86_64.rpm --force".format(St_ip,dir))

                        def stn():
                                os.system("ssh {} hadoop namenode -format".format(St_ip))
                                os.system("ssh {} hadoop-daemon.sh start namenode".format(St_ip))
                                os.system("ssh {} jps".format(St_ip))
                                os.system("ssh {} hadoop dfsadmin -report".format(St_ip))

                        def stpn():
                                os.system("ssh {} hadoop-daemon.sh stop namenode".format(St_ip))
                                os.system("ssh {} jps".format(St_ip))

                        def std():
                                os.system("ssh {} hadoop-daemon.sh start datanode".format(St_ip))
                                os.system("ssh {} jps".format(St_ip))
                                os.system("ssh {} hadoop dfsadmin -report".format(St_ip))

                        def stpd():
                                os.system("ssh {} hadoop-daemon.sh stop datanode".format(St_ip))
                                os.system("ssh {} jps".format(St_ip))


                        St_ip = input("Enter remote Ip : ")
                        while True :
                            print(''' \t\t\t Select Option:
                            Option1: To configure Namenode
                            Option2: To Configurde datanode
                            Option3: To Configure Client
                            Option4: To Start namenode
                            Option5: To Stop namenode
                            Option6: To Start datanode
                            Option7: To Stop datanode
                            Option8: To Exit
                        ''')
                            option = int(input("\t\t\tSelect Any of these options:"))



                            if option == 1:
                                def namenode():
                                    instll()
                                    print("\t\t\tProvide the details about namenode:")
                                    namenode_IP = input("\t\t\tProvide IP at which you want to configure namenode:")
                                    namenode_folder = input("\t\t\tProvide the Folder name for Namenode:")
                                    os.system("ssh {} rm -rf {}".format(St_ip,namenode_folder))#firstly removing if created 
                                    os.system("ssh {} mkdir {}".format(St_ip,namenode_folder))#creating folder
                                    namenode_port = input("\t\t\tProvide Port Number at which you want to run namenode service:")
                                    file_hdfs_nn = open("/etc/hadoop/hdfs-site.xml","w")#opening the hdfs file to configure 
                                    #hdfs data
                                    hdfs_data_nn =  '''<?xml version="1.0"?>                                            
                                <?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

                                <!-- Put site-specific property overrides in this file. -->
                                <configuration>
                                <property>
                                <name>dfs.name.dir</name>
                                <value>{}</value>
                                </property>
                                </configuration>\n'''.format(namenode_folder)
                                    file_hdfs_nn.write(hdfs_data_nn) #writing in data

                                    file_core_nn = open("/etc/hadoop/core-site.xml", "w")
                                    #core file data
                                    core_data_nn = '''<?xml version="1.0"?>
                                <?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
                                <!-- Put site-specific property overrides in this file. -->
                                <configuration>
                                <property>
                                <name>fs.default.name</name>
                                <value>hdfs://{}:{}</value>
                                </property>
                                </configuration>\n'''.format(namenode_IP,namenode_port)
                                    file_core_nn.write(core_data_nn)   

                                namenode()




                            elif option == 2:
                                def datanode():
                                    instll()
                                    datanode_folder = input("\t\t\tFolder name for datanode:")
                                    os.system("ssh {} rm -rf {}".format(St_ip,datanode_folder))
                                    os.system("ssh {} mkdir {}".format(St_ip,datanode_folder))
                                    namenode_IP = input("\t\t\tProvide namenode IP: ")
                                    namenode_port = input("\t\t\tProvide port number of namenode: ")
                                    file_hdfs_dn = open("/etc/hadoop/hdfs-site.xml","w")#opening hdfs-site.xml file
                                     #data of hdfs of datanode
                                    hdfs_data_dn =  '''<?xml version="1.0"?>
                                <?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

                                <!-- Put site-specific property overrides in this file. -->
                                <configuration>
                                <property>
                                <name>dfs.data.dir</name>
                                <value>{}</value>
                                </property>
                                </configuration>\n'''.format(datanode_folder)
                                    file_hdfs_dn.write(hdfs_data_dn) #writing the data

                                    file_core_dn = open("/etc/hadoop/core-site.xml", "w")#opening core-site.xml file
                                    core_data_dn = '''<?xml version="1.0"?>
                                <?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
                                <!-- Put site-specific property overrides in this file. -->
                                <configuration>
                                <property>
                                <name>fs.default.name</name>
                                <value>hdfs://{}:{}</value>
                                </property>
                                </configuration>\n'''.format(namenode_IP,namenode_port)
                                    file_core_dn.write(core_data_dn)   
                                datanode()


                            elif option == 3: 
                                def client():
                                    instll()
                                    namenode_IP = input("\t\t\tProvide namenode IP: ")
                                    namenode_port = input("\t\t\tProvide port number of namenode: ")
                                    print(''' \t\t\t Select Option:
                                        Option1: Do you Want Change replication factor and block size both
                                        Option2: Do you Want to Change only replication_factor
                                        Option3: Do you Want to Change only block size
                                        Option4: Don't Want to do anything.
                                    ''')

                                    option = int(input("\t\t\tSelect Any of these options:"))

                                    if(option==1):
                                        replication_size=int(input("Enter replication_factor:"))
                                        block_size=int(input("Enter block size in bytes:"))
                                        file_hdfs_cn = open("/etc/hadoop/hdfs-site.xml","w")
                                        hdfs_data_cn =  '''<?xml version="1.0"?>
                                <?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

                                <!-- Put site-specific property overrides in this file. -->
                                <configuration>
                                <property>
                                <name>dfs.replication</name>
                                <value>{}</value>
                                </property>
                                <property>
                                <name>dfs.block.size</name>
                                <value>{}</value>
                                </property>
                                </configuration>\n'''.format(replication_size,block_size)
                                        file_hdfs_cn.write(hdfs_data_cn)

                                    if(option==2):
                                        replication_factor=int(input("Enter replication_factor:"))
                                        file_hdfs_cn = open("/etc/hadoop/hdfs-site.xml","w")
                                        hdfs_data_cn =  '''<?xml version="1.0"?>
                                <?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

                                <!-- Put site-specific property overrides in this file. -->
                                <configuration>
                                <property>
                                <name>dfs.replication</name>
                                <value>{}</value>
                                </property>
                                </configuration>\n\n'''.format(replication_factor)
                                        file_hdfs_cn.write(hdfs_data_cn)

                                    if(option==3):
                                        block_size=int(input("Enter block size in bytes:"))
                                        file_hdfs_cn = open("/etc/hadoop/hdfs-site.xml","w")
                                        hdfs_data_cn =  '''<?xml version="1.0"?>
                                <?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

                                <!-- Put site-specific property overrides in this file. -->
                                <configuration>
                                <property>
                                <name>dfs.block.size</name>
                                <value>{}</value>
                                </property>
                                </configuration>\n'''.format(block_size)
                                        file_hdfs_cn.write(hdfs_data_cn)

                                    if(option==4):
                                        file_hdfs_cn = open("/etc/hadoop/hdfs-site.xml","w")
                                        hdfs_data_cn =  '''<?xml version="1.0"?>
                                <?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

                                <!-- Put site-specific property overrides in this file. -->
                                <configuration>
                                </configuration>\n'''
                                        file_hdfs_cn.write(hdfs_data_cn)


                                    file_core_cn = open("/etc/hadoop/core-site.xml", "w")
                                    core_data_cn = '''<?xml version="1.0"?>
                                <?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
                                <!-- Put site-specific property overrides in this file. -->
                                <configuration>
                                <property>
                                <name>fs.default.name</name>
                                <value>hdfs://{}:{}</value>
                                </property>
                                </configuration>\n'''.format(namenode_IP,namenode_port)
                                    file_core_cn.write(core_data_cn)   
                                client()

                            elif option == 4:
                                stn()

                            elif option == 5:
                                stpn()

                            elif option == 6:
                                std()

                            elif option == 7:
                                stpd()
                            elif option == 8:
                                break

                    hadoop_all()



		elif ("partition" in cm) or ("Partition" in cm):
                    print("==============================================================================")
                    print("\n\t\t Welcome to Redhat 8 Linux ( Linux Partitions ) !!\n")

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
                            

                    parti()


		elif ("Docker" in cm) or ("docker" in cm):
                    print("==============================================================================")
                    print("\n\t\t Welcome to Redhat 8 Linux ( Basic Docker ) !!\n")



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
                                break
                            else:
                                print("Not supported ")
                                


                    Dock()




		elif ("webserver" in cm) or ("server" in cm):
                    print("==============================================================================")
                    print("\n\t\t Welcome to Redhat 8 Linux ( Configure WebServer ) !!\n")  


                    def WS():

                        import os 


                        print("\t\t\t Menu Card \n")

                        print("""
                        Press 1: To install Httpd Server
                        Press 2: To start Services
                        Press 3: fOR ALL 
                        Press 4: exit

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
                                elif ipp==4:
                                    break

                   
                    WS()



		elif("AWS" in cm) or ("aws" in  cm):
			def aws():
				def menu():
					print("Press 1 : To install AWS CLI")
					print("Press 2 : To check AWS version")
					print("Press 3 : To create a new Key Pair")
					print("Press 4 : To display all existing Keys")
					print("Press 5 : To create a new Security Group")
					print("Press 6 : To add new inbound rules to a Security Group")
					print("Press 7 : To launch a new EC2 Instance")
					print("Press 8 : To display existing EC2 Instances")
					print("Press 9 : To start an existing EC2 Instance")
					print("Press 10 : To stop a running EC2 Instance")
					print("Press 11 : To terminate an EC2 Instance")
					print("Press 12 : To create an EBS Volume")
					print("Press 13 : To attach an EBS VOlume to an EC2 Instance")
					print("Press 14 : To detach an EBS Volume from an EC2 Instance")
					print("Press 15 : To create a new S3 Bucket")
					print("Press 16 : To copy files to S3 Bucket")
					print("Press 17 : To create a CloudFront Distribution")
					print("Press 18 : To remotely login to an EC2 Instance")
					print("Press 19 : To create a Snapshot")
					print("Press 20 : To restore a snapshot")
					print("Press 21 : TO EXIT")	 
                    
				def version():
					a = os.system("aws --version 2>> ttt.txt")
					if a !=0 :
						print("Please install AWS CLI first")
                    
				def install():
					a = os.system("aws --version | grep 2.0")
					if a != 0 :
						os.system('curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"')
					a = os.system("rpm -q unzip | grep xyz")
					if a !=0 : 
						os.system("yum install unzip -y")
					os.system("unzip awscliv2.zip")
					os.system("sudo ./aws/install")
                    
				def createKey():
					keyn = input("Enter the key name: ")
					a = os.system("aws ec2 create-key-pair --key-name {0} > {0}.pem".format(keyn))
					if a==0:
						os.system("tput setaf 6")
						print("Key successfully created")
                    
				def displayKey():
					os.system("aws ec2 describe-key-pairs")
                    
				def createSecurityGroup():
					name = input("Enter the name of new security group: ")
					des = input("Enter the security group description: ")
					os.system("aws ec2-create-security-group --group-name {} --description {}".format(name, des))
                    
				def addBounds():
					name = input("Enter the security group name: ")
					protocol = input("Enter the protocol: ")
					port = input("Enter the port number: ")
					cidr = input("Enter the cidr block: ")
					a = os.system("aws ec2 authorize-security-group-ingress --group-name {} --protocol {} --port {} --cidr {} 2>> ttt.txt".format(name,protocol,port,cidr))
					if a!=0 :
						print("Enter valid details")
					else:
						os.system("tput setaf 6")
						print("Inbound Rules successfully added")
						os.system("tput setaf 7")
                    
				def newInstance():
					ami = input("Enter the AMI id: ")
					type = input("Enter the instance type: ")
					count = input("Enter the number of instances to be launched: ")
					subid = input("Enter the subnet id: ")
					secname = input("Enter the security group ID: ")
					key = input("Enter the key name: ")
					a = os.system("aws ec2 run-instances --image-id {} --instance-type {} --count {} --subnet-id {} --security-group-ids {} --key-name {} 2>> ttt.txt".format(ami, type, count, subid, secname, key))
					if a != 0 :
						print("Enter the valid details")
                    
                    
				def displayInstance():
					os.system("aws ec2 describe-instances")
                    
				def startInstance():
					id = input("Enter the Instance ID to be launced: ")
					a = os.system("aws ec2 start-instances --instance-ids {} 2>> ttt.txt".format(id))
					if a!=0:
						print("Enter the valid details")
                    
				def stopInstance():
					id = input("Enter the id of instance to be stopped: ")
					a = os.system("aws ec2 stop-instances --instance-ids {} 2>> ttt.txt".format(id))
					if a!=0 :
						print("Enter a valid running instance id")
                    
				def terminateInstance():
					print("WARNING: Terminating an instance would result in loss of all data")
					inp = input("Press 1 to continue with the process: ")
					if inp==1:
						id = input("Enter id of instance to be terminated: ")
					a = os.system("aws ec2 terminate-instances --instance-ids {} 2>> ttt.txt".format(id))
					if a!=0 :
							print("Enter a valid ID")
                    
                    
				def createVolume():
					type = input("Enter the volume type: ")
					size = input("Enter the volume size: ")
					az = input("Enter the availibilty zone: ")
					a = os.system("aws ec2 create-volume --volume-type {} --size {} --availability-zone {} 2>> ttt.txt".format(type, size, az))
					if a!=0 :
						print("Enter valid details")
                    
                    
				def attachVolume():
					id = input("Enter volume id: ")
					insid = input("Enter Instance ID: ")
					dev = input("Enter device name: ")
					a = os.system("aws ec2 attach-volume --instance-id  {} --volume-id {} --device {} 2>> ttt.txt".format(insid, id, dev))
					if a!=0 :
						print("Enter valid details")
                    
				def detachVolume():
					id = input("Enter volume id: ")
					a = os.system("aws ec2 detach-volume --volume-id {} 2>> ttt.txt".format(id))
					if a!=0 :
						print("Enter valid Volume ID")
                    
                    
				def createBucket():
					name = input("Enter the Bucket Name: ")
					access = input("Enter the access permission: ")
					lc = input("Enter the Location Constraint: ")
					a = os.system("aws s3api create-bucket --bucket {} --ac {} --create-bucket-configuration LocationConstraint={} 2>> ttt.txt".format(name, access, lc))
					if a!=0 :
						print("Enter valid details")
                    
				def cpBucket():
					path = input("Enter the complete path of file to be copied in bucket: ")
					name = input("Enter the bucket name: ")
					per = input("Enter the permission: ")
					a = os.system("aws s3 cp {} s3://{} --acl {} 2>> ttt.txt".format(path, name, per))
					if a!=0 :
						print("Enter valid details")
                    
				def createCloudfront():
					id = input("Enter the origin domain name: ")
					a = os.system("aws cloudfront create-distribution --origin-domain-name {} 2>> ttt.txt".format(id))
					if a!=0 :
						print("Enter a valid origin name")
                    
				def loginInstance():
					ip = input("Enter the public ip of the Instance: ")
					name = input("Enter the full path of key: ")
					a = os.system("ssh -i {} ec2-user@{} 2>> ttt.txt".format(name, ip))
					if a!=0 :
						print("Enter valid details")
                    
				def createSnapshot():
					id = input("Enter the volume id: ")
					des = input("Enter the description")
					a = os.system("aws ec2 create-snapshot --volume-id {} --description {} 2>> ttt.txt".format(id, des))
					if a!=0 :
						print("Enter the valid details")
                    
				def restoreSnapshot():
					id = input("Enter the snapshot ID: ")
					a = os.system("aws restore-from-snapshot --snapshot-id {} 2>> ttt.txt".format(id))
					if a!=0 :
						print("Enter valid snapshot ID")
				while True:
					os.system("tput setaf 6")
					menu()
					os.system("tput setaf 7")
					print("\n")
					choice = int(input("Enter your choice: "))
					if choice==1:
						install()
					elif choice==2:
						version()
					elif choice==3:
						createKey()
					elif choice==4:
						displayKey()
					elif choice==5:
						createSecurityGroup()
					elif choice==6:
						addBounds()
					elif choice==7:
						newInstance()
					elif choice==8:
						displayInstance()
					elif choice==9:
						startInstance()
					elif choice==10:
						stopInstance()
					elif choice==11:
						terminateInstance()
					elif choice==12:
						createVolume()
					elif choice==13:
						attachVolume()
					elif choice==14:
						detachVolume()
					elif choice==15:
						createBucket()
					elif choice==16:
						cpBucket()
					elif choice==17:
						createCloudfront()
					elif choice==18:
						loginInstance()
					elif choice==19:
						createSnapshot()
					elif choice==20:
						restoreSnapshot()
					elif choice==21:
						os.system("tput setaf 1")
						print("Do you want to EXIT ?")
						os.system("tput setaf 7")
						ch = input("Press Y to exit and N to continue : ")
						if ch=='y' or ch=='Y':
							print("Terminating...")
							break
						else:
							print("Enter a valid choice")
						os.system("tput setaf 6")
						inp = input("Press Enter to continue")
						os.system("tput setaf 7")
						os.system("clear")	
			aws()
                


		elif ("exit" in cm):
                    print("ThankYou For giving your time \n good bye \n have a nice day...")
                    exit()
            








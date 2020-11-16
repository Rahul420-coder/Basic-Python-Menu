
def aws():
    import os
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
    		ch = input("Press Y to exit and N to continue")
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
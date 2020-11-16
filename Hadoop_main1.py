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

hadoop_all()
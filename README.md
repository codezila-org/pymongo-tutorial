# pymongo-tutorial
This Repo contains example programs of pymongo( Database connectivity with MongoDB ).

# Setup :
### Setup for MongoDB in windows:
1. Download MongoDB Server from MongoDB Download Center. Follow this URL :
   - [Download MongoDB Server for Windows x64](https://fastdl.mongodb.org/win32/mongodb-win32-x86_64-2012plus-4.2.6-signed.msi)

2. Open Download folder double click on downloaded file to start installation. 

    >Now Click on Next.

    ![image1](https://github.com/AmanSingour/Tutorial-Images/blob/master/pymongo/1.PNG)

3. Accept terms & condition and click on Next.

    ![image2](https://github.com/AmanSingour/Tutorial-Images/blob/master/pymongo/2.PNG)

4. Now Choose Setup Type.

    >Click on Complete
    
    >Click on Next
    
    ![image3](https://github.com/AmanSingour/Tutorial-Images/blob/master/pymongo/3.PNG)

5. Now Choose the Service Configuration.

    >Check on Install MongoDB as a service.
    
    >Select Run Service as Network Service User.
    
    >Click on Next
    
    ![image4](https://github.com/AmanSingour/Tutorial-Images/blob/master/pymongo/4.PNG)

6. Ready To Install MongoDB.

    >Click on Install
    
    ![image5](https://github.com/AmanSingour/Tutorial-Images/blob/master/pymongo/6.PNG)

7. Wait for the completion of status.

    >Click Next
      
    ![image6](https://github.com/AmanSingour/Tutorial-Images/blob/master/pymongo/7.PNG)

8. You have Complete the installation of MongoDB Server in Your Machine.

    >Click on Finish
    
    ![image7](https://github.com/AmanSingour/Tutorial-Images/blob/master/pymongo/8.PNG)

9. Now you have to set Environmental Path.

    > Goto the dir on your system :
    
    > C:\Program Files\MongoDB\Server\4.2\bin\
    
    ![image8](https://github.com/AmanSingour/Tutorial-Images/blob/master/pymongo/9.PNG)

10. Now open Edit the System Environmental Variable.
    >Click On Environmental Variables...
    
    >Edit Path
    
    >Add two Paths :
    
    >C:\Program Files\MongoDB\Server\4.2\bin\mongo
    
    >C:\Program Files\MongoDB\Server\4.2\bin\mongod
    
    ![image9](https://github.com/AmanSingour/Tutorial-Images/blob/master/pymongo/10.PNG)

**You have completed MongoDB Server in your Local Machine.**

### Install pymongo

    
      $ python -m pip install pymongo
    

### Connectivity with Database :

1. Clone createDB.py 

2. Replace URL in MongoClient

    > For Localhost
    
        > "mongodb://localhost:27017/" 
      
    > For MongoDB Atlas
    
        > Replace with your Cluster srv
        
        > e.g. "mongodb+srv://<yourusername>:<yourpassword>@cluster0-mgbud.mongodb.net/test?retryWrites=true&w=majority"
 
3. To Create Database
    > Replace DbName with Your Database Name.
    
    > Replace collName with Your Database Collection Name.

    > Enter Data What You Want To Store In Database.
    
4. Run createDB.py

**Hurray... You Have Successfully Created Database With pymongo in MongoDB.**

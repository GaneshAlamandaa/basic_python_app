from pymongo import MongoClient

class OrgConfig:
    MONGO_URI = 'mongodb+srv://nexus-360-dev-user:tgaiqVncYpj6vOpz@nexus-360-dev.6tgnxqq.mongodb.net/'
    DATABASE_NAME = 'Nexus360'
    COLLECTION_NAME = 'Organization'

    @staticmethod
    def get_database():
        client = MongoClient(OrgConfig.MONGO_URI)
        return client[OrgConfig.DATABASE_NAME]

    @staticmethod
    def get_organization_collection():
        db = OrgConfig.get_database()
        return db[OrgConfig.COLLECTION_NAME]

class UserConfig:
    @staticmethod
    def get_mongo_client():
        client = MongoClient('mongodb+srv://nexus-360-dev-user:tgaiqVncYpj6vOpz@nexus-360-dev.6tgnxqq.mongodb.net/')
        return client

    @staticmethod
    def get_database():
        client = UserConfig.get_mongo_client()
        db = client['Nexus360']
        return db

    @staticmethod
    def get_users_collection():
        db = UserConfig.get_database()
        collection = db['users']
        return collection

class LoginConfig:
    @staticmethod
    def get_mongo_client():
        client = MongoClient('mongodb+srv://nexus-360-dev-user:tgaiqVncYpj6vOpz@nexus-360-dev.6tgnxqq.mongodb.net/')
        return client
    
    @staticmethod
    def get_database():
        client = LoginConfig.get_mongo_client()
        db= client['Nexus360']
        return db
    @staticmethod
    def get_login_details():
        db = LoginConfig.get_database()
        collection = db['login_logfiles']
        return collection

class SpaceConfig:
    @staticmethod
    def get_mongo_client():
        client = MongoClient('mongodb+srv://nexus-360-dev-user:tgaiqVncYpj6vOpz@nexus-360-dev.6tgnxqq.mongodb.net/')
        return client

    @staticmethod
    def get_database():
        client = SpaceConfig.get_mongo_client()
        db = client['Nexus360']
        return db
 
    @staticmethod
    def get_Space_collection():
        db = useraccessconfig.get_database()
        collection = db['spaces']
        return collection

class useraccessconfig:
    @staticmethod
    def get_mongo_client():
        client = MongoClient('mongodb+srv://nexus-360-dev-user:tgaiqVncYpj6vOpz@nexus-360-dev.6tgnxqq.mongodb.net/')
        return client

    @staticmethod
    def get_database():
        client = useraccessconfig.get_mongo_client()
        db = client['Nexus360']
        return db
 
    @staticmethod
    def get_useraccess_collection():
        db = useraccessconfig.get_database()
        collection = db['UsersAccessData']
        return collection

class uploadconfig:
    @staticmethod
    def get_mongo_client():
        client = MongoClient('mongodb+srv://nexus-360-dev-user:tgaiqVncYpj6vOpz@nexus-360-dev.6tgnxqq.mongodb.net/')
        return client

    @staticmethod
    def get_database():
        client = uploadconfig.get_mongo_client()
        db = client['Nexus360']
        return db
 
    @staticmethod
    def get_upload_collection():
        db = uploadconfig.get_database()
        collection = db['Uploaded_Documents']
        return collection

class userinfoconfig:
    @staticmethod
    def get_mongo_client():
        client = MongoClient('mongodb+srv://nexus-360-dev-user:tgaiqVncYpj6vOpz@nexus-360-dev.6tgnxqq.mongodb.net/')
        return client

    @staticmethod
    def get_database():
        client = userinfoconfig.get_mongo_client()
        db = client['Nexus360']
        return db
 
    @staticmethod
    def get_user_collection():
        db = userinfoconfig.get_database()
        collection = db['users']
        return collection  

class versionconfig:

    @staticmethod
    def get_mongo_client():
        client = MongoClient('mongodb+srv://nexus-360-dev-user:tgaiqVncYpj6vOpz@nexus-360-dev.6tgnxqq.mongodb.net/')
        return client

    @staticmethod
    def get_database():
        client = userinfoconfig.get_mongo_client()
        db = client['Nexus360']
        return db

    @staticmethod
    def get_version_collection():
        db = userinfoconfig.get_database()
        collection = db['Version_Documents']
        return collection
        
class Deleteconfig:

    @staticmethod
    def get_mongo_client():
        client = MongoClient('mongodb+srv://nexus-360-dev-user:tgaiqVncYpj6vOpz@nexus-360-dev.6tgnxqq.mongodb.net/')
        return client

    @staticmethod
    def get_database():
        client = userinfoconfig.get_mongo_client()
        db = client['Nexus360']
        return db

    @staticmethod
    def get_delete_collection():
        db = userinfoconfig.get_database()
        collection = db['Deleted_Documents']
        return collection

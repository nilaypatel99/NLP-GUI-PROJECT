import json
#Here we are creating a database class
class Database:
    def add_data(self,name,email,password):
        
        json_path='D:\python\corey\oop-project\db.json'
        with open(json_path,'r') as rf:
            database=json.load(rf)
            
        if email in database:     #if email already return 0
            return 0
        else:                     #if not include the data
            database[email]=[name,password]
            with open(json_path,'w') as wf:
                json.dump(database,wf)
            return 1 
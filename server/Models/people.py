

from Database.db import mng_db
from api.Exceptions.SystemErrorException import SystemErrorException


class People():
    
    def findPeopleByCompanyId(self,company_id):

        collection_name = 'people'
        db = mng_db[collection_name]
        listOfCompanies = []
        try:
            result_list = db.find({"company_id":int(company_id)})
            for item in result_list:
                listOfCompanies.append(item)
        
        except:
            raise SystemErrorException("can't use find people service")
        
        if len(listOfCompanies) == 0 :
            return -1
        
        return listOfCompanies

    def getDetailById(self,id):
        collection_name = 'people'
        db = mng_db[collection_name]
        index = int(id)
        
        result_list = db.find_one({"index":index})
        if result_list == None or len(result_list) == 0 :
            return -1
        
        return result_list


    def common_member(self,a, b): 
        a_set = set(a) 
        b_set = set(b) 
        # check length  
        if len(a_set.intersection(b_set)) > 0: 
            return(a_set.intersection(b_set))   
        else: 
            return("no common elements") 
            

    def findFriends(self,people_a_id,people_b_id):

        collection_name = 'people'
        db = mng_db[collection_name]
        
        
        personA = db.find_one({"index":people_a_id})
        personB = db.find_one({"index":people_b_id})

        friendsOfA = []
        friendsOfB = []
        for item in personA['friends']:
            friendsOfA.append(item['index'])

        for item in personB['friends']:
            friendsOfB.append(item['index'])

        common = self.common_member(friendsOfA,friendsOfB )
     
        return common


    def findCommonFriends(self,people_a_id,people_b_id):

        collection_name = 'people'
        db = mng_db[collection_name]
        
        agr = [
                {
                    '$lookup':
                    {
                        'from': "people",
                        'localField': "friends.index",
                        'foreignField': "index",
                        'as': "friendsDetail",
                                
                    },
                },
                {
                    '$match':{
                       	"$and":[
                            {"index": {"$in":[people_a_id,people_b_id]}},
                        ]
                    }
                },
                {
                    '$project': {
                        'name':1,
                        "age":1,
                        "index":1,
                        "phone":1,
                        "address":1,
                        'friendsDetail': {
                            '$filter': {
                                'input': "$friendsDetail",
                                'as': "item",
                                'cond': {  
                                    '$and':[
                                            { '$eq': [ "$$item.eyeColor", "brown" ] },
                                            { '$eq': [ "$$item.has_died", False ] }
                                        ]
                                }
                            }
                        },
                    }
                } 
            ]

        out = db.aggregate(agr)
        friends_alive = []
        friendsIndexList= []
        commonFriend = []
        for item in out: 
            for uu in (item['friendsDetail']):
                if uu['index'] not in friendsIndexList:
                    friendsIndexList.append(uu['index'])
                else:
                    commonFriend.append(uu)


        dataOutput = []
        keys_wanted = ['age','name','eyeColor','has_died']
        for item in commonFriend:
            item = dict((key,value) for key, value in item.items() if key in keys_wanted)
            dataOutput.append(item)
            
        return dataOutput


    def fruitsList(self):
        return {
            "name":"fruits",
            "tags":[
                "banana",
                "apple",
                "strawberry",
                "orange",
            ]
        }
            
    
    def vegetablesList(self):
        return{
            "name":"vegetables",
            "tags": [
                "beetroot",
                "lettuce",
                "cucumber",
                "carrot",
                "celery",
            ]
        }
        
    
    def getTagByCalculateDistance(self,tag):
        
        groups = [
            self.fruitsList(),
            self.vegetablesList()
        ]

        for group in groups:
            if tag in group['tags']:
                return group['name']
        return "nonClassified"

    def findFavourite(self,person_id):

        fruitsList = self.fruitsList()
        vegetablesList = self.vegetablesList()
        
        user_detail = self.getDetailById(person_id)
        favouriteFood = user_detail['favouriteFood']
        targetGroups = {}
        for item in favouriteFood:
            groupName = self.getTagByCalculateDistance(item)
            if  groupName not in targetGroups:

                targetGroups[groupName] = []
                
            targetGroups[groupName].append(item)
        
        result =  {
            "username":user_detail['name'],
            "age":user_detail['age'],
        }
        for key in targetGroups:
            result[key] = targetGroups[key]
            
        return result
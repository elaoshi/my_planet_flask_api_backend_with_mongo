

from Database.db import mng_db
from Models.people import People


class Company():
    def listEmployeeListByName(self,name):
        campany_name = name.upper()
        collection_name = 'companies'
        db = mng_db[collection_name]

        listOfCompanies = []
        try:
            result_campany = db.find_one({"company":campany_name})
            if result_campany != None:
                companyId = result_campany['index']
                people = People()
                company_list = people.findPeopleByCompanyId(companyId)
                return company_list

        except:
            raise Exception("system error")
        
        if len(listOfCompanies) == 0 :
            return -1
        

        return listOfCompanies

    

    def listEmployeeListById(self,index):

        collection_name = 'companies'
        db = mng_db[collection_name]
     
        listOfCompanies = []
        try:
            result_campany = db.find_one({"index":index})
            if result_campany != None:
                companyId = result_campany['index']
                people = People()
                company_list = people.findPeopleByCompanyId(companyId)
                return company_list

        except:
            raise Exception("system error")
        
        if len(listOfCompanies) == 0 :
            return -1
        

        return listOfCompanies
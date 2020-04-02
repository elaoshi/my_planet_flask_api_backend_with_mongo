 
import os
import unittest
 


from Models.people import People

from api.Exceptions.SystemErrorException import SystemErrorException
 
 
class BasicTests(unittest.TestCase):
 
    # executed prior to each test
    def setUp(self):
        pass
    # executed after each test
    def tearDown(self):
        pass
 
 
 
    def test_people_find_people_by_cid(self):
        people = People()
        result = people.findPeopleByCompanyId(1)
        assert(result[0]['index']==289)
    

    def test_people_find_people_not_exist(self):
        people = People()
        result = people.findPeopleByCompanyId(0)
        assert(result== -1 )

    
    def test_people_find_people_not_exist_2(self):
        people = People()
        result = people.findPeopleByCompanyId(9999999)
        assert(result== -1 )


    def test_people_find_people_not_exist_3(self):
        people = People()
        
        expectedMsg =  "can't use find people service"
        try:
            result = people.findPeopleByCompanyId("fasdf")
            self.assertFail()
        except SystemErrorException as inst:
            self.assertEqual(inst.message, expectedMsg)
        
    
        
 
if __name__ == "__main__":
    unittest.main()
from flask_restplus import Namespace, Resource, fields

from Database.db import mng_db
from Models.people import People 

import re

api = Namespace('people', description='People related operations')


@api.route('/')
class ItemList(Resource):
    @api.doc('list_items')
    # @api.marshal_list_with(item)
    def get(self):
        '''List all items'''
        collection_name = 'people'
        db = mng_db[collection_name]

        listOfItems = []
        try:
            result_list = db.find()
        except:
            api.abort(500, 'system error')
        for item in result_list:
            listOfItems.append(item['index'])
        return listOfItems

@api.route('/<id>')
class PersonItem(Resource):
    @api.doc(responses={ 200: 'OK', 400: 'Invalid Input', 204:"not found",500: 'Mapping Key Error' }, 
                params={ 'id': 'Specify the id associated with people' })
    
    def get(self,id ):
        '''get person detail'''
        pattern = re.compile("^[0-9]{1,6}$")
        if bool(pattern.match(id)) is False :
            api.abort(400)


        people = People()

        try:
            index = int(id)
        except:
            api.abort(400)

        result_list = people.getDetailById(index)
        
        if -1 == result_list :
            return '',204

        return result_list


@api.route('/<person_a_id>/<person_b_id>')
class FriendsItem(Resource):

    @api.doc( responses={ 200: 'OK', 400: 'Invalid Argument',204:'not found ',399:'system error' , 500: 'System Error' }, 
                params={ 'person_a_id': 'Specify the Id associated with the people A' , 'person_b_id': 'Specify the Id associated with the people B' })
    # @api.marshal_list_with(item)
    def get(self,person_a_id, person_b_id ):
        '''get common friends between people A and B '''

        pattern = re.compile("^[0-9]{1,10}$")
        if bool(pattern.match(person_a_id)) is False :
            api.abort(400,"input error")
        if bool(pattern.match(person_b_id)) is False :
            api.abort(400,"input error")


        people = People()

        person_a_id = int(person_a_id)
        person_b_id = int(person_b_id)


        person_a_detail = people.getDetailById(person_a_id)
        person_b_detail = people.getDetailById(person_b_id)
        if -1 == person_a_detail or -1 == person_a_detail:
            return '',204
        
        friends = people.findCommonFriends(person_a_id,person_b_id)
        

        details = {
            "person_a" : {
                "Name": person_a_detail['name'],
                "Age": person_a_detail['age'],
                "Address":person_a_detail['address'],
                "Phone":person_a_detail['phone'],
                "index":person_a_detail['index'],
            },
            "person_b" : {
                "Name": person_b_detail['name'],
                "Age": person_b_detail['age'],
                "Address":person_b_detail['address'],
                "Phone":person_b_detail['phone'],
                "index":person_b_detail['index'],
            },
            'common_friend':friends
        }
       
        

        return {"data":details}


@api.route('/favourite/<person_id>')
class FavouriteItem(Resource):

    @api.doc( responses={ 200: 'OK', 400: 'Invalid Argument',399:'system error' , 500: 'System Error' }, 
                params={ 'person_id': 'Specify the Id associated with the people' })
    def get(self,person_id):
        '''get faviourite friuts and vegetables by id of person '''
        pattern = re.compile("^[0-9]+$")
        if bool(pattern.match(person_id)) is False :
            api.abort(400,"input error")

        people = People()
        try:
            items = people.findFavourite(person_id)
        except:
            api.abort(500)
        
        return items



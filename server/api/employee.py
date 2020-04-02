from flask_restplus import Namespace, Resource, fields

from Database.db import mng_db
from Models.company import Company
from Models.people import People 
import re 


api = Namespace('employee', description='Employee related operations')

item = api.model('Employee', {
    'id': fields.String(required=True, description='The item identifier'),
    'name': fields.String(required=True, description='The company name'),
})


@api.route('/company_name/<name>')
class EmployeesList(Resource):
    @api.doc('list_items' , responses={ 200: 'OK', 400: 'Invalid Argument',204: 'not found',399:'system error' , 500: 'system error x01' }, 
                params={ 'name': 'Specify the name associated with the company' })
    def get(self,name):
        '''List all employee by name of campany '''

        
        pattern = re.compile("^[A-Za-z]+$")
        if bool(pattern.match(name)) is False :
            api.abort(400,"input error")

        companyInstance = Company()
        try:
            listOfCompanies =  companyInstance.listEmployeeListByName(name)
        except:
            api.abort(500,"system error x01")
        
        if -1 == listOfCompanies :
            return '',204
        return {"data":listOfCompanies}



@api.route('/company_id/<id>')
class EmployeesListByCampanyId(Resource):
    @api.doc(responses={ 200: 'OK', 400: 'Invalid Argument',204:"not found",399:'system error' , 500: 'System Error' }, 
                params={ 'id': 'Specify the Id associated with the company' })
    def get(self,id):
        '''List all employee by id of company'''
        pattern = re.compile("^[0-9]+$")
        if bool(pattern.match(id)) is False :
            api.abort(400,"input error")

        try:
            index = int(id)
        except:
            api.abort(400, 'input error')

        companyInstance = Company()
        try:
            listOfCompanies =  companyInstance.listEmployeeListById(index)
        except:
            api.abort(500,"system error")

        if -1 == listOfCompanies :
            return '', 204

        return {"data":listOfCompanies}


        


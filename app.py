from flask import Flask, render_template, request
from pymongo import MongoClient
from pprint import pprint

app = Flask(__name__)

client = MongoClient('mongodb://mongo-db:27017/')
db=client.test
storage = db.storage
#storage.drop()
#exit()

def database_new_entry(new_result):

            global storage
            if storage.find({'Name': new_result['Name'] }).count() > 0:
                  avaliability_flag=True
                  print('Trying to overwrite issue')
                  exit()

            
            student_details = {
                  'Name': new_result['Name'],
                  'grds': new_result
            }
            
            entry_status = storage.insert_one(student_details)
            return entry_status

def database_update_entry(key_val,new_result):
            global storage
            entry_status = storage.update_one(
                  {'Name':key_val},
                  {
                        "$set": {'grds':new_result}
                  }
            )
            print('inside database_update_entry', key_val, new_result)
            return entry_status



data={}
#data['Headings']=
@app.route('/')
def student():
   return render_template('student.html')

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form
      print(result)
      print(result['Name'])
      global data
      
      if storage.find({'Name': result['Name'] }).count() > 0:
            avaliability_flag=True
            Queryresult = storage.find_one({'Name': result['Name']})
            pass_dict=Queryresult['grds']
      else:
            avaliability_flag=False
      print('Check if key available: ',avaliability_flag)
      
      print('checking db existance')
      if avaliability_flag==False: #not (result['Name'] in data.keys()):
         data[result['Name'] ]=result
         print('data',data)
         print("result['Name']",data[result['Name']])
         entry_status=database_new_entry(result)
         return render_template("result.html",result = result)
         
      else:
         return render_template("edit.html",result = result, old_result= pass_dict)
      

@app.route('/update',methods = ['POST', 'GET'])
def update():
      result = request.form
      print('result from updater',result)
      global data
      name_var=result['Name']
      print('name_var',type(name_var),name_var)
      name_var_without_padding=name_var[1:-1]
      data[name_var_without_padding]=result
      update_status = database_update_entry(name_var_without_padding,result)
      print('Final result:::::::',result)
      return render_template('student.html')


@app.route('/fulllist',methods = [ 'GET'])
def fulllist():
      print("Into full list===========")
      global data
      tl=['  Student Name  ','  Physics  ','  Chemistry  ','  Mathematics  ']
      global db
      coll1 = db.storage #selecting the coll1 in myDatabase
      mod_dict={}
      for document in coll1.find():
            print('database',document)
            print("split",document['Name'],document['grds'])
            mod_dict[document['Name']]=document['grds']
      return render_template('print.html',dict=mod_dict,headings=tl)





@app.route('/studenteditlink/<string:iname>',methods = [ 'GET'])
def studenteditlink(iname):
      #name_var=data[iname]
      global storage
      Queryresult = storage.find_one({'Name': iname})
      print('Queryresult:::')
      pprint(Queryresult)
      pass_dict=Queryresult['grds']
      print('pass_dict',pass_dict)
      return render_template('editstudent.html',sname=iname,  obj=pass_dict)

if __name__ == '__main__':
   app.run(host="0.0.0.0", port = 5000)
from flask import Flask, json, request, jsonify
from flask_mysqldb import MySQL,MySQLdb 

app = Flask(__name__)

from flask_mysqldb import MySQL,MySQLdb 
 
app = Flask(__name__)
  
app.secret_key = "caircocoders-ednalan-2020"
  
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'machine'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
mysql = MySQL(app)
  
@app.route('/')
def index():
   cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
   cur.execute("SELECT * FROM vm")
   rv = cur.fetchall()
   vm = []
   content = {}
   for result in rv:
       content = {'id': result['id'], 'nom': result['nom'], 'carte': result['carte']}
       vm.append(content)
       content = {}
   return jsonify(vm) 
    
        
if __name__ == '__main__':
    app.run(debug=True)
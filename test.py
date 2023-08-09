import mysql.connector
 
config = {}
 
config['MYSQL_HOST'] = '192.168.167.224'
config['MYSQL_USER'] = 'root'
config['MYSQL_PASSWORD'] = 'password'
config['MYSQL_DB'] = 'test'
 
mydb = mysql.connector.connect(
  host=config['MYSQL_HOST'],
  user=config['MYSQL_USER'],
  password=config['MYSQL_PASSWORD'],
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE mydatabase")
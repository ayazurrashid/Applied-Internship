import psycopg2

class database:
	def __init__(self,conn,cur,db,usr,pswd,hst):
		self.conn=conn
		self.cur=cur
		self.db=db
		self.usr=usr
		self.pswd=pswd
		self.hst=hst
		print("Initialization Done")

	def connect(self):
		self.conn = psycopg2.connect(database = self.db, user =self.usr, password =self.pswd, host =self.hst)
		print("Opened database successfully")
		self.cur = self.conn.cursor()

	#create table tablename(col1 datatype)
	def createtable(self,tname,kwargs):
		string="create table "+tname+"("
		for key,value in kwargs.items():
			string=string+key +" "+ value+","
		string=string.rstrip(",")+")"
		self.cur.execute(string)	
		print("table created successfully")

	def showtables(self):
		self.cur.execute("""select table_name from information_schema.tables
       	where table_schema = 'public'""")
		for table in self.cur.fetchall():
			print(table)

	def droptable(self,tname):
		string="drop table"
		string=string+" "+"if exists"+" "+tname
		self.cur.execute(string)
	
	def commit(self):
		self.conn.commit()
		print("commited")
	
	def connclose(self):
		self.conn.close()
		print("Connection closed")

c1=database('a','b','mytestdb','postgres','ayaz@5553','localhost')
c1.connect()
c1.createtable(input("table name to be created: "),{'col1':'int','col2':'text'})
c1.commit()
c1.showtables()
c1.droptable(input("Enter the table name to be drop: "))
c1.commit()
c1.showtables()
c1.connclose()
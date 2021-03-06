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
	
	def select_query(self):
		self.cur.execute('select * from consumers')
		rows =self.cur.fetchall()
		for row in rows:
	   		print(row)
		print("Retrieval done successfully")
	
	def insert_query(self):
		n=input("Enter The ID: ")
		m=input("Enter the Name: ")
		p=input("Enter The age: ")
		self.cur.execute("insert into consumers values(%s,%s,%s)",(n,m,p))
		print("insertion done successfully")
	
	def update_query(self):
		m=input("Enter the New Name: ")
		p=input("Enter The New age: ")
		n=int(input("Enter The ID: "))
		self.cur.execute("update consumers set name=%s,age=%s where id=(%s)",(m,p,n))
		print("Updation done successfully")
	
	def delete_query(self):
		n=input("Delete The ID: ")
		self.cur.execute("delete from consumers where id=(%s)",(n,))
		print("Deletion done successfully")
	
	def commit(self):
		self.conn.commit()
		print("commited")
	
	def connclose(self):
		self.conn.close()
		print("Connection closed")

i1=database('a','b','mytestdb','postgres','ayaz@5553','localhost')
i1.connect()
print("1-select")
print("2-Insert")
print("3-Update")
print("4-delete")
print("5-commit")
print("6-close")
n=int(input())
if n==1:
	i1.select_query()
	n=int(input())
elif n==2:
	i1.insert_query()
	n=int(input())
elif n==3:
	i1.update_query()
	n=int(input())
elif n==4:
	i1.delete_query()
	n=int(input())
elif n==5:
	i1.commit()
	n=int(input())
else:
	i1.connclose()
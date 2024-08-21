import mysql.connector

mydb=mysql.connector.connect( host="localhost",
user="root",
password="",
database="student"
)

mycursor=mydb.cursor()
print ("WELCOME TO MY WORLD")
print("\n\t1.INSERT \n\t2.DISPLAY \n\t3.DELETE \n\t4.UPDATE \nEnter Choice: ")
ch=int(input())
if (ch==1):
      r=input("Enter Roll No.: ")
      name=input("Enter Name: ")

      sql="insert into stud values("+ r + ",'" +name + "')"
      print(sql)

      mycursor.execute(sql)
      mydb.commit()

if (ch==2):
      mycursor.execute("SELECT * FROM stud")
      myresult = mycursor.fetchall()
      for x in myresult:
            print(x)

if (ch==3):
	r=input("Enter roll No. you want to delete: ")
	dele="DELETE FROM stud WHERE roll=( "+ r +")"
	print(dele)
	mycursor.execute(dele)
	mydb.commit()
	
if (ch==4):
	r=input("Enter roll No. you want to update the name: ")
	name=input("Enter Name: ")
	up = "update stud set name=('"+ name +"') where roll=( "+ r +")"
	print(up)
	mycursor.execute(up)
	mydb.commit()
	
            

import mysql.connector
# import mysql.connector
#create user 'user'@'%' identified by 'password'
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1234"
)
print(mydb)
mycursor = mydb.cursor()
#mycursor.execute('create database ineuron')
#mycursor.execute('create table ineuron.fsds(studentid int , firstname varchar(50) , lastname varchar(50) , registrationdate DATE,class varchar(20) , course_name varchar(50))')
#mycursor.execute("""insert into ineuron.fsds values(123 , 'sudhanshu', 'kumar','2022-11-11','sql','fsds'),
#(124 , 'r', 'singh','2022-11-11','sql','fsds'),
#(125 , 'rohan', 'kumar','2022-11-11','sql','fsds'),
#(126 , 'shreeja', 'maynale','2022-11-11','sql','fsds'),
#(127 , 'shubham', 'vedi','2022-11-11','sql','fsds'),
#(128 , 'abhishek', 'saini','2022-11-11','sql','fsds'),
#(129 , 'manoj', 'tripathi','2022-11-11','sql','fsds'),
#(130 , 'mayur ', 'gupta','2022-11-11','sql','fsds'),
#(131 , 'sumay', 'cahtterjee','2022-11-11','sql','fsds'),
#(132 , 'raunak', 'shgaow','2022-11-11','sql','fsds'),
#(133 , 'danish', 'khan','2022-11-11','sql','fsds')""")

#mydb.commit()

#mycursor.execute('select * from ineuron.fsds')

#for i in mycursor:
 #   print(i)

mycursor.execute("delete from ineuron.fsds where lastname = 'gupta'")
mydb.commit()
    
for i in mycursor:
    print(i)

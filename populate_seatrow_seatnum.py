import mysql.connector
import keyring

keyring.get_password("MySQL", "root")

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="749304Andrew",
    database="theater"
)

mycursor = mydb.cursor()

seatRowList = ["A", "B", "C", "D", "E", "F", "G", "H", "J", "K", "L", "M",
               "N", "O", "P", "Q", "R", "AA", "BB", "CC", "DD", "EE", "FF", "GG", "HH"]

# Populate table SeatRow
for i in seatRowList:
    mycursor.execute('insert into SeatRow values ("{}")'.format(i))

# Populating table SeatNum
for i in range(1, 16):
    mycursor.execute('insert into SeatNum values("{}")'.format(str(i)))

for i in range(101, 127):
    mycursor.execute('insert into SeatNum values("{}")'.format(str(i)))

mydb.commit()
mydb.close()

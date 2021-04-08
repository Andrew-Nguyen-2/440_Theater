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

# Populate Table Seat
# Total number of rows is 25
sqlInsert = "insert into Seat values(%s, %s, %s, %s, %s, %s)"
countMiddle = 1
countSides = 101
for i in range(25):
    countMiddle = 1
    countSides = 101
    # For Rows A, B, C
    if i == 1:
        while countMiddle <= 10:
            mycursor.execute('insert into Seat values("A", "{}", "Main Floor", "Middle", '
                             '"Orchestra", {})'.format(countMiddle, False))
            mycursor.execute('insert into Seat values("B", "{}", "Main Floor", "Middle", '
                             '"Orchestra", {})'.format(countMiddle, False))
            mycursor.execute('insert into Seat values("C", "{}", "Main Floor", "Middle", '
                             '"Orchestra", {})'.format(countMiddle, False))
            countMiddle += 1
        while countSides <= 114:
            if countSides % 2 == 0:
                mycursor.execute('insert into Seat values("A", "{}", "Main Floor", "Right", '
                                 '"Orchestra", {})'.format(countSides, False))
                mycursor.execute('insert into Seat values("B", "{}", "Main Floor", "Right", '
                                 '"Orchestra", {})'.format(countSides, False))
                mycursor.execute('insert into Seat values("C", "{}", "Main Floor", "Right", '
                                 '"Orchestra", {})'.format(countSides, False))
            if countSides % 2 == 1:
                mycursor.execute('insert into Seat values("A", "{}", "Main Floor", "Left", '
                                 '"Orchestra", {})'.format(countSides, False))
                mycursor.execute('insert into Seat values("B", "{}", "Main Floor", "Left", '
                                 '"Orchestra", {})'.format(countSides, False))
                mycursor.execute('insert into Seat values("C", "{}", "Main Floor", "Left", '
                                 '"Orchestra", {})'.format(countSides, False))
            countSides += 1

        while countSides <= 116:
            if countSides % 2 == 0:
                mycursor.execute('insert into Seat values("B", "{}", "Main Floor", "Right", '
                                 '"Side", {})'.format(countSides, False))
                mycursor.execute('insert into Seat values("C", "{}", "Main Floor", "Right", '
                                 '"Side", {})'.format(countSides, False))
            if countSides % 2 == 1:
                mycursor.execute('insert into Seat values("B", "{}", "Main Floor", "Left", '
                                 '"Side", {})'.format(countSides, False))
                mycursor.execute('insert into Seat values("C", "{}", "Main Floor", "Left", '
                                 '"Side", {})'.format(countSides, False))
            countSides += 1
    # For Rows D, E, F
    if i == 4:
        while countMiddle <= 11:
            mycursor.execute('insert into Seat values("D", "{}", "Main Floor", "Middle", '
                             '"Orchestra", {})'.format(countMiddle, False))
            mycursor.execute('insert into Seat values("E", "{}", "Main Floor", "Middle", '
                             '"Orchestra", {})'.format(countMiddle, False))
            mycursor.execute('insert into Seat values("F", "{}", "Main Floor", "Middle", '
                             '"Orchestra", {})'.format(countMiddle, False))
            countMiddle += 1
        while countSides <= 116:
            if countSides % 2 == 0:
                mycursor.execute('insert into Seat values("D", "{}", "Main Floor", "Right", '
                                 '"Orchestra", {})'.format(countSides, False))
                mycursor.execute('insert into Seat values("E", "{}", "Main Floor", "Right", '
                                 '"Orchestra", {})'.format(countSides, False))
                mycursor.execute('insert into Seat values("F", "{}", "Main Floor", "Right", '
                                 '"Orchestra", {})'.format(countSides, False))
            if countSides % 2 == 1:
                mycursor.execute('insert into Seat values("D", "{}", "Main Floor", "Left", '
                                 '"Orchestra", {})'.format(countSides, False))
                mycursor.execute('insert into Seat values("E", "{}", "Main Floor", "Left", '
                                 '"Orchestra", {})'.format(countSides, False))
                mycursor.execute('insert into Seat values("F", "{}", "Main Floor", "Left", '
                                 '"Orchestra", {})'.format(countSides, False))
            countSides += 1
        while countSides <= 118:
            if countSides % 2 == 0:
                mycursor.execute('insert into Seat values("F", "{}", "Main Floor", "Right", '
                                 '"Orchestra", {})'.format(countSides, False))
            if countSides % 2 == 1:
                mycursor.execute('insert into Seat values("F", "{}", "Main Floor", "Left", '
                                 '"Orchestra", {})'.format(countSides, False))
            countSides += 1

    # For Rows G, H, J
    if i == 7:
        while countMiddle <= 12:
            mycursor.execute('insert into Seat values("G", "{}", "Main Floor", "Middle", '
                             '"Orchestra", {})'.format(countMiddle, False))
            mycursor.execute('insert into Seat values("H", "{}", "Main Floor", "Middle", '
                             '"Orchestra", {})'.format(countMiddle, False))
            mycursor.execute('insert into Seat values("J", "{}", "Main Floor", "Middle", '
                             '"Orchestra", {})'.format(countMiddle, False))
            countMiddle += 1
        while countSides <= 118:
            if countSides % 2 == 0:
                mycursor.execute('insert into Seat values("G", "{}", "Main Floor", "Right", '
                                 '"Orchestra", {})'.format(countSides, False))
                mycursor.execute('insert into Seat values("H", "{}", "Main Floor", "Right", '
                                 '"Orchestra", {})'.format(countSides, False))
                mycursor.execute('insert into Seat values("J", "{}", "Main Floor", "Right", '
                                 '"Orchestra", {})'.format(countSides, False))
            if countSides % 2 == 1:
                mycursor.execute('insert into Seat values("G", "{}", "Main Floor", "Left", '
                                 '"Orchestra", {})'.format(countSides, False))
                mycursor.execute('insert into Seat values("H", "{}", "Main Floor", "Left", '
                                 '"Orchestra", {})'.format(countSides, False))
                mycursor.execute('insert into Seat values("J", "{}", "Main Floor", "Left", '
                                 '"Orchestra", {})'.format(countSides, False))
            countSides += 1

    # For Rows K, L, M
    if i == 10:
        while countMiddle <= 13:
            mycursor.execute('insert into Seat values("K", "{}", "Main Floor", "Middle", '
                             '"Orchestra", {})'.format(countMiddle, False))
            mycursor.execute('insert into Seat values("L", "{}", "Main Floor", "Middle", '
                             '"Orchestra", {})'.format(countMiddle, False))
            mycursor.execute('insert into Seat values("M", "{}", "Main Floor", "Middle", '
                             '"Orchestra", {})'.format(countMiddle, False))
            countMiddle += 1
        while countSides <= 120:
            if countSides % 2 == 0:
                mycursor.execute('insert into Seat values("K", "{}", "Main Floor", "Right", '
                                 '"Orchestra", {})'.format(countSides, False))
                mycursor.execute('insert into Seat values("L", "{}", "Main Floor", "Right", '
                                 '"Orchestra", {})'.format(countSides, False))
                mycursor.execute('insert into Seat values("M", "{}", "Main Floor", "Right", '
                                 '"Orchestra", {})'.format(countSides, False))
            if countSides % 2 == 1:
                mycursor.execute('insert into Seat values("K", "{}", "Main Floor", "Left", '
                                 '"Orchestra", {})'.format(countSides, False))
                mycursor.execute('insert into Seat values("L", "{}", "Main Floor", "Left", '
                                 '"Orchestra", {})'.format(countSides, False))
                mycursor.execute('insert into Seat values("M", "{}", "Main Floor", "Left", '
                                 '"Orchestra", {})'.format(countSides, False))
            countSides += 1

    # For Rows N, O, P
    if i == 13:
        while countMiddle <= 14:
            mycursor.execute('insert into Seat values("N", "{}", "Main Floor", "Middle", '
                             '"Orchestra", {})'.format(countMiddle, False))
            mycursor.execute('insert into Seat values("O", "{}", "Main Floor", "Middle", '
                             '"Orchestra", {})'.format(countMiddle, False))
            mycursor.execute('insert into Seat values("P", "{}", "Main Floor", "Middle", '
                             '"Orchestra", {})'.format(countMiddle, False))
            countMiddle += 1
        while countSides <= 120:
            if countSides % 2 == 0:
                mycursor.execute('insert into Seat values("N", "{}", "Main Floor", "Right", '
                                 '"Orchestra", {})'.format(countSides, False))
                mycursor.execute('insert into Seat values("O", "{}", "Main Floor", "Right", '
                                 '"Orchestra", {})'.format(countSides, False))
                if countSides <= 108:
                    mycursor.execute('insert into Seat values("P", "{}", "Main Floor", "Right", '
                                     '"Orchestra", {})'.format(countSides, False))
                if countSides > 108:
                    mycursor.execute('insert into Seat values("P", "{}", "Main Floor", "Right", '
                                     '"Orchestra", {})'.format(countSides, True))
            if countSides % 2 == 1:
                mycursor.execute('insert into Seat values("N", "{}", "Main Floor", "Left", '
                                 '"Orchestra", {})'.format(countSides, False))
                mycursor.execute('insert into Seat values("O", "{}", "Main Floor", "Left", '
                                 '"Orchestra", {})'.format(countSides, False))
                if countSides % 2 == 1:
                    if countSides <= 107:
                        mycursor.execute('insert into Seat values("P", "{}", "Main Floor", "Left", '
                                         '"Orchestra", {})'.format(countSides, False))
                    if countSides > 107:
                        mycursor.execute('insert into Seat values("P", "{}", "Main Floor", "Left", '
                                         '"Orchestra", {})'.format(countSides, True))
            countSides += 1
        while countSides <= 122:
            if countSides % 2 == 0:
                mycursor.execute('insert into Seat values("O", "{}", "Main Floor", "Right", '
                                 '"Orchestra", {})'.format(countSides, False))
                if countSides <= 108:
                    mycursor.execute('insert into Seat values("P", "{}", "Main Floor", "Right", '
                                     '"Orchestra", {})'.format(countSides, False))
                if countSides > 108:
                    mycursor.execute('insert into Seat values("P", "{}", "Main Floor", "Right", '
                                     '"Orchestra", {})'.format(countSides, True))
            if countSides % 2 == 1:
                mycursor.execute('insert into Seat values("O", "{}", "Main Floor", "Left", '
                                 '"Orchestra", {})'.format(countSides, False))
                if countSides <= 108:
                    mycursor.execute('insert into Seat values("P", "{}", "Main Floor", "Left", '
                                     '"Orchestra", {})'.format(countSides, False))
                if countSides > 108:
                    mycursor.execute('insert into Seat values("P", "{}", "Main Floor", "Left", '
                                     '"Orchestra", {})'.format(countSides, True))
            countSides += 1

    # For Rows Q, R
    if i == 16:
        while countMiddle <= 15:
            mycursor.execute('insert into Seat values("Q", "{}", "Main Floor", "Middle", '
                             '"Orchestra", {})'.format(countMiddle, False))
            mycursor.execute('insert into Seat values("R", "{}", "Main Floor", "Middle", '
                             '"Orchestra", {})'.format(countMiddle, False))
            countMiddle += 1
        while countSides <= 122:
            if countSides % 2 == 0:
                if countSides <= 108:
                    mycursor.execute('insert into Seat values("Q", "{}", "Main Floor", "Right", '
                                     '"Orchestra", {})'.format(countSides, False))
                    mycursor.execute('insert into Seat values("R", "{}", "Main Floor", "Right", '
                                     '"Orchestra", {})'.format(countSides, False))
                if countSides > 108:
                    mycursor.execute('insert into Seat values("Q", "{}", "Main Floor", "Right", '
                                     '"Orchestra", {})'.format(countSides, True))
                    mycursor.execute('insert into Seat values("R", "{}", "Main Floor", "Right", '
                                     '"Orchestra", {})'.format(countSides, True))
            if countSides % 2 == 1:
                if countSides <= 107:
                    mycursor.execute('insert into Seat values("Q", "{}", "Main Floor", "Left", '
                                     '"Orchestra", {})'.format(countSides, False))
                    mycursor.execute('insert into Seat values("R", "{}", "Main Floor", "Left", '
                                     '"Orchestra", {})'.format(countSides, False))
                if countSides > 107:
                    mycursor.execute('insert into Seat values("Q", "{}", "Main Floor", "Left", '
                                     '"Orchestra", {})'.format(countSides, True))
                    mycursor.execute('insert into Seat values("R", "{}", "Main Floor", "Left", '
                                     '"Orchestra", {})'.format(countSides, True))
            countSides += 1

    # For Row AA
    if i == 18:
        while countMiddle <= 13:
            mycursor.execute('insert into Seat values("AA", "{}", "Balcony", "Middle", '
                             '"Orchestra", {})'.format(countMiddle, False))
            countMiddle += 1
        while countSides <= 124:
            if countSides % 2 == 0:
                mycursor.execute('insert into Seat values("AA", "{}", "Balcony", "Right", '
                                 '"Side", {})'.format(countSides, False))
            if countSides % 2 == 1:
                mycursor.execute('insert into Seat values("AA", "{}", "Balcony", "Left", '
                                 '"Side", {})'.format(countSides, False))
            countSides += 1

    # For Rows BB, CC, DD
    if i == 19:
        while countMiddle <= 14:
            mycursor.execute('insert into Seat values("BB", "{}", "Balcony", "Middle", '
                             '"Orchestra", {})'.format(countMiddle, False))
            mycursor.execute('insert into Seat values("CC", "{}", "Balcony", "Middle", '
                             '"Orchestra", {})'.format(countMiddle, False))
            mycursor.execute('insert into Seat values("DD", "{}", "Balcony", "Middle", '
                             '"Orchestra", {})'.format(countMiddle, False))
            countMiddle += 1
        while countSides <= 124:
            if countSides % 2 == 0:
                mycursor.execute('insert into Seat values("BB", "{}", "Balcony", "Right", '
                                 '"Side", {})'.format(countSides, False))
                mycursor.execute('insert into Seat values("CC", "{}", "Balcony", "Right", '
                                 '"Side", {})'.format(countSides, False))
                mycursor.execute('insert into Seat values("DD", "{}", "Balcony", "Right", '
                                 '"Side", {})'.format(countSides, False))
            if countSides % 2 == 1:
                mycursor.execute('insert into Seat values("BB", "{}", "Balcony", "Left", '
                                 '"Side", {})'.format(countSides, False))
                mycursor.execute('insert into Seat values("CC", "{}", "Balcony", "Left", '
                                 '"Side", {})'.format(countSides, False))
                mycursor.execute('insert into Seat values("DD", "{}", "Balcony", "Left", '
                                 '"Side", {})'.format(countSides, False))
            countSides += 1
        while countSides <= 126:
            if countSides % 2 == 0:
                mycursor.execute('insert into Seat values("DD", "{}", "Balcony", "Right", '
                                 '"Side", {})'.format(countSides, False))
            if countSides % 2 == 1:
                mycursor.execute('insert into Seat values("DD", "{}", "Balcony", "Left", '
                                 '"Side", {})'.format(countSides, False))
            countSides += 1

    # For Rows EE, FF
    if i == 22:
        while countMiddle <= 10:
            mycursor.execute('insert into Seat values("EE", "{}", "Balcony", "Middle", '
                             '"Upper Balcony", {})'.format(countMiddle, False))
            mycursor.execute('insert into Seat values("FF", "{}", "Balcony", "Middle", '
                             '"Upper Balcony", {})'.format(countMiddle, False))
            countMiddle += 1
        while countSides <= 122:
            if countSides % 2 == 0:
                mycursor.execute('insert into Seat values("EE", "{}", "Balcony", "Right", '
                                 '"Upper Balcony", {})'.format(countSides, False))
                mycursor.execute('insert into Seat values("FF", "{}", "Balcony", "Right", '
                                 '"Upper Balcony", {})'.format(countSides, False))
            if countSides % 2 == 1:
                mycursor.execute('insert into Seat values("EE", "{}", "Balcony", "Left", '
                                 '"Upper Balcony", {})'.format(countSides, False))
                mycursor.execute('insert into Seat values("FF", "{}", "Balcony", "Left", '
                                 '"Upper Balcony", {})'.format(countSides, False))
            countSides += 1

    # For Rows GG, HH
    if i == 24:
        while countMiddle <= 11:
            mycursor.execute('insert into Seat values("GG", "{}", "Balcony", "Middle", '
                             '"Upper Balcony", {})'.format(countMiddle, False))
            mycursor.execute('insert into Seat values("HH", "{}", "Balcony", "Middle", '
                             '"Upper Balcony", {})'.format(countMiddle, False))
            countMiddle += 1
        while countSides <= 118:
            if countSides % 2 == 0:
                mycursor.execute('insert into Seat values("GG", "{}", "Balcony", "Right", '
                                 '"Upper Balcony", {})'.format(countSides, False))
                mycursor.execute('insert into Seat values("HH", "{}", "Balcony", "Right", '
                                 '"Upper Balcony", {})'.format(countSides, False))
            if countSides % 2 == 1:
                mycursor.execute('insert into Seat values("GG", "{}", "Balcony", "Left", '
                                 '"Upper Balcony", {})'.format(countSides, False))
                mycursor.execute('insert into Seat values("HH", "{}", "Balcony", "Left", '
                                 '"Upper Balcony", {})'.format(countSides, False))
            countSides += 1
        while countSides <= 120:
            if countSides % 2 == 0:
                mycursor.execute('insert into Seat values("GG", "{}", "Balcony", "Right", '
                                 '"Upper Balcony", {})'.format(countSides, False))
            if countSides % 2 == 1:
                mycursor.execute('insert into Seat values("GG", "{}", "Balcony", "Left", '
                                 '"Upper Balcony", {})'.format(countSides, False))
            countSides += 1

# Updating the Main Floor Pricing Tier
updatePricingTier = "update Seat set PricingTier = %s where SeatRow = %s and SeatNumber > 106"
rowList = ["A", "B", "C", "D", "E", "F", "G", "H", "J", "K", "L", "M", "N",
           "O", "P", "Q", "R"]
for i in rowList:
    mycursor.execute(updatePricingTier, ("Side", i))

mydb.commit()
mydb.close()

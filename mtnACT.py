
def mainMENU():
    print("1. Add Activity")
    print("2. View Activity")
    print("3. Edit Activity")
    print("4. Delete Activity")
    print("5. Quit")
    while True:
        try:
            optionNum = int(input("Enter Choice: "))
            if optionNum == 1:
                addACT()
                break
            elif optionNum == 2:
                viewACT()
                break
            elif optionNum == 3:
                editACT()
                break
            elif optionNum == 4:
                deleteACT()
                break
            elif optionNum == 5:
                break
            else:
                print("Enter a valid choice between 1 and 5.")
                mainMENU()
        except ValueError:
            print("Invalid choice. Enter a choice between 1 and 5.")
    exit

#add activity (create)
def addACT():
    print("Please answer all requested fields.")
    addActivityName = input("Enter activity name: ")
    addDistance = float(input("Enter activity distance in miles to 2 decimal places: "))
    addElevationGain = float(input("Enter activity elevation gain in feet to 2 decimal places: "))
    addActivityDate = input("Enter date in the following format YYYY-MM-DD HH:MM:SS: ")
    ADDidUSER = int(input(''' Choose User ID number from users listed below:
        1. Jyn Erso
        2. Jon Rambo
        3. Snake Plissken
        4. Lara Croft
        5. Indiana Jones
        '''))
    addAddresses_idAddresses =  int(input(''' Choose address ID number from addresses listed below:
        1. 107 Bear Mountain-Beacon Hwy, Beacon, NY, 10524
        2. 100 Gorham Hill Rd, Randolph, NH, 03593
        3. 321 Eldorado Springs Dr, Boulder, CO, 80303
        4. NF-9041, North Bend, WA, 98045
        5. 200 Happy Isle Loop Rd, Yosemite Valley, CA, 95389
        '''))
    addActivity_Type_idActivityType = int(input(''' Choose activity type from list and enter number:
        1. Hike
        2. Thru Hike
        3. Section Hike
        4. Backpacking
        '''))
    addRoute_Type_idRouteType = int(input('''Choose route type from list and enter number: 
        1. One Way
        2. Out and Back
        3. Loop
        '''))
    addTerrain_Type_idTerrain = int(input('''Choose route type from list and enter number: 
        1. Hills
        2. Mountains
        3. Rivers
        4. Lakes
        '''))
    addDifficulty_idDifficulty = int(input('''Choose difficulty level from list and enter number: 
        1. Easy
        2. Moderate
        3. Challenging
        '''))
    insert_activity = ('''INSERT INTO mydb.activity (ActivityName, Distance, ElevationGain, ActivityDate, idUSER, 
        Addresses_idAddresses, Activity_Type_idActivityType, Route_Type_idRouteType, Terrain_Type_idTerrain, Difficulty_idDifficulty)
    VALUES ("%s", %f, %f, '%s', %d, %d, %d, %d, %d, %d) '''
        % (addActivityName, addDistance, addElevationGain, addActivityDate, ADDidUSER, addAddresses_idAddresses, addActivity_Type_idActivityType, addRoute_Type_idRouteType, addTerrain_Type_idTerrain, addDifficulty_idDifficulty)
    )
    with connection.cursor() as cursor:
        cursor.execute(insert_activity)
        connection.commit()

    select_by_act = ("SELECT * FROM mydb.activity")
    with connection.cursor() as cursor:
        cursor.execute(select_by_act)
        result = cursor.fetchall()
        for row in result:
            print("Updated Records:")
            print(row)

    exit


# view activity (read)
def viewACT():
    print("Select search parameter:")
    print('''
    1. User ID
    2. Activity ID
    3. Route Type
    4. Terrain
    5. Difficulty
    6. Back
    7. Quit

    ''')
    while True:
        try:
            optionNum = int(input("Enter Choice: "))

            # user id
            if optionNum == 1:
                userID = int(input("Enter User ID: "))
                select_by_user = ("SELECT * FROM mydb.activity WHERE idUser = %d" % userID)
                with connection.cursor() as cursor:
                    cursor.execute(select_by_user)
                    result = cursor.fetchall()
                    for row in result:
                        print(row)
                break

            # activity id
            elif optionNum == 2:
                actID = int(input("Enter Activity ID: "))
                select_by_act = ("SELECT * FROM mydb.activity WHERE idActivity = %d" % (actID))
                with connection.cursor() as cursor:
                    cursor.execute(select_by_act)
                    result = cursor.fetchall()
                    for row in result:
                        print(row)
                break

            # route type
            elif optionNum == 3:
                print('''
                1. One Way
                2. Out and Back
                3. Loop
                ''')
                rtType = int(input("Enter Route Type: "))
                select_by_rt = ("SELECT * FROM mydb.activity WHERE Route_Type_idRouteType = %d" % (rtType))
                with connection.cursor() as cursor:
                    cursor.execute(select_by_rt)
                    result = cursor.fetchall()
                    for row in result:
                        print(row)
                break

            # terrain
            elif optionNum == 4:
                print('''
                1. Hills
                2. Mountains
                3. Rivers
                4. Lakes
                ''')
                terrType = int(input("Enter Terrain Type: "))
                select_by_terr = ("SELECT * FROM mydb.activity WHERE Terrain_Type_idTerrain = %d" % (terrType))
                with connection.cursor() as cursor:
                    cursor.execute(select_by_terr)
                    result = cursor.fetchall()
                    for row in result:
                        print(row)
                break

            # difficulty
            elif optionNum == 5:
                print('''
                1. Easy
                2. Moderate
                3. Challenging
                ''')
                diffType = int(input("Enter Difficulty: "))
                select_by_diff = ("SELECT * FROM mydb.activity WHERE Difficulty_idDifficulty = %d" % (diffType))
                with connection.cursor() as cursor:
                    cursor.execute(select_by_diff)
                    result = cursor.fetchall()
                    for row in result:
                        print(row)
                break

            #back
            elif optionNum == 6:
                mainMENU()
                break

            #quit
            elif optionNum == 7:
                break

            else:
                print("Enter a valid choice between 1 and 8.")
                viewACT()

        except ValueError:
            print("Invalid choice. Enter a choice between 1 and 8.")
    exit


#update activity (update)
def editACT():
    print("Select search parameter for activity to update:")
    print('''
    1. User ID
    2. Activity ID
    3. Back
    4. Quit

    ''')
    while True:
        try:
            optionNum = int(input("Enter Choice: "))

            # user id
            if optionNum == 1:
                userID = int(input("Enter User ID to look up: "))
                select_by_user = ("SELECT * FROM mydb.activity WHERE idUser = %d" % userID)
                with connection.cursor() as cursor:
                    cursor.execute(select_by_user)
                    result = cursor.fetchall()
                    for row in result:
                        print(row)

#idActivity, ActivityName, Distance, ElevationGain, ActivityDate, idUSER, Addresses_idAddresses, Activity_Type_idActivityType, Route_Type_idRouteType, Terrain_Type_idTerrain, Difficulty_idDifficulty

                print("If you are not changing a value, enter original value and press enter.")
                UPDactID = int(input("Enter Activity ID to update: "))
                UPDdist = float(input("Enter new distance to 2 decimal places: "))
                UPDelev = float(input("Enter new elevation gain to 2 decimal places: "))

                update_ACT = ('''UPDATE mydb.activity 
                SET Distance = %f, ElevationGain = %f WHERE idActivity = %d''' % (UPDdist, UPDelev, UPDactID))
                with connection.cursor() as cursor:
                    for result in cursor.execute(update_ACT, multi=True):
                        if result.with_rows:
                            print(result.fetchall())
                    connection.commit()

                select_by_act = ("SELECT * FROM mydb.activity WHERE idActivity = %d" % (UPDactID))
                with connection.cursor() as cursor:
                    cursor.execute(select_by_act)
                    result = cursor.fetchall()
                    for row in result:
                        print("Updated Record:")
                        print(row)

                break

            # activity id
            elif optionNum == 2:
                UPDactID = int(input("Enter Activity ID to look up: "))
                select_by_act = ("SELECT * FROM mydb.activity WHERE idActivity = %d" % UPDactID)
                with connection.cursor() as cursor:
                    cursor.execute(select_by_act)
                    result = cursor.fetchall()
                    for row in result:
                        print(row)

                print("If you are not changing a value, enter original value and press enter.")
                UPDdist = float(input("Enter new distance to 2 decimal places: "))
                UPDelev = float(input("Enter new elevation gain to 2 decimal places: "))

                update_ACT = ('''UPDATE mydb.activity 
                SET Distance = %f, ElevationGain = %f WHERE idActivity = %d''' % (UPDdist, UPDelev, UPDactID))
                with connection.cursor() as cursor:
                    for result in cursor.execute(update_ACT, multi=True):
                        if result.with_rows:
                            print(result.fetchall())
                    connection.commit()

                select_by_act = ("SELECT * FROM mydb.activity WHERE idActivity = %d" % (UPDactID))
                with connection.cursor() as cursor:
                    cursor.execute(select_by_act)
                    result = cursor.fetchall()
                    for row in result:
                        print("Updated Record:")
                        print(row)

                break
            # back
            elif optionNum == 3:
                mainMENU()
                break
            # quit
            elif optionNum == 4:
                break

            else:
                print("Enter a valid choice between 1 and 4.")
                viewACT()

        except ValueError:
            print("Invalid choice")
    exit


#delete activity (delete)
def deleteACT():
    print("Select search parameter for activity to delete:")
    print('''
    1. User ID
    2. Activity ID
    3. Back
    4. Quit

    ''')
    while True:
        try:
            optionNum = int(input("Enter Choice: "))

            # user id
            if optionNum == 1:
                userID = int(input("Enter User ID to look up: "))
                select_by_user = ("SELECT * FROM mydb.activity WHERE idUser = %d" % userID)
                with connection.cursor() as cursor:
                    cursor.execute(select_by_user)
                    result = cursor.fetchall()
                    for row in result:
                        print(row)

                DELuserID = int(input("Enter Activity ID to delete: "))
                delete_ACT_user = ("DELETE FROM mydb.activity WHERE idActivity = %d" % DELuserID)
                with connection.cursor() as cursor:
                    cursor.execute(delete_ACT_user)
                    connection.commit()
                    print("Record Deleted")

                break

            # activity id
            elif optionNum == 2:
                actID = int(input("Enter Activity ID to look up: "))
                select_by_act = ("SELECT * FROM mydb.activity WHERE idActivity = %d" % (actID))
                with connection.cursor() as cursor:
                    cursor.execute(select_by_act)
                    result = cursor.fetchall()
                    for row in result:
                        print(row)

                DELactID = int(input("Enter Activity ID to delete: "))
                delete_ACT_user = ("DELETE FROM mydb.activity WHERE idActivity = %d" % DELactID)
                with connection.cursor() as cursor:
                    cursor.execute(delete_ACT_user)
                    connection.commit()
                    print("Record Deleted")

                break
            #back
            elif optionNum == 3:
                mainMENU()
                break
            #quit
            elif optionNum == 4:
                break

            else:
                print("Enter a valid choice between 1 and 4.")
                viewACT()

        except ValueError:
            print("Invalid choice. Enter a choice between 1 and 4.")
    exit




#main
from getpass import getpass
from mysql.connector import connect, Error

try:
    with connect(
        host="localhost",
        user=input("Enter username: "),
        password=getpass("Enter password: "),
        database="mydb",
    ) as connection:
        print(connection)
        mainMENU()

except Error as err:
    print(err)


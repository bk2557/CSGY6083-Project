
def mainMENU():
    print('''
    1. Activity Management
    2. Reports
    3. Updates
    4. Quit
    ''')
    while True:
        try:
            optionNum = int(input("Enter Choice: "))
            if optionNum == 1:
                actMENU()
                break
            elif optionNum == 2:
                reportMENU()
                break
            elif optionNum == 3:
                adminMENU()
                break
            elif optionNum == 4:
                break
            else:
                print("Enter a valid choice between 1 and 4.")
                mainMENU()
        except ValueError:
            print("Invalid choice. Enter a choice between 1 and 4.")
    exit

#edit activities
def actMENU():
    print('''
    1. Add Activity
    2. View Activity
    3. Edit Activity
    4. Delete Activity
    5. Main Menu
    6. Quit
    ''')
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
                mainMENU()
                break
            elif optionNum == 6:
                break
            else:
                print("Enter a valid choice between 1 and 5.")
                mainMENU()
        except ValueError:
            print("Invalid choice. Enter a choice between 1 and 5.")
    exit

#pull reports
def reportMENU():
    print('''
    1. All Activities Report
    2. User Totals Report
    3. All Users Totals Report
    4. Back
    5. Quit
    ''')
    while True:
        try:
            optionNum = int(input("Enter Choice: "))
            if optionNum == 1:
                print("All Activities Report: ")
                select_all_table = ("SELECT * FROM mydb.wordstab")
                with connection.cursor() as cursor:
                    cursor.execute(select_all_table)
                    results = cursor.fetchall()
                    field_names = [i[0] for i in cursor.description]
                    print(tabulate(results, headers=field_names, tablefmt='psql'))
                mainMENU()
                break
            elif optionNum == 2:
                # pull user info
                select_userINFO = ("SELECT idUser, FirstName, LastName FROM mydb.User")
                with connection.cursor() as cursor:
                    cursor.execute(select_userINFO)
                    results = cursor.fetchall()
                    field_names = [i[0] for i in cursor.description]
                    print(tabulate(results, headers=field_names, tablefmt='psql'))
                #call user report
                userID = int(input("Enter User ID from list above: "))
                select_by_user = ("CALL mydb.metricsByUser(%d)" % userID)
                with connection.cursor() as cursor:
                    cursor.execute(select_by_user)
                    result = cursor.fetchall()
                    field_names = [i[0] for i in cursor.description]
                    print(tabulate(result, headers=field_names, tablefmt='psql'))

                mainMENU()
                break
            elif optionNum == 3:
                #call all user metrics
                select_by_user = ("CALL mydb.allMetrics()")
                with connection.cursor() as cursor:
                    cursor.execute(select_by_user)
                    result = cursor.fetchall()
                    field_names = [i[0] for i in cursor.description]
                    print(tabulate(result, headers=field_names, tablefmt='psql'))
                mainMENU()
                break
            elif optionNum == 4:
                mainMENU()
                break
            elif optionNum == 5:
                break
            else:
                print("Enter a valid choice between 1 and 5.")
                mainMENU()
        except ValueError:
            print("Invalid choice. Enter a choice between 1 and 5.")
    exit

#user management
# def NEWuserMENU():
    #    print('''
    #    1. Self Register
    #    2. Back
    #    3. Quit
    #    ''')
    #    while True:
    #        try:
    #            optionNum = int(input("Enter Choice: "))
    #       if optionNum == 1:
    #           addUser()
    #           break
    #       elif optionNum == 2:
    #           mainMENU()
    #           break
    #       elif optionNum == 3:
    #            break
     #       else:
     #           print("Enter a valid choice between 1 and 3.")
    #            mainMENU()
    #    except ValueError:
    #        print("Invalid choice. Enter a choice between 1 and 3.")
    #exit

#admin management
def adminMENU():
    print('''
    1. Activity Type
    2. Addresses
    3. Difficulty
    4. Region
    5. Route Type
    6. Terrain Type
    7. User
    8. Back
    9. Quit
    ''')
    while True:
        try:
            optionNum = int(input("Select Table to manage: "))
            if optionNum == 1:
                actTypeMENU()
                break
            elif optionNum == 2:
                addressMENU()
                break
            elif optionNum == 3:
                diffMENU()
                break
            elif optionNum == 4:
                regionMENU()
                break
            elif optionNum == 5:
                routeTypeMENU()
                break
            elif optionNum == 6:
                terrainTypeMENU()
                break
            elif optionNum == 7:
                userMENU()
                break
            elif optionNum == 8:
                mainMENU()
                break
            elif optionNum == 9:
                break
            else:
                print("Enter a valid choice between 1 and 5.")
                mainMENU()
        except ValueError:
            print("Invalid choice. Enter a choice between 1 and 5.")
    exit

#edit activities type
def actTypeMENU():
    print('''
    1. Add Activity Type
    2. View Activity Types
    3. Edit Activity Type
    4. Delete Activity Type
    5. Main Menu
    6. Quit
    ''')
    while True:
        try:
            optionNum = int(input("Enter Choice: "))
            if optionNum == 1:
                addACTtype()
                break
            elif optionNum == 2:
                viewACTtype()
                break
            elif optionNum == 3:
                editACTtype()
                break
            elif optionNum == 4:
                deleteACTtype()
                break
            elif optionNum == 5:
                mainMENU()
                break
            elif optionNum == 6:
                break
            else:
                print("Enter a valid choice between 1 and 6.")
                mainMENU()
        except ValueError:
            print("Invalid choice. Enter a choice between 1 and 6.")
    exit

#edit address
def addressMENU():
    print('''
    1. Add Address
    2. View Addresses
    3. Edit Address
    4. Delete Address
    5. Main Menu
    6. Quit
    ''')
    while True:
        try:
            optionNum = int(input("Enter Choice: "))
            if optionNum == 1:
                addAddresses()
                break
            elif optionNum == 2:
                viewAddresses()
                break
            elif optionNum == 3:
                editAddresses()
                break
            elif optionNum == 4:
                deleteAddresses()
                break
            elif optionNum == 5:
                mainMENU()
                break
            elif optionNum == 6:
                break
            else:
                print("Enter a valid choice between 1 and 6.")
                mainMENU()
        except ValueError:
            print("Invalid choice. Enter a choice between 1 and 6.")
    exit

# edit difficulty
def diffMENU():
    print('''
    1. Add Difficulty
    2. View Difficulties
    3. Edit Difficulty
    4. Delete Difficulty
    5. Main Menu
    6. Quit
    ''')
    while True:
        try:
            optionNum = int(input("Enter Choice: "))
            if optionNum == 1:
                addDiff()
                break
            elif optionNum == 2:
                viewDiff()
                break
            elif optionNum == 3:
                editDiff()
                break
            elif optionNum == 4:
                deleteDiff()
                break
            elif optionNum == 5:
                mainMENU()
                break
            elif optionNum == 6:
                break
            else:
                print("Enter a valid choice between 1 and 6.")
                mainMENU()
        except ValueError:
            print("Invalid choice. Enter a choice between 1 and 6.")
    exit

# edit region
def regionMENU():
    print('''
    1. Add Region
    2. View Regions
    3. Edit Region
    4. Delete Region
    5. Main Menu
    6. Quit
    ''')
    while True:
        try:
            optionNum = int(input("Enter Choice: "))
            if optionNum == 1:
                addRegion()
                break
            elif optionNum == 2:
                viewRegion()
                break
            elif optionNum == 3:
                editRegion()
                break
            elif optionNum == 4:
                deleteRegion()
                break
            elif optionNum == 5:
                mainMENU()
                break
            elif optionNum == 6:
                break
            else:
                print("Enter a valid choice between 1 and 6.")
                mainMENU()
        except ValueError:
            print("Invalid choice. Enter a choice between 1 and 6.")
    exit

# edit Route Type
def routeTypeMENU():
    print('''
    1. Add Route Type
    2. View Route Types
    3. Edit Route Type
    4. Delete Route Type
    5. Main Menu
    6. Quit
    ''')
    while True:
        try:
            optionNum = int(input("Enter Choice: "))
            if optionNum == 1:
                addRouteType()
                break
            elif optionNum == 2:
                viewRouteType()
                break
            elif optionNum == 3:
                editRouteType()
                break
            elif optionNum == 4:
                deleteRouteType()
                break
            elif optionNum == 5:
                mainMENU()
                break
            elif optionNum == 6:
                break
            else:
                print("Enter a valid choice between 1 and 6.")
                mainMENU()
        except ValueError:
            print("Invalid choice. Enter a choice between 1 and 6.")
    exit

# edit Route Type
def terrainTypeMENU():
    print('''
    1. Add Terrain Type
    2. View Terrain Types
    3. Edit Terrain Type
    4. Delete Terrain Type
    5. Main Menu
    6. Quit
    ''')
    while True:
        try:
            optionNum = int(input("Enter Choice: "))
            if optionNum == 1:
                addTerrainType()
                break
            elif optionNum == 2:
                viewTerrainType()
                break
            elif optionNum == 3:
                editTerrainType()
                break
            elif optionNum == 4:
                deleteTerrainType()
                break
            elif optionNum == 5:
                mainMENU()
                break
            elif optionNum == 6:
                break
            else:
                print("Enter a valid choice between 1 and 6.")
                mainMENU()
        except ValueError:
            print("Invalid choice. Enter a choice between 1 and 6.")
    exit

# edit Route Type
def userMENU():
    print('''
    1. Add User
    2. View User
    3. Edit User
    4. Delete User
    5. Main Menu
    6. Quit
    ''')
    while True:
        try:
            optionNum = int(input("Enter Choice: "))
            if optionNum == 1:
                addUser()
                break
            elif optionNum == 2:
                viewUser()
                break
            elif optionNum == 3:
                editUser()
                break
            elif optionNum == 4:
                deleteUser()
                break
            elif optionNum == 5:
                mainMENU()
                break
            elif optionNum == 6:
                break
            else:
                print("Enter a valid choice between 1 and 6.")
                mainMENU()
        except ValueError:
            print("Invalid choice. Enter a choice between 1 and 6.")
    exit


#output mysql to table
def makeTable(tabName):
    select_all_table = ("SELECT * FROM mydb.%s" % tabName)
    with connection.cursor() as cursor:
        cursor.execute(select_all_table)
        results = cursor.fetchall()
        field_names = [i[0] for i in cursor.description]
        print(tabulate(results, headers=field_names, tablefmt='psql'))

#add/insert activity (create)
def addACT():
    print("Please answer all requested fields.")
    addActivityName = input("Enter activity name: ")
    addDistance = float(input("Enter activity distance in miles to 2 decimal places: "))
    addElevationGain = float(input("Enter activity elevation gain in feet to 2 decimal places: "))
    addActivityDate = input("Enter date in the following format YYYY-MM-DD HH:MM:SS: ")
#pull user info
    select_userINFO = ("SELECT idUser, FirstName, LastName FROM mydb.User")
    with connection.cursor() as cursor:
        cursor.execute(select_userINFO)
        result = cursor.fetchall()
        field_names = [i[0] for i in cursor.description]
        print(tabulate(result, headers=field_names, tablefmt='psql'))
    ADDidUSER = int(input(''' Choose User ID number from users listed above:
        '''))
# pull address info
    select_addINFO = ("SELECT idAddresses, line1, line2, city, state, zipCD FROM mydb.Addresses")
    with connection.cursor() as cursor:
        cursor.execute(select_addINFO)
        result = cursor.fetchall()
        field_names = [i[0] for i in cursor.description]
        print(tabulate(result, headers=field_names, tablefmt='psql'))
    addAddresses_idAddresses =  int(input(''' Choose address ID number from addresses listed above:
        '''))
# pull activity type info
    select_actTypeINFO = ("SELECT idActivityType, Activity_Type_Name FROM mydb.Activity_Type")
    with connection.cursor() as cursor:
        cursor.execute(select_actTypeINFO)
        result = cursor.fetchall()
        field_names = [i[0] for i in cursor.description]
        print(tabulate(result, headers=field_names, tablefmt='psql'))
    addActivity_Type_idActivityType = int(input(''' Choose activity type from above list and enter number:
        '''))
# pull route type info
    select_routeTypeINFO = ("SELECT idRouteType, Route_Name FROM mydb.Route_Type")
    with connection.cursor() as cursor:
        cursor.execute(select_routeTypeINFO)
        result = cursor.fetchall()
        field_names = [i[0] for i in cursor.description]
        print(tabulate(result, headers=field_names, tablefmt='psql'))
    addRoute_Type_idRouteType = int(input('''Choose route type from above list and enter number: 
        '''))
# pull terrain type info
    select_terraintTypeINFO = ("SELECT idTerrain, Terrian_name FROM mydb.Terrain_Type")
    with connection.cursor() as cursor:
        cursor.execute(select_terraintTypeINFO)
        result = cursor.fetchall()
        field_names = [i[0] for i in cursor.description]
        print(tabulate(result, headers=field_names, tablefmt='psql'))
    addTerrain_Type_idTerrain = int(input('''Choose route type from above list and enter number: 
        '''))
# pull difficulty type info
    select_diffINFO = ("SELECT idDifficulty, Difficulty_Level FROM mydb.Difficulty")
    with connection.cursor() as cursor:
        cursor.execute(select_diffINFO)
        result = cursor.fetchall()
        field_names = [i[0] for i in cursor.description]
        print(tabulate(result, headers=field_names, tablefmt='psql'))
    addDifficulty_idDifficulty = int(input('''Choose difficulty level from above list and enter number: 
        '''))

    insert_activity = ('''INSERT INTO mydb.activity (ActivityName, Distance, ElevationGain, ActivityDate, idUSER, 
        Addresses_idAddresses, Activity_Type_idActivityType, Route_Type_idRouteType, Terrain_Type_idTerrain, Difficulty_idDifficulty)
    VALUES ('%s', %f, %f, '%s', %d, %d, %d, %d, %d, %d) '''
        % (addActivityName, addDistance, addElevationGain, addActivityDate, ADDidUSER, addAddresses_idAddresses, addActivity_Type_idActivityType, addRoute_Type_idRouteType, addTerrain_Type_idTerrain, addDifficulty_idDifficulty)
    )
    with connection.cursor() as cursor:
        cursor.execute(insert_activity)
        connection.commit()

    select_by_act = ("SELECT * FROM mydb.activity")
    with connection.cursor() as cursor:
        cursor.execute(select_by_act)
        results = cursor.fetchall()
        field_names = [i[0] for i in cursor.description]
        print(tabulate(results, headers=field_names, tablefmt='psql'))

    mainMENU()
    exit

# view/read/select activity (read)
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

                # pull user info
                select_userINFO = ("SELECT idUser, FirstName, LastName FROM mydb.User")
                with connection.cursor() as cursor:
                    cursor.execute(select_userINFO)
                    results = cursor.fetchall()
                    field_names = [i[0] for i in cursor.description]
                    print(tabulate(results, headers=field_names, tablefmt='psql'))


                userID = int(input("Enter User ID from list above: "))
                select_by_user = ("SELECT * FROM mydb.all_activities WHERE idUser = %d" % userID)
                with connection.cursor() as cursor:
                    cursor.execute(select_by_user)
                    result = cursor.fetchall()
                    field_names = [i[0] for i in cursor.description]
                    print(tabulate(result, headers=field_names, tablefmt='psql'))

                mainMENU()
                break

            # activity id
            elif optionNum == 2:

                # pull activity info
                select_actINFO = ("SELECT idActivity, ActivityName FROM mydb.Activity")
                with connection.cursor() as cursor:
                    cursor.execute(select_actINFO)
                    results = cursor.fetchall()
                    field_names = [i[0] for i in cursor.description]
                    print(tabulate(results, headers=field_names, tablefmt='psql'))

                actID = int(input("Enter Activity ID: "))
                #select_by_act = ("SELECT * FROM mydb.activity WHERE idActivity = %d" % actID)
                with connection.cursor() as cursor:
                    cursor.execute("SELECT * FROM mydb.all_activities WHERE idActivity = %d" % actID)
                    result = cursor.fetchall()
                    field_names = [i[0] for i in cursor.description]
                    print(tabulate(result, headers=field_names, tablefmt='psql'))

                mainMENU()
                break
            # route type
            elif optionNum == 3:

                # pull route type info
                select_routeTypeINFO = ("SELECT idRouteType, Route_Name FROM mydb.Route_Type")
                with connection.cursor() as cursor:
                    cursor.execute(select_routeTypeINFO)
                    results = cursor.fetchall()
                    field_names = [i[0] for i in cursor.description]
                    print(tabulate(results, headers=field_names, tablefmt='psql'))

                rtType = int(input("Enter Route Type: "))
                select_by_rt = ("SELECT * FROM mydb.all_activities WHERE Route_Type_idRouteType = %d" % rtType)
                with connection.cursor() as cursor:
                    cursor.execute(select_by_rt)
                    result = cursor.fetchall()
                    field_names = [i[0] for i in cursor.description]
                    print(tabulate(result, headers=field_names, tablefmt='psql'))

                mainMENU()
                break

            # terrain
            elif optionNum == 4:

                # pull terrain type info
                select_terraintTypeINFO = ("SELECT idTerrain, Terrian_name FROM mydb.Terrain_Type")
                with connection.cursor() as cursor:
                    cursor.execute(select_terraintTypeINFO)
                    results = cursor.fetchall()
                    field_names = [i[0] for i in cursor.description]
                    print(tabulate(results, headers=field_names, tablefmt='psql'))

                terrType = int(input("Enter Terrain Type: "))
                select_by_terr = ("SELECT * FROM mydb.all_activities WHERE Terrain_Type_idTerrain = %d" % terrType)
                with connection.cursor() as cursor:
                    cursor.execute(select_by_terr)
                    result = cursor.fetchall()
                    field_names = [i[0] for i in cursor.description]
                    print(tabulate(result, headers=field_names, tablefmt='psql'))

                mainMENU()
                break

            # difficulty
            elif optionNum == 5:

                # pull difficulty type info
                select_diffINFO = ("SELECT idDifficulty, Difficulty_Level FROM mydb.Difficulty")
                with connection.cursor() as cursor:
                    cursor.execute(select_diffINFO)
                    results = cursor.fetchall()
                    field_names = [i[0] for i in cursor.description]
                    print(tabulate(results, headers=field_names, tablefmt='psql'))

                diffType = int(input("Enter Difficulty: "))
                select_by_diff = ("SELECT * FROM mydb.all_activities WHERE Difficulty_idDifficulty = %d" % diffType)
                with connection.cursor() as cursor:
                    cursor.execute(select_by_diff)
                    result = cursor.fetchall()
                    field_names = [i[0] for i in cursor.description]
                    print(tabulate(result, headers=field_names, tablefmt='psql'))

                mainMENU()
                break

            #back
            elif optionNum == 6:
                mainMENU()
                break

            #quit
            elif optionNum == 7:
                break

            else:
                print("Enter a valid choice between 1 and 7.")
                viewACT()

        except ValueError:
            print("Invalid choice. Enter a choice between 1 and 7.")
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

                # pull user info
                select_userINFO = ("SELECT idUser, FirstName, LastName FROM mydb.User")
                with connection.cursor() as cursor:
                    cursor.execute(select_userINFO)
                    # for row in cursor.fetchall():
                    #    print(row)
                    # connection.commit()
                    results = cursor.fetchall()
                    field_names = [i[0] for i in cursor.description]
                    print(tabulate(results, headers=field_names, tablefmt='psql'))


                userID = int(input("Enter User ID to look up: "))
                select_by_user = ("SELECT * FROM mydb.all_activities WHERE idUser = %d" % userID)
                with connection.cursor() as cursor:
                    cursor.execute(select_by_user)
                    result = cursor.fetchall()
                    field_names = [i[0] for i in cursor.description]
                    print(tabulate(result, headers=field_names, tablefmt='psql'))

#idActivity, ActivityName, Distance, ElevationGain, ActivityDate, idUSER, Addresses_idAddresses, Activity_Type_idActivityType, Route_Type_idRouteType, Terrain_Type_idTerrain, Difficulty_idDifficulty

                print("If you are not changing a value, enter original value and press enter. Type 0 to exit to menu")
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

                select_by_act = ("SELECT * FROM mydb.all_activities WHERE idActivity = %d" % (UPDactID))
                with connection.cursor() as cursor:
                    cursor.execute(select_by_act)
                    result = cursor.fetchall()
                    field_names = [i[0] for i in cursor.description]
                    print(tabulate(result, headers=field_names, tablefmt='psql'))

                mainMENU()
                break

            # activity id
            elif optionNum == 2:

                # pull activity info
                select_actINFO = ("SELECT idActivity, ActivityName FROM mydb.Activity")
                with connection.cursor() as cursor:
                    cursor.execute(select_actINFO)
                    results = cursor.fetchall()
                    field_names = [i[0] for i in cursor.description]
                    print(tabulate(results, headers=field_names, tablefmt='psql'))

                UPDactID = int(input("Enter Activity ID to look up: "))
                select_by_act = ("SELECT * FROM mydb.all_activities WHERE idActivity = %d" % UPDactID)
                with connection.cursor() as cursor:
                    cursor.execute(select_by_act)
                    result = cursor.fetchall()
                    field_names = [i[0] for i in cursor.description]
                    print(tabulate(result, headers=field_names, tablefmt='psql'))

                print("If you are not changing a value, enter original value and press enter. Type 0 to exit to the menu.")
                UPDdist = float(input("Enter new distance to 2 decimal places: "))
                UPDelev = float(input("Enter new elevation gain to 2 decimal places: "))

                update_ACT = ('''UPDATE mydb.activity 
                SET Distance = %f, ElevationGain = %f WHERE idActivity = %d''' % (UPDdist, UPDelev, UPDactID))
                with connection.cursor() as cursor:
                    for result in cursor.execute(update_ACT, multi=True):
                        if result.with_rows:
                            print(result.fetchall())
                    connection.commit()

                select_by_act = ("SELECT * FROM mydb.all_activities WHERE idActivity = %d" % (UPDactID))
                with connection.cursor() as cursor:
                    cursor.execute(select_by_act)
                    result = cursor.fetchall()
                    field_names = [i[0] for i in cursor.description]
                    print(tabulate(result, headers=field_names, tablefmt='psql'))

                mainMENU()
                break
            # back
            elif optionNum == 3:
                actMENU()
                break
            # quit
            elif optionNum == 4:
                break
            #exit to main
            elif optionNum == 0:
                mainMENU()
                break
            else:
                print("Enter a valid choice between 1 and 4.")
                editACT()

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

                # pull user info
                select_userINFO = ("SELECT idUser, FirstName, LastName FROM mydb.User")
                with connection.cursor() as cursor:
                    cursor.execute(select_userINFO)
                    # for row in cursor.fetchall():
                    #    print(row)
                    # connection.commit()
                    results = cursor.fetchall()
                    field_names = [i[0] for i in cursor.description]
                    print(tabulate(results, headers=field_names, tablefmt='psql'))

                userID = int(input("Enter User ID to look up: "))
                select_by_user = ("SELECT * FROM mydb.activity WHERE idUser = %d" % userID)
                with connection.cursor() as cursor:
                    cursor.execute(select_by_user)
                    results = cursor.fetchall()
                    field_names = [i[0] for i in cursor.description]
                    print(tabulate(results, headers=field_names, tablefmt='psql'))

                DELuserID = int(input("Enter Activity ID to delete, enter 0 to exit to main menu:  "))
                delete_ACT_user = ("DELETE FROM mydb.activity WHERE idActivity = %d" % DELuserID)
                with connection.cursor() as cursor:
                    cursor.execute(delete_ACT_user)
                    connection.commit()
                    print("Record Deleted")

                makeTable("activity")

                mainMENU()
                break

            # activity id
            elif optionNum == 2:

                # pull activity info
                select_actINFO = ("SELECT idActivity, ActivityName FROM mydb.Activity")
                with connection.cursor() as cursor:
                    cursor.execute(select_actINFO)
                    results = cursor.fetchall()
                    field_names = [i[0] for i in cursor.description]
                    print(tabulate(results, headers=field_names, tablefmt='psql'))

                actID = int(input("Enter Activity ID to look up: "))
                select_by_act = ("SELECT * FROM mydb.activity WHERE idActivity = %d" % (actID))
                with connection.cursor() as cursor:
                    cursor.execute(select_by_act)
                    results = cursor.fetchall()
                    field_names = [i[0] for i in cursor.description]
                    print(tabulate(results, headers=field_names, tablefmt='psql'))

                DELactID = int(input("Enter Activity ID to delete, enter 0 to exit to main menu: "))
                delete_ACT_user = ("DELETE FROM mydb.activity WHERE idActivity = %d" % DELactID)
                with connection.cursor() as cursor:
                    cursor.execute(delete_ACT_user)
                    connection.commit()
                    print("Record Deleted")

                makeTable("activity")

                mainMENU()
                break
            #back
            elif optionNum == 3:
                actMENU()
                break
            #quit
            elif optionNum == 4:
                break
            #exit to main
            elif optionNum == 0:
                mainMENU()
                break
            else:
                print("Enter a valid choice between 1 and 4.")
                deleteACT()

        except ValueError:
            print("Invalid choice. Enter a choice between 1 and 4.")
    exit


#add/insert activity type (create)
def addACTtype():
    print("Please answer all requested fields.")
    addActivityTypeName = input("Enter activity type name: ")

    insert_activity_type = ('''INSERT INTO mydb.Activity_Type (Activity_Type_Name)
        VALUES ('%s') ''' % addActivityTypeName)

    with connection.cursor() as cursor:
        cursor.execute(insert_activity_type)
        connection.commit()

    makeTable("activity_type")

    mainMENU()
    exit

# view/read/select activity type (read)
def viewACTtype():
    print("Select search parameter:")
    print('''
    1. View all Activity Types
    2. Back
    3. Quit

    ''')
    while True:
        try:
            optionNum = int(input("Enter Choice: "))

            # act id
            if optionNum == 1:

                # pull act type info
                makeTable("activity_type")

                mainMENU()
                break

            #back
            elif optionNum == 2:
                actTypeMENU()
                break

            #quit
            elif optionNum == 3:
                break

            else:
                print("Enter a valid choice between 1 and 3.")
                viewACTtype()

        except ValueError:
            print("Invalid choice. Enter a choice between 1 and 3.")
    exit

#update activity type (update)
def editACTtype():
    print("Select search parameter activity type to update:")
    print('''
    1. View all Activity Types
    2. Back
    3. Quit

    ''')
    while True:
        try:
            optionNum = int(input("Enter Choice: "))

            # user id
            if optionNum == 1:

                # pull act type info
                makeTable("Activity_Type")

                actTypeID = int(input("Enter Activity Type ID from list above: "))
                select_by_actType = ("SELECT * FROM mydb.Activity_Type WHERE idActivityType = %d" % actTypeID)
                with connection.cursor() as cursor:
                    cursor.execute(select_by_actType)
                    result = cursor.fetchall()
                    field_names = [i[0] for i in cursor.description]
                    print(tabulate(result, headers=field_names, tablefmt='psql'))

                print("If you are not changing a value, enter original value and press enter. Type 0 to exit to menu.")
                UPDactTypeID = int(input("Enter Activity Type ID to update: "))
                UPDactTypeName = input("Enter new activity type name: ")

                update_ACTtype = ('''UPDATE mydb.Activity_Type 
                    SET Activity_Type_Name = '%s' WHERE idActivityType = %d''' % (UPDactTypeName, UPDactTypeID))
                with connection.cursor() as cursor:
                    for result in cursor.execute(update_ACTtype, multi=True):
                        if result.with_rows:
                            print(result.fetchall())
                    connection.commit()

                select_by_actType = ("SELECT * FROM mydb.all_activities WHERE idActivityType = %d" % (UPDactTypeID))
                with connection.cursor() as cursor:
                    cursor.execute(select_by_actType)
                    result = cursor.fetchall()
                    field_names = [i[0] for i in cursor.description]
                    print(tabulate(result, headers=field_names, tablefmt='psql'))

                mainMENU()
                break

            # back
            elif optionNum == 2:
                actTypeMENU()
                break
            # quit
            elif optionNum == 3:
                break
            #exit to main
            elif optionNum == 0:
                mainMENU()
                break
            else:
                print("Enter a valid choice between 1 and 3.")
                editACTtype()

        except ValueError:
            print("Invalid choice")

    exit

#delete activity type (delete)
def deleteACTtype():
    print("Select search parameter for activity type to delete:")
    print('''
    1. View all Activity Types
    2. Back
    3. Quit

    ''')
    while True:
        try:
            optionNum = int(input("Enter Choice: "))

            # act type id
            if optionNum == 1:

                # pull act type info
                makeTable("Activity_Type")

                actTypeID = int(input("Enter Activity Type ID from list above: "))
                select_by_actType = ("SELECT * FROM mydb.Activity_Type WHERE idActivityType = %d" % actTypeID)
                with connection.cursor() as cursor:
                    cursor.execute(select_by_actType)
                    result = cursor.fetchall()
                    field_names = [i[0] for i in cursor.description]
                    print(tabulate(result, headers=field_names, tablefmt='psql'))


                DELactTypeID = int(input("Enter Activity Type ID to delete, enter 0 to exit to main menu:  "))
                delete_ACT_user = ("DELETE FROM mydb.Activity_Type WHERE idActivityType = %d" % DELactTypeID)
                with connection.cursor() as cursor:
                    cursor.execute(delete_ACT_user)
                    connection.commit()
                    print("Record Deleted")

                makeTable("Activity_Type")

                mainMENU()
                break

            #back
            elif optionNum == 2:
                actTypeMENU()
                break
            #quit
            elif optionNum == 3:
                break
            #exit to main
            elif optionNum == 0:
                mainMENU()
                break
            else:
                print("Enter a valid choice between 1 and 4.")
                deleteACTtype()

        except ValueError:
            print("Invalid choice. Enter a choice between 1 and 4.")
    exit


#add/insert difficulty (create)
def addDiff():
    print("Please answer all requested fields.")
    addDifficulty = input("Enter difficulty name: ")

    insert_diff_type = ('''INSERT INTO mydb.Difficulty (Difficulty_Level)
        VALUES ('%s') ''' % addDifficulty)

    with connection.cursor() as cursor:
        cursor.execute(insert_diff_type)
        connection.commit()

    makeTable("Difficulty")

    mainMENU()
    exit

# view/read/select difficulty (read)
def viewDiff():
    print("Select search parameter:")
    print('''
    1. View all Activity Types
    2. Back
    3. Quit

    ''')
    while True:
        try:
            optionNum = int(input("Enter Choice: "))

            # pull difficulty info
            if optionNum == 1:
                makeTable("Difficulty")

                mainMENU()
                break

            #back
            elif optionNum == 2:
                diffMENU()
                break

            #quit
            elif optionNum == 3:
                break

            else:
                print("Enter a valid choice between 1 and 3.")
                viewDiff()

        except ValueError:
            print("Invalid choice. Enter a choice between 1 and 3.")
    exit

#update difficulty (update)
def editDiff():
    print("Select search parameter activity type to update:")
    print('''
    1. View all Activity Types
    2. Back
    3. Quit

    ''')
    while True:
        try:
            optionNum = int(input("Enter Choice: "))

            # user id
            if optionNum == 1:

                # pull act type info
                makeTable("Difficulty")

                diffTypeID = int(input("Enter Difficulty Type ID from list above: "))
                select_by_diffType = ("SELECT * FROM mydb.Difficulty WHERE idDifficulty = %d" % diffTypeID)
                with connection.cursor() as cursor:
                    cursor.execute(select_by_diffType)
                    result = cursor.fetchall()
                    field_names = [i[0] for i in cursor.description]
                    print(tabulate(result, headers=field_names, tablefmt='psql'))

                print("If you are not changing a value, enter original value and press enter. Type 0 to exit to menu.")
                UPDdiffID = int(input("Enter Difficulty ID to update: "))
                UPDdiffName = input("Enter new difficulty type name: ")

                update_DIFFtype = ('''UPDATE mydb.Difficulty 
                    SET Difficulty_Level = '%s' WHERE idDifficulty = %d''' % (UPDdiffName, UPDdiffID))
                with connection.cursor() as cursor:
                    for result in cursor.execute(update_DIFFtype, multi=True):
                        if result.with_rows:
                            print(result.fetchall())
                    connection.commit()

                select_by_diffType = ("SELECT * FROM mydb.Difficulty WHERE idDifficulty = %d" % (UPDdiffID))
                with connection.cursor() as cursor:
                    cursor.execute(select_by_diffType)
                    result = cursor.fetchall()
                    field_names = [i[0] for i in cursor.description]
                    print(tabulate(result, headers=field_names, tablefmt='psql'))

                mainMENU()
                break

            # back
            elif optionNum == 2:
                diffMENU()
                break
            # quit
            elif optionNum == 3:
                break
            #exit to main
            elif optionNum == 0:
                mainMENU()
                break
            else:
                print("Enter a valid choice between 1 and 3.")
                editDiff()

        except ValueError:
            print("Invalid choice")

    exit

#delete difficulty (delete)
def deleteDiff():
    print("Select search parameter for difficulty to delete:")
    print('''
    1. View all Difficulty Types
    2. Back
    3. Quit

    ''')
    while True:
        try:
            optionNum = int(input("Enter Choice: "))

            # act type id
            if optionNum == 1:

                # pull act type info
                makeTable("Difficulty")

                diffTypeID = int(input("Enter Difficulty Type ID from list above: "))
                select_by_actType = ("SELECT * FROM mydb.Difficulty WHERE idDifficulty = %d" % diffTypeID)
                with connection.cursor() as cursor:
                    cursor.execute(select_by_actType)
                    result = cursor.fetchall()
                    field_names = [i[0] for i in cursor.description]
                    print(tabulate(result, headers=field_names, tablefmt='psql'))


                DELdiffTypeID = int(input("Enter Difficulty Type ID to delete, enter 0 to exit to main menu:  "))
                delete_ACT_user = ("DELETE FROM mydb.Difficulty WHERE idDifficulty = %d" % DELdiffTypeID)
                with connection.cursor() as cursor:
                    cursor.execute(delete_ACT_user)
                    connection.commit()
                    print("Record Deleted")

                makeTable("Difficulty")

                mainMENU()
                break

            #back
            elif optionNum == 2:
                diffMENU()
                break
            #quit
            elif optionNum == 3:
                break
            #exit to main
            elif optionNum == 0:
                mainMENU()
                break
            else:
                print("Enter a valid choice between 1 and 4.")
                deleteDiff()

        except ValueError:
            print("Invalid choice. Enter a choice between 1 and 4.")
    exit


#add/insert region (create)
def addRegion():
    print("Please answer all requested fields.")
    addReg = input("Enter region name: ")

    insert_region = ('''INSERT INTO mydb.Region (RegionName)
        VALUES ('%s') ''' % addReg)

    with connection.cursor() as cursor:
        cursor.execute(insert_region)
        connection.commit()

    makeTable("Region")

    mainMENU()
    exit

# view/read/select region (read)
def viewRegion():
    print("Select search parameter:")
    print('''
    1. View all Regions
    2. Back
    3. Quit

    ''')
    while True:
        try:
            optionNum = int(input("Enter Choice: "))

            # pull difficulty info
            if optionNum == 1:
                makeTable("Region")

                mainMENU()
                break

            #back
            elif optionNum == 2:
                regionMENU()
                break

            #quit
            elif optionNum == 3:
                break

            else:
                print("Enter a valid choice between 1 and 3.")
                viewDiff()

        except ValueError:
            print("Invalid choice. Enter a choice between 1 and 3.")
    exit

#update region (update)
def editRegion():
    print("Select search parameter region type to update:")
    print('''
    1. View all Region Types
    2. Back
    3. Quit

    ''')
    while True:
        try:
            optionNum = int(input("Enter Choice: "))

            # user id
            if optionNum == 1:

                # pull act type info
                makeTable("Region")

                regTypeID = int(input("Enter Region Type ID from list above: "))
                select_by_regType = ("SELECT * FROM mydb.Region WHERE idRegion = %d" % regTypeID)
                with connection.cursor() as cursor:
                    cursor.execute(select_by_regType)
                    result = cursor.fetchall()
                    field_names = [i[0] for i in cursor.description]
                    print(tabulate(result, headers=field_names, tablefmt='psql'))

                print("If you are not changing a value, enter original value and press enter. Type 0 to Exit")
                UPDregID = int(input("Enter Region ID to update: "))
                UPDregName = input("Enter new region type name: ")

                update_ACTtype = ('''UPDATE mydb.Region
                    SET RegionName = '%s' WHERE idRegion = %d''' % (UPDregName, UPDregID))
                with connection.cursor() as cursor:
                    for result in cursor.execute(update_ACTtype, multi=True):
                        if result.with_rows:
                            print(result.fetchall())
                    connection.commit()

                select_by_actType = ("SELECT * FROM mydb.Region WHERE idRegion = %d" % (UPDregID))
                with connection.cursor() as cursor:
                    cursor.execute(select_by_actType)
                    result = cursor.fetchall()
                    field_names = [i[0] for i in cursor.description]
                    print(tabulate(result, headers=field_names, tablefmt='psql'))

                mainMENU()
                break

            # back
            elif optionNum == 2:
                regionMENU()
                break
            # quit
            elif optionNum == 3:
                break
            #exit to main
            elif optionNum == 0:
                mainMENU()
                break
            else:
                print("Enter a valid choice between 1 and 3.")
                editDiff()

        except ValueError:
            print("Invalid choice")

    exit

#delete region (delete)
def deleteRegion():
    print("Select search parameter region type to delete:")
    print('''
    1. View all Region Types
    2. Back
    3. Quit

    ''')
    while True:
        try:
            optionNum = int(input("Enter Choice: "))

            # act type id
            if optionNum == 1:

                # pull region type info
                makeTable("Region")


                regTypeID = int(input("Enter Region ID from list above: "))
                select_by_actType = ("SELECT * FROM mydb.Region WHERE idRegion = %d" % regTypeID)
                with connection.cursor() as cursor:
                    cursor.execute(select_by_actType)
                    result = cursor.fetchall()
                    field_names = [i[0] for i in cursor.description]
                    print(tabulate(result, headers=field_names, tablefmt='psql'))


                DELregTypeID = int(input("Enter Region ID to delete, enter 0 to exit to main menu:  "))
                delete_REG_user = ("DELETE FROM mydb.Region WHERE idRegion = %d" % DELregTypeID)
                with connection.cursor() as cursor:
                    cursor.execute(delete_REG_user)
                    connection.commit()
                    print("Record Deleted")

                makeTable("Region")

                mainMENU()
                break

            #back
            elif optionNum == 2:
                regionMENU()
                break
            #quit
            elif optionNum == 3:
                break
            #exit to main
            elif optionNum == 0:
                mainMENU()
                break
            else:
                print("Enter a valid choice between 1 and 3.")
                deleteDiff()

        except ValueError:
            print("Invalid choice. Enter a choice between 1 and 3.")
    exit


#add/insert route type (create)
def addRouteType():
    print("Please answer all requested fields.")
    addINFO = input("Enter Route Type name: ")

    insert_into = ('''INSERT INTO mydb.Route_Type (Route_Name)
        VALUES ('%s') ''' % addINFO)

    with connection.cursor() as cursor:
        cursor.execute(insert_into)
        connection.commit()

    makeTable("Route_Type")

    mainMENU()
    exit

# view/read/select route type (read)
def viewRouteType():
    print("Select search parameter:")
    print('''
    1. View all Route Types
    2. Back
    3. Quit

    ''')
    while True:
        try:
            optionNum = int(input("Enter Choice: "))

            # pull difficulty info
            if optionNum == 1:
                makeTable("Route_Type")

                mainMENU()
                break

            #back
            elif optionNum == 2:
                routeTypeMENU()
                break

            #quit
            elif optionNum == 3:
                break

            else:
                print("Enter a valid choice between 1 and 3.")
                viewDiff()

        except ValueError:
            print("Invalid choice. Enter a choice between 1 and 3.")
    exit

#update region (update)
def editRouteType():
    print("Select search parameter route type to update:")
    print('''
    1. View all Route Types
    2. Back
    3. Quit

    ''')
    while True:
        try:
            optionNum = int(input("Enter Choice: "))

            # user id
            if optionNum == 1:

                # pull act type info
                makeTable("Route_Type")

                typeID = int(input("Enter Route Type ID from list above: "))
                select_by = ("SELECT * FROM mydb.Route_Type WHERE idRouteType = %d" % typeID)
                with connection.cursor() as cursor:
                    cursor.execute(select_by)
                    result = cursor.fetchall()
                    field_names = [i[0] for i in cursor.description]
                    print(tabulate(result, headers=field_names, tablefmt='psql'))

                print("If you are not changing a value, enter original value and press enter. Type 0 to Exit")
                UPDid = int(input("Enter Route Type ID to update: "))
                UPDname = input("Enter new route type type name: ")

                update_type = ('''UPDATE mydb.Route_Type
                    SET Route_Name = '%s' WHERE idRouteType = %d''' % (UPDname, UPDid))
                with connection.cursor() as cursor:
                    for result in cursor.execute(update_type, multi=True):
                        if result.with_rows:
                            print(result.fetchall())
                    connection.commit()

                select_by = ("SELECT * FROM mydb.Route_Type WHERE idRouteType = %d" % (UPDid))
                with connection.cursor() as cursor:
                    cursor.execute(select_by)
                    result = cursor.fetchall()
                    field_names = [i[0] for i in cursor.description]
                    print(tabulate(result, headers=field_names, tablefmt='psql'))

                mainMENU()
                break

            # back
            elif optionNum == 2:
                routeTypeMENU()
                break
            # quit
            elif optionNum == 3:
                break
            #exit to main
            elif optionNum == 0:
                mainMENU()
                break
            else:
                print("Enter a valid choice between 1 and 3.")
                editDiff()

        except ValueError:
            print("Invalid choice")

    exit

#delete region (delete)
def deleteRouteType():
    print("Select search parameter route type to delete:")
    print('''
    1. View all Route Types
    2. Back
    3. Quit

    ''')
    while True:
        try:
            optionNum = int(input("Enter Choice: "))

            # act type id
            if optionNum == 1:

                # pull region type info
                makeTable("Route_Type")


                typeID = int(input("Enter Route Type ID from list above: "))
                select_by = ("SELECT * FROM mydb.Route_Type WHERE idRouteType = %d" % typeID)
                with connection.cursor() as cursor:
                    cursor.execute(select_by)
                    result = cursor.fetchall()
                    field_names = [i[0] for i in cursor.description]
                    print(tabulate(result, headers=field_names, tablefmt='psql'))


                DELid = int(input("Enter Route Type ID to delete, enter 0 to exit to main menu:  "))
                delete_id = ("DELETE FROM mydb.Route_Type WHERE idRouteType = %d" % DELid)
                with connection.cursor() as cursor:
                    cursor.execute(delete_id)
                    connection.commit()
                    print("Record Deleted")

                makeTable("Route_Type")

                mainMENU()
                break

            #back
            elif optionNum == 2:
                routeTypeMENU()
                break
            #quit
            elif optionNum == 3:
                break
            #exit to main
            elif optionNum == 0:
                mainMENU()
                break
            else:
                print("Enter a valid choice between 1 and 3.")
                deleteDiff()

        except ValueError:
            print("Invalid choice. Enter a choice between 1 and 3.")
    exit


#add/insert terrain type (create)
def addTerrainType():
    print("Please answer all requested fields.")
    addINFO = input("Enter Terrain Type name: ")

    insert_into = ('''INSERT INTO mydb.Terrain_Type (Terrian_Name)
        VALUES ('%s') ''' % addINFO)

    with connection.cursor() as cursor:
        cursor.execute(insert_into)
        connection.commit()

    makeTable("Terrain_Type")

    mainMENU()
    exit

# view/read/select terrain type (read)
def viewTerrainType():
    print("Select search parameter:")
    print('''
    1. View all addresses
    2. Back
    3. Quit

    ''')
    while True:
        try:
            optionNum = int(input("Enter Choice: "))

            # pull difficulty info
            if optionNum == 1:
                makeTable("Terrain_Type")

                mainMENU()
                break

            #back
            elif optionNum == 2:
                terrainTypeMENU()
                break

            #quit
            elif optionNum == 3:
                break

            else:
                print("Enter a valid choice between 1 and 3.")
                viewDiff()

        except ValueError:
            print("Invalid choice. Enter a choice between 1 and 3.")
    exit

#update terrain (update)
def editTerrainType():
    print("Select search parameter terrain type to update:")
    print('''
    1. View all Terrain Types
    2. Back
    3. Quit

    ''')
    while True:
        try:
            optionNum = int(input("Enter Choice: "))

            # user id
            if optionNum == 1:

                # pull act type info
                makeTable("Terrain_Type")

                typeID = int(input("Enter Terrain Type ID from list above: "))
                select_by = ("SELECT * FROM mydb.Terrain_Type WHERE idTerrain = %d" % typeID)
                with connection.cursor() as cursor:
                    cursor.execute(select_by)
                    result = cursor.fetchall()
                    field_names = [i[0] for i in cursor.description]
                    print(tabulate(result, headers=field_names, tablefmt='psql'))

                print("If you are not changing a value, enter original value and press enter. Type 0 to Exit")
                UPDid = int(input("Enter Terrain Type ID to update: "))
                UPDname = input("Enter new terrain type type name: ")

                update_type = ('''UPDATE mydb.Route_Type
                    SET Terrian_Name = '%s' WHERE idTerrain = %d''' % (UPDname, UPDid))
                with connection.cursor() as cursor:
                    for result in cursor.execute(update_type, multi=True):
                        if result.with_rows:
                            print(result.fetchall())
                    connection.commit()

                select_by = ("SELECT * FROM mydb.Terrain_Type WHERE idTerrain = %d" % (UPDid))
                with connection.cursor() as cursor:
                    cursor.execute(select_by)
                    result = cursor.fetchall()
                    field_names = [i[0] for i in cursor.description]
                    print(tabulate(result, headers=field_names, tablefmt='psql'))

                mainMENU()
                break

            # back
            elif optionNum == 2:
                terrainTypeMENU()
                break
            # quit
            elif optionNum == 3:
                break
            #exit to main
            elif optionNum == 0:
                mainMENU()
                break
            else:
                print("Enter a valid choice between 1 and 3.")
                editDiff()

        except ValueError:
            print("Invalid choice")

    exit

#delete terrain (delete)
def deleteTerrainType():
    print("Select search parameter route type to delete:")
    print('''
    1. View all Route Types
    2. Back
    3. Quit

    ''')
    while True:
        try:
            optionNum = int(input("Enter Choice: "))

            # act type id
            if optionNum == 1:

                # pull region type info
                makeTable("Terrain_Type")


                typeID = int(input("Enter Terrain Type ID from list above: "))
                select_by = ("SELECT * FROM mydb.Terrain_Type WHERE idTerrain = %d" % typeID)
                with connection.cursor() as cursor:
                    cursor.execute(select_by)
                    result = cursor.fetchall()
                    field_names = [i[0] for i in cursor.description]
                    print(tabulate(result, headers=field_names, tablefmt='psql'))


                DELid = int(input("Enter Terrain Type ID to delete, enter 0 to exit to main menu:  "))
                delete_id = ("DELETE FROM mydb.Terrain_Type WHERE idTerrain = %d" % DELid)
                with connection.cursor() as cursor:
                    cursor.execute(delete_id)
                    connection.commit()
                    print("Record Deleted")

                makeTable("Terrain_Type")

                mainMENU()
                break

            #back
            elif optionNum == 2:
                terrainTypeMENU()
                break
            #quit
            elif optionNum == 3:
                break
            #exit to main
            elif optionNum == 0:
                mainMENU()
                break
            else:
                print("Enter a valid choice between 1 and 3.")
                deleteDiff()

        except ValueError:
            print("Invalid choice. Enter a choice between 1 and 3.")
    exit


#add/insert address (create)
def addAddresses():
    print("Please answer all requested address info fields.")
    addLine1 = input("Enter address line 1: ")
    addLine2 = input("Enter address line 2: ")
    addCity = input("Enter city name: ")
    addState = input("Enter 2 letter state code: ")
    addZip = input("Enter 5 digit zip code: ")
    addPhone = input("Enter 10 digit phone number in 123-456-7890 format: ")

    # pull user info
    select_userINFO = ("SELECT idUser, FirstName, LastName FROM mydb.User")
    with connection.cursor() as cursor:
        cursor.execute(select_userINFO)
        result = cursor.fetchall()
        field_names = [i[0] for i in cursor.description]
        print(tabulate(result, headers=field_names, tablefmt='psql'))
    ADDidUSER = int(input(''' Choose User ID number for user adding address:
            '''))

    makeTable("Region")
    addRegion = input("Enter 2 digit region code for address location: ")


    insert_address = ('''INSERT INTO mydb.Addresses (idUSER, line1, line2, city, state, zipCD, phone, Region_idRegion)
        VALUES (%d, '%s', '%s', '%s', '%s', '%s', '%s', '%s') '''
                       % (ADDidUSER, addLine1, addLine2, addCity, addState, addZip, addPhone, addRegion)
                       )
    with connection.cursor() as cursor:
        cursor.execute(insert_address)
        connection.commit()

    makeTable("Addresses")

    mainMENU()
    exit

# view/read/select address (read)
def viewAddresses():
    print("Select search parameter:")
    print('''
    1. View all addresses
    2. Back
    3. Quit

    ''')
    while True:
        try:
            optionNum = int(input("Enter Choice: "))

            # act id
            if optionNum == 1:

                # pull act type info
                makeTable("Addresses")

                mainMENU()
                break

            #back
            elif optionNum == 2:
                addressMENU()
                break

            #quit
            elif optionNum == 3:
                break

            else:
                print("Enter a valid choice between 1 and 3.")
                viewACT()

        except ValueError:
            print("Invalid choice. Enter a choice between 1 and 3.")
    exit

#update address (update)
def editAddresses():
    print("Select option to update addresses:")
    print('''
    1. View all addresses 
    2. Back
    3. Quit

    ''')
    while True:
        try:
            optionNum = int(input("Enter Choice: "))

            # user id
            if optionNum == 1:

                # pull address info
                makeTable("Addresses")

                addTypeID = int(input("Enter Address ID from list above: "))
                select_by_add = ("SELECT * FROM mydb.Addresses WHERE idAddresses = %d" % addTypeID)
                with connection.cursor() as cursor:
                    cursor.execute(select_by_add)
                    result = cursor.fetchall()
                    field_names = [i[0] for i in cursor.description]
                    print(tabulate(result, headers=field_names, tablefmt='psql'))

                print("If you are not changing a value, enter original value and press enter. Type 0 to exit.")
                addLine1 = input("Enter address line 1: ")
                addLine2 = input("Enter address line 2: ")
                addCity = input("Enter city name: ")
                addState = input("Enter 2 letter state code: ")
                addZip = input("Enter 5 digit zip code: ")
                addPhone = input("Enter 10 digit phone number in 123-456-7890 format: ")

                # pull user info
                select_userINFO = ("SELECT idUser, FirstName, LastName FROM mydb.User")
                with connection.cursor() as cursor:
                    cursor.execute(select_userINFO)
                    result = cursor.fetchall()
                    field_names = [i[0] for i in cursor.description]
                    print(tabulate(result, headers=field_names, tablefmt='psql'))
                ADDidUSER = int(input(''' Choose User ID number for user adding address:
                        '''))

                makeTable("Region")
                addRegion = input("Enter 2 digit region code for address location: ")

                update_address = ('''UPDATE mydb.Addresses SET idUSER = %d, line1 ='%s', line2 ='%s', city ='%s', state ='%s', zipCD ='%s', phone ='%s', Region_idRegion ='%s'
                    WHERE idAddresses = %d '''
                                  % (ADDidUSER, addLine1, addLine2, addCity, addState, addZip, addPhone, addRegion, addTypeID)
                                  )
                with connection.cursor() as cursor:
                    cursor.execute(update_address)
                    connection.commit()

                select_by = ("SELECT * FROM mydb.Addresses WHERE idAddresses = %d" % (addTypeID))
                with connection.cursor() as cursor:
                    cursor.execute(select_by)
                    result = cursor.fetchall()
                    field_names = [i[0] for i in cursor.description]
                    print(tabulate(result, headers=field_names, tablefmt='psql'))

                mainMENU()
                break

            # back
            elif optionNum == 2:
                addressMENU()
                break
            # quit
            elif optionNum == 3:
                break
            # exit to menu
            elif optionNum == 0:
                mainMENU()
                break
            else:
                print("Enter a valid choice between 1 and 3.")
                viewACT()

        except ValueError:
            print("Invalid choice")

    exit

#delete address (delete)
def deleteAddresses():
    print("Select search parameter for activity type to delete:")
    print('''
    1. View all addresses
    2. Back
    3. Quit

    ''')
    while True:
        try:
            optionNum = int(input("Enter Choice: "))

            # act type id
            if optionNum == 1:

                # pull act type info
                makeTable("Addresses")

                TypeID = int(input("Enter Address ID from list above: "))
                select_by_actType = ("SELECT * FROM mydb.Addresses WHERE idAddresses = %d" % TypeID)
                with connection.cursor() as cursor:
                    cursor.execute(select_by_actType)
                    result = cursor.fetchall()
                    field_names = [i[0] for i in cursor.description]
                    print(tabulate(result, headers=field_names, tablefmt='psql'))


                DELid = int(input("Enter Address ID to delete, enter 0 to exit to main menu:  "))
                delete_add = ("DELETE FROM mydb.Addresses WHERE idAddresses = %d" % DELid)
                with connection.cursor() as cursor:
                    cursor.execute(delete_add)
                    connection.commit()
                    print("Record Deleted")

                makeTable("Addresses")


                mainMENU()
                break

            #back
            elif optionNum == 2:
                addressMENU()
                break
            #quit
            elif optionNum == 3:
                break
            #exit to main
            elif optionNum == 0:
                mainMENU()
                break
            else:
                print("Enter a valid choice between 1 and 4.")
                viewACT()

        except ValueError:
            print("Invalid choice. Enter a choice between 1 and 4.")
    exit


#add/insert user (create)
def addUser():
    print("Please answer all requested user info fields.")
    addFirst = input("Enter First Name: ")
    addLast = input("Enter Last Name: ")
    addEmail = input("Enter email address: ")

    makeTable("Addresses")
    addIdAdd = int(input("Enter user address ID: "))


    insert_user = ('''INSERT INTO mydb.User (FirstName, LastName, email, Addresses_idAddresses)
        VALUES ('%s', '%s', '%s', %d) '''
                       % (addFirst, addLast, addEmail, addIdAdd)
                       )
    with connection.cursor() as cursor:
        cursor.execute(insert_user)
        connection.commit()

    makeTable("User")

    mainMENU()
    exit

# view/read/select user (read)
def viewUser():
    print("Select search parameter:")
    print('''
    1. View all addresses
    2. Back
    3. Quit

    ''')
    while True:
        try:
            optionNum = int(input("Enter Choice: "))

            # act id
            if optionNum == 1:

                # pull act type info
                makeTable("User")

                mainMENU()
                break

            #back
            elif optionNum == 2:
                userMENU()
                break

            #quit
            elif optionNum == 3:
                break

            else:
                print("Enter a valid choice between 1 and 3.")
                viewACT()

        except ValueError:
            print("Invalid choice. Enter a choice between 1 and 3.")
    exit

#update user (update)
def editUser():
    print("Select option to update users:")
    print('''
    1. View all users 
    2. Back
    3. Quit

    ''')
    while True:
        try:
            optionNum = int(input("Enter Choice: "))

            # user id
            if optionNum == 1:

                # pull user info
                makeTable("User")

                useID = int(input("Enter Address ID from list above: "))
                select_by = ("SELECT * FROM mydb.User WHERE idUser = %d" % useID)
                with connection.cursor() as cursor:
                    cursor.execute(select_by)
                    result = cursor.fetchall()
                    field_names = [i[0] for i in cursor.description]
                    print(tabulate(result, headers=field_names, tablefmt='psql'))

                print("If you are not changing a value, enter original value and press enter. Type 0 to exit.")

                addFirst = input("Enter First Name: ")
                addLast = input("Enter Last Name: ")
                addEmail = input("Enter email address: ")

                makeTable("Addresses")
                addIdAdd = int(input("Enter user address ID: "))

                update_user = ('''UPDATE mydb.User SET FirstName = '%s', LastName ='%s', email ='%s', Addresses_idAddresses =%d
                    WHERE idUser = %d '''
                                  % (addFirst, addLast, addEmail, addIdAdd, useID)
                                  )
                with connection.cursor() as cursor:
                    cursor.execute(update_user)
                    connection.commit()

                select_by = ("SELECT * FROM mydb.User WHERE idUser = %d" % (useID))
                with connection.cursor() as cursor:
                    cursor.execute(select_by)
                    result = cursor.fetchall()
                    field_names = [i[0] for i in cursor.description]
                    print(tabulate(result, headers=field_names, tablefmt='psql'))

                mainMENU()
                break

            # back
            elif optionNum == 2:
                userMENU()
                break
            # quit
            elif optionNum == 3:
                break
            # exit to menu
            elif optionNum == 0:
                mainMENU()
                break
            else:
                print("Enter a valid choice between 1 and 3.")
                viewACT()

        except ValueError:
            print("Invalid choice")

    exit

#delete user (delete)
def deleteUser():
    print("Select search parameter for user to delete:")
    print('''
    1. View all users
    2. Back
    3. Quit

    ''')
    while True:
        try:
            optionNum = int(input("Enter Choice: "))

            # act type id
            if optionNum == 1:

                # pull act type info
                makeTable("User")

                TypeID = int(input("Enter User ID from list above: "))
                select_by = ("SELECT * FROM mydb.User WHERE idUser = %d" % TypeID)
                with connection.cursor() as cursor:
                    cursor.execute(select_by)
                    result = cursor.fetchall()
                    field_names = [i[0] for i in cursor.description]
                    print(tabulate(result, headers=field_names, tablefmt='psql'))


                DELid = int(input("Enter User ID to delete, enter 0 to exit to main menu:  "))
                delete_add = ("DELETE FROM mydb.User WHERE idUser = %d" % DELid)
                with connection.cursor() as cursor:
                    cursor.execute(delete_add)
                    connection.commit()
                    print("Record Deleted")

                makeTable("User")


                mainMENU()
                break

            #back
            elif optionNum == 2:
                userMENU()
                break
            #quit
            elif optionNum == 3:
                break
            #exit to main
            elif optionNum == 0:
                mainMENU()
                break
            else:
                print("Enter a valid choice between 1 and 3.")
                viewACT()

        except ValueError:
            print("Invalid choice. Enter a choice between 1 and 3.")
    exit

#main
from getpass import getpass
from mysql.connector import connect, Error
from tabulate import tabulate

try:
    with connect(
        host="localhost",
        user=input("Enter username: "),
        password=getpass("Enter password: "),
        database="mydb",
        connect_timeout=28800
    ) as connection:
        print(connection)
        mainMENU()

except Error as err:
    print(err)


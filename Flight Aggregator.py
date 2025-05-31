# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 23:42:34 2024

@author: Navneet
"""

"""Travel Aggregator"""

#%%
import csv
import mysql.connector as sqlconnect



print("__________________________________________________________")
print("|                                                        |")
print("|                                                        |")
print("|             ___  __   __           __                  |")
print("|              |  |__| |__| |_   _| |_  |                |")
print("|              |  |\   |  |   | |   |   |                |")
print("|              |  | \  |  |   |_|   |__ |___             |")
print("|                                                        |")
print("|     __   ___  ___   ___  __  ___  __  ___  ___  ___    |")
print("|    |  | |    |     |__| |   |    |  |  |  |  | |__|    |")
print("|    |__| | __ |  __ |\   |_  | __ |__|  |  |  | |\      |")
print("|    |  | |__| |__|  | \  |__ |__| |  |  |  |__| | \     |")
print("|                                                        |")
print("|                   Press Enter to start                 |")
print("_________________________________________________________|")

a = input()
print()

"""Function to convert CSV file 'routes.csv' to a SQL file"""

def csvtosql():
    try:     
        sqlconnext = sqlconnect.connect(host = "localhost", user = "root", password = "Lacnor", database = "flightaggregator3")
        
    except:    
        global pathcsv1
        global pathcsv2
        global pathtxt
        
        pathcsv1 = "C:/Users/USER/Desktop/Programs/Flight Aggregator/routes.csv"#input("Enter Path of routes.csv: ")
        pathcsv2 = "C:/Users/USER/Desktop/Programs/Flight Aggregator/Airlines.csv"#input("Enter Path of airlines.csv: ")
        pathtxt = "C:/Users/USER/Desktop/Programs/Flight Aggregator/GlobalAirportDatabase.txt"#input("Enter Path of GlobalairportDatabase.txt")
        connext = sqlconnect.connect(host = "localhost", user = "root", password = "Lacnor")
        cursor= connext.cursor()
        command = "create database flightaggregator3;"
        cursor.execute(command)
        connext.commit()
        connext.close()
        sqlconnext = sqlconnect.connect(host = "localhost", user = "root", password = "Lacnor", database = "flightaggregator3")
        

        
        airlinelis = ["123_","456_","789_","A","B","C","D","E","F","G","H","I","J"
                      ,"K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
        cursor = sqlconnext.cursor()    
        
        for i in airlinelis:
            creator = "create table "+i+"(airlinecode varchar(100),airline_id varchar(100),source_airport varchar(100),sourceairportid varchar(100),destination_airport varchar(100), destinationairport_id varchar(100),code_share varchar(100), stops varchar(100),equipment varchar(100));"
            cursor.execute(creator)
            sqlconnext.commit()        
        
        for j in airlinelis:
            with open(pathcsv1,"r") as f1:
                reader1 = csv.reader(f1)
                for k in reader1:
                    if k[2][0] in j:
                        tup1 = tuple(k)
                        command1 = "insert into "+str(j)+" values"+str(tup1)+";"
                        cursor.execute(command1)
                        sqlconnext.commit()
        sqlconnext.close()
        print("Uploaded routes.csv into sql!")
        
        csvtosql2()
        txttosql()

def csvtosql2():
    sqlconnext = sqlconnect.connect(host = "localhost", user = "root", password = "Lacnor", database = "flightaggregator3")
    
    if sqlconnext.is_connected:
        print("Database Connected")
    cursor= sqlconnext.cursor()
    
    command = "create table airlines(Code Varchar(4),Name Varchar(100));"
    cursor.execute(command)
    sqlconnext.commit()
    
    with open(pathcsv2,"r") as f:
        a = csv.reader(f)
        for i in a:
            command = "insert into airlines values('"+str(i[0])+"','"+str(i[1])+"');"
            
            try:
                cursor.execute(command)
                sqlconnext.commit()
            except:
                pass
    sqlconnext.close()
    print("Uplaoded airlines.csv into sql")

"""Function to convert txt file 'GlobalAirportDatabase.txt' to a SQL file"""

def txttosql():
    sqlconnext = sqlconnect.connect(host = "localhost", user = "root", password = "Lacnor", database = "flightaggregator3")
    txt = open(pathtxt)
    regulator = 0
    cursor = sqlconnext.cursor()
    
    command = "create table airportdata (ICAOcode varchar(100),IATAcode varchar(100), AirportName varchar(100), City varchar(100), Country varchar(100))"
    cursor.execute(command)
    sqlconnext.commit()
    print("Done")
    
    
    while True:
        line = txt.readline()
    
        tupline = tuple(line.split(":"))
        try:
            tup = (tupline[0],tupline[1],tupline[2],tupline[3],tupline[4])
        except IndexError:
            print("SQL file is ready!")
            break
        print(tup)
        command = "insert into airportdata values"+str(tup)+";"
        print(command)
        cursor.execute(command)
        sqlconnext.commit()
    
    txt.close()
    sqlconnext.close()
    print("Uploaded Global Airport database into sql")

csvtosql()

def asksql():
    counter = 0
    counters = 0
    sqlconnext = sqlconnect.connect(host = "localhost", user = "root", password = "Lacnor", database = "flightaggregator3")
    lis = []
    lisf = []
    liss = []
    
    while True:
        
        cursor = sqlconnext.cursor()
        print()
        print("Enter 1 to Explore all routes")
        print("Enter 2 to Find your flight")
        print("Enter 3 to Access Saved Routes")
        print("Enter 4 to Find out how to work the program")
        print("Enter 5 to exit")
        print()
        choice = input("Enter your choice: ")
        
        if choice == "1":
            lis = []
            print()
            print("Enter at least one of the following to view all air routes through them")
            country = input("Name of the country: ")
            depcity = input("City of departure: ")
            code = input("Enter the IATA code of arriving airport: ")
            print()
            choice1lis = [[country,"country"],[depcity,"city"],[code,"IATAcode"]]
            
            counter = 0
            for i in choice1lis:
                if i[0]:
                    counter = counter +  1
                    if counter == 1:                        
                        command = 'select * from airportdata where '+str(i[1])+' = "'+str(i[0])+'"'

                    if counter > 1:
                        command = command + ' and '+str(i[1])+' = '+'"'+str(i[0])+'"'
                
            command = command + ";"
            cursor.execute(command)
            data = cursor.fetchall()
            
            cursor = sqlconnext.cursor()
            counter2 = 0
            routesdata = []
            
            for i in data:
                switchdata = i[1]
                command = 'select * from '+str(switchdata[0])+' where source_airport = "'+str(switchdata)+'";'
                cursor.execute(command)
                data2 = cursor.fetchall()                                
                
                for j in data2:
                    counter2 = counter2 + 1
                    routesdata.append([counter2,j[0],j[2],j[4]])
            
            print("No., Airline code, Code of depart,Name of airport,City,Country,Code of arriv, Name, City, Country")
            
            counter3 = 0
            for i in routesdata: 
                cursor = sqlconnext.cursor()
                command = 'select IATAcode,Airportname,City,Country from airportdata where IATAcode = "'+str(i[3])+'";'
                cursor.execute(command)
                arriv = cursor.fetchall()
                if not arriv:
                    continue
                
                
                cursor = sqlconnext.cursor()
                command = 'select IATAcode,Airportname,City,Country from airportdata where IATAcode = "'+str(i[2])+'";'
                cursor.execute(command)
                depart = cursor.fetchall()
                counter3 = counter3 + 1
                
                print(counter3,i[1],"From",depart[0][0],depart[0][1],depart[0][2],depart[0][3],"To",arriv[0][0],arriv[0][1],arriv[0][2],arriv[0][3])
                
        
        elif choice == "2":
            departing = input("Enter City of Departure:")
            
            cursor = sqlconnext.cursor()
            command = "select * from airportdata where city = '"+departing+"';"
            cursor.execute(command)
            a = cursor.fetchall()
            print()
            if len(a) >= 1:
                
                print("Code    :    Name of the Airport     :      City")
                for i in a:
                    print(i[1],"    :   ",i[2],"    :   ",i[3])
                
                departurecode = input("Enter the Code of the airport of Departure: ")
            else:
                print("The name of this City is invalid. Try again")
                departurecode = None
                
            print()
            arrival = input("Enter city of Arrival: ")
            
            command = "select * from airportdata where city = '"+arrival+"';"
            cursor.execute(command)
            a = cursor.fetchall()
            print()
            
            if len(a) >= 1:
                
                print("Code    :    Name of the Airport     :      City")
                for i in a:
                    print(i[1],"    :   ",i[2],"    :   ",i[3])
                
                arrivalcode = input("Enter the Code of the airport of Arrival: ")
            else:
                print("The name of this city is invalid. Try Again")
                arrivalcode = None
            
            if departurecode is not None and arrivalcode is not None:
                startingletter = departurecode[0]
                command = "select * from "+startingletter+" where destination_airport ='"+arrivalcode+"' and source_airport = '"+departurecode+"';"
                print()            
                cursor.execute(command)
                a = cursor.fetchall()
            

                if len(a) == 0:
                    lis = []
                    print("There are no direct flights. But these connecting flights are available!")
                    print()
                    command = "select * from "+startingletter+" where source_airport ='"+departurecode+"';"
                    cursor.execute(command)
                    a = cursor.fetchall()
                    
                    print("Airline      :       Source airport :        :       Destination Airport")
                    
                    for i in a:
                        command = "select * from "+i[4][0]+" where destination_airport ='"+arrivalcode+"' and source_airport = '"+i[4]+"';"
                        cursor.execute(command)
                        b = cursor.fetchall()
                        
                        if len(b) == 0:
                            pass
                        else:
                            counters = counters + 1
                            
                            command = "select * from airlines where code = '"+i[0]+"';"
                            cursor.execute(command)
                            c = cursor.fetchall()
                            print(counters, end = "  ")
                           
                            try:
                                airf = c[0][1]
                                print(airf, end = " : ")
                            except:
                                airf = "NA"
                                print(airf, end = " : ")
                            
                            command = "select * from airportdata where IATAcode = '"+i[2]+"';"
                            cursor.execute(command)
                            d = cursor.fetchall()
                            try:
                                birf = d[0][2]
                                print(birf, end  = " : ")
                            except:
                                birf = "NA"
                                print(birf, end  = " : ")
                            
                            command = "select * from airportdata where IATAcode = '"+i[4]+"';"
                            cursor.execute(command)
                            e = cursor.fetchall()
                            try:
                                cirf = e[0][2]
                                print(cirf, end  = " : ")
                            except:
                                cirf = "NA"
                                print(cirf, end  = " : ")
                            
                            print()
                            lisf.append([counters,airf,birf,cirf])
                            
                            print("Followed by: ")
                            
                            command = "select * from airlines where code = '"+b[0][0]+"';"
                            cursor.execute(command)
                            c = cursor.fetchall()
                            print(counters, end = "  ")
                           
                            try:
                                airs = c[0][1]
                                print(airs, end = " : ")
                            except:
                                airs = "NA"
                                print(airs, end = " : ")
                            
                            command = "select * from airportdata where IATAcode = '"+b[0][2]+"';"
                            cursor.execute(command)
                            d = cursor.fetchall()
                            try:
                                birs = d[0][2]
                                print(birs, end  = " : ")
                            except:
                                birs = "NA"
                                print(birs, end  = " : ")
                            
                            
                            command = "select * from airportdata where IATAcode = '"+b[0][4]+"';"
                            cursor.execute(command)
                            e = cursor.fetchall()
                            try:
                                cirs = e[0][2]
                                print(cirs, end  = " : ")
                            except:
                                cirs = "NA"
                                print(cirs, end  = " : ")
                            
                            print()
                            print()
                            liss.append([counters,airs,birs,cirs])
                        
    
                else:
                    liss = []
                    lisf = []
                    print("Airline      :       Source airport :        :       Destination Airport")
                    
                    
                    for i in a:
                        counters = counters + 1
                        command = "select * from airlines where code ='"+i[0]+"';"
                        cursor.execute(command)
                        c = cursor.fetchall()
                        
                        print(counters, end = "  ")
                        try:
                            air = c[0][1]
                            print(air, end = " : ")
                        except:
                            air = "NA"
                            print(air, end = " : ")
                        
                        command = "select * from airportdata where IATAcode = '"+i[2]+"';"
                        cursor.execute(command)
                        d = cursor.fetchall()
                        try:
                            bir = d[0][2]
                            print(bir, end  = " : ")
                        except:
                            bir = "NA"
                            print(bir, end  = " : ")
                            
                        command = "select * from airportdata where IATAcode = '"+i[4]+"';"
                        cursor.execute(command)
                        e = cursor.fetchall()
                        try:
                            cir = e[0][2]
                            print(cir, end  = " : ")
                        except:
                            cir = "NA"
                            print(cir, end  = " : ")
                        
                        print()
                        lis.append([counter,air,bir,cir])
                    
        elif choice == "3":
            while True:
                print()
                print("Enter 1 to Add a route")
                print("Enter 2 to delete a route")
                print("Enter 3 to see all saved routes")
                print("Enter 4 to go back")
                print()
                choices = input("Enter your choice: ")
                
                if choices == "1":
                    if liss == [] and lisf == []:                        
                        if len(lis) == 0:
                            print("You can only Save Routes after looking up specific flights")
                        else:
                            number = int(input("Enter the Route number of the flight to be saved: "))
                            with open("Savedroutes.csv","r") as f:
                                a = csv.reader(f)
                                count = len(list(a))
                                
                            with open("Savedroutes.csv","a+",newline = "") as f:
                                a = csv.writer(f)
                                adder = [count+1,lis[number-1][1],lis[number-1][2],lis[number-1][3]]
                                a.writerow(adder)
                    
                    elif lis == []:
                        if len(lisf) == 0 or len(liss) == 0:
                            print("You can only save routes after looking up specific flights")
                        else:
                            number = int(input("Enter the Route number of the flight to be saved: "))
                            with open("Savedroutes.csv","r") as f:
                                a = csv.reader(f)
                                count = len(list(a))
                                
                            with open("Savedroutes.csv","a+",newline = "") as f:
                                a = csv.writer(f)
                                adder = [count+1,lisf[number-1][1],lisf[number-1][2],lisf[number-1][3],"|",liss[number-1][1],liss[number-1][2],liss[number-1][3]]
                                a.writerow(adder)
                    liss = []
                    lisf = []
                    lis = []
                                
                elif choices == "2":
                    with open("Savedroutes.csv","r") as f:
                        a = csv.reader(f) 
                        lisa = list(a)
                        number = int(input("Enter the Number of the route to be deleted:"))
                        
                        with open("Savedroutes.csv","w", newline = "") as f:
                            b = csv.writer(f)
                            for i in lisa:
                                if int(i[0]) != number:
                                    b.writerow(i)
                    liss = []
                    lisf = []
                    lis = []
                    
                elif choices == "3":
                    with open("Savedroutes.csv","r") as f:
                        a = csv.reader(f)
                        for i in a:
                            print(i)                    
                    liss = []
                    lisf = []
                    lis = []
                
                
                elif choices == "4":
                    break
                    liss = []
                    lisf = []
                    lis = []
                
                else:
                    print("Enter a valid choice!")
                
            
        elif choice == "4":
            print("Travel Aggregator")
            print()
            print("""
Users can make use of this software to optimise their long-distance travel.

We will start with a Welcome screen where the following options would be displayed:
    1. Explore Routes
    2. Find your flight
    3. Saved Routes
    4. Learn more about the software

    
Explore your routes enables you to search up all flight options availble in different 
countries and cities. It allows one to get a sense of the scale of the 
available data and spot patterns.

You can enter your destinaiton and your starting point and the software will
find list out all available flights by different airlines. If there are no
direct flights between the two destinations, then the code finds out which 
airports the airport of departure does have flights to and if any of these 
airports have routes connecting them with the final destination. As of now
the code can only find routes with one connecting flight.

Saved Routes allows you to store and view the routes you found. There are
seperate options to view, add, and delete routes.


This software is the amalgamation of 3 large datasets. The first one was a
csv file that contains a list of all the routes between different airports.
It also holds the the various airport codes, airline codes, and other 
miscellaneous data.
The second dataset is a textfile that contains the IATA airport codes,and 
data on the airport, city, and country names.
The last dataset is a csv file that contains IATA airline codes along with
the airline names.

This program accesses these files and uplaodes their data onto sql, from 
where they are linked up to provide all the information we need.
 
            """)
            
        elif choice == "5":
            break
        
        else:
            print("Enter a valid opton!")
asksql()
        


        
# Flight-Aggregator

The aim of this project is to come up with software that aggregates enormous amounts of aviation-related data into an interface that aids travellers in navigating the hugely complex world of flight bookings.

The Program first checks whether the database has already been configured on the system. If it hasn’t been, then it creates the database, extracts the data from the datasets (see below), and uploads them into sql tables. If the data was already available on sql, then the above step is skipped and the user-oriented part of the program starts up.
Users are greeted by a banner followed by 5 options. Choosing the first option, Explore all Routes, allows users to grasp the sheer scale of the data available in this program. We can enter the country name, the city name, and the IATA Code of the airport (or just one of these) and the program can fish out every single flight operated out of the place. If a user simply wishes to see which flights go out of Turkmenistan, they may just put the country name and leave the rest of the criteria blank. If a user would like to find flights out of their home city, then they can leave the rest of the criteria blank.

The second option, Find your flight, allows you to find all flights between two airports. The users must enter the cities in which the two airports are situated and will be provided with the codes of all the airports in these towns. After specifying the code, the users will now be able to view all the routes flown by different airlines between the two airports. If there are no direct flights between the two airports, the program will find intermediate airports that are connected to both the source and destination airports and display the routes flown by the airport to that end.

The Third option, Access Saved Routes, allows the user to save the flights displayed in the second option onto a csv file. The user can add a route, delete a route, and see all the saved routes. It will all be based on flight numbers that will be displayed when using the second option.

The fourth option, Find out how to work the program, provides the user with information on how to use the program and how it works. 

Lastly, the user can press 5 to exit the program.

The project is founded on 3 datasets obtained from reputable sources on the Internet. All the airport and airline codes are based on IATA regulations.
 The first dataset, “Routes.csv”, contains a set of 67,663 flight routes flown across the globe, all the way from regional flights to intercontinental ones. It includes the airline code of the company flying the route, the source and destination codes and ids, as well as other miscellaneous information. 
The second dataset, “Airlines.csv” contains a list of 947 airline names followed by their codes. 
The last dataset is “Globalairportdatabase.txt” that contains 9300 entries on the airports of the world. Nearly every airport and aerodrome in every part of the world is covered here, with their ICAO Codes, IATA Codes, Airport Names, City, Country, and Coordinates all made available.

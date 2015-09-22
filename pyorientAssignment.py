
import pyorient
import sys  #a system lib with some useful functions for working with the operation system.

client = pyorient.OrientDB("localhost", 2424)#"."syntax to access the library pyorient.
session_id = client.connect("root", "xiaozhuasha")
db_name = "soufun"
db_username = "admin"
db_password = "admin"


# Error Handling with expected errors to make users aware whether the error is due to code or their mistakes.
if client.db_exists( db_name, pyorient.STORAGE_TYPE_MEMORY ):
	client.db_open( db_name, db_username, db_password )
	print db_name + " opened successfully"
else:
	print "database [" + db_name + "] does not exist! session ending..."
	sys.exit() #.exit() function within the sys lib is to close the program intentionally instead of letting it crash.

# test your program constantly, especially after you implement a key feature.
#22.536025, 114.050236  22.555961, 114.075986
lat1 = 22.536025
lat2 = 22.555961

lng1 = 114.050236
lng2 = 114.075986

query = 'SELECT FROM Listing WHERE latitude BETWEEN {} AND {} AND longitude BETWEEN {} AND {}'

records = client.command(query.format(lat1, lat2, lng1, lng2))

numListings = len(records)

print 'received ' + str(numListings) + ' records'


# [ANALYZE THE RETURNED RECORDS TO DETERMINE THE MINIMUM, MAXIMUM, AND AVERAGE PRICE OF THE LISTINGS]
# Hint: the loop that you need to look into each record is already provided below.
# To find the average price, add up all the prices and divide by the number of results
# To find the minimum price, create a variable and initialize it to a very large number, 
# then test each price to see if it is smaller than the current minimum. If it is, update 
# the minimum variable with that price. You can do something similar to find the maximum.


minimumPrice=1000000
maximumPrice=1
totalPrice=0
for record in records:
	print record.price
	totalPrice+=record.price
	if record.price<minimumPrice:
	    minimumPrice=record.price
	else:
	    minimumPrice=minimumPrice
	if record.price>maximumPrice:
	    maximumPrice=record.price
	else:
	    maximumPrice=maximumPrice
	    
print minimumPrice
print maximumPrice
print totalPrice

avePrice=totalPrice/numListings
print avePrice
# [PRINT OUT THE RESULTING VALUES BY CONCATENATING THEM TO THESE LINES TO CHECK YOUR WORK]

print 'min price: '+str(minimumPrice)
print 'max price: ' +str(maximumPrice)
print 'average price: '+str(avePrice)

client.db_close()
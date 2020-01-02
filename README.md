# leftfield test

this uses a bruteforce method for calculating most optimal paths for a Travelling Salesman Problem
while I am aware of a dynamic programming method this method was a bit easier to implement within the time constraints

I used the django framework for the web framework due to familiarity

This API ingests any list of venues in this format [[x,y],[x,y],[x,y]] where index 0 is home

### There are two end points

/venue_list/ POST which takes an array of the format above as a venue list and adds it to the database returns the pk of the venue list

/tour_path/{pk} GET provide it a pk for a venue_list and it calculates the most optimal path of the tour specified and stores it in the DB if the path exists already it will be returned from the DB

There are Two models

### VenueList

venue_list - (nvarchar(200)) a string array intended to be formatted as [[x,y], [x,y]] etc where index 0 is home

### Path

path - (nvarchar(250)) a string array that has an optimal path for a set of venues formatted as [[x,y], [x,y]] where index 0 is the start and the last index is the end of the path

distance - (float) a float that is the total distance travelled on the path

venues_id - (foreign key) meant to link the path to list of venues

I used django's built-in ORM and SQLite for speed and simplicity

### The ORM functions being used more or less translate to the following queries

In the insert of the x,y coordinates 

INSERT INTO tour_venuelist (venuelist) VALUES ({string list})

To grab existing venue lists 

SELECT * FROM tour_venuelist where id={specified id}

and to insert Paths

INSERT INTO tour_path (path, distance, venues_id) VALUES ({string path list}, {float for distance}, {id of venue list})

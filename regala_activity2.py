from pymongo import *

## CHANGE THE 'localhost' VALUE AT THE BOTTOM OF THE CODE TO CONNECT TO YOUR MONGODB SERVER ##
def openConnection(host='localhost'):
    port = 27017
    conn = MongoClient(host, port)
    return conn

def closeConnection(conn):
    conn.close()

# [1] use manilaRecords

def useManilaRecords(conn):
    conn = openConnection()
    db = conn["manilaRecords"]

# [2] create a collection 

"""
The collection is implicitly created when using the CRUD operations.
"""

# [3] insertMany Mathematics Albums

def insertMathematics(conn):

    db = conn["manilaRecords"]
    MathematicsRecords = [
            # PLUS
        {
            "title": "The A Team",
            "year": 2011,
            "album": "plus",
            "runtime": 268
        },
        {
            "title": "Drunk",
            "year": 2012,
            "album": "plus",
            "runtime": 200
        },
        {
            "title": "U.N.I.",
            "year": 2011,
            "album": "plus",
            "runtime": 228
        },
        {
            "title": "Grade 8",
            "year": 2011,
            "album": "plus",
            "runtime": 179
        },
        {
            "title": "Wake Me Up",
            "year": 2011,
            "album": "plus",
            "runtime": 229
        },
            # MULTIPLY 
        {
            "title": "One",
            "year": 2014,
            "album": "multiply",
            "runtime": 252
        },
        {
            "title": "I'm a Mess",
            "year": 2014,
            "album": "multiply",
            "runtime": 244
        },
        {
            "title": "Sing",
            "year": 2014,
            "album": "multiply",
            "runtime": 235
        },
        {
            "title": "Don't",
            "year": 2014,
            "album": "multiply",
            "runtime": 219
        },
        {
            "title": "Nina",
            "year": 2014,
            "album": "multiply",
            "runtime": 225
        },
            # DIVIDE
        {
            "title": "Eraser",
            "year": 2017,
            "album": "divide",
            "runtime": 227
        },
        {
            "title": "Eraser",
            "year": 2017,
            "album": "divide",
            "runtime": 261
        },
        {
            "title": "Eraser",
            "year": 2017,
            "album": "divide",
            "runtime": 238
        },
        {
            "title": "Eraser",
            "year": 2017,
            "album": "divide",
            "runtime": 233
        },
        {
            "title": "Eraser",
            "year": 2017,
            "album": "divide",
            "runtime": 263
        },
            # EQUALS
        {
            "title": "Tides",
            "year": 2021,
            "album": "equals",
            "runtime": 195
        },
        {
            "title": "Shivers",
            "year": 2021,
            "album": "equals",
            "runtime": 207
        },
        {
            "title": "First Times",
            "year": 2021,
            "album": "equals",
            "runtime": 185
        },
        {
            "title": "Bad Habits",
            "year": 2021,
            "album": "equals",
            "runtime": 230
        },
        {
            "title": "Overpass Graffiti",
            "year": 2021,
            "album": "equals",
            "runtime": 236
        },
            # SUBTRACT
        {
            "title": "Boat",
            "year": 2023,
            "album": "subtract",
            "runtime": 185
        },
        {
            "title": "Salt Water",
            "year": 2023,
            "album": "subtract",
            "runtime": 239
        },
        {
            "title": "Eyes Closed",
            "year": 2023,
            "album": "subtract",
            "runtime": 194
        },
        {
            "title": "Life Goes On",
            "year": 2023,
            "album": "subtract",
            "runtime": 210
        },
        {
            "title": "Dusty",
            "year": 2023,
            "album": "subtract",
            "runtime": 222
        }
    ]

    db['regala_edSheeranDiscography'].insert_many(MathematicsRecords)

# [4] insertMany Autumn Variations

def insertAutumnVariations(conn):
    
    db = conn["manilaRecords"]
    AutumnVariationsRecords = [
        {
            "title": "Magical",
            "year": 2023,
            "album": "autumn variations",
            "runtime": 194
        },
        {
            "title": "England",
            "year": 2023,
            "album": "autumn variations",
            "runtime": 226
        }
    ]

    db['regala_edSheeranDiscography'].insert_many(AutumnVariationsRecords)

# [5] Query songs released in 2019 and 2020

def findFunction(conn):

    query1 = {"year": { "$in": [2019, 2020]}}
    db = conn["manilaRecords"]
    results1 = db['regala_edSheeranDiscography'].find(query1)
    """
    Using a list to print it out because otherwise it prints out a string like this
    "<pymongo.synchronous.cursor.Cursor object at 0x7c732cad72f0>".
    """
    results1_list = list(results1)
    print(results1_list)

# [6] Update Documents

def updateMathematics(conn):

    db = conn["manilaRecords"]
 
    # Plus Credits
    updateQuery1 = { "album" : "plus" }
    updateValue1 = {
        "$set": { 
            "credits" : [
                {"producers" : [
                    {"name" : "Jake Gosling"}, 
                    {"name" : "Steve Robson"}, 
                    {"name" : "Example"}, 
                    {"name" : "Chris Leonard"}, 
                    {"name" : "Paul Golder"}]
                },
                {"writer" : "Ed Sheeran"}
            ]
        }
    }

    # Multiply Credits
    updateQuery2 = { "album" : "multiply" }
    updateValue2 = {
        "$set": { 
            "credits" : [
                {"producers" : [
                    {"name" : "Ed Sheeran"}, 
                    {"name" : "Steve Robson"}, 
                    {"name" : "Jake Gosling"}, 
                    {"name" : "Benny Blanco"}, 
                    {"name" : "Rick Rubin"}, 
                    {"name" : "Mike Elzondo"}, 
                    {"name" : "Jimmy Napes"}]
                },
                {"writer" : "Ed Sheeran"}
            ]
        }
    }

    # Divide Credits
    updateQuery3 = { "album" : "divide" }
    updateValue3 = {
        "$set": { 
            "credits" : [
                {"producers" : [
                    {"name" : "Ed Sheeran"},
                    {"name" : "Steve Robson"},
                    {"name" : "Benjamin Levin (Benny Blanco)"},
                    {"name" : "Mike Elzondo"},
                    {"name" : "Foy Vance"},
                    {"name" : "Ryan Tedder"}]
                },
                {"writer" : "Ed Sheeran"}
            ]
        }
    }

    # Equals Credits
    updateQuery4 = { "album" : "equals" }
    updateValue4 = {
        "$set": { 
            "credits" : [
                {"producers" : [
                    {"name" : "Ed Sheeran"},
                    {"name" : "Steve Robson"},
                    {"name" : "Aaron Dessner"},
                    {"name" : "Jacknife Lee"},
                    {"name" : "Max Martin"},
                    {"name" : "FRED"},
                    {"name" : "Ben Kohn"}]
                },
                {"writer" : "Ed Sheeran"}
            ]
        }
    }

    # Subtract Credits
    updateQuery5 = { "album" : "subtract" }
    updateValue5 = {
        "$set": { 
            "credits" : [
                {"producers" : [{"name" : "Dessner"}]},
                {"writer" : "Ed Sheeran"}
            ]
        }
    }

    db['regala_edSheeranDiscography'].update_many(updateQuery1, updateValue1)
    db['regala_edSheeranDiscography'].update_many(updateQuery2, updateValue2)
    db['regala_edSheeranDiscography'].update_many(updateQuery3, updateValue3)
    db['regala_edSheeranDiscography'].update_many(updateQuery4, updateValue4)
    db['regala_edSheeranDiscography'].update_many(updateQuery5, updateValue5)

# [7] Rename Field

def renameRuntime(conn):
    
    db = conn["manilaRecords"]
    runtimeQuery = {}
    runtimeUpdate = {
        "$rename": { "runtime": "duration" }
    }

    db['regala_edSheeranDiscography'].update_many(runtimeQuery, runtimeUpdate)

# [8] Query songs in 'Multiply' with duration > 4 minutes

def findFunction2(conn):

    db = conn["manilaRecords"]
    query2 = {
        "$and": [
            { "album" : "multiply"},
            { "duration" : { "$gt": 240 } }
        ]
    }
    results2 = db['regala_edSheeranDiscography'].find(query2)
    """
    Using a list to print it out because otherwise it prints out a string like this
    "<pymongo.synchronous.cursor.Cursor object at 0x7c732cad72f0>".
    """
    results2_list = list(results2)
    print(results2_list)

def deleteAutumnVariations(conn):

    db = conn["manilaRecords"]
    deleteQuery = { "album" : "autumn variations" }
    db['regala_edSheeranDiscography'].delete_many(deleteQuery)

if __name__ == "__main__":

    conn = openConnection("localhost") # Change IP Address here!
    useManilaRecords(conn)
    insertMathematics(conn)
    insertAutumnVariations(conn)
    findFunction(conn)
    updateMathematics(conn)
    renameRuntime(conn)
    findFunction2(conn)
    deleteAutumnVariations(conn)
    closeConnection(conn) 
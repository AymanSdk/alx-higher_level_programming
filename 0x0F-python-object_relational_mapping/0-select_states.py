import MySQLdb
import sys

def list_states(username, password, database_name):

    try:
        db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database_name)
        cursor = db.cursor()

        # Execute the query to retrieve states
        cursor.execute("SELECT * FROM states ORDER BY id ASC")
        
        # Fetch all rows and display results
        states = cursor.fetchall()
        for state in states:
            print(state)

        # Close connection
        cursor.close()
        db.close()

    except MySQLdb.Error as e:
        print("Error connecting to the database:", e)

if __name__ == "__main__":
    # Check if 3 arguments are provided
    if len(sys.argv) != 4:
        print("Usage: python script.py <username> <password> <database_name>")
    else:
        # Retrieve arguments
        username = sys.argv[1]
        password = sys.argv[2]
        database_name = sys.argv[3]

        # Call the function to list states
        list_states(username, password, database_name)

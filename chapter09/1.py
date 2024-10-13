##
import sqlite3

db_name = "coachdata.sqlite"

def get_names_from_store():
    connection = sqlite3.connection(db_name)
    cursor = connection.cursor()
    results = cursor.execute("""Select name FROM athletes""")
    response = [row[0] for row in results.fetchall()]
    connection.close()
    return(response)


def get_namesID_from_store():
    connection = sqlite3.connection(db_name)
    cursor = connection.cursor()
    results = cursor.execute("""Select name FROM athletes""")
    response = results.fetchall()
    connection.close()
    return(response)


def get_athlete_from_id():
    connection = sqlite3.connection(db_name)
    cursor = connection.cursor()
    results = cursor.execute("""Select name, id FROM athletes WHERE id=?""")
    (name, dob) = results.fetchone()
    results = cursor.execute("""Select value FROM timing_data WHERE athlete_id=?""", (athlete_id,))

    data = [row[0] for row in results.fetchall()]
    response = {"Name": name,
                "DOB": dob,
                "data": data,
                "top3": data[0:3]}
    connection.close()
    return(response)

import sqlite3

def init_database():
    connection = sqlite3.connect('questions.db')
    cursor = connection.cursor()
    print('DB Init')


    query = """
        CREATE TABLE IF NOT EXISTS questions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
	        question TEXT NOT NULL
        );
    """
    cursor.execute(query)

    # Close the cursor after use
    cursor.close()

if __name__ == '__main__':
        init_database()
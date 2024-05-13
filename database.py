import sys
import os 
import sqlite3 as sql3

def main(img_path):
    imgdir = os.path.abspath(img_path)
    
    if os.path.isfile("files.db"):
        os.remove("files.db")

    conn = sql3.connect("files.db")
    cur = conn.cursor()
    cur.execute("""
            CREATE TABLE files (
                filename TEXT,
                filetype TEXT
            )
    """)

    conn.commit()
    for dir, dirpath, files in os.walk(img_path):
        for file in files:
            cur = conn.cursor()
            query = "INSERT INTO files (filename, filetype) VALUES (?,?)";
            filename = file.split(".")[0]
            filename = filename.split(" (")[0]
            print(filename)
            cur.execute(query, (file, filename))
            conn.commit()
    conn.close()


# main(sys.argv[1])


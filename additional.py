import  sqlite3

con = sqlite3.connect("data.db")
cur = con.cursor()
def setup():
    time=input("Enter the time: ")
    name=input("Enter the name: ")
    cur.execute("insert into druglist (time,name) values('{}','{}')".format(time,name))
    con.commit()
    print("drug added successfully")
def brows():
    data=cur.execute("select * from druglist")
    return data.fetchall()


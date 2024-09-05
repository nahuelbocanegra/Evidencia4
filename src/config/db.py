import mysql.connector

db= mysql.connector.connect(
    host = "localhost",
    user= "nahuboca",
    password= "Nahuboca7.",
    database= "fresadoracnc",
)

print(db) 
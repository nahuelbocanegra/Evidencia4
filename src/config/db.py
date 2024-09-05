import mysql.connector # type: ignore

db= mysql.connector.connect(
    host = "localhost",
    user= "nahuboca",
    password= "Nahuboca7.",
    database= "fresadoracnc",
)

print(db)
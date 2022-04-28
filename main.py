import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "libraryDB"
)

def add_book():
    book_name = input("Enter the book name : ")
    book_code = input("Enter the book code : ")
    total_books = input("Total books : ")
    subject = input("Enter the subject : ")
    data = (book_name, book_code, total_books, subject)
    sql = "Insert into books values(%s,%s,%s,%s)"
    c = mydb.cursor()
    c.execute(sql, data)
    mydb.commit()
    print("....................")
    print("Data entered successfully")
    main()

def issue_book():
    name = input("Enter name : ")
    roll_no = input("Enter roll no : ")
    code = input("Enter book code : ")
    date = input("Enter date : ")
    sql = "Insert into issue values(%s,%s,%s,%s)"
    data = (name, roll_no, code,date)
    c = mydb.cursor()
    c.execute(sql, data)
    mydb.commit()
    print("....................")
    print("Book issued to : ", name)
    book_update(code, 1)

    

def submit_book():
    name = input("Enter name : ")
    roll_no = input("Enter roll no : ")
    code = input("Enter book code : ")
    date = input("Enter date : ")   
    sql = "Insert into submit values(%s,%s,%s,%s)"
    data = (name, roll_no, code,date)
    c = mydb.cursor()
    c.execute(sql, data)
    mydb.commit()
    print("....................")
    print("Book submitted by : ", name)
    book_update(code, 1)

def book_update(code, u):
    sql = "select TOTAL from books where book code = %s"
    data = (code,)
    c = mydb.cursor()
    c.execute(sql, data)
    myresult = c.fetchone()
    t = myresult[0] + u
    sql = "Update books set TOTAL = %s where book code = %s"
    d = (t, code)
    c.execute(sql, d)
    mydb.commit()
    main()

def delete_book():
    ac = input("Enter the book code : ")
    sql = "delete from books where book code = %s"
    data = (ac,)
    c = mydb.cursor()
    c.execute(sql, data)
    mydb.commit()
    main()

def display_books():
    sql = "select * from books"
    c = mydb.cursor()
    c.execute(sql)
    myresult = c.fetchall()
    for i in myresult:
        print("Book name : ", i[0])
        print("Book code : ", i[1])
        print("Total books : ", i[2])
        print(".....................")
    main()


def main():
    print(""".....................LIBRARY MANAGEMENT.....................
    1. Add book
    2. Issue book
    3. Submit book
    4. Delete book
    5. Display book
    """)

    choice = input("Enter task no : ")
    if(choice == '1'):
        add_book()
    elif(choice == '2'):
        issue_book()
    elif(choice == '3'):
        submit_book()
    elif(choice == '4'):
        delete_book()
    elif(choice == '5'):
        display_books()
    else:
        print("Enter a valid choice !!!")
        main()

def password():
    import random
    ps = random.randint(0000000, 1000000)

    user = input("Enter the Username : ")
    print("Your password : ", ps)

    verify = input("Enter the password : ")
    if verify == str(ps):
        main()
    else:
        verify != str(ps)
        print("Incorrect Password!!!")
        password()

password()
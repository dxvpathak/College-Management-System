import mysql.connector as mysql

db = mysql.connect(host="localhost",user="root",password="",database="college")
command_handler = db.cursor(buffered=True)

def admin_session():
    while 1:
        print("")
        print("Admin Menu : - ")
        print("1. Register new Student")
        print("2. Register new Teacher")
        print("3. Delete Existing Student")
        print("4. Delete Existing Teacher")
        print("5. Logout\n")

        user_option = input(str("Option : "))
        if user_option == "1":
            print("")
            print("Register New Student - ")
            username = input(str("Student username : "))
            password = input(str("Student password : "))
            query_vals = (username,password)
            command_handler.execute("INSERT INTO users (username,password,privilege) VALUES (%s,%s,'student')",query_vals)
            db.commit()
            print(username + " has been registered as a student")
        
        elif user_option == "2":
            print("")
            print("Register New Teacher - ")
            username = input(str("Teacher username : "))
            password = input(str("Teacher password : "))
            query_vals = (username,password)
            command_handler.execute("INSERT INTO users (username,password,privilege) VALUES (%s,%s,'teacher')",query_vals)
            db.commit()
            print(username + " has been registered as a teacher")
    
        elif user_option == "3":
            print("")
            print("Delete Existing Student Account - ")
            username = input(str("Student username : "))
            query_vals = (username,"student")
            command_handler.execute("DELETE FROM users WHERE username = %s AND privilege = %s ",query_vals)
            db.commit()
            if command_handler.rowcount < 1:
                print("User not found")
            else:
                print(username + " has been deleted")

        elif user_option == "4":
            print("")
            print("Delete Existing Teacher Account - ")
            username = input(str("Teacher username : "))
            query_vals = (username,"teacher")
            command_handler.execute("DELETE FROM users WHERE username = %s AND privilege = %s ",query_vals)
            db.commit()
            if command_handler.rowcount < 1:
                print("User not found")
            else:
                print(username + " has been deleted")

        elif user_option == "5":
            print("You have logged out as admin")
            break
        
        else:
            print("No valid option selected")


def auth_admin():
    print("")
    print("You choosed Admin Login")
    print("Kindly enter the credentials.. ")
    username = input(str("Username : "))
    password = input(str("Password : "))
    if username == "admin":
        if password == "pwd":
            admin_session()
        else:
            print("Incorrect password !")
    else:
        print("Login details not recognised") 

def main():
    while 1:
        print("\nWelcome to the college system\n")
        print("1. Login as student")
        print("2. Login as teacher")
        print("3. Login as admin")
        print("4. Exit\n")

        user_option = input(str("Option : "))
        if user_option == "1":
            print("You choosed Student Login")
        elif user_option == "2":
            print("You choosed Teacher Login")
        elif user_option == "3":
            auth_admin()
        elif user_option == "4":
            break    
        else:
            print("No valid option was selected")

main() 
print("\nThanks, the program is terminated now!!\n")
class PasswordManager:


    def __init__(self):
        self.passwords = []

        try:
            with open("passwords.txt",)as f:
                for line in f:
                    site,username,password = line.strip().split(",")
                    self.passwords.append([site,username,password])
        except FileNotFoundError:
            pass
    def save_passwords(self):
        with open ("passwords.txt", "w") as f:
            for item in self.passwords:
                f.write(f"{item[0]}, {item[1]} , {item[2]}\n")
        

    def add_password(self):
        site = input("enter site name: ")
        username = input("enter username: ")
        password = input("enter password: ")

        self.passwords.append([site,username,password])
        self.save_passwords()
        print("password added successfully")
        
    def view_passwords(self):
        if len(self.passwords) == 0:
            print("no passwords stored")
        else:
            print("\n--- saved passwords ---")
            for item in self.passwords:
                print("site:", item[0], "|username:", item[1], "|password:", item[2])

    def delete_password(self):
        site = input("enter site name to delete: ").strip().lower()

        found = False
        for item in self.passwords:
            if item[0].strip().lower() == site:
                self.passwords.remove(item)
                self.save_passwords()
                print("password deleted successfully")
                found = True
                break
        if not found:
            print("site not found")
            
pm = PasswordManager()

while True:
    print("\n--- PasswordManager --- ")
    print("1.Add Passwords")
    print("2.View Passwords")
    print("3.Delete Pssword ")
    print("4.Exit ")

    choice = input("enter your choice: ")

    if choice == "1":
        pm.add_password()
        
    elif choice == "2":
        pm.view_passwords()

    elif choice == "3":
        pm.delete_password()

    elif choice == "4":
        print("exiting...")
        break
    else:
        print("Invalid choice")


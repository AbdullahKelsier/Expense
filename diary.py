def diary_app():
    password = "1234"
    password_attempt = input("Enter password: ")

    if password_attempt != password:
        print("Incorrect password. Access denied.")
        return

    print("Password correct! Welcome to your diary.")
    
    while True:
        action = input("Do you want to (w)rite or (r)ead a diary entry? Type 'exit' to quit: ").lower()

        if action == "w":
            entry = input("Write your diary entry: ")
            with open("diary.txt", "a") as file:
                file.write(entry + "\n")
            print("Diary entry saved.")
        elif action == "r":
            try:
                with open("diary.txt", "r") as file:
                    entries = file.readlines()
                print("Your Diary Entries:")
                for entry in entries:
                    print(entry.strip())
            except FileNotFoundError:
                print("No diary entries found.")
        elif action == "exit":
            print("Exiting diary app. Goodbye!")
            break
        else:
            print("Invalid option. Please choose 'w', 'r', or 'exit'.")

if __name__ == "__main__":
    diary_app()

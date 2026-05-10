import os

def dreams_file_manager():
    filename = "dreams.txt"

    while True:
        print("\n==== DREAMS FILE MANAGER ====")
        print("1. Read inspiring messages")
        print("2. Add a new inspiring message")
        print("3. Rewrite the entire file")
        print("4. Exit")
        
        choice = input("\nEnter your choice: ")

        if choice == '1':
            if os.path.exists(filename):
                with open(filename, "r") as file:
                    print("\n--- Your Dreams ---")
                    print(file.read())
            else:
                print("\nThe file is empty. Try adding a message first!")

        elif choice == '2':
            new_message = input("Write your inspiring message: ")
            with open(filename, "a") as file:
                file.write(new_message + "\n")
            print("Message added")

        elif choice == '3':
            print("Warning: This will overwrite the file.")
            confirm = input("Type YES to continue: ")
            
            if confirm == "YES":
                new_content = input("Write your new set of inspiring messages:\n")
                with open(filename, "w") as file:
                    file.write(new_content + "\n")
                print("File has been overwritten.")
            else:
                print("Action cancelled.")

        elif choice == '4':
            print("Goodbye!")
            break
        
        else:
            print("Invalid Option. Please Pick 1-4.")

if __name__ == "__main__":
    dreams_file_manager()
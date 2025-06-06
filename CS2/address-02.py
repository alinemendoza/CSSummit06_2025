# Address book
import json  # For saving and loading data

# Dictionary format: nickname: [contact, contact, contact...]
database = dict()

# Main command loop
while True:
    menu = input("Command (? for help)?: ")

    # Using the match-case structure
    match menu:
        case "?":
            print("""Command List: [encode] [list] [query] [save] [load] [delete] [quit]""")
            
        case "encode":
            print("Data Entry")
            name = input("Enter Name (blank to abort): ")

            # Warn and check if user wants to update an existing record
            if name in database:
                if input("Sorry, name already exists. Overwrite? [y/n] ").lower() != "y":
                    break

            # Collect contact information
            contents = []
            while True:
                value = input("Enter contact information (or blank to exit): ")
                if value == "":
                    break
                contents.append(value)

            database[name] = contents   # Save into database

        case "list":
            print("Records List")
            names = database.keys()
            for name in names:
                print(name)

        case "query": 
            print("Records Info")
            search = input("Enter Name: ")
            if search in database:
                print(database[search])
            else:
                print("Sorry, {0} not found!".format(search))

        case "save":
            print("Saving Records to Database...")
            with open("./db2.json", "w") as f:
                json.dump(database, f, indent=4)
    
        case "load":
            print("Loading Records from Database...")
            try:
                with open("./db2.json", "r") as f:
                    database = json.load(f)
            except FileNotFoundError:
                print("Error Loading File... File does not exist.")
            except json.JSONDecodeError:
                print("Error Loading File... File is not in a valid JSON format.")

        case "delete":
            print("Delete Record")
            name_to_delete = input("Enter Name to delete: ")
            if name_to_delete in database:
                confirm = input(f"Are you sure you want to delete {name_to_delete}? [y/n] ").lower()
                if confirm == "y":
                    del database[name_to_delete]
                    print(f"Record for {name_to_delete} deleted.")
                else:
                    print("Deletion canceled.")
            else:
                print(f"Record for {name_to_delete} not found.")

        case "quit":
            print("Closing Transactions... Goodbye!")
            break
        
        case _:
            print("Unknown Command")

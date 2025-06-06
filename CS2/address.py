# Address book
import json     # For saving and loading data

# Dictionary format: nickname: [contact, contact, contact...]
database = dict()

# Main command loop
while True:
    menu = input("Command (? for help)?: ")

    # Using the match-case structure
    match menu:
        case "?":
            print("""Commands:
                  encode
                  list
                  query
                  save
                  load
                  quit""")
            
        case "encode":
            print("Encode")
            name = input("Enter name (blank to abort): ")

            # Warn and check if user wants to update an existing record
            if name in database:
                if input("Sorry, name exists. Overwrite?").lower() != "yes":
                    break

            # Collect contact information
            contents = []
            while True:
                value = input("Enter contact information (or blank to exit): ")
                if value == "":
                    break
                else:
                    contents.append(value)

            database[name] = contents   # Save into database

        case "list":
            print("List")
            names = database.keys()
            for name in names:
                print(name)

        case "query": 
            print("Query")
            search = input("Enter name: ")
            if search in database:
                print(database[search])
            else:
                print("Sorry, {0} not found".format(search))

        case "save":
            print("Saving")
            with open("./db.json", "w") as f:
                json.dump(database, f)
    
        case "load":
            print("Loading")
            try:
                with open("./db.json", "r") as f:
                    database = json.load(f)
            except:
                print("Failed to load file")

        case "quit":
            print("Goodbye")
            break
        
        case _:
            print("Unknown commmand")
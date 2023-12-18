import json

with open("data.json", "r") as file:
    data = json.load(file)

def display_json_content():
    print(json.dumps(data, indent=2))

def add_record(name, height, gender):
    new_record = {"name": name, "height": height, "gender": gender}
    data.append(new_record)
    print("Record added successfully.")

def remove_record(name):
    for record in data:
        if record["name"] == name:
            data.remove(record)
            print(f"Record for {name} removed successfully.")
            return
    print(f"No record found for {name}.")

def search_by_field(field, value):
    results = [record for record in data if record.get(field) == value]
    if results:
        print(f"Search results for {field} = {value}:")
        print(json.dumps(results, indent=2))
    else:
        print(f"No records found for {field} = {value}.")

def compare_height():
    girls_height = sum(record["height"] for record in data if record["gender"] == "female")
    boys_height = sum(record["height"] for record in data if record["gender"] == "male")

    if girls_height > boys_height:
        result = {"message": "Girls' total height exceeds boys' total height."}
    else:
        result = {"message": "Boys' total height equals or exceeds girls' total height."}

    with open("height_comparison_result.json", "w") as result_file:
        json.dump(result, result_file, indent=2)

if __name__ == "__main__":
    while True:
        print("\nOptions:")
        print("1. Display JSON content")
        print("2. Add a new record")
        print("3. Remove a record")
        print("4. Search by field")
        print("5. Compare total height")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            display_json_content()
        elif choice == "2":
            name = input("Enter name: ")
            height = int(input("Enter height: "))
            gender = input("Enter gender: ")
            add_record(name, height, gender)
        elif choice == "3":
            name = input("Enter name to remove: ")
            remove_record(name)
        elif choice == "4":
            field = input("Enter field to search (name, height, gender): ")
            value = input(f"Enter {field} value to search: ")
            search_by_field(field, value)
        elif choice == "5":
            compare_height()
            print("Comparison result saved in 'height_comparison_result.json'.")
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

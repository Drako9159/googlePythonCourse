import csv
def __readWithDictionari__():
    with open("googleDic.csv") as file:
        reader = csv.DictReader(file)
        for row in reader:
            print("Name: {}, Phone: {}, Role: {}".format(row["name"], row["phone"], row["role"]))

users = [{"name": "Sol Mansi", "username": "solm", "department": "IT infrastructure"},
         {"name": "Lio Nelson", "username": "lion", "department": "User Experience Research"},
         {"name": "Charlie Grey", "username": "greyc", "department": "Development"}]

keys = ["name", "username", "department"]

def __createWithDictionary__():
    with open("googleDic.csv", mode="w") as file:
        writer = csv.DictWriter(file, fieldnames=keys, lineterminator="\n")
        writer.writeheader()
        writer.writerows(users)

__createWithDictionary__()
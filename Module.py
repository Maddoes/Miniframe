print("Imported module")

test = "Test string"

def find_index(to_search, target):
        for i, value in enumerate(to_search):
            if value == target:
                return i
        return -1

for index, value in enumerate(test):
    print(index, value)
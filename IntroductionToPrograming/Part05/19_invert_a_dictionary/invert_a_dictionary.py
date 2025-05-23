def invert(dictionary: dict) -> None:
    new_dictionary = {}

    for key, value in dictionary.items():
        new_dictionary[value] = key

    dictionary.clear()
    
    for key, value in new_dictionary.items():
        dictionary[key] = value

if __name__ == "__main__":
    s = {1: "first", 2: "second", 3: "third", 4: "fourth"}
    invert(s)
    print(s)
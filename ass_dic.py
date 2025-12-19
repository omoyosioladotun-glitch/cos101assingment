# Dictionary Project
yoruba_dict = {
    "Water": "Omi",
    "House": "Ile",
    "Food": "Ounje",
    "Mother": "Iya",
    "Father": "Baba",
    "Child": "Omo",
    "Rain": "Ojo",
    "Sun": "Oorun",
    "Road": "Ona",
    "Cloth": "Aso",
    "Book": "Iwe",
    "Farm": "Oko",
    "Work": "Ise",
    "Friend": "Ore",
    "Dog": "Aja",
    "Cat": "Ologbo",
    "Fish": "Eja",
    "Forest": "Igbo",
    "City": "Ilu",
    "Morning": "Owuro"
}

hausa_dict = {
    "Water": "Ruwa",
    "House": "Gida",
    "Food": "Abinci",
    "Mother": "Uwa",
    "Father": "Uba",
    "Child": "Yaro",
    "Sun": "Rana",
    "Rain": "Ruwa Sama",
    "Road": "Hanya",
    "Cloth": "Tufafi",
    "Book": "Littafi",
    "Work": "Aiki",
    "Friend": "Aboki",
    "Dog": "Kare",
    "Cat": "Mage",
    "Fish": "Kifi",
    "Town": "Gari",
    "Forest": "Daji",
    "Morning": "Safiya",
    "Car": "Mota"
}

igbo_dict = {
    "Water": "Mmiri",
    "House": "Ulo",
    "Food": "Nri",
    "Mother": "Nne",
    "Father": "Nna",
    "Child": "Nwa",
    "Sun": "Anyanwu",
    "Rain": "Mmiri Ozuzo",
    "Road": "Uzo",
    "Book": "Akwukwo",
    "Work": "Oria",
    "Friend": "Enyi",
    "Dog": "Nkita",
    "Cat": "Pusi",
    "Fish": "Azụ",
    "Town": "Obodo",
    "Forest": "Ohia",
    "Cloth": "Uwe",
    "Morning": "Ututu",
    "Car": "Ugboala"
}


def show_dictionary(dictionary):
    print("Available words:")
    for word in dictionary:
        print(word)

    choice = input("Enter a word to see its meaning: ")

    if choice in dictionary:
        print("Meaning:", dictionary[choice])
    else:
        print("Word not found.")

while True:
    print("=== NIGERIAN LANGUAGE DICTIONARY ===")
    print("1. Yoruba Dictionary")
    print("2. Hausa Dictionary")
    print("3. Igbo Dictionary")
    print("4. Exit")

    option = input("Choose a dictionary (1-4): ")

    if option == "1":
        show_dictionary(yoruba_dict)
    elif option == "2":
        show_dictionary(hausa_dict)
    elif option == "3":
        show_dictionary(igbo_dict)
    elif option == "4":
        print("Thank you for using the dictionary.")
        break
    else:
        print("Invalid choice. Try again.")
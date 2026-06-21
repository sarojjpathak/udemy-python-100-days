import random

    

word_list = [
    "elephant", "giraffe", "penguin", "dolphin", "hamster",
    "parrot", "rabbit", "turtle", "monkey", "zebra",
    "python", "laptop", "monitor", "keyboard", "network",
    "browser", "printer", "database", "website", "internet",
    "nepal", "canada", "brazil", "germany", "france",
    "japan", "mexico", "italy", "sweden", "norway",
    "cricket", "football", "tennis", "hockey", "baseball",
    "volleyball", "badminton", "swimming", "cycling", "bowling",
    "adventure", "backpack", "calendar", "diamond", "festival",
    "garden", "holiday", "journey", "library", "mountain",
    "variable", "function", "integer", "boolean", "string",
    "dictionary", "operator", "argument", "package", "module",
    "airport", "battery", "camera", "chocolate", "fantasy",
    "guitar", "island", "jungle", "lantern", "machine",
    "necklace", "pyramid", "rocket", "suitcase", "village",
    "weather", "yogurt", "zipper", "captain", "treasure",
    "umbrella", "victory", "whisper", "blanket", "octopus",
    "gorilla", "buffalo", "panther", "storage", "server",
    "coding", "compiler", "program", "algorithm", "recursion"
]
restart = True

while restart:
    life = 7
    selected = random.choice(word_list)
    show = ""
    for i in range(len(selected)):
        show += "_"
    print(show)
    choose = ""
    show_list = list(show)
    while show_list != list(selected) and life > 0:
        ch = input("Enter a letter for a word :")
        if ch in selected:
            for i in range(len(selected)):
                if(selected[i] == ch):
                    show_list[i] = ch
        else:
            life -= 1
        if life == 7:
            print('''
                +---+
                |   |
                    |
                    |
                    |
                    |
                =========
                ''')
        elif life == 6:
            print('''
                    +---+
                    |   |
                    O   |
                        |
                        |
                        |
                    =========
                    ''')
        elif life == 5:
            print('''
                    +---+
                    |   |
                    O   |
                    |   |
                        |
                        |
                    =========
                    ''')
        elif life == 4:
            print('''
                        +---+
                        |   |
                        O   |
                       /|   |
                            |
                            |
                        =========
                        ''')
        elif life == 3:
            print('''
                    +---+
                    |   |
                    O   |
                   /|\  |
                        |
                        |
                    =========
                    ''')
        elif life == 2:
            print('''
                    +---+
                    |   |
                    O   |
                   /|\  |
                    |   |
                        |
                    =========
                    ''')
        elif life == 1:
            print('''
                    +---+
                    |   |
                    O   |
                   /|\  |
                    |   |
                    /   |
                    =========
                    ''')
        elif life == 0:
            print('''
                    +---+
                    |   |
                    O   |
                   /|\  |
                    |   |
                   / \  |
                    =========
                    ''')
                            
        
        print(show_list)
       
    print("you had 5 chance but you waste all of them you are noob")
    again = input("Do you want to guess another word : (y/n)")
    if again == "y":
        restart = True
    elif again == "n":
        restart == False

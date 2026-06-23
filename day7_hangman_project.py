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
    word = ' '.join(show)
    print(word)
    
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
            print(f"LIFE {'♥ ' * life}{'♡ ' * (7 - life)}")
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
            print(f"LIFE {'♥ ' * life}{'♡ ' * (7 - life)}")
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
            print(f"LIFE {'♥ ' * life}{'♡ ' * (7 - life)}")
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
            print(f"LIFE {'♥ ' * life}{'♡ ' * (7 - life)}")
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
            print(f"LIFE {'♥ ' * life}{'♡ ' * (7 - life)}")
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
            print(f"LIFE {'♥ ' * life}{'♡ ' * (7 - life)}")
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
            print(f"LIFE {'♥ ' * life}{'♡ ' * (7 - life)}")
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
            print(f"LIFE {'♥ ' * life}{'♡ ' * (7 - life)}")
            print('''
                    +---+
                    |   |
                    O   |
                   /|\  |
                    |   |
                   / \  |
                    =========
                    ''')
                            
        word = ''.join(show_list)
        print(word)
    if life == 0: 
        print("GAME OVER  you have wasted all of your life")
        give_answer = input("do you want to know the answer ? (y/n)")
        print("word is " + selected) if give_answer == 'y' else print("ok thats totally fine boss")
    elif show_list == list(selected):
        print(f"You win !")
    
    again = input("Do you want to guess another word : (y/n)")
    if again == "y":
        restart = True
    else:
        restart = False
print("I HOPE YOU ENJOYED THIS GAME")
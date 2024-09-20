# Text-based adventure game

inventory, wordle_solution, wordle_attempts = [], "magic", 0
current_room, game_over = "entrance", False

rooms = {
    "entrance": {"desc": "You are at the entrance of a mysterious castle.", "exits": {"north": "hall", "east": "library"}, "items": ["key"], "chars": ["guard"]},
    "hall": {"desc": "A grand hall with statues. There's a locked door to the north.", "exits": {"south": "entrance"}, "items": [], "chars": ["sage"]},
    "library": {"desc": "A dusty library filled with old books.", "exits": {"west": "entrance"}, "items": ["book"], "chars": []},
    "treasure_room": {"desc": "The treasure room! Solve the puzzle to claim your prize.", "exits": {"south": "hall"}, "items": [], "chars": []}
}

characters = {
    "guard": {"desc": "A stern guard blocks your path.", "interaction": "Guard: 'I can't let you pass unless you give me the key.'"},
    "sage": {"desc": "An old sage who knows riddles.", "interaction": "Sage: 'Solve the treasure room puzzle to win.'"}
}

def show_room():
    room = rooms[current_room]
    print(f"\n{room['desc']}")
    if room["items"]: print(f"You see: {', '.join(room['items'])}")
    if room["chars"]: print(f"Characters here: {', '.join(room['chars'])}")
    print(f"Exits: {', '.join(room['exits'])}")

def handle_command(command):
    global current_room, inventory, wordle_attempts, game_over
    words = command.split()

    if words[0] in ["go", "move"] and words[1] in rooms[current_room]["exits"]:
        current_room = rooms[current_room]["exits"][words[1]]; show_room()
    elif words[0] == "take" and words[1] in rooms[current_room]["items"]:
        inventory.append(words[1]); rooms[current_room]["items"].remove(words[1]); print(f"You took the {words[1]}.")
    elif words[0] == "use" and words[1] in inventory:
        if words[1] == "key" and current_room == "hall":
            rooms["hall"]["exits"]["north"] = "treasure_room"; print("The door to the treasure room is unlocked!")
    elif words[0] == "talk" and words[2] in rooms[current_room]["chars"]:
        print(characters[words[2]]["interaction"])
        if words[2] == "guard" and "key" in inventory:
            rooms["entrance"]["exits"]["north"] = "hall"; print("The guard steps aside.")
    elif words[0] == "examine" and words[1] == "book" and current_room == "library":
        print("The book contains strange symbols.")
    elif words[0] == "puzzle" and current_room == "treasure_room":
        solve_puzzle()
    elif words[0] == "inventory":
        print(f"Inventory: {', '.join(inventory)}")
    else:
        print("Unknown command.")

def solve_puzzle():
    global wordle_attempts, game_over
    guess = input("Guess the 5-letter word: ").strip().lower()
    if guess == wordle_solution:
        print("You solved the puzzle and won the treasure!"); game_over = True
    else:
        wordle_attempts += 1
        print("Wrong guess!") if wordle_attempts < 3 else print("You failed the puzzle.")

def game_loop():
    show_room()
    while not game_over:
        handle_command(input("\n> "))
    print("Congrats! You completed the game!")

if __name__ == "__main__":
    print("Welcome to the Adventure Game!"); game_loop()

def Show_note():
    try:
        with open('Notes.txt', 'r') as file:
            lines = file.readlines()
            index = 1
            for line in lines:
                if line.startswith("Title:"):
                    print(f"{index}. {line.strip()}")
                    index += 1
                else:
                    print(line.strip())
    except FileNotFoundError:
        print("No notes found. 'Notes.txt' does not exist.")

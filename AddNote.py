def Add_Note():
    title = input("Enter a title for your note: ").strip()
    note = input("Write the note you want to add: ").strip()

    try:
        with open('Notes.txt', 'r') as file:
            lines = file.readlines()
            if lines:
                index = sum(1 for line in lines if line.strip().startswith('Title:')) + 1
            else:
                index = 1
    except FileNotFoundError:
        index = 1

    with open('Notes.txt', 'a') as file:
        file.write(f"Title: {title}\n")
        file.write(f"{note}\n\n")
    print(f"{title} has been added to the list")

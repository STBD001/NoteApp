from AddNote import Add_Note
from RemoveNote import remove_note_by_title
from ShowNote import Show_note
from SearchNote import search_note_by_title

def main():
    while True:
        print("\n--- Note Management Menu ---")
        print("1. Add Note")
        print("2. Remove Note")
        print("3. Show Notes")
        print("4. Search Note by Title")
        print("5. Exit")

        option = input("Choose your option (1-5): ").strip()

        if option == '1':
            Add_Note()
        elif option == '2':
            title = input("Enter the title of the note to remove: ").strip()
            remove_note_by_title('Notes.txt', title)
        elif option == '3':
            Show_note()
        elif option == '4':
            title = input("Enter the title of the note to search: ").strip()
            search_note_by_title('Notes.txt', title)
        elif option == '5':
            break
        else:
            print("ERROR - Incorrect option")

if __name__ == "__main__":
    main()

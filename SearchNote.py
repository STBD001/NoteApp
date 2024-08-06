def search_note_by_title(file_path, title_to_search):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            note_found = False
            note_content = ""
            title_prefix = "Title:"

            for line in lines:
                if line.startswith(title_prefix):
                    if note_found:
                        break  # Stop if we found the note and now encounter a new title
                    line_title = line[len(title_prefix):].strip()
                    if title_to_search == line_title:
                        note_found = True
                        note_content = line
                elif note_found:
                    note_content += line

            if note_found:
                print(f"Note found:\n{note_content.strip()}")
            else:
                print("No note found with the given title.")

    except FileNotFoundError:
        print("File not found. Make sure 'Notes.txt' exists.")
    except Exception as e:
        print(f"An error occurred: {e}")

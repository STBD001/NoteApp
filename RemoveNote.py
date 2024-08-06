def remove_note_by_title(file_path, title_to_remove):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()

        updated_lines = []
        note_found = False
        skip = False
        title_prefix = "Title:"

        for line in lines:
            if line.startswith(title_prefix):
                line_title = line[len(title_prefix):].strip()
                if title_to_remove == line_title:
                    note_found = True
                    skip = True
                else:
                    if skip:
                        skip = False
                    updated_lines.append(line)
            elif skip and line.strip() == '':
                skip = False
            elif not skip:
                updated_lines.append(line)

        if not note_found:
            print("No note found with the given title.")
            return

        with open(file_path, 'w') as file:
            for line in updated_lines:
                file.write(line)

    except FileNotFoundError:
        print("File not found. Make sure 'Notes.txt' exists.")
    except Exception as e:
        print(f"An error occurred: {e}")

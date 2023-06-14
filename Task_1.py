import csv
from datetime import datetime


FILENAME = 'notes.csv'
FIELDS = ['id', 'title', 'body', 'timestamp']


def get_notes():
    with open(FILENAME, 'r') as file:
        reader = csv.DictReader(file, delimiter=';')
        return [note for note in reader]


def save_notes(notes):
    with open(FILENAME, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=FIELDS, delimiter=';')
        writer.writeheader()
        for note in notes:
            writer.writerow(note)


def add_note():
    title = input('Enter title: ')
    body = input('Enter body: ')
    timestamp = datetime.now().isoformat()
    notes = get_notes()
    max_id = max([int(note['id']) for note in notes], default=0)
    new_note = {'id': max_id + 1, 'title': title, 'body': body, 'timestamp': timestamp}
    notes.append(new_note)
    save_notes(notes)


def edit_note():
    note_id = input('Enter note id: ')
    notes = get_notes()
    for note in notes:
        if note['id'] == note_id:
            title = input('Enter new title (or leave blank): ')
            if title:
                note['title'] = title
            body = input('Enter new body (or leave blank): ')
            if body:
                note['body'] = body
            note['timestamp'] = datetime.now().isoformat()
            save_notes(notes)
            break


def delete_note():
    note_id = input('Enter note id: ')
    notes = get_notes()
    notes = [note for note in notes if note['id'] != note_id]
    save_notes(notes)


def filter_notes_by_date():
    date_str = input('Enter date (format: YYYY-MM-DD): ')
    notes = get_notes()
    filtered_notes = [note for note in notes if note['timestamp'].startswith(date_str)]
    if filtered_notes:
        print_notes(filtered_notes)
    else:
        print('No notes found')


def print_notes(notes):
    for note in notes:
        print(f'{note["id"]}. {note["title"]}')
        print(note['body'])
        print(note['timestamp'])
        print()


def print_all_notes():
    notes = get_notes()
    if notes:
        print_notes(notes)
    else:
        print('No notes found')


def menu():
    print('1. Add Note')
    print('2. Edit Note')
    print('3. Delete Note')
    print('4. Filter Notes by Date')
    print('5. List All Notes')
    print('6. Exit')


def main():
    while True:
        menu()
        choice = input('Enter choice: ')
        if choice == '1':
            add_note()
        elif choice == '2':
            edit_note()
        elif choice == '3':
            delete_note()
        elif choice == '4':
            filter_notes_by_date()
        elif choice == '5':
            print_all_notes()
        elif choice == '6':
            break
        else:
            print('Invalid choice')


if __name__ == '__main__':
    main()
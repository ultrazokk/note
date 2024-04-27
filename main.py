from note import Note
from note_manager import NoteManager


def main():
    manager = NoteManager() 
    while True:
        print("1. Добавить заметку")
        print("2. Просмотреть все заметки")
        print("3. Редактировать заметку")
        print("4. Удалить заметку")
        print("5. Выход")
        choice = input("Выберите действие: ")
        if choice == '1':
            title = input("Введите заголовок заметки: ")
            body = input("Введите тело заметки: ")
            manager.add_note(Note(title, body)) 
        elif choice == '2':
            for note in manager.list_notes():
                print(f"ID: {note.id}, Заголовок: {note.title}, Дата создания: {note.created_at}")
        elif choice == '3':
            note_id = input("Введите ID заметки для редактирования: ")
            title = input("Введите новый заголовок(оставьте пустым, если не хотите изменять): ")
            body = input("Введите новое тело (оставьте пустым, если не хотите изменять): ")
            manager.update_note(note_id, title, body)
        elif choice == '4':
            note_id = input("Введите ID заметки для удаления: ")
            manager.delete_note(note_id)
        elif choice == '5':
            break
        else:
            print("Неверный выбор. Попробуйте ещё раз.")          

if __name__ == "__main__":
    main()
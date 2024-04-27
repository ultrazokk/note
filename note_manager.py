class NoteManager:
    def __init__(self, filename='notes.json'):
        self.filename = filename
        self.notes = self.load_notes()

    def load_notes(self):
        try:
            with open(self.filename, 'r') as file:
                return [Note(**note) for note in json.load(file)]
        except FileNotFoundError:
            return []

    def save_notes(self):
        with open(self.filename, 'w') as file:
            json.dump([note.to_dict() for note in self.notes], file, indent=4)

    def add_note(self, note):
        self.notes.append(note)
        self.save_notes()

    def get_note_by_id(self, note_id):
        for note in self.notes:
            if note.id == note_id:
                return note
        return None
    
    def update_note(self, note_id, title=None, body=None):
        note = self.get_note_by_id(note_id)
        if note:
            note.update(title,body)
            self.save_notes()

    def delete_note(self, note_id):
        self.notes = [note for note in self.notes if note.id != note_id]
        self.save_notes()

    def list_notes(self):
        return self.notes
    




import myDiary
from myDiary import entry
from myDiary.entry import Entry


class Diary:

    entry = myDiary.entry.Entry("Test Entry")

    diaryName = ""
    entries = {}
    entry_passwords = {}
    diary_password = None
    isLocked = False

    entries[entry.get_id()] = [entry.get_title(), "Hello World"]

    def __init__(self, diaryName, diaryPassword=None):
        self.diaryName = diaryName
        self.entries = {}
        self.diary_password = diaryPassword
        self.isLocked = False

    def get_diaryName(self):
        return self.diaryName

    def get_entries(self):
        return self.entries.values()

    def get_entry(self, entry_id):
        if entry_id in self.entries:
            return self.entries[entry_id]
        return f"There exists no entry with ID {entry_id}"

    def add_entry(self, title, body):
        user_entry = Entry(title, body)
        self.entries[user_entry.get_id()] = [title, body]

    def edit(self, id_number):
        if not self.verify_entry_details(id_number): return f"Entry with ID {id_number} does not exist. Try again."
        self.edit_choice(id_number)

    def verify_entry_details(self, id_number):
        return id_number in self.entries

    def edit_choice(self, id_number):
        user_choice = input("""
                What do you want to do?

                1. Change Title
                2. Edit Entry
                4. Both Title & Entry
                5. Delete Entry
                6. Return""")

        match user_choice:
            case "1":
                self.change_title(id_number)

            case "2":
                self.edit_entry(id_number)

            case "3":
                self.change_title(id_number)
                self.edit_entry(id_number)

            case "4":
                self.delete_entry(id_number)

            case "5":
                return

            case _:
                return "Invalid input. Try again."

    def change_title(self, id_number):
        new_title = input("Enter new title:\n")
        self.entries[id_number][0] = new_title

    def edit_entry(self, title):
        self.entries[title] = input("Enter new entry:\n")

    def delete_entry(self, title):
        self.entries.pop(title)

    def find_entry_by_title(self, title: str):
       for id_number in self.entries.keys():
           if self.entries[id_number][0] == title: return self.entries[id_number]
       return f"There exists no with named {title}"

    def find_entry_by_id(self, id_number: int):
        if id_number in self.entries: return self.entries[id_number]
        return f"There exists no entry with ID {id_number}"

    def lock_diary(self):
        self.isLocked = True

    def open_diary(self):
        self.isLocked = False



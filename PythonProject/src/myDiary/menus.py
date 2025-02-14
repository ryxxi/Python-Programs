import myDiary
from myDiary import diary
from myDiary.diary import Diary

class Menus(Diary):
    def __init__(self):
        super().__init__("")

    def entry_menu(self, entry_name):
        if entry_name not in self.entries: return f"There exists no entry named {entry_name}"
        print(
        f"""
        ***{entry_name}***
        ------------------
        {self.entries[entry_name]}
        """)

    def diary_menu(self, diary_name):



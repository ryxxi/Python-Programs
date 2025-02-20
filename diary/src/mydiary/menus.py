import mydiary
from mydiary import diary
from mydiary.diary import Diary
from mydiary.diaries import Diaries

class Menus(Diary, Diaries):
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
        if diary_name not in self.diaries: return f"There exists no diary named {diary_name}"
        print(
        f"""
        ***{diary_name}***
        ------------------
        """)

        for count in range(len(self.diaries[diary_name])):
            print(f"Entry {count + 1}: {self.diaries[diary_name]}")



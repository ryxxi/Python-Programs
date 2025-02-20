import mydiary
from mydiary.diary import Diary
from mydiary.entry import Entry
from mydiary.menus import Menus

class Diaries:

    def __init__(self):
        self.menu = Menus()
        self.diaries = {}
        self.diary = Diary("Test Diary")
        self.diaries = {self.diary.get_diaryName(): self.diary.diary_password}

    def create_diary(self, diaryName, diaryPassword=None):
        if diaryName in self.diaries: return f"A diary with name {diaryName} already exists. Try again."
        self.diaries[diaryName] = Diary(diaryName, diaryPassword).diary_password

    def delete_diary(self, diaryName, diaryPassword=None):
        if self.verify_diary_details(diaryName, diaryPassword): del self.diaries[diaryName]
        else: return
        f"""
        A diary with name {diaryName} does not exist
        OR
        Diary password is incorrect.
        
        Try again.
        """

    def verify_diary_details(self, diaryName, diaryPassword=None):
        if diaryName not in self.diaries: return False
        if diaryPassword != self.diaries[diaryName]: return False
        return True

    def edit_diary(self, diaryName, diaryPassword=None):
        if not self.verify_diary_details(diaryName, diaryPassword): return "Diary name or password is incorrect. Try again."
        self.diary.open_diary()


    def view_diary(self, diary_name, diary_password=None):
        if self.verify_diary_details(diary_name, diary_password):
            self.diary.open_diary()
            print(self.menu.diary_menu(diary_name))
        else:
            print("Diary name or password is incorrect. Try again.")



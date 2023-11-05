from datetime import datetime
from note import Note
from exceptions import InvalidUserInputError


class UserInput:
    USER_MESSAGES = {
        "title": "Введите заголовок заметки: ",
        "content": "Введите текст заметки: ",
        "start": "Введите начальную дату: ",
        "end": "Введите конечную дату: ",
    }
    DATETIME_FORMAT = "%Y-%m-%d"

    def __init__(self) -> None:
        self.note_title = ""
        self.note_body = ""
        self.start_date = datetime(1900, 1, 1, 0, 0, 0, 0)
        self.end_date = datetime(9999, 1, 1, 0, 0, 0, 0)

    def set_user_input(self, message: str = "") -> str:
        user_str = input(message)
        return user_str

    def set_title(self) -> None:
        self.note_title = self.set_user_input(self.USER_MESSAGES["title"])

    def set_content(self) -> None:
        self.note_content = self.set_user_input(self.USER_MESSAGES["content"])

    def set_user_input_as_dates(self):
        try:
            self.set_dates()
        except ValueError:
            raise InvalidUserInputError

    def set_dates(self) -> None:
        start = self.set_user_input(self.USER_MESSAGES["start"])
        end = self.set_user_input(self.USER_MESSAGES["end"])
        self.start_date = self.convert_to_datetime(start)
        self.end_date = self.convert_to_datetime(end)

    def convert_to_datetime(self, str_date: str) -> datetime:
        date = datetime.strptime(str_date, self.DATETIME_FORMAT)
        return date


class ConsolePrinter:
    DATETIME_FORMAT = "%Y-%m-%d"

    @classmethod
    def print_search_by_parameter(cls):
        print("Введите параметр для поиска")

    @classmethod
    def not_found(cls):
        print('По заданному параметру ничего не найдено')

    @classmethod
    def print_new_note_message_title(cls) -> None:
        print("Введите заголовок новой заметки")

    @classmethod
    def print_new_note_message_content(cls) -> None:
        print("Введите текст новой заметки")

    @classmethod
    def print_change_message_title(cls) -> None:
        print("Введите заголовок редактируемой заметки")

    @classmethod
    def print_change_message_content(cls) -> None:
        print("Введите текст редактируемой заметки")

    @classmethod
    def print_dates_input_message(cls) -> None:
        print("Ввод начальной и конечной даты в формате год-месяц-день")

    @classmethod
    def print_find_notes_message(cls) -> None:
        print("Ввод названия заметки для поиска")

    @classmethod
    def print_find_note_to_edit(cls) -> None:
        print("Ввод названия заметки для изменения")

    @classmethod
    def print_find_note_to_delete(cls) -> None:
        print("Ввод названия заметки для удаления")

    @classmethod
    def print_delete_message(cls):
        print("Заметки были удалены")

    @classmethod
    def print_list_of_notes(cls, notes_list: list[dict]) -> None:
        print('\n' + '=' * 50)
        for n in notes_list:
            cls.print_note(n)
            print('=' * 50 + '\n')

    @classmethod
    def print_note(cls, note: dict) -> None:
        print(note["note_title"])
        print()
        print(note["note_content"])
        print()
        print(f"Заметка создана/отредактирована: {cls.format_datetime(note['note_date'])}")


    @classmethod
    def format_datetime(cls, date_str: str) -> str:
        date = datetime.strptime(date_str, Note.NOTE_DT_FORMAT)
        date = date.strftime(cls.DATETIME_FORMAT)
        return date

    @classmethod
    def print_help(cls):
        print(
            """
Доступные команды:
    1 - Создать новую заметку
    2 - Посмотреть все заметки
    3 - Посмотреть заметку, введя заголовок
    4 - Изменить заметку, введя заголовок
    5 - Удалить заметку
    6 - Посмотреть заметки в интервале дат создания/редактирования
    7 - Поиск заметок по содержимому
"""
        )
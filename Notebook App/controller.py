from note import Note, NoteList
from view import UserInput as ui
from view import ConsolePrinter as cp
from model import FileSaver as fs
from exceptions import InvalidUserInputError


class Controller:
    def __init__(self) -> None:
        pass

    def create_note(self) -> None:
        cp.print_new_note_message_title()
        user_input_t = ui()
        user_input_t.set_title()
        cp.print_new_note_message_content()
        user_input_c = ui()
        user_input_c.set_content()
        note = Note()
        note.set_title(user_input_t.note_title)
        note.set_content(user_input_c.note_content)
        file_name = note.get_note_id()
        file_data = note.get_note_data()
        fs.save_to_file(file_name, file_data)

    def get_list_of_notes(self):
        files_content = fs.get_contents_list()
        note_list = NoteList()
        note_list.set_list_data(files_content)
        notes_data = note_list.get_list_data()
        cp.print_list_of_notes(notes_data)

    def get_list_of_notes_by_date(self):
        cp.print_dates_input_message()
        user_input = self.set_dates_by_user()
        files_content = fs.get_contents_list()
        note_list = NoteList()
        note_list.set_list_data(files_content)
        note_list.set_dates(user_input.start_date, user_input.end_date)
        notes_data = note_list.get_list_data()
        cp.print_list_of_notes(notes_data)

    def set_dates_by_user(self) -> ui:
        try:
            user_input: ui = ui()
            user_input.set_dates()
            return user_input
        except InvalidUserInputError as e:
            print("Дата была введена в неправильном формате", e)
            return self.set_dates_by_user()

    def get_list_of_notes_by_name(self):
        cp.print_find_notes_message()
        user_input = ui()
        user_input.set_title()
        files_content = fs.get_contents_list()
        note_list = NoteList()
        note_list.set_list_data(files_content)
        notes_data = note_list.get_notes_by_title(user_input.note_title)
        cp.print_list_of_notes(notes_data)

    def edit_note(self):
        cp.print_find_note_to_edit()
        orig_title_input = ui()
        orig_title_input.set_title()
        files_content = fs.get_contents_list()
        note_list = NoteList()
        note_list.set_list_data(files_content)
        notes_data = note_list.get_notes_by_title(orig_title_input.note_title)
        cp.print_change_message_title()
        user_input_t = ui()
        user_input_t.set_title()
        cp.print_change_message_content()
        user_input_c = ui()
        user_input_c.set_content()
        for nd in notes_data:
            note = Note()
            note.set_storage_data(nd)
            note.set_title(user_input_t.note_title)
            note.set_content(user_input_c.note_content)
            file_name = note.get_note_id()
            file_data = note.get_note_data()
            fs.save_to_file(file_name, file_data)

    def delete_note(self):
        cp.print_find_note_to_delete()
        orig_title_input = ui()
        orig_title_input.set_title()
        files_content = fs.get_contents_list()
        note_list = NoteList()
        note_list.set_list_data(files_content)
        notes_data = note_list.get_notes_by_title(orig_title_input.note_title)
        for nd in notes_data:
            note = Note()
            note.set_storage_data(nd)
            file_name = note.get_note_id()
            fs.delete_file(file_name)
        cp.print_delete_message()

    def find_note_by_content(self):
        cp.print_search_by_parameter()
        user_input = ui()
        files_content = fs.search_by_parameter(user_input.set_user_input())
        if len(files_content) > 0:
            note_list = NoteList()
            note_list.set_list_data(files_content)
            notes_data = note_list.get_notes_by_title(user_input.note_title)
            cp.print_list_of_notes(notes_data)
        else:
            cp.not_found()






class Program:
    def __init__(self) -> None:
        pass

    def get_menu_command(self) -> str:
        cp.print_help()
        command = input("Введите желаемую команду: ")
        print()
        return command

    def get_command_from_user(self):
        try:
            self.run_controller()
        except KeyError:
            print("Введена неверная комманда, попробуйте еще раз")
            self.get_command_from_user()

    def run_controller(self):
        control = Controller()
        dict_of_methods = {
            "1": control.create_note,
            "2": control.get_list_of_notes,
            "3": control.get_list_of_notes_by_name,
            "4": control.edit_note,
            "5": control.delete_note,
            "6": control.get_list_of_notes_by_date,
            "7": control.find_note_by_content
        }
        command = self.get_menu_command()
        dict_of_methods[command]()



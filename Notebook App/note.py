import itertools
from datetime import datetime

class Note:

    NOTE_ID_FORMAT = "%Y%m%d%H%M%S"
    NOTE_DT_FORMAT = "%Y%m%d%H%M%S%f"

    def __init__(self):
        self.note_title = ""
        self.note_content = ""
        self.note_date = datetime.now()
        self.note_id = self._note_id_format()

    def _note_id_format(self) -> str:
        _note_id = self.note_date.strftime(self.NOTE_ID_FORMAT)
        return _note_id

    def set_title(self, title: str):
        self.note_title = title

    def set_content(self, content: str):
        self.note_content = content

    def get_note_id(self):
        return self.note_id

    def set_date(self):
        self.note_date = datetime.now()

    def get_note_data(self) -> dict:
        n_dict = {}
        n_dict.update(
            {
                "note_title": self.note_title,
                "note_content": self.note_content,
                "note_id": self.get_note_id(),
                "note_date": self._format_datetime_to_string(self.note_date),
            }
        )
        return n_dict

    def set_storage_data(self, data: dict) -> None:
        for key in data:
            if key == "note_date":
                setattr(
                    self, key, datetime.strptime(data[key], self.NOTE_DT_FORMAT)
                )
            else:
                setattr(self, key, data[key])

    def _format_datetime_to_string(self, _note_datetime: datetime) -> str:
        _datetime_to_string = datetime.strftime(_note_datetime, self.NOTE_DT_FORMAT)
        return _datetime_to_string




class NoteList:

    INIT_START_DATE = datetime(1900, 1, 1, 0, 0, 0, 0)
    INIT_END_DATE = datetime(2099, 1, 1, 0, 0, 0, 0)

    def __init__(self) -> None:
        self.note_list = []
        self.start_date = self.INIT_START_DATE
        self.end_date = self.INIT_END_DATE

    def set_dates(self, start_date: datetime, end_date: datetime) -> None:
        self.start_date = start_date
        self.end_date = end_date

    def set_list_data(self, lst: list) -> None:
        for x in lst:
            note = Note()
            note.set_storage_data(x)
            self.note_list.append(note)

    def get_list_data(self) -> list:
        list_data = []
        for n in self.note_list:
            if self.start_date <= n.note_date <= self.end_date:
                list_data.append(n.get_note_data())
        return list_data


    def get_notes_by_title(self, title: str) -> list:
        list_data = []
        for n in self.note_list:
            if title in n.note_title:
                list_data.append(n.get_note_data())
        return list_data







import os
from glob import glob
import json


class FileSaver:
    STORAGE_DIR = "Notes"
    FILE_FORMAT = ".json"
    FILE_NOT_EXISTS_MESSAGE = "File didn't exist"

    @classmethod
    def save_to_file(cls, file_path: str, file_content: dict) -> None:
        file_path = cls.get_filepath(file_path)
        try:
            os.mkdir(cls.STORAGE_DIR)
        except FileExistsError:
            pass
        finally:
            with open(file_path, "w+", encoding="utf-8") as f:
                json.dump(file_content, f, indent=3)

    @classmethod
    def delete_file(cls, file_name):
        file_name = cls.get_filepath(file_name)
        try:
            os.remove(file_name)
        except:
            print(cls.FILE_NOT_EXISTS_MESSAGE)

    @classmethod
    def get_filepath(cls, file_title: str) -> str:
        file_path = (os.getcwd() + "/" + cls.STORAGE_DIR + "/" + str(file_title) + cls.FILE_FORMAT)
        return file_path

    @classmethod
    def get_contents_list(cls) -> list:
        contents_list = []
        for file_path in glob(os.getcwd() + "/**/*.json"):
            with open(file_path, "r") as f:
                file_content = json.loads(f.read())
                contents_list.append(file_content)
        return contents_list

    @classmethod
    def search_by_parameter(cls, parameter: str) -> list:
        result = []
        for file_path in glob(os.getcwd() + "/**/*.json"):
            with open(file_path, "r") as f:
                file_data = json.loads(f.read())
                if parameter in file_data["note_content"]:
                    result.append(file_data)
        return result


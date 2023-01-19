import os
import json

class FileHandler:
    poster_folder = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'Poster')
    metadata_folder = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'Metadata')
        
    def __init__(self):
        self.__create_necessary_folders()
        self.json_path = None

    @property
    def movie_path(self):
        pass

    @movie_path.setter
    def movie_path(self, mpath):
        self.__file_path = mpath

    def __create_necessary_folders(self):
        #Poster és Metadata mappák létrehozása
        if not os.path.exists(self.poster_folder):
            os.mkdir(self.poster_folder)
        if not os.path.exists(self.metadata_folder):
            os.mkdir(self.metadata_folder)

    def get_data_from_folder(self):
        if not os.path.exists(self.__movie_folder):
            raise FileNotFoundError(f"{self.__movie_folder} does not exist")
   #     temp = []
   #     for item in os.listdir(self.__movie_folder):
   #         if item[-4:] == '.mkv':
   #             temp.append(item[-4])
        return [item[-4] for item in os.listdir(self.__movie_folder) if item[-4:] == '.mkv']

    def get_json_path(self, movie_name):
        self.json_path = os.path.join(self.metadata_folder, f"{movie_name}.json")

    def write_json(self, json_path, data):
        if not os.path.exists(self.metadata_folder):
            raise FileNotFoundError(f"{self.metadata_folder} does not exist")
        with open(self-json_path, "w", encoding = "utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

if __name__ == '__main__':
    test = FileHandler()
    test.get_data_from_folder('Alien')
    test.write_json('Data':'adat')
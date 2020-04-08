from os import path, listdir
import uuid, json
class MinecraftFileHandler:
    def __init__(self, stats_location):
        if path.isdir(stats_location):
            self.stats_location = stats_location
        else:
            raise ValueError(f"'{stats_location}' is not a valid location!")
    

    def __list_files_inside(self):
        return [f for f in listdir(self.stats_location) if path.isfile(path.join(self.stats_location, f))]
    
    def __extract_filename_extension(self, s):
        s = s.split(".")
        
        name = ""
        ext = ""
        for i in range(0, len(s)-1):
            name += s[i]
        ext = s[len(s)-1]
        return [name, ext]
    
    def __valid_uuid(self, s):
        try:
            uuid.UUID(s,version=4)
            return True
        except ValueError:
            return False
    
    def __get_user_files(self):
        files = self.__list_files_inside()
        user_files = list()
        for file in files:
            _file = self.__extract_filename_extension(file)
            if _file[1] == "json" and self.__valid_uuid(_file[0]):
                user_files.append(file)
        return user_files
    

    def get_users_stats(self):
        user_files = self.__get_user_files()


        users_stats = list()
        for user_file in user_files:
            u_file_location = path.join(self.stats_location, user_file)

            content = json.load(open(u_file_location))
            user_id = self.__extract_filename_extension(user_file)[0]

            users_stats.append({
                "uuid": user_id,
                "content": content
            })

        return users_stats
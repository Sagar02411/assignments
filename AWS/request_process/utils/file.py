import os


class FileUtils:
    
    def get_file_path(self, event):
    
        key, value = list(event.items())[0]
        file = value
        # print(file)
        cur_path = os.getcwd()
        # print(f'cureent : {cur_path}')
        return os.path.join(cur_path, 'data', file)

    def get_file_key(self, event):
        
        # print(f'file key: {list(event.values())[0]}')
        
        return list(event.values())[0]
    

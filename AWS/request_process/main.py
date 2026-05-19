import logging
import time
from request_process.utils.file import FileUtils
from request_process.utils.upload import UploadFile
from request_process.utils.read import Read
from request_process.utils.delete import DeleteFile

logger = logging.getLogger("SimpleLogger")
logger.setLevel('INFO')

class Process:

    def __init__(self, event):
        
        self.event = event
        self.file = FileUtils()
        self.uploader = UploadFile()
        self.reader = Read()
        self.deleter = DeleteFile()

    def run(self):
        
        try:
            
            filename = self.file.get_file_path(self.event)
            print(f'filename: {filename}')
            
            file_key = self.file.get_file_key(self.event)
            print(f'filekey: {file_key}')

            self.uploader.upload(filename, file_key)
            logger.info(f'uploaded')
        
        except Exception as e:
            logger.error(f"error in Uploading(main): {str(e)}")
            
        try:
            # self.reader.read_file(file_key)
            logger.info(f'reading')
            dataframe = self.reader.read_file(file_key)
            logger.info(dataframe.head(3))
            del dataframe
            time.sleep(2)

        except Exception as e:
            logger.error(f"error in Reading(main): {str(e)}")
            
        try :
            self.deleter.delete_file(file_key)
            logger.info(f'Deleted')

        except Exception as e:
            logger.error(f"error in Deleting(main): {str(e)}")

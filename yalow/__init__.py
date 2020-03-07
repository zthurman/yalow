import os
import logging


class Yalow:
    def __init__(self, root_path, project='Yalow', level=logging.DEBUG, file_write_mode='w'):
        if not os.path.exists(root_path / 'log'):
            os.makedirs(root_path / 'log')
        self.log_filename = root_path/f'log/{project}.log'
        self.logger = logging.getLogger(project)
        self.handler = logging.FileHandler(root_path/self.log_filename, mode=file_write_mode)
        self.formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s')
        self.handler.setFormatter(self.formatter)
        self.logger.addHandler(self.handler)
        self.logger.setLevel(level)
        self.logger.info(f'Logging initialized for project: {project}')

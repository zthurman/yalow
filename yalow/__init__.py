import os
import logging


class Yalow:
    """Yet Another LOgging Wrapper

    This class wraps Python's logging module functionality for the
    generic use case of generating and writing to a shared project
    log file in the 'root_path/log' directory.

    Parameters
    ----------
    root_path : pathlib.Path
        Root path of project.
    project : str
        Name of project.
    level : logging.Logger.level
        Default logging level for events added to log.
    file_write_mode : str
        Mode for writing log file, 'w' for overwrite, 'a' for append.
        Default behavior is overwrite.

    Attributes
    ----------
    log_filename : pathlib.Path
        Path for generated log file for project.
    logger : logging.Logger
        Project shared logger object.
    handler : logging.FileHandler
        Responsible for writing the project log to file.
    formatter : logging.Formatter
        Responsible for formatting project log file output.
    """
    def __init__(self, root_path, project='Yalow', level=logging.DEBUG, file_write_mode='w'):
        if not os.path.exists(root_path / 'log'):
            os.makedirs(root_path / 'log')
        self.log_filepath = root_path/f'log/{project}.log'
        self.logger = logging.getLogger(project)
        self.handler = logging.FileHandler(root_path/self.log_filepath, mode=file_write_mode)
        self.formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s')
        self.handler.setFormatter(self.formatter)
        self.logger.addHandler(self.handler)
        self.logger.setLevel(level)
        self.logger.info(f'Logging initialized for project: {project}')

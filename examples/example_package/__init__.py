import logging

module_logger = logging.getLogger('logalog.example_package')


def super_mega_ukulele():
    module_logger.error(f'And its minion is HUGE!')

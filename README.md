
# yalow

## Yet Another LOgging Wrapper

[![Documentation Status](https://readthedocs.org/projects/yalow/badge/?version=latest)](https://yalow.readthedocs.io/en/latest/?badge=latest)
![Python package](https://github.com/zthurman/yalow/workflows/Python%20package/badge.svg)

#### Overview

This package provides a generic wrapper for Python's [logging](https://docs.python.org/3.8/library/logging.html)
module. A log directory is created in the project root directory. The log generated by yalow is intended for use
in situations where you need a single project log that all of the packages in your project write to.

#### Installation

    pip install yalow

#### How Does Do

Get the root path of your project in whatever way you would like. Once that's accomplished
provide it to Yalow along with your project name:

    from yalow import Yalow
    logger = Yalow(root_path=I_AM_GROOT, project_name='logalog').logger


Example log output format:

    2020-03-06 21:16:13,495 - logalog - INFO: Logging initialized for project: logalog
    2020-03-06 21:16:13,495 - logalog - INFO: IT'S ALIVE!!!!!
    2020-03-06 21:16:13,496 - logalog.example_package - ERROR: And its minion is HUGE!

Refer to examples for usage details.

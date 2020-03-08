# yalow

## Yet Another LOgging Wrapper

#### Overview
This package provides a generic wrapper for Python's logging module. The log generated
by yalow is intended for use in situations where you need a single project log that all 
packages in your project write to.

#### How Does Do
Get the root path of your project in whatever way you would like then provide it to Yalow
along with your project name:

    from yalow import Yalow
    logger = Yalow(root_path=I_AM_GROOT, project='logalog').logger

Example log output format:

    2020-03-06 21:16:13,495 - logalog - INFO: Logging initialized for project: logalog
    2020-03-06 21:16:13,495 - logalog - INFO: IT'S ALIVE!!!!!
    2020-03-06 21:16:13,496 - logalog.example_package - ERROR: And its minion is HUGE!
Refer to examples directory for usage details.

#### TODO
* Docs
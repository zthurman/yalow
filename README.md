# yalow

## Yet Another Logging Wrapper

#### Overview
This library provides a generic wrapper for the Python logging package. The log generated
is intended for use in situations where you need a single project log that all packages 
in your project write to.

#### How Does Do
Get the root path of your project in whatever way you would like then provide it to Yalow
along with your project name:

    from yalow import Yalow
    logger = Yalow(root_path=I_AM_GROOT, project='logalog').logger

Example log output format:

    2020-03-06 21:16:13,495 - logalog - INFO: Logging initialized for project: logalog
    2020-03-06 21:16:13,495 - logalog - INFO: IT'S ALIVE!!!!!
    2020-03-06 21:16:13,496 - logalog.example_package - ERROR: And its minion is HUGE!
Refer to examples repo directory for all the not so nitty gritty details.

#### Roadmap
* Unit tests
* Docs
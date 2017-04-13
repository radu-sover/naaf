# Not Another Automation Framework #



**Stack**
- Gherkin language
- Behave framework
- Page Objects pattern
- Selenium WebDriver
- Protractor ported to python


**Setup**
***Local Run***
- virtualenv created for vagrant machine can not be used by local (`rm -r virtualenv`)
- creates the environment and install requirements: `. setup.sh`
- if running local on mac, do a: `brew install chromedriver`

***Headless Run***
- using vagrant
- virtualenv created locally can not be used by VM (`rm -r virtualenv`)
- `vagrant up`
- `vagrant ssh`
- change the `behave.ini` and set `browser.headless = True`


**Usage**
- check that code meets coding standards: `make check`
- run the tests: `make run`


**Reporting and Visualization**
- See the graph of features: `docker run -t -p 8000:80 -v /Users/rsover/work/personal/tsf/app_name/:/my-share jenmud/behave-graph`
- behave reports in junit (see `behave.ini`) format the test execution - can be used by CI reporting


**Framework**:
- Using a fluent API
- Defined generic steps for most common operations

***Page***
- Found in `naaf.base.py`
- Provides a `Page` base class that has wrappers for common operations with selenium
- One can override the `url` where the page is found allowing `navigation` and `at` assert
- `at` assert can also be made by a locator overriding the `at_check_locator` 
- Advanced checks can be made overriding the `at_check_element` or `at`

***Steps***
- Found in `naaf.page_steps.py` (it should be here but had some issues resolving the classNames)
- actually now is in `app_name.steps.generic_steps.py` - temp place

***Step parameter converters*** 
- Found in `naaf.converters.py`
- The framework defines a set of converters for the steps parameters

***Infrastructure***
- Found in `naaf.infrastructure.py`
- Base setup of the behave

***Utils***
- Found in `naaf.utils.py`
- Utilities classes provided for miscellaneous operations
- Defines a Screenshot class

**License**
MIT
https://choosealicense.com/licenses/mit/

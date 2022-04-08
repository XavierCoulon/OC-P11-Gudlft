OC - Gudlft - Tests
=

<u>Openclassrooms - DA Python - Project 11 :</u>

## 1. <u>Context</u> :

- Purpose: from an existing project, to fix some identified bugs, to implement some tests and features.
- Initial Github repository: [OC - Python Testing](https://github.com/OpenClassrooms-Student-Center/Python_Testing).
- Technologies: Python, Flask, pytest

<u>Warning</u>: the goal of the project was not to review all the initial code and structure of the project, but to focus on the testing part. So improvements can easily be spotted.

## 2. <u> Documentation</u>

- Initial OC requirements available in the folder [doc](../doc).


## 3. <u>Installation</u>

The app does not include a DB but handle datas from JSON files (mandatory).<br>
The os.environ["ENV"]= TEST enables to test the app from JSON test files stored in the folder [tests](tests/) (clubs_dataset & competitions_dataset)

```bash
git clone https://github.com/XavierCoulon/OC-P11-Gudlft.git
cd P11_Gudlft
virtualenv .
source bin/activate
pip install -r requirements.txt
```
To execute on the test env:
```bash
export FLASK_NAME=server
ENV=TEST flask run
```

App available on http://127.0.0.1:5000/

## 3. <u>Tests</u>

You will find in the folder [tests](tests/): units, integration, functional and performance tests, using [Pytest](https://docs.pytest.org/en/7.1.x/contents.html), [Selenium](https://www.selenium.dev/documentation/) and [Locust](http://docs.locust.io/en/stable/).

To run all the tests, from the folder "Python_Testing".
<br><u>WARNING</u>: once run, Selenium tests will need a reboot of the local server to pass (to be improved).
```bash
pytest -v
```

To run tests coverage and generate [HTML report](htmlcov): 
```bash
pytest --cov=. --cov-report html
```

To run performance tests: 
```bash
cd test/performance
locust
```
Locust web interface available on http://0.0.0.0:8089 

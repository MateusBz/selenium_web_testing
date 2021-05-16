# Selenium Web Testing

 This repository contains my test cases and scripts for learning selenium in automated tests.





## General Info
 All tests were carried out on the 'The Internet ver. 0.58.0'.

In each folder there are test cases in xml format to be imported into TestLink and test cases in xls format.

#### List of test cases:
- test_dropdown_list
- test_upload_page
- test_login_page


## Technologies
- Python
- Selenium Grid
- Docker
- Pytest

## Setup
1. Clone repository
```
https://github.com/MateusBz/selenium_web_testing
```
2. Install pipenv if you don't have one
```
pip install pipenv
```
3. Install dependencies
```
pipenv install
```
4. Activate a virtual environment
```
pipenv shell
```
5. Run docker-compose
```
docker-compose up -d
```
6. Run all tests
```
pytest -v
```
or

7. Run selected test
```
pytest -v test_(test name from list)
```

<h2 align="center">Test Automation Project for <a href="https://www.automationexercise.com/">AutomationExercise.com</a></h2>
___
<p align="center">
<a><img src="https://img.shields.io/website-up-down-green-red/http/https://prog420.github.io/AutomationExercise.svg"></a>
<a><img src="https://img.shields.io/badge/python-3.8%20|%203.9%20|%203.10%20|%203.11-blue"></a>
<a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>
</p>

---
#### 1. Local Machine:

##### Start new test run:
    pytest -vs --alluredir=allure-reports

##### Check allure results:
    allure serve allure-reports

##### CLI Arguments:
1. `--headless` - run tests without loading the browser's UI.
2. `--use_local_driver` - use local driver without downloading it by `webdriver-manager` if added.
3. `--driver-path` - path to the driver (`external_files/drivers/chromedriver.exe` by default).
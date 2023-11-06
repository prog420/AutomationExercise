import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from fixtures.user_manager import user_manager


def pytest_addoption(parser: pytest.Parser):
    parser.addoption(
        "--browser", default="chrome"
    )
    parser.addoption(
        "--headless", action="store_true"
    )
    parser.addoption(
        "--use_local_driver", action="store_true"
    )
    parser.addoption(
        "--driver_path", default="external_files/drivers/chromedriver.exe"
    )


@pytest.fixture(scope="session")
def config(request: pytest.FixtureRequest):
    browser: str = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")
    use_local_driver = request.config.getoption("--use_local_driver")
    exec_path = request.config.getoption("--driver_path")
    options = None

    if browser.lower() == "chrome":
        options = ChromeOptions()
    elif browser.lower() == "firefox":
        options = FirefoxOptions()
    else:
        raise ValueError(f"Browser {browser} is not supported!")

    options.add_argument("--window-size=1920,1080")
    options.add_extension(
        "external_files/extensions/uBlock0_1.52.0.chromium.zip"
    )

    # Set page load strategy to eager to speed up long waits
    # options.set_capability("pageLoadStrategy", "normal")
    options.set_capability("pageLoadStrategy", "eager")
    # options.set_capability("pageLoadStrategy", "none")

    if headless:
        options.add_argument("-headless")

    return {
        "driver": driver,
        "browser": browser,
        "headless": headless,
        "options": options,
        "use_local_driver": use_local_driver,
        "driver_path": exec_path,
    }


@pytest.fixture(scope="function")
def driver(config):
    driver = None
    browser = config.get("browser")
    options = config.get("options")
    use_local_driver = config.get("use_local_driver")
    exec_path = config.get("driver_path")

    if browser == "chrome":
        if use_local_driver:
            driver = webdriver.Chrome(
                options=options, service=ChromeService(
                    executable_path=exec_path)
            )
        else:
            driver = webdriver.Chrome(
                options=options, service=ChromeService(
                    ChromeDriverManager().install())
            )
    elif browser == "firefox":
        if use_local_driver:
            driver = webdriver.Firefox(
                options=options, service=FirefoxService(
                    executable_path=exec_path)
            )
        else:
            driver = webdriver.Firefox(
                options=options, service=FirefoxService(
                    GeckoDriverManager().install())
            )

    yield driver
    driver.quit()

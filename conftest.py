import pytest

from functions import log


def pytest_addoption(parser):
    parser.addoption("--log", action="store", default="log.txt",
                     help="file name for log")


@pytest.fixture(scope='session')
def file_name(request):
    path = request.config.getoption("log")
    yield path


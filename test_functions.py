import pytest as pytest

from constant_test_cases import VALID_EMAIL_CORRECT_DATA_CASES, VALID_EMAIL_INCORRECT_DATA_CASES
from functions import valid_email, log


class TestValidEmail:
    @pytest.mark.parametrize('test_case', VALID_EMAIL_CORRECT_DATA_CASES)
    def test_valid_email_correct_data(self, test_case, file_name):
        test_input = test_case.get("test_input")
        expected = test_case.get("expected")
        actual = valid_email(test_input)
        assert actual == expected, log(file_name, f"Test with {test_input} not passed \n")
        log(file_name, f"Test with {test_input} passed \n")

    @pytest.mark.parametrize('test_case', VALID_EMAIL_INCORRECT_DATA_CASES)
    def test_valid_email_incorrect_data(self, test_case, file_name):
        test_input = test_case.get("test_input")
        expected = test_case.get("expected")
        actual = valid_email(test_input)
        assert actual == expected, log(file_name, f"Test with {test_input} not passed \n")
        log(file_name, f"Test with {test_input} passed \n")

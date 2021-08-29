VALID_EMAIL_CORRECT_DATA_CASES = [
    {"test_input": "test@test.ru",
     "expected": True},
    {"test_input": "w@w.com",
     "expected": True},
    {"test_input": "123QWE@mmm.mmm",
     "expected": True}]
VALID_EMAIL_INCORRECT_DATA_CASES = [
    {"test_input": "test@test.",
     "expected": False},
    {"test_input": "'w@",
     "expected": False},
    {"test_input": "@tt",
     "expected": False}]

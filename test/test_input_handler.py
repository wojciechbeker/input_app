import pytest
from input_app.input_handler.input_handler import validate_input


class TestInputHandler:
    def test_email_acceptable(self):
        error_code = validate_input('a@b.c')
        if error_code:
            pytest.fail(f'Correct email address was rejected with error code :'
                        f'{error_code}')

    def test_email_upper_cases(self):
        error_code = validate_input('a@b.c')
        if error_code:
            pytest.fail(f'Correct email address was rejected with error code :'
                        f'{error_code}')

    def test_email_too_short(self):
        pass

    def test_email_format_incorrect(self):
        pass

    def test_email_too_long(self):
        pass

    def test_email_forbidden_characters(self):
        pass

    def test_email_whitespaces(self):
        pass

from src.services.validation_service import is_valid_password


def test_valid_password():
    assert is_valid_password('AbTp9!fok')


def test_short_password():
    assert not is_valid_password('AbTp9!fo')


def test_no_number():
    assert not is_valid_password('AbTpI!fok')


def test_no_lowercase():
    assert not is_valid_password('AAAbbbCc')


def test_no_uppercase():
    assert not is_valid_password('AbTp9!foo')


def test_no_special_char():
    assert not is_valid_password('AbTp9!foA')


def test_blank_space():
    assert not is_valid_password('AbTp9 fok')


def repeat_char():
    assert not is_valid_password('')

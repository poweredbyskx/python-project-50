import pytest
from hexlet_code.scripts.gendiff import generate_diff

def test_generate_diff_json():
    expected_output = """{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}"""
    result = generate_diff(
        'hexlet_code/scripts/file1.json',
        'hexlet_code/scripts/file2.json'
    )
    assert result == expected_output

def test_generate_diff_yaml():
    expected_output = """{
  - follow: false
  + follow: true
    host: hexlet.io
  - timeout: 50
  + timeout: 20
  + verbose: true
}"""
    result = generate_diff(
        'hexlet_code/scripts/file1.yml',
        'hexlet_code/scripts/file2.yml'
    )
    assert result == expected_output

def test_generate_diff_nonexistent_file():
    with pytest.raises(FileNotFoundError):
        generate_diff('nonexistent1.json', 'nonexistent2.json')

def test_generate_diff_invalid_format():
    with pytest.raises(ValueError):
        generate_diff('hexlet_code/scripts/invalid_file.txt', 'hexlet_code/scripts/file2.json')

def test_generate_diff_same_content():
    expected_output = """{
    follow: false
    host: hexlet.io
    proxy: 123.234.53.22
    timeout: 50
}"""
    result = generate_diff(
        'hexlet_code/scripts/file1.json',
        'hexlet_code/scripts/file1.json'
    )
    assert result == expected_output

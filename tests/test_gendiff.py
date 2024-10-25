from hexlet_code.scripts.gendiff import generate_diff

def test_generate_diff():
    expected_output = """{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}"""
    result = generate_diff('hexlet_code/scripts/file1.json', 'hexlet_code/scripts/file2.json')
    assert result == expected_output

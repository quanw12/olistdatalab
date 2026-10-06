# A pytest version to practise
Install the extension requirements first. Create test_normalize.py next to exercise.py with your own test cases.

Syntax demonstration using an independent toy function:
~~~python
import pytest

def normalize(text):
    return text.strip().lower()

@pytest.mark.parametrize("text, expected", [(" A ", "a"), ("Hue", "hue")])
def test_normalize(text, expected):
    assert normalize(text) == expected

def test_file_fixture(tmp_path):
    path = tmp_path / "example.txt"
    path.write_text("hello", encoding="utf-8")
    assert path.read_text(encoding="utf-8") == "hello"
~~~
Run with the extension interpreter:
~~~powershell
& "C:\DE Courses\.venv-python-de\Scripts\python.exe" -m pytest .\test_normalize.py -q
~~~
tmp_path is supplied by pytest and differs for each test. Add your error cases using with pytest.raises(ValueError):. This toy normalizer is only a syntax demonstration; your main exercise must test the stricter callable contract.
[Reference](https://docs.pytest.org/en/stable/how-to/parametrize.html).

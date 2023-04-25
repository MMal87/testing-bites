from lib.string_builder import *
def test_returns_new_string_build():
    string_builder = StringBuilder()
    string_builder.add("horse")
    string_builder.size()
    result = string_builder.output()
    assert result == "horse"
def test_return_extra_spaces():
    string_builder = StringBuilder()
    string_builder.add(" horse ")
    string_builder.size()
    result = string_builder.output()
    assert result == " horse "
def test_return_no_string():
    string_builder = StringBuilder()
    string_builder.add(" ")
    string_builder.size()
    result = string_builder.output()
    assert result == " "
def test_return_no_space():
    string_builder = StringBuilder()
    string_builder.add("")
    string_builder.size()
    result = string_builder.output()
    assert result == ""








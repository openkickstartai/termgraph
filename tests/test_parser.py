"""Tests for input parser."""
import json
import tempfile
import os
from termgraph.parser import parse_input

def test_parse_json_list():
    with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as f:
        json.dump([10, 20, 30], f)
        f.flush()
        data = parse_input(f.name)
    os.unlink(f.name)
    assert len(data) == 3
    assert data[0][1] == 10.0

def test_parse_json_dict():
    with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as f:
        json.dump({"foo": 10, "bar": 20}, f)
        f.flush()
        data = parse_input(f.name)
    os.unlink(f.name)
    assert len(data) == 2

def test_parse_csv():
    with tempfile.NamedTemporaryFile(mode="w", suffix=".csv", delete=False) as f:
        f.write("apples,30\noranges,50\nbananas,20\n")
        f.flush()
        data = parse_input(f.name)
    os.unlink(f.name)
    assert len(data) == 3
    assert data[0] == ("apples", 30.0)

def test_parse_comma_values():
    with tempfile.NamedTemporaryFile(mode="w", suffix=".txt", delete=False) as f:
        f.write("10,20,30,40")
        f.flush()
        data = parse_input(f.name)
    os.unlink(f.name)
    assert len(data) == 4

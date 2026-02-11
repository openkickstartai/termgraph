"""Tests for chart rendering."""
from termgraph.charts import bar_chart, sparkline

def test_bar_chart_basic():
    data = [("a", 10), ("b", 20), ("c", 30)]
    output = bar_chart(data, width=30, color=False)
    assert "a" in output
    assert "b" in output
    assert "c" in output
    lines = output.strip().split("\n")
    assert len(lines) == 3

def test_bar_chart_empty():
    assert bar_chart([]) == "No data"

def test_bar_chart_zero():
    data = [("x", 0), ("y", 0)]
    output = bar_chart(data, color=False)
    assert "x" in output

def test_sparkline():
    result = sparkline([1, 3, 5, 2, 4])
    assert len(result) == 5
    assert all(c in " \u2581\u2582\u2583\u2584\u2585\u2586\u2587\u2588" for c in result)

def test_sparkline_empty():
    assert sparkline([]) == ""

def test_sparkline_constant():
    result = sparkline([5, 5, 5])
    assert len(result) == 3

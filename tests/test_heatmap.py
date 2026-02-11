"""Tests for heatmap chart."""
from termgraph.heatmap import heatmap

def test_heatmap_basic():
    data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    output = heatmap(data, color=False)
    lines = output.strip().split("\n")
    assert len(lines) == 3
    assert len(lines[0]) == 3

def test_heatmap_empty():
    assert heatmap([]) == "No data"
    assert heatmap([[]]) == "No data"

def test_heatmap_constant():
    data = [[5, 5], [5, 5]]
    output = heatmap(data, color=False)
    assert len(output.strip().split("\n")) == 2

def test_heatmap_single():
    data = [[42]]
    output = heatmap(data, color=False)
    assert len(output.strip()) == 1

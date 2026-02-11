"""Parse input data from various formats."""
import sys
import json
import csv
import io
from typing import List, Tuple


def parse_input(source: str) -> List[Tuple[str, float]]:
    if source == "-":
        text = sys.stdin.read().strip()
    else:
        with open(source) as f:
            text = f.read().strip()
    # Try JSON
    try:
        data = json.loads(text)
        if isinstance(data, list):
            return [(str(i), float(v)) for i, v in enumerate(data)]
        if isinstance(data, dict):
            return [(k, float(v)) for k, v in data.items()]
    except (json.JSONDecodeError, ValueError, TypeError):
        pass
    # Try CSV
    try:
        reader = csv.reader(io.StringIO(text))
        rows = list(reader)
        if rows:
            if len(rows[0]) == 1:
                return [(str(i), float(rows[i][0])) for i in range(len(rows))]
            return [(row[0], float(row[1])) for row in rows if len(row) >= 2]
    except (ValueError, IndexError):
        pass
    # Try comma-separated values
    try:
        vals = [float(x.strip()) for x in text.split(",")]
        return [(str(i), v) for i, v in enumerate(vals)]
    except ValueError:
        pass
    return []

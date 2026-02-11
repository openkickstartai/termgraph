"""Heatmap chart rendering."""
from typing import List

HEAT_CHARS = " ░▒▓█"
HEAT_COLORS = [
    "\033[34m",  # blue (cold)
    "\033[36m",  # cyan
    "\033[32m",  # green
    "\033[33m",  # yellow
    "\033[31m",  # red (hot)
]
RESET = "\033[0m"


def heatmap(data: List[List[float]], color: bool = True) -> str:
    if not data or not data[0]:
        return "No data"
    flat = [v for row in data for v in row]
    mn, mx = min(flat), max(flat)
    rng = mx - mn if mx != mn else 1
    lines = []
    for row in data:
        cells = []
        for v in row:
            idx = min(int((v - mn) / rng * 4), 4)
            char = HEAT_CHARS[idx]
            if color:
                cells.append(f"{HEAT_COLORS[idx]}{char}{RESET}")
            else:
                cells.append(char)
        lines.append("".join(cells))
    return "\n".join(lines)

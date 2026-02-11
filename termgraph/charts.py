"""Chart rendering functions."""
from typing import List, Tuple

BLOCKS = " \u2581\u2582\u2583\u2584\u2585\u2586\u2587\u2588"
COLORS = ["\033[32m", "\033[33m", "\033[34m", "\033[35m", "\033[36m"]
RESET = "\033[0m"


def bar_chart(data: List[Tuple[str, float]], width: int = 40, color: bool = True) -> str:
    if not data:
        return "No data"
    max_val = max(v for _, v in data)
    if max_val == 0:
        max_val = 1
    lines = []
    for i, (label, value) in enumerate(data):
        bar_len = int(value / max_val * width)
        bar = "\u2588" * bar_len
        if color:
            c = COLORS[i % len(COLORS)]
            bar = f"{c}{bar}{RESET}"
        lines.append(f"{label:>15s} | {bar} {value:.1f}")
    return "\n".join(lines)


def sparkline(values: List[float]) -> str:
    if not values:
        return ""
    mn, mx = min(values), max(values)
    rng = mx - mn if mx != mn else 1
    return "".join(BLOCKS[min(int((v - mn) / rng * 7) + 1, 8)] for v in values)

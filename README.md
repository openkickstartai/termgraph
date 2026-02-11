# termgraph

Beautiful charts in your terminal. Bar charts, sparklines, heatmaps.

## Install

```bash
pip install termgraph
```

## Usage

```bash
echo '10,20,30,40' | termgraph bar
termgraph bar data.csv --color
termgraph spark data.json --key values
```

## Testing

```bash
pip install -e .
pytest -v
```

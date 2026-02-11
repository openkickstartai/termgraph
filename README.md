# termgraph

Beautiful charts in your terminal. Bar charts, sparklines, heatmaps.

## Install from source

```bash
git clone https://github.com/openkickstartai/termgraph.git
cd termgraph
pip install -e .
```

## Usage

```bash
echo '10,20,30' | termgraph bar
termgraph bar data.csv --color
termgraph spark data.json
```

## Testing

```bash
pip install pytest
pytest -v
```

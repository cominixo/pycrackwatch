# pycrackwatch

A simple wrapper for the crackwatch API (https://crackwatch.com/api)


## Installing

To install pycrackwatch just run

```
pip install pycrackwatch
```

## Testing

The tests are located inside the tests folder, to run them with pytest use

```
py.test tests
```

## Usage

```python
>>> import pycrackwatch
>>> games = pycrackwatch.getGames()
>>> cracks = pycrackwatch.getCracks()
>>> games[0].title
'F1 2018'
>>> cracks[0].title
'F1.2018-CODEX'
```

To see more properties check models.py on the pycrackwatch folder.

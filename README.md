POMM - Planetary Orbital Mosaicking and Mapping

### Dev Install:

1. `git clone {github repo url}`
1. `python3 -m pip install -r requirements.txt`

### Dev Run:

3. `python3 pomm-ui.py`

### Bundling:

1. `pyinstaller --onefile --windowed --collect-all tkinterweb pomm.py`
1. Copy `src/assets` into `/dist/src` (need to test)

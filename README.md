POMM - Planetary Orbital Mosaicking and Mapping

### Dev Install:

1. `git clone https://github.jpl.nasa.gov/tsoliman/POMM`
1. `python3 -m pip install -r requirements.txt`

### Dev Run:

3. `python3 pomm.py`

### Bundling:

1. `pyinstaller --onefile --windowed --collect-all tkinterweb pomm.py`
1. Copy `/assets` into `/dist`

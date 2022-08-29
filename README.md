POMM - Planetary Orbital Mosaicking and Mapping

### Dev Install:

`git clone https://github.jpl.nasa.gov/tsoliman/POMM`
`python3 -m pip install -r requirements.txt`

### Dev Run:

`python3 pomm.py`

### Bundling:

#### Windows

1. `pyinstaller --onefile --windowed --collect-all tkinterweb pomm.py`
1. Copy `/assets` into `/dist`

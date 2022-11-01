# POMM - Planetary Orbital Mosaicking and Mapping

POMM is a set of workstation tools supporting the automation of planetary orbital mosaicking and mapping requirements. POMM is designed to enable the planetary scientist, student, and enthusiast with easy-to-use tools that perform the basic functions needed for most satellite mapping and analysis studies. These capabilities include: 1) The ability to co-register (stack) multiple images over the same location for time series analysis; 2) Mosaic multiple adjacent images to create large-area base map coverages and regional overviews; and 3) Create map-projected orbital satellite images from selected sensors and bands provided in raw PDS format.

POMM (v1) supports the co-registration and mosaicking of (existing) single-band map-projected orbital image of Mars, Earth, and the Earth’s Moon (excluding polar areas). However, if map-projected images are not available, POMM can create them from their raw/EDR PDS format for the following mission sensors:

- Mars Reconnaissance Orbiter (MRO) Context Camera (CTX)
- MRO High Resolution Imaging Science Experiment (HiRISE) Red-band
- Mars Express (MEX) High Resolution Stereo Camera (HRSC) “nd2” format
- Lunar Reconnaissance Orbiter (LRO) Narrow Angle Camera (NAC "LE/RE" format)
- LRO Wide Angle Camera (WAC "CC" format) COLOR VIS bands

POMM was funded by the Advanced Multi-Mission Operations System (AMMOS) which supports NASA robotic missions with tools for planetary exploration, including earth and space science. All available AMMOS tools (and how to obtain them, including POMM) are described in the online AMMOS catalog . AMMOS is managed by the Multi-Mission Ground Systems (MGSS), a division of the NASA Interplanetary Network Directorate.

November 2022  
Version: 1.0

## Development

### Dev Install:

1. `git clone {github repo url}`
1. `python3 -m pip install -r requirements.txt`

### Dev Run:

1. `python3 pomm-ui.py`

### Bundling:

**May be unnecessary**

1. `pyinstaller --onefile --windowed --collect-all tkinterweb pomm.py`
1. Copy `src/assets` into `/dist/src` (need to test)

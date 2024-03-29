<!-- Header block for project -->
<hr>

<div align="center">

<!--[INSERT YOUR LOGO IMAGE HERE (IF APPLICABLE)] -->
<!-- ☝️ Replace with your logo (if applicable) via ![](https://uri-to-your-logo-image) ☝️ -->
<!-- ☝️ If you see logo rendering errors, make sure you're not using indentation, or try an HTML IMG tag -->

<h1 align="center">AFIDS-POMM</h1>
<!-- ☝️ Replace with your repo name ☝️ -->

</div>

<pre align="center">Planetary Orbital Mosaicking and Mapping (POMM) is a set of workstation tools supporting the
automation of planetary orbital mosaicking and mapping requirements.</pre>
<!-- ☝️ Replace with a single sentence describing the purpose of your repo / proj ☝️ -->

<!-- Header block for project -->

<!--[INSERT YOUR BADGES HERE (SEE: https://shields.io)] [![SLIM](https://img.shields.io/badge/Best%20Practices%20from-SLIM-blue)](https://nasa-ammos.github.io/slim/) -->
<!-- ☝️ Add badges via: https://shields.io e.g. ![](https://img.shields.io/github/your_chosen_action/your_org/your_repo) ☝️ -->
POMM is designed to provide the planetary scientist, student, and enthusiast with easy-to-use tools that perform
basic functions necessary for most satellite mapping and analysis studies. 
<br>
<div align="center">
<img width="300" alt="image" src="https://user-images.githubusercontent.com/28875376/224439303-41697f09-3e90-4d7d-9584-9580822558a0.png">
</div>
<br>

POMM was funded by the <a href="https://ammos.nasa.gov/">Advanced Multi-Mission Operations System (AMMOS)</a> which supports NASA robotic missions with tools for planetary exploration, including Earth and space science. Available AMMOS tools are described in the online AMMOS catalog. AMMOS is managed by the Multi-Mission Ground Systems (MGSS), a division of the NASA Interplanetary Network Directorate. 

<a href="https://github.com/nasa-ammos/" rel="NASA AMMOS">![NASA Ammos](https://avatars.githubusercontent.com/u/37851411?s=200&v=4)</a>

<!-- ☝️ Replace with a more detailed description of your repository, including why it was made and whom its intended for.  ☝️ -->

<!-- example links>
[Website](INSERT WEBSITE LINK HERE) | [Docs/Wiki](INSERT DOCS/WIKI SITE LINK HERE) | [Discussion Board](INSERT DISCUSSION BOARD LINK HERE) | [Issue Tracker](INSERT ISSUE TRACKER LINK HERE)
-->

## Features

* The ability to co-register (stack) multiple images over the same location for time series analysis
* Mosaic multiple adjacent images to create large-area base map coverages and regional overviews
* Create map-projected orbital satellite images from selected sensors and bands provided in raw PDS format

<br>
<div align="center">
<img width="350" alt="image" src="https://user-images.githubusercontent.com/28875376/224439896-5cf4f2b0-3eea-4d74-8cf8-6dc3a05c91c2.png">
<img width="400" alt="image" src="https://user-images.githubusercontent.com/28875376/224438931-289ce2ee-d351-4377-b65a-4d9e35f9df82.png">
<img width="250" alt="image" src="https://user-images.githubusercontent.com/28875376/224439939-adbdf405-fa84-41bf-a124-5b0285a08251.png">
</div>
<br>

POMM is a set of workstation tools supporting the automation of planetary orbital mosaicking and mapping requirements. POMM is designed to enable the planetary scientist, student, and enthusiast with easy-to-use tools that perform the basic functions needed for most satellite mapping and analysis studies. These capabilities include: 1) The ability to co-register (stack) multiple images over the same location for time series analysis; 2) Mosaic multiple adjacent images to create large-area base map coverages and regional overviews; and 3) Create map-projected orbital satellite images from selected sensors and bands provided in raw PDS format.

POMM (v1) supports the co-registration and mosaicking of (existing) single-band map-projected
orbital images of Mars, Earth, and the Earth’s Moon (excluding polar areas). However, if mapprojected
images are not available, POMM can create them from their raw/EDR PDS format for
the following mission sensors:

  - Mars Reconnaissance Orbiter (MRO) Context Camera (CTX);
  - MRO High Resolution Imaging Science Experiment (HiRISE) Red-band;
  - Mars Express (MEX) High Resolution Stereo Camera (HRSC) “level-2” format;
  - Lunar Reconnaissance Orbiter (LRO) Narrow Angle Camera (NAC “LE/RE” format); and
  - LRO Wide Angle Camera (WAC “CC” format) COLOR VIS bands

POMM was funded by the Advanced Multi-Mission Operations System (AMMOS) which supports NASA robotic missions with tools for planetary exploration, including earth and space science. All available AMMOS tools (and how to obtain them, including POMM) are described in the online AMMOS catalog . AMMOS is managed by the Multi-Mission Ground Systems (MGSS), a division of the NASA Interplanetary Network Directorate.

<!-- ☝️ Replace with a bullet-point list of your features ☝️ -->

## Contents

* [Quick Start](#quick-start)
* [Changelog](#changelog)
* [FAQ](#frequently-asked-questions-faq)
* [Support](#support)

## Quick Start

This guide below provides a quick way to get started with AFIDS-POMM. Please see the [AFIDS-POMM User Guide](./documentation/POMM_AFIDS_User_Guide_v1.pdf) for a more comprehensive guide.

<!-- ☝️ Replace with a numbered list of your requirements, including hardware if applicable ☝️ -->

### Setup Instructions

POMM is distributed as a Docker image, which can be used to run the POMM
software. The docker image is available at the [releases page](https://github.com/NASA-AMMOS/AFIDS-POMM/releases).

#### POMM Ancillary Data Download

The POMM mosaicking and co-registration tools have all their required ancillary data built-in to the docker. However, the map projection tools require a planetary DEM (elevation/height) model and Sensor-base SPICE Kernel information, which must be obtained from external sources.

#### DEM Data

Global Mars and Lunar/Moon elevation models can be downloaded from the following locations. Because these are large files, be sure to include available restart options, for example, use “—continue” with wget, or “-C” with curl.

- [Global MARS DEM](https://planetarymaps.usgs.gov/mosaic/Mars/HRSC_MOLA_Blend/Mars_HRSC_MOLA_BlendDEM_Global_200mp_v2.tif) (11G)

- [Global Lunar DEM](https://planetarymaps.usgs.gov/mosaic/Lunar_LRO_LOLA_Global_LDEM_118m_Mar2014.tif) (8G)

- [Higher resolution Lunar DEM](https://planetarymaps.usgs.gov/mosaic/LolaKaguya_Topo/Lunar_LRO_LOLAKaguya_DEMmerge_60N60S_512ppd.tif) (22G)

The files are downloaded in “bigtiff” format, which should be converted to VICAR format for ease of use:

    gdal_translate -of VICAR <input>.tif <output>.vic

#### ISIS data

POMM makes use of the [ISIS](https://isis.astrogeology.usgs.gov/7.0.0/UserStart/index.html) software. The software is included in the POMM Docker image,
but because of its size the support data for ISIS needs to be downloaded
separately.

There are two sets of [ISIS data](https://github.com/DOI-USGS/ISIS3#the-isis-data-area). One set is the specific data needed to process an image (e.g., the
specific [NAIF](https://naif.jpl.nasa.gov/naif/) kernels to support the
time range of the data), POMM automatically downloads this as needed. There
is also a set of "core" data needed for all ISIS processing, this needs to
be downloaded and then provided to the Docker image for its use (e.g., 
as a [Docker volume](https://docs.docker.com/storage/volumes/)).

The ISIS data is downloaded using [Rclone](https://rclone.org), this should
be installed on your system (e.g. install the yum package "rclone" on a
Red Hat system).

The directions for downloading can be found on the 
[ISIS download directions](https://github.com/DOI-USGS/ISIS3#isis-spice-web-service). In addition the file "rclone.conf" should be copied to this directory.
As a convenience, there is a [isis_data_download.sh](isis_data_download.sh) script that can be run to download this data.

    ./isis_data_download.sh <directory to place data>

<!-- ☝️ Replace with a numbered list of how to set up your software prior to running ☝️ -->

### Run Instructions

Please see [Docker Quick Start](./documentation/POMM_Docker_Quick_Start.pdf)
for directions on using the docker image. Also see 
[Docker GUI Appendum](./documentation/POMM_Docker_GUI_Addendum.pdf) for
information on using the GUI app.

<!-- ☝️ Replace with a numbered list of your run instructions, including expected results ☝️ -->

## Changelog

See our <a href="https://github.com/NASA-AMMOS/AFIDS-POMM/releases/">releases page</a> for our versioned releases. 

<!-- ☝️ Replace with links to your changelog and releases page ☝️ -->

## Frequently Asked Questions (FAQ)
Q: When will AFIDS-POMM be available?

A: The first AFIDS-POMM downloadable docker release has been posted in April 2023 and is available now. 

Q: Where can I find the AFIDS POMM source code?

A: We're currently in the process of merging portions of AFIDS into VICAR. When the merging is complete, the AFIDS-POMM source code will be posted in the <a href="https://github.com/NASA-AMMOS/VICAR">VICAR open source repo</a> and will be maintained there going forward. 

## Support
Key points of contact are:

<a href = "mailto: thomas.l.logan@jpl.nasa.gov">Tom Logan</a>

<a href = "mailto: mike.m.smyth@jpl.nasa.gov">Mike Smyth</a> 

<!-- ☝️ Replace with the key individuals who should be contacted for questions ☝️ -->

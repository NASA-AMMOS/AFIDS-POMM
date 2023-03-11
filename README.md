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

POMM (v1) supports the co-registration and mosaicking of (existing) single-band map-projected
orbital images of Mars, Earth, and the Earth’s Moon (excluding polar areas). However, if mapprojected
images are not available, POMM can create them from their raw/EDR PDS format for
the following mission sensors:
  - Mars Reconnaissance Orbiter (MRO) Context Camera (CTX);
  - MRO High Resolution Imaging Science Experiment (HiRISE) Red-band;
  - Mars Express (MEX) High Resolution Stereo Camera (HRSC) “level-2” format;
  - Lunar Reconnaissance Orbiter (LRO) Narrow Angle Camera (NAC “LE/RE” format); and
  - LRO Wide Angle Camera (WAC “CC” format) COLOR VIS bands
  
<!-- ☝️ Replace with a bullet-point list of your features ☝️ -->

## Contents

* [Quick Start](#quick-start)
* [Changelog](#changelog)
* [FAQ](#frequently-asked-questions-faq)
* [Support](#support)

## Quick Start

This guide below provides a quick way to get started with AFIDS-POMM. Please see the <a href="https://github.com/NASA-AMMOS/AFIDS-POMM/tree/main/documentation">AFIDS-POMM User Guide</a> for a more comprehensive guide.

### Requirements

* Stay tuned. Will be posted in May 2023 when AFIDS-POMM docker image download will be available.
  
<!-- ☝️ Replace with a numbered list of your requirements, including hardware if applicable ☝️ -->

### Setup Instructions

* Stay tuned. Will be posted in May 2023 when AFIDS-POMM docker image download will be available.
   
<!-- ☝️ Replace with a numbered list of how to set up your software prior to running ☝️ -->

### Run Instructions

* Stay tuned. Will be posted in May 2023 when AFIDS-POMM docker image download will be available.

<!-- ☝️ Replace with a numbered list of your run instructions, including expected results ☝️ -->

## Changelog

See our <a href="https://github.com/NASA-AMMOS/AFIDS-POMM/releases/">releases page</a> for our versioned releases. Our first downloadable docker release will be posted in May 2023.

<!-- ☝️ Replace with links to your changelog and releases page ☝️ -->

## Frequently Asked Questions (FAQ)
Q: When will AFIDS-POMM be available?

A: The first AFIDS-POMM downloadable docker release will be available in May 2023 in this repo. This repo is intended to house the docker releases of AFIDS-POMM.


Q: Where can I find the AFIDS POMM source code?

A: We're currently in the process of merging portions of AFIDS into VICAR. When the merging is complete, the AFIDS-POMM source code will be posted in the <a href="https://github.com/NASA-AMMOS/VICAR">VICAR open source repo</a> and will be maintained there going forward. 

## Support
Key points of contact are:

<a href = "mailto: thomas.l.logan@jpl.nasa.gov">Tom Logan</a>

<a href = "mailto: mike.m.smyth@jpl.nasa.gov">Mike Smyth</a> 

<!-- ☝️ Replace with the key individuals who should be contacted for questions ☝️ -->

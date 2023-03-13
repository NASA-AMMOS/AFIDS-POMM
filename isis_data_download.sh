#! /bin/bash
# Script for downloading isis data.

usage()
{
    cat <<EOF
Usage $0 <directory to place data>

This is a short script to download the ISIS data needed for the POMM software.
EOF
}

while getopts “h” OPTION; do
    case $OPTION in
        h)
            usage
            exit 1
            ;;
        ?)
            usage
            exit
            ;;
    esac
done
if [ $# -ne 1 ]; then
    usage
    exit
fi

# Die on error
set -e
set -o pipefail

# Download data
mkdir -p $1
cp rclone.conf $1
rclone --progress --config rclone.conf sync base_usgs: $1/base
rclone --progress --config rclone.conf --exclude='kernels/**' sync mex_usgs: $1/mex
rclone --progress --config rclone.conf --exclude='kernels/**' sync mro_usgs: $1/mro
rclone --progress --config rclone.conf --exclude='kernels/**' sync mgs_usgs: $1/mgs
rclone --progress --config rclone.conf --exclude='kernels/**' sync lro_usgs: $1/lro

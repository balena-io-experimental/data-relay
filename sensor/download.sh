#!/bin/sh

outfile="/tmp/daprd.tar.gz"
download_base="https://github.com/dapr/dapr/releases/download/v1.1.2/"

case $1 in
   aarch64) package_file="daprd_linux_arm64.tar.gz"
       ;;
   amd64) package_file="daprd_linux_amd64.tar.gz"
       ;;
    *) package_file="daprd_linux_arm.tar.gz"
esac
wget -O "${outfile}" "${download_base}${package_file}"

tar -xvf /tmp/daprd.tar.gz
rm -rf /tmp/daprd.tar.gz

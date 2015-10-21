#!/bin/sh

set -eux

make

mkdir -p /tmp/lighttpd-test
echo "test123" > /tmp/lighttpd-test/index.html

CONTAINER=`./run.py --address 127.0.0.1 --port 8080 /tmp/lighttpd-test`

wget 127.0.0.1:8080

diff /tmp/lighttpd-test/index.html index.html

docker stop $CONTAINER
docker rm $CONTAINER

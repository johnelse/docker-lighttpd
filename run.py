#!/usr/bin/env python

"""
Helper script for launching lighttpd in a docker container.
"""

import argparse
import os
import subprocess
import sys


DEFAULT_ADDRESS = '127.0.0.1'


def main():
    """
    Main entry point.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('--address', default=DEFAULT_ADDRESS,
                        help='Host address on which the container will listen')
    parser.add_argument('--port', default=8080, type=int,
                        help='Host port which will forwarded to the '
                             'container\'s listening port')
    parser.add_argument('--root',
                        help='Root directory to be served')

    args = parser.parse_args(sys.argv[1:])
    address = DEFAULT_ADDRESS
    if args.address:
        address = args.address
    image = "%s/lighttpd" % os.getenv("USER")
    docker_args = [
        "docker", "run", "-d", "--name", "lighttpd-container-%d" % args.port,
        "-p", "%s:%d:8080" % (address, args.port),
        "-v", "%s:/var/www" % args.root,
        image
        ]
    print "Launching docker with args %s" % docker_args
    subprocess.call(docker_args)


if __name__ == "__main__":
    main()

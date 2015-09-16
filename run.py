#!/usr/bin/env python

"""
Helper script for launching lighttpd in a docker container.
"""

import argparse
import os
import subprocess
import sys


def main():
    """
    Main entry point.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('--root',
                        help='Root directory to be served')

    args = parser.parse_args(sys.argv[1:])
    image = "%s/lighttpd" % os.getenv("USER")
    docker_args = [
        "docker", "run", "-d", "--name", "lighttpd-container",
        "-p", "8080:8080",
        "-v", "%s:/var/www" % args.root,
        image
        ]
    print "Launching docker with args %s" % docker_args
    subprocess.call(docker_args)


if __name__ == "__main__":
    main()

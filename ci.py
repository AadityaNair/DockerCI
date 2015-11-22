#!/usr/bin/env python
"""
    DockerCI - CI/CD Pipeline using docker.

    Main File. Accepts user input.
    Shows status of last job or all jobs.
"""

def show_last_status():
    pass

def show_all_status():
    pass


# --------------------------------------------------------------
import argparse
parser = argparse.ArgumentParser()

parser.add_argument('status',
        type=str,
        help="takes either 'last' or 'all'. Prints either status of last job or all jobs. "
        )

args = parser.parse_args()
status = args.status.lower()

if status == 'last':
    show_last_status()
elif status == 'all':
    show_all_status()
else:
    print "Wrong argument. Try again.\n"



#!/usr/bin/env python
"""
    DockerCI - CI/CD Pipeline using docker.

    Main File. Accepts user input.
    Shows status of last job or all jobs.
"""
import requests
def show_last_status():
    resp = requests.get("http://127.0.0.1:5000/ci/status/last")
    return resp.json()

def show_all_status():
    resp = requests.get("http://127.0.0.1:5000/ci/status/all")
    return resp.json()

# --------------------------------------------------------------
import argparse
parser = argparse.ArgumentParser()

parser.add_argument('status',
        type=str,
        help="takes either 'last' or 'all'. Prints either status of last job or all jobs. ",
        choices=['last', 'all', 'init']
        )

args = parser.parse_args()
status = args.status.lower()

if status == 'last':
    show_last_status()

if status == 'all':
    show_all_status()

if status == 'init':
    import os
    os.system("git init --template=/home/Aaditya/projects/DockerCI/git-templates")

from __future__ import print_function

import argparse
import itertools
import os
import subprocess


def parse_args():
    parser = argparse.ArgumentParser(
        description='build parity data for each directory in a tree',
    )
    parser.add_argument(
        '--no-verify', action="store_true", help="disable verification")
    parser.add_argument(
        '--no-create', action="store_true", help="disable parity data creation")
    parser.add_argument('path', default=os.getcwdu(), help='path')
    return parser.parse_args()


def handle_dir(path, files, no_create, no_verify):
    parity_filename = ".rotten.par2"
    max_mtime = None
    parity_st = None
    for entry in files:
        stat = os.lstat(os.path.join(path, entry))
        if entry == parity_filename:
            parity_st = stat
        else:
            if stat.st_mtime > max_mtime:
                max_mtime = stat.st_mtime
    if parity_st is None or parity_st.st_mtime < max_mtime:
        if no_create:
            return
        args = [f for f in files if f != parity_filename]
        if len(args) == 0:
            return
        cmd = ["par2create", parity_filename] + args
        print("missing or outdated pairity data for {}".format(path))
        subprocess.check_call(cmd, cwd=path)
    else:
        if no_verify:
            return
        print("verifying pairity for {}".format(path))
        subprocess.check_call(["par2verify", parity_filename], cwd=path)


def walk(path, no_verify=False, no_create=False):
    for root, _, files in os.walk(path):
        print("entering: {}".format(root))
        handle_dir(root, files, no_verify=no_verify, no_create=no_create)


def main():
    args = parse_args()
    walk(args.path, no_create=args.no_create, no_verify=args.no_verify)


if __name__ == '__main__':
    main()

#!/usr/bin/env python3

import argparse, os

parser = argparse.ArgumentParser()
parser.add_argument('file')
parser.add_argument('outdir')
parser.add_argument('-d', "--dimension", type=int, required=True)
args = parser.parse_args()

def reg_indicators(text):
    if len(text) != 2: raise ValueError()
    return reg_indicators_unchecked(text)

def reg_indicators_unchecked(text):
    text = text.upper()
    if any([ord(a) not in range(65, 91) for a in text]): raise ValueError()
    text = [hex(0x1F1E6-65+ord(a))[2:] for a in text]
    return "-".join(text)


bare_filename = args.file.rsplit(".", 1)[0].rsplit("/", 1)[-1]

out_file = bare_filename

if bare_filename.startswith("country_"):
    out_file = reg_indicators(bare_filename.replace("country_", ""))

os.system(f"inkscape -z -w {args.dimension} -e {args.outdir}/{out_file}.png {args.file}")


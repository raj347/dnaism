#!/usr/bin/env python

import sys
import glob
from jinja2 import Template

start = 1100000
stop = 1200000
size = 1280
chrm = "Chr17"
step = 2

samples = []
for b in glob.glob("*.bed"):
    samples.append(b)

template = Template(open("index.template.html").read())
print template.render(start=start, stop=stop, size=size, chrm=chrm, step=step, metrics=samples)

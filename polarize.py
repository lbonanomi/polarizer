#!/bin/python3.6

# pylint: disable=C0103

"""Grouping with ChartJS"""

import os
import sys
import logging
from flask import Flask, render_template


# Quiet Flask console
#

log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)


try:
    port = int(sys.argv[1])
except IndexError:
    port = 9990


set_data = []
scale = 'head2head.html'


for line in sys.stdin.readlines():
    line = line.strip()

    if ',' not in line:
        sys.stderr.write("Couldn't find a ',' in input, disposing of line `" + line + "'\n")
    else:
        words = line.split(",")

        try:
            count = words[0]

            if '%' in count:
                scale = 'percentage.html'
                count = count.translate(None, '%')

            del words[0]
            label = " ".join(words)

            set_data.append([label, count])

        except IndexError:
            continue

if not set_data:
    sys.stderr.write("Nothing to graph. Quitting.\n")
    sys.exit(1)

app = Flask(__name__)

sys.stderr.write("listening on port " + str(port) + "\n")


@app.route('/', methods=['GET'])
def draw():
    """Render HTML on-demand"""
    return render_template(scale, marks=set_data)


if __name__ == '__main__':
    if os.path.isfile('cert.pem') and os.path.isfile('key.pem'):
        app.run(host='0.0.0.0', port=9990, ssl_context=('cert.pem', 'key.pem'))
    else:
        app.run(host='0.0.0.0', port=9990)

#!/opt/bb/bin/python

"""Grouping with ChartJS"""

import sys
from flask import Flask, render_template

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

if len(set_data) == 0:
        sys.stderr.write("Nothing to graph. Quitting.\n")
        sys.exit(1)


app = Flask(__name__)


@app.route('/', methods=['GET'])
def draw():
        return render_template(scale, marks=set_data )


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9990)

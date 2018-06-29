# polarizer

> A picture is worth 1,000 words  
> -Frederick R. Barnard, allegedly


## Whats this?

polarizer accepts csv data (in the form of value,label) from &lt;STDIN&gt; and graphs it on a [Chart.js](http://www.chartjs.org) polar-area graph served locally with [Flask](http://flask.pocoo.org/).

If data in the first column begins with a '%', the chart is auto-scaled to 100, otherwise the chart is automagically scaled by Chart.js. If there are more than 8 items in the chart a legend is included at the bottom of the page.


## Got a screenshot?

Sure!

```du -ms ~ | sort -rnk1 | awk '{ print $1","$2 }' | head -10 | ~/polarizer/polarize.py```:

![polarizer screencap](source/images/polarized.png)


```df -hP | awk '{ print $5","$6 }' | ~/polarizer/polarize.py```

![polarizer_screepcap_percentage](source/images/polarized_pct.png)


## This doesn't seem like a big-deal, what's the use-case?

Polarizer was assembled[*](#hat-tip) for use with [cosanguine.py](https://github.com/lbonanomi/scripts/blob/master/cosanguine.py) to graph trends in Employer's ticketing system. Its also proved useful with `du -ms` and [natural.py](https://github.com/lbonanomi/scripts/blob/master/natural.py) for visualizing what was chewing disk space.


[](#hat-tip)
## Hat-Tip

[Chart.js](http://www.chartjs.org) and [Flask](http://flask.pocoo.org/). I didn't really build this thing, I just put it together.

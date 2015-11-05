# The MIT License (MIT)
#
# Copyright (c) 2014 Johannes Schlatow
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""
Helper class for drawing stacked and grouped bar charts with matplotlib
"""

from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import division

from math import *
from collections import OrderedDict

import matplotlib.pyplot as pyplot

import numpy as np
import brewer2mpl

class BarChart(object):
    def __init__(self, title="Title", ylabel="Unknown", xlabel=None, xticks=None, noxticks=False, width=0.15, colorshift=0, rotation=70,
            xticksize=12, legend_loc="upper right", legendsize=None):
        """
        Arguments
        ----------
        title -- The title of plot.
        ylabel -- The label of the y-axis.
        xlabel -- The label ot the x-axis
        xticks -- Override ticks on the x-axis
        noxticks -- Omit ticks on the x-axis
        width -- The (relative) width of the bars.
        colorshift -- Shift the color set. (default: 0)
        rotation -- Rotate the x-tick labels. (default: 70)
        xticksize -- Font size of the x-ticks
        legend_loc -- Location of the legend
        legendsize -- Font size of the legend
        """

        self.groups = OrderedDict()
        self.categories = OrderedDict()
        self.bars = list()
        self.ylabel = ylabel
        self.xlabel = xlabel
        self.title  = title
        self.width  = width
        self.colorshift = colorshift
        self.rotation = rotation
        self.errvalues = dict()
        self.xticksize = xticksize
        self.xticks = xticks
        self.noxticks = noxticks
        self.legend_loc = legend_loc
        if rotation == "vertical" or rotation == "horizontal":
            self.xtickalign = "center"
        elif rotation > 0 and rotation < 90:
            self.xtickalign = "right"
        elif rotation < 0 and rotation > -90:
            self.xtickalign = "left"
        else:
            self.xtickalign = "center"

        if legendsize is not None:
            self.legendsize = legendsize
        else:
            self.legendsize = xticksize

        # Get "11-class Paired" from ColorBrewer, a nice print-friendly color set.
        # For more on ColorBrewer, see http://colorbrewer2.org/
        self.colors = brewer2mpl.get_map('Paired', 'qualitative', 11).mpl_colors

    def plot(self, axis, legend=True, sort=False, stacked=False):
        """ Create bars on the given axis.
        Arguments
        ----------
        axis -- A pyplot axis object
        legend -- Draw a legend (default: True)
        sort -- Sort categories (default: False)
        stacked -- Plot stacked bars instead of groups (default: False)
        """

        self.cat_list = list(self.categories.keys())
        if sort:
            self.cat_list = sorted(self.cat_list)

        num_colors = len(self.colors)

        # assign colors
        j = self.colorshift
        for name in self.cat_list:
            self.categories[name]["color"] = self.colors[j % num_colors]
            j = j + 1

        N = len(self.groups)
        ind = np.arange(N) * 1.3
        bottom = np.zeros(N)
        j = 0
        if stacked:
            offset = self.width/2
            tick_offset = self.width
        else:
            M = len(self.cat_list)
            ind = ind * M
            offset = self.width*(M/2)
            tick_offset = self.width*M

        for name in self.cat_list:
            cat_data = list()
            for group in self.groups:
                if name in self.groups[group]:
                    cat_data.append(self.groups[group][name])
                else:
                    cat_data.append(0)

            cat_err = None
            if name in self.errvalues:
                cat_err = list()
                for group in self.groups:
                    cat_err.append(self.errvalues[name][group])

            self.bars.append(axis.bar(ind+offset, cat_data, self.width, bottom=bottom, color=self.categories[name]["color"], yerr=cat_err))

            if stacked:
                j = j + 1
                for i in range(0, N):
                    bottom[i] = bottom[i] + cat_data[i]
            else:
                offset = offset + self.width

        axis.set_ylabel(self.ylabel)
        if self.xlabel is not None:
            axis.set_xlabel(self.xlabel)
        axis.set_title(self.title)

        if self.xticks is not None:
            labels = list()
            minorticks = list()
            majorticks = list([0+offset])
            last = 0
            for tick in self.xticks:
                cur  = ind[tick['index']]+offset
                majorticks.append(cur)
                minorticks.append((last+cur)/2)
                last = cur
                labels.append(tick['label'])

            axis.xaxis.set_tick_params(direction="out", top=False, labelbottom=False, size=20, width=2)
            axis.set_xticks(majorticks)
            axis.set_xticks(minorticks, minor=True)
            axis.set_xticklabels(labels, rotation=self.rotation, fontsize=self.xticksize,
                    horizontalalignment=self.xtickalign, minor=True)
        elif self.noxticks:
            axis.xaxis.set_tick_params(top=False, bottom=False, labelbottom=False)
        else:
            axis.set_xticks(ind+tick_offset)
            axis.set_xticklabels(list(self.groups.keys()), rotation=self.rotation,
                    fontsize=self.xticksize, ha=self.xtickalign)


        if legend:
            self._add_legend()

    def add_category(self, name, label=None):
        """ Manually pick a category from the added data (use add_group_data() first).
        Arguments
        ----------
        name -- The name of the category (as in the added data).
        label -- The label of the category as it will be shown in the plot. (default: name)
        """
        self.categories[name] = dict()
        if label is None:
            self.categories[name]['label'] = name
        else:
            self.categories[name]['label'] = label

    def auto_add_categories(self):
        """ Automatically pick all categories from the added data (use add_group_data() first).
        """
        for group in self.groups:
            for name in self.groups[group]:
                self.add_category(name)

    def add_group_data(self, label, tuples):
        """ Add a group and its data to the barchart.
        Arguments
        ----------
        label -- The label of the group as it will be shown in the plot.
        tuples -- A list of tuples of category names and the corresponding data
        """
        self.groups[label] = dict(tuples)

    def add_group_error(self, group, category, errval):
        """ Add an optional error (e.g. variance) to the datum of a specific category in a group.
        By setting an error value, error bars will automatically be added to the barchart.
        Arguments
        ----------
        group -- The group to which an error value shall be added.
        category -- The category of the group to which an error value shall be added.
        errval -- The error value (e.g. variance).
        """
        if category not in self.errvalues:
            self.errvalues[category] = dict()
        self.errvalues[category][group] = errval

    def _add_legend(self):
        revbars = list(self.bars)
        revbars.reverse()
        revnames = list()
        for cat in self.cat_list:
            revnames.append(self.categories[cat]['label'])
        revnames.reverse()
        pyplot.legend( (revbars), (revnames), loc=self.legend_loc, fontsize=self.legendsize,
                handlelength=1, labelspacing=0.2)

    def _normalize(self, groupname):
        for group in self.groups:
            basevalue = self.groups[group][groupname]
            for name in self.groups[group]:
                self.groups[group][name] /= basevalue


# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4

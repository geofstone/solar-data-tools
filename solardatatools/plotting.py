# -*- coding: utf-8 -*-
''' Plotting Module



'''

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def plot_2d(D, figsize=(12, 6), units='kW', clear_days=None):
    """
    A function for plotting the power heat map for solar power data
    
    :param D: PV power data arranged as a matrix, typically the output of
        `data_transforms.make_2d()`
    :param figsize: the size of the desired figure (passed to `matplotlib`)
    :param units: the units of the power data
    :param clear_days: a boolean array marking the location of clear days in
        the data set, typically the output of `clear_day_detection.find_clear_days()`
    :return: `matplotlib` figure
    """
    if D is not None:
        with sns.axes_style("white"):
            fig, ax = plt.subplots(nrows=1, figsize=figsize)
            foo = ax.imshow(D, cmap='hot', interpolation='none', aspect='auto', vmin=0)
            ax.set_title('Measured power')
            plt.colorbar(foo, ax=ax, label=units)
            ax.set_xlabel('Day number')
            ax.set_yticks([])
            ax.set_ylabel('(sunset)        Time of day        (sunrise)')
            if clear_days is not None:
                xlim = ax.get_xlim()
                ylim = ax.get_ylim()
                use_day = clear_days
                days = np.arange(D.shape[1])
                y1 = np.ones_like(days[use_day]) * D.shape[0] * .999
                ax.scatter(days[use_day], y1, marker='|', color='yellow', s=2)
                ax.scatter(days[use_day], .995*y1, marker='|', color='yellow', s=2)
                ax.set_xlim(*xlim)
                ax.set_ylim(*ylim)
        return fig
    else:
        return

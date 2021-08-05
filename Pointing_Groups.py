from matplotlib import colors
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



def add_value_labels(ax, spacing=5):
    """Add labels to the end of each bar in a bar chart.

    Arguments:
        ax (matplotlib.axes.Axes): The matplotlib object containing the axes
            of the plot to annotate.
        spacing (int): The distance between the labels and the bars.
    """

    # For each bar: Place a label
    for rect in ax.patches:
        # Get X and Y placement of label from rect.
        y_value = rect.get_height()
        x_value = rect.get_x() + rect.get_width() / 2

        # Number of points between bar and label. Change to your liking.
        space = spacing
        # Vertical alignment for positive values
        va = 'bottom'

        # If value of bar is negative: Place label below bar
        if y_value < 0:
            # Invert space to place label below
            space *= -1
            # Vertically align label at top
            va = 'top'

        # Use Y value as label and format number with one decimal place
        label = "{:.1f}".format(y_value)

        # Create annotation
        ax.annotate(
            label,                      # Use `label` as label
            (x_value, y_value),         # Place label at end of the bar
            xytext=(0, space),          # Vertically shift label by `space`
            textcoords="offset points", # Interpret `xytext` as offset in points
            ha='center',                # Horizontally center label
            va=va)                      # Vertically align label differently for
                                        # positive and negative values.



def Analiz_groups(frequencies,x_labels):
    # Bring some raw data.
    # In my original code I create a series and run on that,
    # so for consistency I create a series from the list.
    freq_series = pd.Series(frequencies)
    # Plot the figure.
    fig= plt.figure(figsize=(20, 16))
    plt.rc('axes', unicode_minus=False)
    ax = freq_series.plot(kind='bar' , color={'b', 'g','c', 'r', 'm', 'y', 'k'} )
    ax.set_title('Group Points')
    ax.set_xlabel('Title' , fontweight='bold')
    ax.set_ylabel('Points', fontweight='bold')
    fig.patch.set_facecolor('xkcd:black')
    ax.tick_params(axis='x', colors='lawngreen' )
    ax.tick_params(axis='y', colors='snow'  )
    ax.set_facecolor('xkcd:white')
    ax.set_xticklabels(x_labels ,  rotation = 45, zorder=100 , weight='bold', fontsize=15)
    # Call the function above. All the magic happens there.
    add_value_labels(ax)
    plt.savefig("image.jpg")
    try:
        plt.cla()
        plt.clf()
        plt.close()
    except:
        pass
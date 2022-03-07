import json
import matplotlib.pyplot as plt
from sklearn import preprocessing
import numpy as np


def autolabel(rects, ax, values):
    for idx, rect in enumerate(rects):
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width() / 2., 1 * height,
                values[idx],
                ha='center', va='bottom', rotation=0)
    return rects


def plot_graph1(inputfile):
    content_as_dict = json.load(open(inputfile, 'r'))
    actual_values = list(content_as_dict.values())
    print(np.array(actual_values))

    for index, (key, value) in enumerate(content_as_dict.items()):
        colors = ['b', 'g', 'r', 'y', 'o']
        qw_dict = value
        print(type(qw_dict))
        plt.plot(qw_dict.keys(), qw_dict.values(), color=colors[index], marker='o', label="Date:" + key)
    direction = "Triad direction: A->B->C" if inputfile.split('_')[-1] == "nonwh" else "Triad direction: A<-B->C"
    title = 'Total triads (vs) time allowed for triad formation(' + direction + ')'
    plt.title(title)
    plt.xlabel('Query window (in seconds)')
    plt.ylabel('Total no. of triads')
    plt.legend()
    plt.show()


def plot_graph2(inputfile):
    content_as_dict = json.load(open(inputfile, 'r'))
    actual_values = list(content_as_dict.values())
    print(np.array(actual_values))

    for index, (key, value) in enumerate(content_as_dict.items()):
        colors = ['b', 'g', 'r', 'y', 'o']
        tod_dict = value
        print(type(tod_dict))
        plt.plot(tod_dict.keys(), tod_dict.values(), color=colors[index], marker='o', label="Date:" + key)
    direction = "Triad direction: A->B->C" if inputfile.split('_')[-1] == "nonwh" else "Triad direction: A<-B->C"
    title = 'Total triads (vs) Time of the day(' + direction + ')'
    plt.title(title)
    plt.xlabel('Time/Hour of the day')
    plt.ylabel('Total no. of triads')
    plt.legend()
    plt.show()


plot_graph1("qw_analysis_nonwh")
#plot_graph2("tod_analysis_nonwh")

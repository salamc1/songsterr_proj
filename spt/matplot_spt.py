import matplotlib.pyplot as plt

def make_histogram_from_dict(dictionary, path, title, xlabel, ylabel):
    plt.figure()
    plt.bar(dictionary.keys(), dictionary.values())
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.savefig(path)
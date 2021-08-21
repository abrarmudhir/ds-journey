import seaborn as sns
import matplotlib.pyplot as plt


def plot_iris():
    dataset = sns.load_dataset('iris')
    dataset.hist()
    plt.show()

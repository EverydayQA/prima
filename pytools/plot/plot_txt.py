import numpy as np
from pprint import pprint
import matplotlib.pyplot as plt


class PlotAny(object):

    def __init__(self):
        pass

    def get_np_random(self):
        # Fixing random state for reproducibility
        np.random.seed(19680801)

        mu, sigma = 100, 15
        x = mu + sigma * np.random.randn(10000)

        print(type(x))
        pprint(x)
        return x

    def csv_to_npa(self, acsv):
        return np.genfromtxt(acsv, delimiter=',')

    def plot_demo(self):
        npx = self.get_np_random()
        pprint(npx)
        print(type(npx))
        self.plot_hist_np(npx)

    def csv_to_df(self, acsv):
        import pandas
        df = pandas.read_csv(acsv, sep=',')
        return df

    def acsv(self):
        return '/tmp/iden.csv'

    def plot_df(self):
        df = self.csv_to_df(self.acsv())
        pprint(df)
        plt.xlabel('correlation')
        plt.ylabel('Probability')
        plt.title('Histogram of 2 group')

        plt.hist([df['one'], df['other']], bins=30)
        plt.grid(True)

        plt.show()

    def plot_csv(self):
        npx = self.csv_to_npa('/tmp/iden.csv')
        print(npx)

    def plot_hist_np(self, x):
        # the histogram of the data
        n, bins, patches = plt.hist(x, 50, density=True, facecolor='g', alpha=0.75)
        plt.xlabel('Smarts')
        plt.ylabel('Probability')
        plt.title('Histogram of IQ')
        plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
        plt.xlim(40, 160)
        plt.ylim(0, 0.03)
        plt.grid(True)
        plt.show()


def main():
    pa = PlotAny()
    pa.plot_df()
    # pa.plot_demo()


if __name__ == '__main__':
    main()

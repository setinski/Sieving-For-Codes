import matplotlib.pyplot as plt
import csv

def csv_write_data(directory, fields, data, name, n, w, N, i = 0):
    with open("%s%s-n%d-w%d-N%d-%d.csv"%(directory, name, n, w, N, i), "w", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fields)
        writer.writeheader()
        for row in data:
            writer.writerow(row)
            
def plot_data(directory, exp_data, theory_data, n, w, N, values):
    fig, axs = plt.subplots(2, 2, sharex=True)
    fig.tight_layout(pad=2.0)
    axs_iter = 0

    for dt in values:
        exp_d = [x[dt] for x in exp_data]
        theo_d = [x[dt] for x in theory_data]
        axs[axs_iter % 2, axs_iter // 2].plot(exp_d, 'ro', markersize=4)
        axs[axs_iter % 2, axs_iter // 2].plot(theo_d, 'bx', markersize=2)
        axs[axs_iter % 2, axs_iter // 2].set_title(dt + "  n=%d, w=%d, N=%d"%(n, w, N))
        axs[axs_iter % 2, axs_iter // 2].set_yscale("log",base=2)
        axs_iter += 1

    plt.savefig('%scomparison-n%d-w%d-N%d.png'%(directory, n, w, N), dpi=600)
import timeit
import matplotlib.pyplot as plt
import numpy as np
# import Christodes-Serdyukov as cs
# import Pairwise-Exchange as pe 
# import Held-Karp as hk
# import Nearest Neighbor as nn 
from functools import partial


def to_time(items):
    return sum(items)

test_items = [1, 2, 3] * 500


hk_runtimes = []
nn_runtimes = []
cs_runtimes = []
pe_runtimes = []

n_values = np.array([i for i in range(500)])


for i in n_values:

    # graph = nx.Graph()

    nn_runtimes.append(min(timeit.Timer(partial(to_time, test_items)).repeat(3, 500))/500)
    hk_runtimes.append(min(timeit.Timer(partial(to_time, test_items)).repeat(3, 500))/500)
    cs_runtimes.append(min(timeit.Timer(partial(to_time, test_items)).repeat(3, 500))/500)
    pe_runtimes.append(min(timeit.Timer(partial(to_time, test_items)).repeat(3, 500))/500)


fig, axs = plt.subplots(2, 2)
axs[0, 0].plot(n_values, hk_runtimes)
axs[0, 0].set_title("Held-Karp")
axs[1, 0].plot(n_values, nn_runtimes)
axs[1, 0].set_title("Nearest Neighbor")

axs[0, 1].plot(n_values, cs_runtimes)
axs[0, 1].set_title("Christofides")
axs[1, 1].plot(n_values, pe_runtimes)
axs[1, 1].set_title("Pairwise Exchange")
fig.tight_layout()
plt.show()
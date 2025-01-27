# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

import numpy as np

path = '/Users/luissilva/PycharmProjects/Workshop101Biosignals/G1/G1_task_emg_acc_serie2.txt'
data = np.loadtxt(path)
emg = data[:, 1]
acc = data[:, 3]

# Filter

plt.plot(acc)
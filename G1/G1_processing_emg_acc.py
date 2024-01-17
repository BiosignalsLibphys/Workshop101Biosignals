import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

path_emg_acc = 'C:/Users/marci/PycharmProjects/Workshop101Biosignals/G1/G1_task_emg_acc_serie1.txt'
fs = 1000
def load_file(path):

    df_emg_acc = pd.read_csv(path, delimiter='\t', comment='#', header=None, index_col=[0])
    df_emg_acc = df_emg_acc.drop(columns=[1,6], axis=1)
    col_names = ['EMG','Z','Y','X']
    df_emg_acc.columns = col_names
    return df_emg_acc

def ACC_convert_mV(df_emg_acc):

    c_min = -3.6
    c_max = 3.6

    for col in df_emg_acc.columns[-3:]:
        df_emg_acc[col] = (((df_emg_acc[col]/2**16) - c_min)/(c_max - c_min))*2-1
    return df_emg_acc

def EMG_convert_mV(df_emg_acc):
    vcc = 3
    g_emg = 1007
    df_emg_acc['EMG'] = ((df_emg_acc['EMG']/2**16-0.5)*vcc/g_emg)*1000
    return df_emg_acc

def plot(df):

    samples = len(df)
    duration = samples/fs
    time = np.arange(0, duration, 1/fs)

    fig, axs = plt.subplots(4, 1, figsize=(14, 6))

    # Plotting each signal
    axs[0].plot(time, df['EMG'])
    axs[0].set_title('EMG')
    axs[0].set_ylabel('Amplitude [mV]')

    axs[1].plot(time, df['Z'])
    axs[1].set_title('ACC_Z')
    axs[1].set_ylabel('Amplitude [g]')

    axs[2].plot(time, df['Y'])
    axs[2].set_title('ACC_Y')
    axs[2].set_ylabel('Amplitude [g]')

    axs[3].plot(time, df['X'])
    axs[3].set_title('ACC_X')
    axs[3].set_ylabel('Amplitude [g]')
    axs[3].set_xlabel('Time [s]')

    # Adjust layout and show plot
    plt.tight_layout()
    plt.show()

df_emg_acc = load_file(path_emg_acc)
df_emg_acc = EMG_convert_mV(df_emg_acc)
df_emg_acc = ACC_convert_mV(df_emg_acc)
plot_emg_acc = plot(df_emg_acc)

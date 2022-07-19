import numpy as np
import matplotlib.pylab as plt


def sine_drone(f1, f2, fbase, period=0.5, sampleRate=10000, length=15):
    t = np.linspace(0, length, length * sampleRate)
    dt = t[1] - t[0]  # needed for integration

    # define desired frequency sweep
    f_inst = np.sin(2 * np.pi * (1 / period) * t + 0.5) * (f2-f1) + f1
    phi = 2 * np.pi * np.cumsum(f_inst) * dt  # integrate to get phase

    # make plots
    plt.plot(t, f_inst)
    plt.xlabel('Time (s)')
    plt.ylabel('Frequency (Hz)')
    plt.title('Frequency time dependence')
    plt.show()

    return np.sin(phi), np.sin(2 * np.pi * fbase * t), f_inst


def drone(PLOT=False):  # "C", "F", "A"):
    from .rr_utils import readdata
    import sonifyFED.sonify.core as sonify

    data, _ = readdata()
    duration = int(data.mjd.max() - data.mjd.min() + 0.5)
    cycles = duration / 365.25
    N = int(cycles * 13 + 0.5)  # one note per moon cycle?
    time = np.linspace(0, 15, N)
    stepsinhalfcycle = int(np.round(N / cycles / 2))
    dronenote = [41] * stepsinhalfcycle + [45] * stepsinhalfcycle

    dronenote = dronenote * (int(cycles) + 1)
    dronenote = np.array(dronenote[:N])
    dronebase = np.zeros(N) + 36  # configs.drone_base
    # print(list(zip(time, dronenote)))

    # make plots
    if PLOT:
        plt.plot(time, dronebase, label="base")
        plt.plot(time, dronenote, label="drone")
        plt.xlabel('Time (s)')
        plt.ylabel('note')
        plt.title('drone')
        plt.legend()
        plt.show()

    quantized_x = sonify.quantize_x_value(time, steps=0.01)
    return list(zip(quantized_x, dronenote)), list(zip(quantized_x, dronebase))


def drone_glissando(data=None, root=None, PLOT=False):
    import sonifyFED.sonify.core as sonify
    if data is None:
        from .rr_utils import readdata
        if root is None:
            root = "../data"
        data, _ = readdata(root=root)

    duration = int(data.mjd.max() - data.mjd.min() + 0.5)
    years = duration / 365.25  # duration in years (22 notes)
    time = np.linspace(0, 15, int(22 * years + 0.5))
    y = list(range(1, 13)) + list(range(11, 1, -1))
    y = y * int(years + 0.5)
    data = list(zip(time, y))
    converted_data = sonify.convert_to_key(data, 'chromatic', number_of_octaves=1)
    x, y = zip(*converted_data)
    y_base = [36] * len(x)

    # make plots
    if PLOT:
        plt.plot(time, y_base, label="base")
        plt.plot(time, y, label="drone")
        plt.xlabel('Time (s)')
        plt.ylabel('note')
        plt.title('drone')
        plt.legend()
        plt.show()
    quantized_x = sonify.quantize_x_value(time, steps=0.01)
    return list(zip(quantized_x, y)), list(zip(quantized_x, y_base))

def drum_beat(drum, data=None):
    import sonifyFED.sonify.core as sonify
    from sonifyFED.sonify.constants import PERCUSSION
    percussions = list(PERCUSSION.keys())
    assert drum in percussions, 'Current drone options are glissando "gliss" and step "step"'

    if data is None:
        from .rr_utils import readdata
        data, _ = readdata()
    duration = int(data.mjd.max() - data.mjd.min() + 0.5)
    mooncycles = int(duration / 28 + 0.5)
    time = np.linspace(0, 15, mooncycles)
    y = np.ones_like(time)
    data = list(zip(time, y))
    return data

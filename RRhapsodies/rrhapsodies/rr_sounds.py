import numpy as np

def sine_drone(f1, f2, fbase, period=0.5, sampleRate=10000, length=15):

  t = np.linspace(0,length,length*sampleRate)
  dt = t[1] - t[0] # needed for integration

  # define desired frequency sweep
  f_inst = np.sin(2 * np.pi * (1 / period) * t + 0.5) * (f2-f1) + f1
  phi = 2 * np.pi * np.cumsum(f_inst) * dt # integrate to get phase

  # make plots
  plt.plot(t, f_inst)
  plt.xlabel('Time (s)')
  plt.ylabel('Frequency (Hz)');
  plt.title('Frequency time dependence')
  plt.show()

  return np.sin(phi), np.sin(2 * np.pi * fbase * t), f_inst

def drone(PLOT=False):#"C", "F", "A"):
  from . import configs as configs
  from .rr_utils import readdata
  import pylab as plt
  import sonifyFED.sonify.core as sonify

  #N = 100
  data, _ = readdata()
  duration = int(data.mjd.max() - data.mjd.min() + 0.5)
  cycles = duration / 365.25
  N = int(cycles * 13 + 0.5)  # one note per moon cycle?
  time = np.linspace(0, 15, N)
  stepsinhalfcycle = int(np.round(N / cycles / 2))
  # dronenote = [configs.drone_low] * stepsincycle + \
  #            [configs.drone_high] * stepsincycle
  dronenote = [41] * stepsincycle + [45] * stepsinhalfcycle

  # 41, 43, 45, 47, 48, 50, 52
  dronenote = dronenote * (int(cycles) + 1)
  dronenote = np.array(dronenote[:N])
  dronebase = np.zeros(N) + 36  # configs.drone_base
  # print(list(zip(time, dronenote)))

  # make plots
  if PLOT:
    plt.plot(time, dronebase, label="base")
    plt.plot(time, dronenote, label="drone")
    plt.xlabel('Time (s)')
    plt.ylabel('note');
    plt.title('drone')
    plt.legend()
    plt.show()

  quantized_x = sonify.quantize_x_value(time, steps=0.01)
  return list(zip(quantized_x, dronenote)),list(zip(quantized_x, dronebase))
  # sonify.play_midi_from_data(list(zip(quantized_x, dronebase)), track_type='single')

def drone_glissando(PLOT=False):#"C", "F", "A"):
  from . import configs as configs
  from .rr_utils import readdata
  import pylab as plt
  import sonifyFED.sonify.core as sonify

  data, _ = readdata()
  duration = int(data.mjd.max() - data.mjd.min() + 0.5)
  years = duration / 365.25 #duration in years (22 notes)
  time = np.linspace(0, 15, int(22 * years + 0.5))
  y = list(range(1,13)) + list(range(11,1,-1))
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
  #sonify.play_midi_from_data([list(zip(quantized_x, y_base)), list(zip(quantized_x, y))], track_type='multiple')
  return list(zip(quantized_x, y)),list(zip(quantized_x, y_base))

import numpy as np
import matplotlib.pyplot as plt
# from tqdm import tqdm

plt.rcParams['text.usetex']=True


def kuramoto(theta, T, dt, omega, k=.5):
    N = len(theta)

    for t in range(T):
        t0phase = theta[t, :]
        phase_diff = t0phase[:, None] - t0phase[None, :]
        coupling = np.sum(np.sin(phase_diff), axis=1)
        t1phase = (t0phase + (omega.T + k*coupling)*dt) % 2*np.pi
        
        theta = np.vstack([theta, t1phase])
        
    return theta

def KuramotoOrder(theta):
     return np.abs(np.mean(np.exp(1j*phase_arr), axis=1))

N = 10
T = 1000
dt = .05
theta = np.random.uniform(0, 2*np.pi, N).reshape(1,N)
omega = np.random.uniform(2, 6, N)
phase_arr = kuramoto(theta, T, dt, omega, k =50)
r = KuramotoOrder(phase_arr)
colors = plt.cm.inferno(np.linspace(0, 1, N))


duratiom = 10
# print('a')
# for i in range(duratiom):
#     plt.clf()
#     plt.axes(projection= 'polar')
#     for j in range(N):
#         plt.plot(phase_arr[i,j],1, 'o', markersize=10, color=colors[j])
#     # plt.plot(phase_arr[i,1],1, 'o', markersize=10, color = 'red')
#     # plt.plot(phase_arr[i,2],1, 'o', markersize=10, color = 'green')
#     plt.title(f'R = {r[i]}; Time = {i}')
#     plt.pause(.1)
fig = plt.figure()
axis = plt.axes(projection='polar')
oscillator, =axis.plot([], [], markersize=5)

def init():
    oscillator.set_data([], [])
    return oscillator, 

def animate(theta): 
    oscillator.set_data(phase_arr)
    return oscillator,

from matplotlib.animation import FuncAnimation
anim = FuncAnimation(fig, animate,
                     init_func=init,
                     frames=100, interval=20,
                     blit=True)
anim.save('kuramoto-oscillators.mp4', 
          writer='ffmpeg', fps=30)
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.cm import get_cmap
plt.rcParams['text.usetex']=True

def kuramoto(theta, T, dt, omega, k, noise='False', spread=.05):
    N = len(theta)
    theta_full = np.zeros((T, N))
    theta_full[0] = theta
    if noise==True:
        eta = 1
    else:
        eta=0

    for t in range(1, T):
        t0phase = theta_full[t - 1]
        phase_diff = t0phase[None, :] - t0phase[:, None]
        coupling = np.sum(k*np.sin(phase_diff), axis=1)
        t1phase = (t0phase + eta*np.random.normal(.5, spread, N)+ (omega + coupling) * dt) % (2 * np.pi)
        theta_full[t] = t1phase

    return theta_full

def KuramotoOrder(theta):
     return np.abs(np.mean(np.exp(1j*phase_arr), axis=1))


N = 4
T = 10
dt = 0.05
K = np.random.uniform(.001, .1, (N,N))
theta = np.random.uniform(0, 2 * np.pi, N)
omega = np.random.normal(.5, 10)
phase_arr = kuramoto(theta, T, dt, omega, K, noise=True,spread=.25)
r = KuramotoOrder(phase_arr)
time = np.linspace(0,T,T)
r = KuramotoOrder(phase_arr)
time = np.linspace(0,T,T)

cmap = get_cmap('twilight')
norm = plt.Normalize(0, 2 * np.pi)
colors = [cmap(norm(phase)) for phase in theta]

grid_size = np.sqrt(N)
circle_radius = 0.4
circle_positions = [(i % grid_size, i // grid_size) for i in range(N)]

fig, ax = plt.subplots(figsize=(6,6))
fig.patch.set_facecolor('black')


circles = [plt.Circle((pos[0], pos[1]), circle_radius, color=cmap(norm(theta[i])), lw=2) 
           for i, pos in enumerate(circle_positions)]
for circle in circles:
    ax.add_artist(circle)

ax.set_xlim(-1, grid_size)
ax.set_ylim(-1, grid_size)
ax.set_aspect('equal')
ax.axis('off')

def init():
    for circle in circles:

        circle.set_color(cmap(norm(0)))
    return circles

def animate(i):
    phases = phase_arr[i]
    ax.set_title(f'Kuramoto Oscillators \n $r={ round(r[i], 3)}, t={round(time[i],1)}$', color = 'white', fontsize=24)
    for j, circle in enumerate(circles):
        color = cmap(norm(phases[j]))
        circle.set_color(color)
    return circles

anim = FuncAnimation(fig, animate , init_func=init, frames=T, interval=100, blit=True)
 
anim.save('phase-matrix.mp4', writer='ffmpeg', fps=15, dpi=450, bitrate=2000)   
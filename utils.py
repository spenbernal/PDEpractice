import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from IPython.display import HTML

def plot(x, t, u, is_heat):
    '''
    x: space domain
    t: time domain
    u: solution matrix
    is_heat: bool
    '''
    fig, ax = plt.subplots(figsize=(10,6))

    type_of_plot = 'Heat Equation' if is_heat else 'Wave Equation'
    label = 'Temperature' if is_heat else 'Displacement'
    X,T = np.meshgrid(x,t)
    cp = ax.contourf(X, T, u, cmap='RdBu_r')
    ax.set_xlabel('Position')
    ax.set_ylabel('Time (s)')
    ax.set_title(type_of_plot)
    fig.colorbar(cp, label=label)
    plt.show()
    return

def animated_plot(x, t, u, is_dirichlet, is_heat):
    '''
    x: space domain
    t: time domain
    u: solution matrix
    is_dirichlet: bool
    is_heat: bool
    '''
    fig, ax = plt.subplots()
    title = 'Heat Equation' if is_heat else 'Wave Equation'
    ylabel = 'Temperature' if is_heat else 'Displacement'
    boundary = 'with Dirichlet Boundaries' if is_dirichlet else 'with Neumann Boundaries'
    line = ax.plot(x, u[0, :], label='t = 0.0')[0]
    ax.set(xlim=[0, 1], ylim= [u.min(), u.max()], xlabel='Position', ylabel=ylabel, 
           title=f"Solution to {title} {boundary}")
    
    legend = ax.legend(loc="upper right")  
    
    def update(frame):
        line.set_ydata(u[frame, :])
        line.set_label(f"t = {t[frame]:.3f}")
        ax.legend(loc="upper right")
        return line, legend
    
    ani = animation.FuncAnimation(fig=fig, func=update, frames=range(0,len(t), len(t)//300), interval=30)
    plt.close(fig)
    return ani
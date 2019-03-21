#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

#-----------------------------------------------------------------------------------#
def arc_params_calculating(In_value):
    """
    Calculating all arc parameters.
    
    In_value - array with initial values
    
    Return:
    alpha - angle betwin arc border points
    a, b - arc center coordinates
    L - arc length
    R - radius    
    """
    
    m_a = (In_value[1,1]-In_value[0,1]) / (In_value[1,0]-In_value[0,0])
    m_b = (In_value[2,1]-In_value[1,1]) / (In_value[2,0]-In_value[1,0])
    
    x_numerator = (m_a*m_b * (In_value[0,1]-In_value[2,1]) +
                   m_b * (In_value[0,0]+In_value[1,0]) -
                   m_a * (In_value[1,0]+In_value[2,0]))
    
    x_denumerator = 2 * (m_b-m_a)
    
    a = x_numerator / x_denumerator
    
    b = ((-1/m_a) * (a - (In_value[0,0]+In_value[1,0]) / 2) + 
                    (In_value[0,1]+In_value[1,1]) / 2)
    
    R = np.sqrt((a-In_value[0,0])**2 + (b-In_value[0,1])**2)
    
    l = np.sqrt((In_value[0,0]-In_value[1,0])**2 + (In_value[0,1]-In_value[1,1])**2)
    alpha = np.arcsin(l / (2*R)) * 2
    
    L = alpha*R
    
    return (a, b, R, L, alpha)
#-----------------------------------------------------------------------------------#

#-----------------------------------------------------------------------------------#
def arc_equation(In_value, a, b, R, L, alpha, step=0.01):
    """
    Return array whith X and Y values.
    
    alpha - angle betwin arc border points
    In_value - array with initial values
    a, b - arc center coordinates
    L - arc length
    R - radius 
    
    Step is needed for better or worse trajectory smoothing.
    """
    steps_sum = np.int(L/step)
    
    starting_y = In_value[0,1]
    starting_x = In_value[0,0]
    
    X, Y = np.zeros(steps_sum), np.zeros(steps_sum)
    
    x_0, y_0 = a, b+R
    
    l = np.sqrt((starting_x-x_0)**2 + (starting_y-y_0)**2)
    betta = 2 * np.arcsin(l / (2*R))
    
    if starting_x-x_0 > 0:
        steps_alpha = np.linspace(betta, betta+alpha, steps_sum)
    else:
        steps_alpha = np.linspace(-betta, -betta+alpha, steps_sum)

    for i, angle in enumerate(steps_alpha):
        Y[i] = b + R*np.cos(angle)
        X[i] = a + R*np.sin(angle)
    
    return X, Y
#-----------------------------------------------------------------------------------#

#-----------------------------------------------------------------------------------#
def Q1_Q2_Q3_values(In_value, X, Y, L1, L2, albow=1):
    """
    
    """
    Psi = np.concatenate((np.linspace(In_value[0,2], In_value[1,2], len(X)//2),
                          np.linspace(In_value[1,2], In_value[2,2], len(X)//2+1)[1:]),
                          axis=0)
    
    Psi = np.deg2rad(Psi)
    
    B = np.sqrt(X**2 + Y**2)

    q1 = np.arccos(X/B)
    q2 = np.arccos((L1**2 - L2**2 + B**2) / (2*B*L1))
    
    if albow == 1:
        Q1 = q1-q2
        Q2 = np.pi - np.arccos((L1**2 + L2**2 - B**2) / (2 * L1*L2))
        Q3 = Psi-Q2-Q1
    else:
        Q1 = q1+q2
        Q2 = -1 * (np.pi - np.arccos((L1**2 + L2**2 - B**2) / (2 * L1*L2)))
        Q3 = Psi-Q2-Q1
        
    return Q1, Q2, Q3
#-----------------------------------------------------------------------------------#

#-----------------------------------------------------------------------------------#
def coordinates_for_every_unit(Q1, Q2, Q3, L1, L2):
    """
    
    """
    X_L1, Y_L1 = L1*np.cos(Q1), L1*np.sin(Q1)
    X_L2, Y_L2 = X_L1 + L2*np.cos(Q1 + Q2), Y_L1 + L2*np.sin(Q1 + Q2)
    
    return X_L1, X_L2, Y_L1, Y_L2
#-----------------------------------------------------------------------------------#

#-----------------------------------------------------------------------------------#
def Trajectory_ploting(X_L1, X_L2, Y_L1, Y_L2, m=5, fig_size=[5,5], x_lim=(-1,6),
            y_lim=(-1,6), save=False, fps=15, lw_unit=2, lw_way=1, interval=1):
    """
    This function is needed for ploting manipulator moving and it's trajectory.
    
    save - saving figure in mp4 if save=False, saving figure if True
    fps - frame per second. Needed if figure will be save
    interval - time in ms detween 2 frames ploting
    lw_unit, lw_way - unit and way line size
    x_lim, y_lim - x, y axis range
    fig_size - figure size
    m - ploting speed 
    """
    
    fig = plt.figure(figsize=fig_size)
    ax = fig.add_subplot(111, autoscale_on=False, xlim=x_lim, ylim=y_lim)
    ax.grid()

    line, = ax.plot([], [], 'o-', lw=lw_unit)
    way_line, = ax.plot([], [], color='red', lw=lw_way)

    def init():
        line.set_data([], [])
        way_line.set_data([], [])
        
        return line, way_line

    def animate(i):
        thisx = [0, X_L1[i], X_L2[i]]
        thisy = [0, Y_L1[i], Y_L2[i]]

        line.set_data(thisx, thisy)
        way_line.set_data([X_L2[:i]], [Y_L2[:i]])
        
        return line, way_line
    
    ani = animation.FuncAnimation(fig, animate, np.arange(1, len(X_L1), m), 
                                  interval=interval, blit=True, init_func=init, repeat=False)
    if save == True:
        ani.save('double_manipulator.mp4', fps=fps)
    plt.show()
    return ani
#-----------------------------------------------------------------------------------#

#-----------------------------------------------------------------------------------#
def Q_velosity(Q1, Q2, Q3, T):
    T_vector = np.linspace(0, T, len(Q1))
    dt = np.ediff1d(T_vector)
    
    _Q1 = np.ediff1d(Q1) / dt
    _Q2 = np.ediff1d(Q2) / dt
    _Q3 = np.ediff1d(Q3) / dt
    
    return _Q1, _Q2, _Q3
#-----------------------------------------------------------------------------------#

#-----------------------------------------------------------------------------------#    
def Q_axeleration(Q1, Q2, Q3, T):
    T_vector = np.linspace(0, T, len(Q1))
    dt = np.ediff1d(T_vector)
    
    _Q1_ = np.ediff1d((np.ediff1d(Q1) / dt) / dt)
    _Q2_ = np.ediff1d((np.ediff1d(Q2) / dt) / dt)
    _Q3_ = np.ediff1d((np.ediff1d(Q3) / dt) / dt)
    
    return _Q1_, _Q2_, _Q3_
#-----------------------------------------------------------------------------------#

#-----------------------------------------------------------------------------------#
def Q_plot(Q1, Q2, Q3, T, fig_size=[5,5], lw_unit=2, lw_way=1):
    T = np.linspace(0, T, len(Q1))
    
    figure = plt.figure(figsize=fig_size)
    ax = figure.add_subplot(111, autoscale_on=True)
    ax.grid()
    
    ax.plot(T,Q1, T,Q2)
    plt.show()
#-----------------------------------------------------------------------------------#

#-----------------------------------------------------------------------------------#
def Time(Distance, Speed, Axeleration):
    velosity_time = Speed/Axeleration
    S_velosity = (Axeleration**2 * velosity_time) / 2
    t_lin = (Distance - 2*S_velosity) / Speed
    T = t_lin + velosity_time*2
    return T
#-----------------------------------------------------------------------------------#


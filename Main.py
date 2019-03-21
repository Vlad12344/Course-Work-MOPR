#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import sys
import numpy as np
import manipulator as mn
import Manipulator_app as M_app
import matplotlib.pyplot as plt
import matplotlib.animation as animation

from PyQt5 import QtWidgets, QtGui, QtCore

L1, L2, A, V = 5, 2, 7, 0.075
Initial_value = np.array([[2.9, 5.1, 5, 0, 0],
                          [3.1, 1, -122, 0, 0],
                          [5, 3, -25, 0, 0]]) 
(a, b, R, L, alpha) = mn.arc_params_calculating(Initial_value)
T = mn.Time(L, V, A)
X, Y = mn.arc_equation(Initial_value, a, b, R, L, alpha)
Q1, Q2, Q3 = mn.Q1_Q2_Q3_values(Initial_value, X, Y, L1, L2)
X_L1, X_L2, Y_L1, Y_L2 = mn.coordinates_for_every_unit(Q1, Q2, Q3, L1, L2) 

class MainWindow(QtWidgets.QMainWindow, M_app.Ui_MainWindow):
    
    def __init__(self, Q1, Q2, Q3, T, X_L1, X_L2, Y_L1, Y_L2):
        super().__init__()
        
        self.T = T
        self.Q1 = Q1
        self.Q2 = Q2
        self.Q3 = Q3
        self.X_L1 = X_L1
        self.X_L2 = X_L2
        self.Y_L1 = Y_L1
        self.Y_L2 = Y_L2
        self.home()

    def home(self):
        self.setupUi(self)
        self.Velosity_plot_btn.clicked.connect(self.Velosity_plot)
        self.Axeleration_plot_btn.clicked.connect(self.Axeleration_plot)
        self.Moving_plot_btn.clicked.connect(self.Moving_plot)
        self.Trajectory_plot_btn.clicked.connect(self.Trajectory_plot)
        self.show()       

    def Velosity_plot(self):
        _Q1, _Q2, _Q3 = mn.Q_velosity(Q1, Q2, Q3, T)     
        return mn.Q_plot(_Q1, _Q2, _Q3, T)

    def Axeleration_plot(self):
        _Q1, _Q2, _Q3 = mn.Q_axeleration(Q1, Q2, Q3, T)     
        return mn.Q_plot(_Q1, _Q2, _Q3, T)

    def Moving_plot(self):     
        return mn.Q_plot(Q1, Q2, Q3, T)

    def Trajectory_plot(self):     
        fig = plt.figure(figsize=[5,5])
        ax = fig.add_subplot(111, autoscale_on=False, xlim=(-1, 6), ylim=(-1, 6))
        ax.grid()

        line, = ax.plot([], [], 'o-', lw=2)
        way_line, = ax.plot([], [], color='red', lw=1)

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
    
        ani = animation.FuncAnimation(fig, animate, np.arange(1, len(X_L1), 10), 
                                      interval=1, blit=True, init_func=init, repeat=False)         
        plt.show()
    
        return ani

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow(Q1, Q2, Q3, T, X_L1, X_L2, Y_L1, Y_L2)
    window.show()
    app.exec_()
    
if __name__ == '__main__':
    main()


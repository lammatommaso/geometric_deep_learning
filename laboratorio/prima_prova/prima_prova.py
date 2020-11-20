import numpy
from math import exp
from matplotlib import pyplot
from calibrazione import V as V_1
from calibrazione import e_V as e_V_1
from calibrazione import I as i_1
from calibrazione import e_I as e_i_1

x = numpy.linspace(0, 2, 100)
R_1 = 1
fig_1, plot_1 = pyplot.subplots()
plot_1.errorbar(V_1, i_1, e_V_1, e_i_1, barsabove=True, uplims=True, lolims=True, ls = 'none', fmt = '.', capthick = 1)
plot_1.plot(x, R_1*x, label = 'fit')
pyplot.yscale('linear') #log otherwise
plot_1.set_xlabel('Tensione [mV]')
plot_1.set_ylabel('Corrente [mA]')
plot_1.set_title('Calibrazione Oscilloscopio-Multimetro')
plot_1.legend()
fig_1.savefig('Calibrazione.png')

V_2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
i_2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
fig_2, plot_2 = pyplot.subplots()
plot_2.scatter(V_2, i_2, label = 'linear')
pyplot.yscale('linear') #should be log
plot_2.set_xlabel('Tensione [mV]')
plot_2.set_ylabel('Corrente [mA]')
plot_2.set_title('Caratteristica I-V del diodo al Germanio')
plot_2.legend()
fig_2.savefig('Ge.png')

V_3 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
i_3 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
fig_3, plot_3 = pyplot.subplots()
plot_3.scatter(V_3, i_3, label = 'linear')
pyplot.yscale('linear') #should be log
plot_3.set_xlabel('Tensione [mV]')
plot_3.set_ylabel('Corrente [mA]')
plot_3.set_title('Caratteristica I-V del diodo al Silicio')
plot_3.legend()
fig_3.savefig('Si.png')

from BR_Plotter import BR_Plotter
import math
import matplotlib.pyplot as plt
class Surface_Plotter(BR_Plotter):
	def __init__(self, command_line_arguments):
		BR_Plotter.__init__(self, command_line_arguments)

		self.sphere_plot()

	def sphere_plot(self):
		pi = 3.141592653589793
		center = [self.br_object.surface.center[i].real for i in self.indices]
		radius = self.br_object.surface.radius.real
		num_indices = 2
		if num_indices == 2:
			num_samples = 100
			to_2_pi = [ii/ 100.0 * 2*pi for ii in xrange(0, 100)]
			x  = [radius * math.cos(ii) + center[0] for ii in to_2_pi]
			y  = [radius * math.sin(ii) + center[1] for ii in to_2_pi]
			fig = plt.figure()
			plt.plot(x, y)
			self.sphere = fig
			

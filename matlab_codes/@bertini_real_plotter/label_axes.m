%add labels to the current axes
function label_axes(br_plotter)

curr_axis = br_plotter.axes.main;


name1 = br_plotter.BRinfo.var_names{br_plotter.indices(1)};
name2 = br_plotter.BRinfo.var_names{br_plotter.indices(2)};



fontsize = br_plotter.options.fontsizes.labels;
interpreter = 'none';
% interpreter = 'tex';
switch length(br_plotter.indices)
	case {2}
		xlabel(name1, 'interpreter', interpreter,'FontSize',fontsize,'Parent',curr_axis);
		ylabel(name2, 'interpreter', interpreter,'FontSize',fontsize,'Parent',curr_axis);
	case {3}
		name3 = br_plotter.BRinfo.var_names{br_plotter.indices(3)};
		xlabel(name1, 'interpreter', interpreter,'FontSize',fontsize,'Parent',curr_axis);
		ylabel(name2, 'interpreter', interpreter,'FontSize',fontsize,'Parent',curr_axis);
		zlabel(name3, 'interpreter', interpreter,'FontSize',fontsize,'Parent',curr_axis);
	otherwise
			
end
end



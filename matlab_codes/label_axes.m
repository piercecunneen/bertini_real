%add labels to the current axes
function label_axes(ind,BRinfo,curr_axis)
global plot_params
%

switch length(ind)
	case {2}
		xlabel(BRinfo.var_names{ind(1)}, 'interpreter', 'none','FontSize',plot_params.fontsize,'Parent',curr_axis);
		ylabel(BRinfo.var_names{ind(2)}, 'interpreter', 'none','FontSize',plot_params.fontsize,'Parent',curr_axis);
	case {3}
		xlabel(BRinfo.var_names{ind(1)}, 'interpreter', 'none','FontSize',plot_params.fontsize,'Parent',curr_axis);
		ylabel(BRinfo.var_names{ind(2)}, 'interpreter', 'none','FontSize',plot_params.fontsize,'Parent',curr_axis);
		zlabel(BRinfo.var_names{ind(3)}, 'interpreter', 'none','FontSize',plot_params.fontsize,'Parent',curr_axis);
	otherwise
			
end
end


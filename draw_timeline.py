"""
the goal of this file is to generate a timeline of consecutive non-overlapping events
inputs are the durations of these events, and whether we should use Roman or Arab digits to number them
"""
import datetime
import matplotlib.pyplot as plt
import numpy as np

#from the duration in weeks return the starting and end dates of each event
#start_date is a datetime.date object
def get_dates(start_date,durations):
	date_str = [start_date.strftime('%a %d %b')]
	for duration in durations:
		start_date = start_date + datetime.timedelta(days=7*duration)
		date_str.append(start_date.strftime('%a %d %b'))
	return date_str

#draw the timeline
def draw_timeline(start_date,durations):
	fig,ax = plt.subplots(constrained_layout=True)
	ax.set_facecolor('gray')
	ax.set_aspect('equal')

	#compute the x coordinates of the vertical separators
	x_coords = np.cumsum([0]+durations)
	ymax = x_coords[-1]/5
	
	#compute the x labels
	xlabels = get_dates(start_date,durations)

	#plot the vertical separators
	for x in x_coords:
		ax.plot([x,x],[0,ymax],color="black")

	#add text referring to each event
	for i,(x,duration) in enumerate(zip(x_coords,durations)):
		xy = (x+duration/2,ymax/2)
		ax.annotate(str(i+1),xytext=xy,xy=xy)
	
	#plot the horizontal line: arrow pointing from xytext to xy
	ax.annotate("",xytext=(0,0),xy=(x_coords[-1]+0.33,0),arrowprops=dict(arrowstyle="->"))
	
	#draw the labels of both axes
	ax.set_xticks(x_coords)
	ax.set_xticklabels(xlabels,rotation=45)
	ax.tick_params(axis='x',length=0)
	ax.yaxis.set_visible(False)

	#set the limits of both axes
	ax.set_ylim(0,ymax)
	ax.set_xlim(0,x_coords[-1]+0.33)

	#save the figure
	plt.savefig("images/phase_4_timeline.png")

year = 2025
month = 4
day = 23
start_date = datetime.date(year,month,day)
durations = [1,2,2,1,2,3,3,1]

draw_timeline(start_date,durations)
print("done")

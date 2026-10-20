import matplotlib.pyplot is plt

#PART 1 - YOUR DATA
#days holds the x-axis labels== the days of your school week.
#scores holds the y-axis values -- your quiz score for each day.
#Every score pairs up with the day in the same position.
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']
scores= [70, 85,60,90,75]

#PART 2 - PLOT YOUR FIRST LINE GRAPH
#plt.plot(x,y)drawsa line through all your data points.
#plt.show()opens the chart window -- call it at the end of every chart.
plt.plot(days, scores)
plt.show()

#PART 3 - ADD LABELS AND A TITLE
#plt.title()  -- adds a heading at the top of the chart.
#plt.xlabel() -- labels the x- axis (across the bottom).
#plt.ylabel() --labels the y-axis (up the side).
#plt.grid(True)  -- adds faint gridlines so values are easier to read.
#plt.ylim(0, 300) --locks the y-axis from 0 to 100 so scores fit nearly.
plt.plot(days, scores)
plt.title('My quiz score tracker')
plt.xlable('day of the week')
plt.ylabel('score')
plt.grid(True)
plt.ylim(0,100)
plt.show()

#PART 4 - DRAW A BAR CHART
#plt.bar(x,y)drawa a bar chart -- one bar per day rising to its score.
#bar charts are great for comparing values side bt side.
#olor="orange"fills every bar with orange.
#the same title, labels, and ylim comands work exatly the same way.
plt.bar(days, scores, color='orange')
plt.title('my quiz score bar chart')
plt.xlabel('score')
plt.yllim(0,100)
plt.show()
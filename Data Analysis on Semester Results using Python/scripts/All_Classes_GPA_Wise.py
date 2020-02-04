from matplotlib import pyplot as plt
import pandas as pd
from math import ceil
files = ["cse1.txt","cse2.txt","cse3.txt","cse4.txt","cse5.txt","cse6.txt","cse7.txt"]
count = {}
for file in files:
	cse = open(file).read().split()
	df = pd.read_excel("results.xlsx")
	df.set_index("ID",inplace=True)
	Class = dict(zip(range(6,11),[0]*6))
	for i in cse:
		d = list(df.loc[i])[-1]
		if isinstance(d,str):
			Class[6] += 1
		else:
			Class[ceil(d)] += 1
	count[file.split(".")[0]] = Class
w = 0.25
fig = plt.figure(figsize=(20,10))
ax = fig.add_subplot(111)
c ,t  = 0 , 0
l = []
for Class in count:
	y = [count[Class][i] for i in range(6,11)]
	x = [i + w*c for i in range(6,15,2)]
	l.append(ax.bar(x,y,width=0.25,label=Class))
	[ ax.text(x[i],y[i]+0.5,y[i],fontsize=8,weight= "bold",horizontalalignment='center',verticalalignment='center') for i in range(len(y))]
	w = -w
	if (t%2==1):
		pass
	else:
		c +=1
	t += 1
ax.set_xticklabels([1, "FAIL", *[str(i-0.9) + "-" + str(float(i)) for i in range(7,11)] ],fontsize=12)
ax.legend(loc="upper left")
plt.title("All Classes",weight="bold",fontsize=14)
plt.savefig("All_Classes.png")
plt.show()

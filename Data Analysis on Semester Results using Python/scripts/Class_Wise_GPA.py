from matplotlib import pyplot as plt
import pandas as pd
from math import ceil
files = ["CSE-1.txt","CSE-2.txt","CSE-3.txt","CSE-4.txt","CSE-5.txt","CSE-6.txt","CSE-7.txt"]
for file in files:
	cse_id = open(file).read().split()
	df = pd.read_excel("Results.xlsx")
	df.set_index("ID",inplace=True)
	count = {}
	for i in cse_id:
		d = list(df.loc[i])[-1]
		if isinstance(d,str):
			d = d.strip()
		else:
			d = ceil(d)
		if d in count:
			count[d] += 1
		else:
			count[d] = 1
	x = [0 if i=="FAIL" else i for i in list(count.keys())]
	x.sort()
	y = [count["FAIL"] if i==0 else count[i] for i in x]
	fig ,(ax1,ax2) = plt.subplots(1,2,figsize=(20,10))
	ax1.bar(range(len(y)),y)
	fontproperties = {'family':'sans-serif','weight' : "bold", 'size' : 10}
	[ ax1.text(i,y[i]+0.5,y[i],fontsize=12,weight= "bold",horizontalalignment='center',verticalalignment='center') for i in range(len(y))]
	ax1.set_xticklabels([1, "FAIL", *[str(i-0.9) + "-" + str(float(i)) for i in x[1:]]])
	ax1.set_xlabel("GPA",fontproperties)
	ax1.set_ylabel("No_Of_Students",fontproperties)
	ax1.set_title("Count")
	ax2.pie(y,labels=["FAIL",*[str(i-0.9) + "-" + str(float(i)) for i in x[1:]]],autopct="%1.1f%%",textprops={'fontsize': 12})
	ax2.legend(bbox_to_anchor=(1.2, 1),loc="upper right")
	ax2.set_title("Percentage")
	fig.suptitle(file[:5],fontsize=12,weight="bold")
	plt.savefig(file[:5] + ".png")
	plt.show()


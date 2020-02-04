import pandas as pd
from math import ceil
from matplotlib import pyplot as plt
df = pd.read_excel("Results.xlsx")
df.set_index("ID",inplace=True)
count = {}
for i in range(len(df)):
	d = list(df.iloc[i])[-1]
	if isinstance(d,str):
		d = d.strip()
	else:
		d = ceil(d)
	if d in count:
		count[d] += 1
	else:
		count[d] = 1
x = list(count.keys())[::-1]
y = list(count.values())[::-1]
fig ,(ax1,ax2) = plt.subplots(1,2,figsize=(20,10))
ax1.bar(range(len(y)),y)
fontproperties = {'family':'sans-serif','weight' : "bold", 'size' : 10}
[ ax1.text(i,y[i]+3,y[i],fontsize=12,weight= "bold",horizontalalignment='center',verticalalignment='center') for i in range(len(y))]
ax1.set_xticklabels([1, "FAIL", *[str(i-0.9) + "-" + str(float(i)) for i in x[1:]]])
ax1.set_xlabel("GPA",fontproperties)
ax1.set_ylabel("No_Of_Students",fontproperties)
ax1.set_title("Count")
ax2.pie(y,labels=["FAIL",*[str(i-0.9) + "-" + str(float(i)) for i in x[1:]]],autopct="%1.1f%%",textprops={'fontsize': 12})
ax2.legend(bbox_to_anchor=(1.2, 1),loc="upper right")
ax2.set_title("Percentage")
fig.suptitle("E2_CSE-SEM1",fontsize=12,weight="bold")
plt.savefig("Like.png")
plt.show()

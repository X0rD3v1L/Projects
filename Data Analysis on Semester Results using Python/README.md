# Data Analysis on Semester Results using Python.

## How it started?
Hello World,
This a Simple Data Analysis Project which we did in our 2nd year of B.Tech as a part-time and self usage project just to improve our skills.
We scraped the results of our department students who are over 400 in count and we have 5 subjects and 4 Labs,from the results webpage using requests module and scraped the data using BeautifulSoup from bs4 module and plotted the graphs of the data using matplotlib library in python. We analyzed this data in various ways section-wise,gender-wise,subject-wise.This simple project helped us learn on how to analyze huge data and moreover the patterns which we observed in the data were quite interesting.

Team Size : 2 (<a href="github.com/X0r_D3v1L">Benarjee Sambangi</a>,<a href="https://github.com/S0m3-th1ng">Johny Vasamsetti</a>)
<br>
Language used : Python (requests,matplotlib,bs4 modules were used)
<br>
My Role : Programmer

Here are the files attached :

<a href="https://github.com/X0rD3v1L/Projects/blob/master/Data%20Analysis%20on%20Semester%20Results%20using%20Python/scripts/main.py">main.py</a>

```python3

import requests,os,time,pandas as pd
from bs4 import BeautifulSoup as bs
subjects = ["ID","NAME","DAA","OOPS","OS","DBMS","IRB","OOPS_LAB","OS_LAB","DBMS_LAB","ENG_LAB","GPA"]
results_dic = {"Ex":10,"A":9,"B":8,"C":7,"D":6,"WH":0,"AB":0,"R":0}

def get_Result(id):
	r = requests.post("https://████████████████████████████████████████████████.php", data = {"SID":id})
	soup = bs(r.text,"html.parser")
	tr = soup.find('table').findAll('tr')
	student_result = [id,name_dic[id]]
	for row in tr[1:]:
		o = row.findAll('td')
		student_result.append(o[4].text)
	student_result = student_result[:11]
	if any(item in ["WH","R","AB"] for item in student_result):
		student_result.append("FAIL")
	else:
		calc_gpa(student_result)
	return student_result

def calc_gpa(student_result):
	subj_gpa = 0.0
	for i in student_result[2:6]:
		subj_gpa += res_dic[i]*4
	for i in student_result[6:]:
		subj_gpa += res_dic[i]*2
	subj_gpa = round((subj_gpa/26),2)
	student_result.append(subj_gpa)

names = open("Name_CSE.txt").readlines()
name_dic = {}
for i in names:
	i = i.split()
	name_dic[i[0]] = ' '.join(i[1:])
file = open("CSE_IDs.txt").read().split()
main_list = [];gp = []
c = 1
for i in file:
	print(c)
	c +=1
	try:
		data = get_Result(i)
		gp.append(data[-1])
		main_list.append(data)
	except:
		print(i)
		pass
	time.sleep(3)
print(gp)
pd_frame = pd.DataFrame(main_list,columns=subj)
pd_frame.to_excel (r'Results.xlsx', index = None, header=True)
os.system("xdg-open Results.xlsx")

```
With main.py all the results were extracted and stored in a file named Results.xlsx. Results.xlsx contains grades subjects wise and Avg.GPA.This file gave us a major insight to the data inside and now we plotted various graphs on different criterias from this data using matplotlib library in python.

<a href="https://github.com/X0rD3v1L/Projects/blob/master/Data%20Analysis%20on%20Semester%20Results%20using%20Python/scripts/All_Students_Graph.py">All_Students_Graph.py</a>

```python3
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
```
<br>

![All_Students_Graph](/Graphs/All_Students_Graph.png)

<br>

<a href="https://github.com/X0rD3v1L/Projects/blob/master/Data%20Analysis%20on%20Semester%20Results%20using%20Python/scripts/All_Classes_GPA_Wise.py">All_Classes_GPA_Wise.py</a>

```python3
from matplotlib import pyplot as plt
import pandas as pd
from math import ceil
files = ["CSE-1.txt","CSE-2.txt","CSE-3.txt","CSE-4.txt","CSE-5.txt","CSE-6.txt","CSE-7.txt"]
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
```
<br>

![All_Classes_GPA_Wise](/Graphs/All_Classes_GPA_Wise.png)

<br>

<a href="https://github.com/X0rD3v1L/Projects/blob/master/Data%20Analysis%20on%20Semester%20Results%20using%20Python/scripts/Class_Wise_GPA.py">Class_Wise_GPA.py</a>

```python3
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
```
![CSE-1](/Graphs/CSE-1.png)
<br>
![CSE-2](/Graphs/CSE-2.png)
<br>
<br>
![CSE-3](/Graphs/CSE-3.png)
<br>
<br>
![CSE-4](/Graphs/CSE-4.png)
<br>
<br>
![CSE-5](/Graphs/CSE-5.png)
<br>
<br>
![CSE-6](/Graphs/CSE-6.png)
<br>
<br>
![CSE-7](/Graphs/CSE-7.png)
<br>






import requests,os,time,pandas as pd
from bs4 import BeautifulSoup as bs
subjects = ["ID","NAME","DAA","OOPS","OS","DBMS","IRB","OOPS_LAB","OS_LAB","DBMS_LAB","ENG_LAB","GPA"]
results_dic = {"Ex":10,"A":9,"B":8,"C":7,"D":6,"WH":0,"AB":0,"R":0}

def get_Result(id):
	r = requests.post("https://examcell.rguktn.ac.in/results/201920s1-regular/getResult.php", data = {"SID":id})
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

names = open("/home/x0r_d3v1l/Desktop/Python/requests/Results/SEM2/Name_CSE.txt").readlines()
name_dic = {}
for i in names:
	i = i.split()
	name_dic[i[0]] = ' '.join(i[1:])
file = open("/home/x0r_d3v1l/Desktop/Python/requests/Results/SEM2/CSE_IDs.txt").read().split()
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

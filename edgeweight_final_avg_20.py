import numpy as np

from numpy import dot
from numpy.linalg import norm

count = 0
list_temp = []
list_vec = []
list_avg_final = []
list_temp1 = []
node_list = []
node_list_final = []
i = 0
with open('word_all.txt', 'r') as ss:
    for l in ss:
        if count%2 == 0:
                node_list.append(l.split(" ")[0:1])
                list_temp = l.split(" ")[1:]
                list_temp = list_temp[:len(list_temp)-1]
                list_vec.append(list_temp)           
        count = count + 1


#print(len(list_vec))

for i in range(len(list_vec)):
    if len(list_vec[i]) < 300:
        print i

m = 0


for i in range(len(list_vec)):
    if i%2 == 0:
        for k in range(len(list_vec[i])):
            avg = (float(list_vec[i][k]) + float(list_vec[i+1][k]))/2
            list_temp1.append(avg)
        #print i

    #print i


for i in range(len(list_temp1)):
    if i%300 == 0:
        list_avg_final.append(list_temp1[i:i+299])
    i = i + 300

#print(len(list_avg_final))
#print

#print list_avg_final[0]
#print list_avg_final[981]
#print (len(list_avg_final[981]))
#print (len(list_avg_final[0]))

for i in range(len(node_list)):
    if i%2 == 0:
        node_list_final.append(node_list[i][0] + ":" + node_list[i+1][0])


nonseed = []
seed1 = []
seed2 = []
seed3 = []
seed4 = []
seed5 = []
seed6 = []
seed7 = []
seed8 = []
seed9 = []
seed10 = []






seed1.append(list_avg_final[0:20])
seed2.append(list_avg_final[98:118])
seed3.append(list_avg_final[196:216])
seed4.append(list_avg_final[294:314])
seed5.append(list_avg_final[392:412])
seed6.append(list_avg_final[490:510])
seed7.append(list_avg_final[588:608])
seed8.append(list_avg_final[687:707])
seed9.append(list_avg_final[786:806])
seed10.append(list_avg_final[884:904])



seed1 = seed1[0]
seed2 = seed2[0]
seed3 = seed3[0]
seed4 = seed4[0]
seed5 = seed5[0]
seed6 = seed6[0]
seed7 = seed7[0]
seed8 = seed8[0]
seed9 = seed9[0]
seed10 = seed10[0]





nonseed.append(list_avg_final[20:98])
nonseed.append(list_avg_final[118:196])
nonseed.append(list_avg_final[216:294])
nonseed.append(list_avg_final[314:392])
nonseed.append(list_avg_final[412:490])
nonseed.append(list_avg_final[510:588])
nonseed.append(list_avg_final[608:687])
nonseed.append(list_avg_final[707:786])
nonseed.append(list_avg_final[806:884])
nonseed.append(list_avg_final[904:982])

nonseed_final = []

for i in range(len(nonseed)):
        for j in range(len(nonseed[i])):
                nonseed_final.append(nonseed[i][j])




#print node_list_final
temp_list = []
temp1_list =[]
temp2_list = []
temp3_list = []
temp4_list = []
temp5_list = []
temp6_list =[]
temp7_list = []
temp8_list = []
temp9_list = []
temp10_list = []





for i in range(len(nonseed_final)):
    	temp_list = nonseed_final[i]
#   print len(temp_list)
#  print len(nonseed_final)
                                                                                                                            
	for j in range(i+1,len(nonseed_final)):
#     print j
        	cos_sim = dot(temp_list, nonseed_final[j])/(norm(temp_list)*norm(nonseed_final[j]))
        	cos_sim = abs(cos_sim)
		print ("N"+str(i)+"\t"+"N"+str(j)+"\t\t\t\t\t"+str(cos_sim)+"\n")
        	f = open('avg_edgeweight_20.txt','a+')
        	f.write("N"+str(i)+"\t"+"N"+str(j)+"\t"+str(cos_sim)+"\n")
        	f.close()



for i in range(len(seed1)):
        temp1_list = seed1[i]
        for j in range(0,78):
                cos_sim = dot(temp1_list, nonseed_final[j])/(norm(temp1_list)*norm(nonseed_final[j]))
		cos_sim = abs(cos_sim)
        #print nonseed_final[j]
                print ("N"+str(i+782)+"\t"+"N"+str(j)+"\t"+"\t\t\t\t\t"+str(cos_sim)+"\n")
                f = open('avg_edgeweight_20.txt','a+')
                f.write("N"+str(i+782)+"\t"+"N"+str(j)+"\t"+str(cos_sim)+"\n")
                f.close()

for k in range(len(seed2)):
        temp2_list = seed2[k]
        for l in range(0,78):
                cos_sim = dot(temp2_list, nonseed_final[l+78])/(norm(temp2_list)*norm(nonseed_final[l+78]))
		cos_sim = abs(cos_sim)
                print ("N"+str(k+802)+"\t"+"N"+str(l+78)+"\t"+"\t\t\t\t\t"+str(cos_sim)+"\n")
                f = open('avg_edgeweight_20.txt','a+')
                f.write("N"+str(k+802)+"\t"+"N"+str(l+78)+"\t"+str(cos_sim)+"\n")
                f.close()
        #print nonseed_final[l]

for m in range(len(seed3)):
        temp3_list = seed3[m]
        for n in range(0,78):
                cos_sim = dot(temp3_list, nonseed_final[n+156])/(norm(temp3_list)*norm(nonseed_final[n+156]))
		cos_sim = abs(cos_sim)
                print ("N"+str(m+822)+"\t"+"N"+str(n+156)+"\t"+"\t\t\t\t\t"+str(cos_sim)+"\n")
                f = open('avg_edgeweight_20.txt','a+')
                f.write("N"+str(m+822)+"\t"+"N"+str(n+156)+"\t"+str(cos_sim)+"\n")
                f.close()
        #print nonseed_final[n]

for p in range(len(seed4)):
        temp4_list = seed4[p]
        for q in range(0,78):
                cos_sim = dot(temp4_list, nonseed_final[q+234])/(norm(temp4_list)*norm(nonseed_final[q+234]))
		cos_sim = abs(cos_sim)
                print ("N"+str(p+842)+"\t"+"N"+str(q+234)+"\t"+"\t\t\t\t\t"+str(cos_sim)+"\n")
                f = open('avg_edgeweight_20.txt','a+')
                f.write("N"+str(p+842)+"\t"+"N"+str(q+234)+"\t"+str(cos_sim)+"\n")
                f.close()
        #print nonseed_final[q]

for p in range(len(seed5)):
        temp5_list = seed5[p]
        for q in range(0,78):
                cos_sim = dot(temp5_list, nonseed_final[q+312])/(norm(temp5_list)*norm(nonseed_final[q+312]))
                cos_sim = abs(cos_sim)
		print ("N"+str(p+862)+"\t"+"N"+str(q+312)+"\t"+"\t\t\t\t\t"+str(cos_sim)+"\n")
                f = open('avg_edgeweight_20.txt','a+')
                f.write("N"+str(p+862)+"\t"+"N"+str(q+312)+"\t"+str(cos_sim)+"\n")
                f.close()
                
for p in range(len(seed6)):
        temp6_list = seed6[p]
        for q in range(0,78):
                cos_sim = dot(temp6_list, nonseed_final[q+390])/(norm(temp6_list)*norm(nonseed_final[q+390]))
                cos_sim = abs(cos_sim)
		print ("N"+str(p+882)+"\t"+"N"+str(q+390)+"\t"+"\t\t\t\t\t"+str(cos_sim)+"\n")
                f = open('avg_edgeweight_20.txt','a+')
                f.write("N"+str(p+882)+"\t"+"N"+str(q+390)+"\t"+str(cos_sim)+"\n")
                f.close()

for p in range(len(seed7)):
        temp7_list = seed7[p]
        for q in range(0,79):
                cos_sim = dot(temp7_list, nonseed_final[q+469])/(norm(temp7_list)*norm(nonseed_final[q+469]))
                cos_sim = abs(cos_sim)
		print ("N"+str(p+902)+"\t"+"N"+str(q+469)+"\t"+"\t\t\t\t\t"+str(cos_sim)+"\n")
                f = open('avg_edgeweight_20.txt','a+')
                f.write("N"+str(p+902)+"\t"+"N"+str(q+469)+"\t"+str(cos_sim)+"\n")
                f.close()

for p in range(len(seed8)):
        temp8_list = seed8[p]
        for q in range(0,79):
                cos_sim = dot(temp8_list, nonseed_final[q+548])/(norm(temp8_list)*norm(nonseed_final[q+548]))
                cos_sim = abs(cos_sim)
		print ("N"+str(p+922)+"\t"+"N"+str(q+548)+"\t"+"\t\t\t\t\t"+str(cos_sim)+"\n")
                f = open('avg_edgeweight_20.txt','a+')
                f.write("N"+str(p+922)+"\t"+"N"+str(q+548)+"\t"+str(cos_sim)+"\n")
                f.close()

for p in range(len(seed9)):
        temp9_list = seed9[p]
        for q in range(0,78):
                cos_sim = dot(temp9_list, nonseed_final[q+626])/(norm(temp9_list)*norm(nonseed_final[q+626]))
                cos_sim = abs(cos_sim)
		print ("N"+str(p+942)+"\t"+"N"+str(q+626)+"\t"+str(cos_sim)+"\n")
                f = open('avg_edgeweight_20.txt','a+')
                f.write("N"+str(p+942)+"\t"+"N"+str(q+626)+"\t"+str(cos_sim)+"\n")
                f.close()

for p in range(len(seed10)):
        temp10_list = seed10[p]
        for q in range(0,78):
                cos_sim = dot(temp10_list, nonseed_final[q+704])/(norm(temp10_list)*norm(nonseed_final[q+704]))
                cos_sim = abs(cos_sim)
		print ("N"+str(p+962)+"\t"+"N"+str(q+704)+"\t"+str(cos_sim)+"\n")
                f = open('avg_edgeweight_20.txt','a+')
                f.write("N"+str(p+962)+"\t"+"N"+str(q+704)+"\t"+str(cos_sim)+"\n")
                f.close()





print ("This is seed")
print (len(seed1))
print (len(seed1[0]))
#print (len(seed2[0][0]))
print(len(nonseed_final))
print(len(nonseed_final[1]))




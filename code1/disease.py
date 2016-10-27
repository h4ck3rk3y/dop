import  numpy, math
#dengue = nltk.defaultdict(str)

num_disease = 6
num_symptom = 28
disease = numpy.zeros((num_disease, num_symptom))
disease_inv = numpy.zeros((num_disease, num_symptom))
mutual_info = numpy.zeros((num_disease, num_symptom))
info_gain = numpy.zeros((num_disease, num_symptom))
#a = numpy.zeros((num_disease, num_symptom))
#a[0] = [ 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1]

disdata = ['dengue','typhoid','malaria','heartattack','acidreflux','constipation']
classdata= ['fever','fever','fever','heart','digestion','digestion']
'''            0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27 '''
disease[0] = [ 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] #,1 ,1 ,0, 1 ,0]
disease[1] = [ 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
disease[2] = [ 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
disease[3] = [ 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0]
disease[4] = [ 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0]
disease[5] = [ 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1]


disease_inv = 1-disease
#print disease
#print disease[1]*disease[2]

rsum = numpy.zeros((num_disease))
csum = numpy.zeros((num_symptom))
rsumi = numpy.zeros((num_disease))
csumi = numpy.zeros((num_symptom))
msum=0
i=0
j=0
rsum = disease.sum(axis=1)
csum = disease.sum(axis=0)
rsumi = disease_inv.sum(axis=1)
csumi = disease_inv.sum(axis=0)
msum = disease.sum()
msumi = disease_inv.sum()



for i in range (0,num_disease):
    for j in range (0,num_symptom):
        if disease[i][j] != 0:
            mutual_info[i][j] = disease[i][j]*math.log((disease[i][j]*msum*msum)/(rsum[i]*csum[j]))
            info_gain[i][j] = 0
            #info_gain[i][j] = disease[i][j]*math.log((disease[i][j]*msum*msum)/(rsum[i]*csum[j]))
        else:
            mutual_info[i][j] = 0
            info_gain[i][j] = disease_inv[i][j]*math.log((disease_inv[i][j]*msum*msum)/(rsum[i]*(msum-csum[j])))


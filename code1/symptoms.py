import nltk
symptom = nltk.defaultdict(str)
symptom[''] = 0
symptom['headache'] = 1
symptom['vomit'] = 2
symptom['nausea'] = 3
symptom['pain'] = {'eye': 4, 'muscle': 5 ,'chest': 6, 'nerve': 8, 'joint': 9 ,'abdomin': 14 , 'stomach': 14 ,'breast':19,'left arm':20}
symptom['bleed'] = {'gum': 10, 'nose' : 18}#, 'muscle': 5' ,'ligament': 6', 'tendon': 7' ,'nerve': 8', 'joint': 9' }
symptom['chill'] = 7
symptom['itch'] = 11
symptom['rash'] = 12
symptom['fever'] = 13
symptom['diarrhea'] = 15
symptom['bradycardia'] = 16
symptom['dizz'] = 16
symptom['weak'] = 16
symptom['fatigue'] = 16
symptom['malaise'] = 17
symptom['uneas'] = 17
symptom['discomfort'] = 17
symptom['choking']= 21
symptom['sweat']=22
#symptom['breathlessness']=23
symptom['breath']=23
symptom['bitter']=24
symptom['sorethroat']=25
symptom['chestpain']=6
symptom['bowel'] = 26
#symptom['bowel']={'few':26, 'trouble':26}
symptom['stool']={'hard':27, 'small':27}
#print symptom['fatigue']


'''
Symptoms of Heart Attack :
discomfort
pain in chest 
pain in breast bone
pain in left arm
choking
sweating 
shortness of breath

Symptoms of Acid Refluxes:
chest pains which worsens on rest
post meal pain
Bitter taste
Hoarseness
sore throat

Symptoms of Constipation:
    Few bowel movements.
    Trouble having a bowel movement (straining)
    Hard or small stools.
    Swollen abdomen or abdominal pain.
    Vomiting.

Symptoms of Food poisoning:
	abdominal cramps
	diarrhea
	vomiting
	loss of appetite
	mild fever
	weakness
	nausea
	headaches
 
Symptoms of dengue:
headache
vomit
nausea
pain in eye, muscle, ligament, joint, tendon, nerve
bleeding gum
itch
rash
fever

Symptoms of Typhoid:
headache
vomit
diarrhea
nausea
pain in abdomin, muscle
bleeding nose, gums
rash
fever
weak
discomfort

Symptoms of Malaria
lack of a sense of well-being
fatigue - tiredness
fever
prominence of headache
chest pain
abdominal pain
arthralgia
myalgia - muscle pain
diarrhea
Nausea
vomiting
chills
'''

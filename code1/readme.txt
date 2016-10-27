**** REQUIREMENTS ****

- 
Install Python 2.7 win 32bit

- Install numpy
- Install nltk

- Download nltk data

- Install aiml



**** STORING THE PROJECT ****

save the code in local disk C (on windows OS).


**** RUNNING THE CODE****


open command prompt.


using cd command go to the project folder "code1". (we use "cd code1" if the present directory is 'C:').


execute the pythonscript"medical_diagnosis.py" using command " python medical_diagnosis.py ".


then the script asks us the symptom that we have.
 enter the symptoms and press enter.


then there will be some questions asked by the system. answer yes or no appropriately.


this will go on until we are surely able to differentiate a particular disease.
 then the system stops and gives us the corresponding disease. 
it also tells us which class the disease belongs to.


we have implemented the following classes



****HEART RELATED DISEASE****


Symptoms of Heart Attack :

discomfort

pain in chest 

pain in breast bone

pain in left arm

choking

sweating
 
shortness of breath



****DIGESTION RELATED DISEASE****


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




**** FEVER RELATED DISEASE ****
 

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



**** FILES INCLUDED ****


medical_diagnosis.py - analog of main file the analysis begins from here

check.py - contains all the functions to be implemented for analysis
 as well as for the identification 

disease.py - contains the database of disease vs. symptoms and 
	mutual information matrix and information gain matrix

symptoms.py - contains the database of all the diseases


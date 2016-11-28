from django.shortcuts import render
from django.http import HttpResponse

import nltk, re, check, disease
from disease import *
from check import *
import array

from .models import Diagnosis

import pytz

def sentenizer(str): #getting sentences
    sent_tokenizer=nltk.data.load('tokenizers/punkt/english.pickle')
    sents = sent_tokenizer.tokenize(str)
    return sents

def utc_to_local(utc_dt):
    local_tz = pytz.timezone("Asia/Kolkata")
    local_dt = utc_dt.replace(tzinfo=pytz.utc).astimezone(local_tz)
    return local_tz.normalize(local_dt)


def stem(word):
    regexp = r'^(.*?)(ing|ly|ed|ious|ies|ive|es|s|ment|ous)?$'
    stem, suffix = re.findall(regexp, word)[0]
    return stem

def stem2(word):
     regexp = r'^(.*?)(s|ous|ness|iness)?$'
     stem, suffix = re.findall(regexp, word)[0]
     return stem


# Create your views here.
def first_try(request):
    initialise()
    count = 0
    prob = [] #stores problems faced
    symc = [] #symc stores all symptoms
    cp=0


    #cond = raw_input('Enter your current conditions and sufferings if any \n') #input
    request = str(request)
    start = request.find('?')
    end = request.find('#')
    cond = request[start+1:end]
    cond = cond.replace('_',' ')
    ind_sen = sentenizer(cond)
    for num in ind_sen:
        cp = cp+1
        sym = '' #sym stores symptoms in a sentence
        pain = ''
        b_part = ''
        neg = ''
        count=0
        ind_wod = nltk.word_tokenize(num)
        for t in ind_wod:
            t = t.lower()
            if(check_neg(t)== True):
                neg = 'no'
            t1 = stem(t)
            t2 = stem2(t)
            if(check_sym(t1)== True):
                if(sym is not ''):
                    sym = sym + ' and ' + t
                    symc.append(t1)
                else:
                    sym = t
                    symc.append(t1)

                if(sym is not ''):
                    prob.append(neg + ' ' + sym)



    print 'Symptoms Observed are\n'
    j=0

    #print sym_arr
    #print 'Symptoms Matching to that of Dengue\n'

    '''symc stores all the symptoms after the cleaning part'''
    print symc
    sym_arr = get_sym_arr(symc)
    '''sym_arr is an array of 0's and 1's if the symptoms is present sym_arr[symp_number]=1
    else it is 0'''
    print sym_arr
    '''
    d = dis_id2(sym_arr)
    print '\nThe disease with maximum probability is \n'
    print d
    '''

    return HttpResponse(str(sym_arr))


def second_try(request):
    initialise()

    # print request.body

    # print request.META.items()


    regex = re.compile('^HTTP_')
    headers=dict((regex.sub('', header), value) for (header, value)
       in request.META.items() if header.startswith('HTTP_'))

    print headers
    
    user = headers["USERID"]
    print user

    request = str(request)
    start = request.find('?')
    end = request.find('#')
    cond = request[start+1:end-1]
    sym = []
    #sym = array.array('i', (int(t) for t in cond.split(",")))
    sym = map(int, cond.split(","))
    d, diagnosed = dis_id2(sym)

    if diagnosed!=None:
        if diagnosed:
            diagnosis = Diagnosis(disease=d, user_id=user)
            diagnosis.save()
        else:
            diagnosis = Diagnosis(disease="Unsuccesful diagnosis", user_id=user)
            diagnosis.save()


    #d = disdata[2]
    print str(d)
    return  HttpResponse(str(d))


def disease_history(request):
    regex = re.compile('^HTTP_')
    headers=dict((regex.sub('', header), value) for (header, value)
       in request.META.items() if header.startswith('HTTP_'))

    user = headers["USERID"]

    print user

    diseases = Diagnosis.objects.filter(user_id=user).order_by('-created_at')

    print 'ohkay'

    output = []

    for disease in diseases:
        output.append(utc_to_local(disease.created_at).strftime("%H:%M:%S %d-%m-%y") + " " +  disease.disease)


    return HttpResponse(str(','.join(output)))


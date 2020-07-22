from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from app.models import *
from app.trycheck import *
from django.http import HttpResponse
#from google.appengine.api import memcache
from app.word_cloud import *
#from app.gen_keywords import get_keywords
from app.para_phrase import *
import csv
import time
import datetime
from app.grading import *
from app.maketable import *
import random
import re
x=nltk.download('averaged_perceptron_tagger')


@csrf_exempt
def checkcohession(topic,text,category):
	result=check_cohession(text[3:len(text)-4],topic)
	p_rep=str(result['Phrase repitions'])
	s_rep=str(result['Sentence repitions'])
	preplex_score=str(result['Preplexity score'])
	relevance=str(result['RElevance Score'])
	para=str(result['Paragraphs'])
	dictionary_of_paras=result['dictionary']
	table={
			'p_rep':p_rep,
			's_rep':s_rep,
			'preplex_score':preplex_score,
			'relevance':relevance,
			'para':para
	}
	
	context = {
			'data':table,
			'topic':topic
	}
	return context

@csrf_exempt
def checkscore(topic,data,category):
	tk=TweetTokenizer()
	t=tk.tokenize(str(data))
	text=[]
	count=0
	for u in t:
		if len(u)>1:
			text.append(u)
			count+=1
  
	length = count
	spell_details = Check_spelling(str(data))
	spell=spell_details['AB2149uhbdsfuw3847rgfbc']
	spell_err=spell_details['dictionary']
	grammer = Capitalize(str(data[3:len(data)-4]))
	art=check_articles(str(data))
	Graded_result=Main_fun(str(data))
	res=para_phrasing(str(data),topic)
	totalerror=int(spell)+int(grammer)+int(art)

	#print(obj)
	data={}
	table=[]
	values={}
	values['spell']=spell_err
	data={'topic':topic,
				'grade':Graded_result,
				'wordcount':length,
				'para_phrasing':res,
				'spellcheck':spell,
				'grammercheck':grammer,
				'articlecheck':art,
				'error':totalerror,}
	table.append(data)
	values['table']=table
	return values

def version2(text):
	s=contractions(str(text))
	data={}
	table=[]
	data={'contractions':s}
	table.append(data)
	return table

	
@csrf_exempt
def choicemade(request):
	if request.method=="POST":
		content=request.POST.get
		topic = request.POST.get('topic')
		#print(topic)
		text = request.POST.get('essay')
		category=request.POST.get('category')
		import re
		Tag_Re=re.compile(r'<[^>]+>')
		text=Tag_Re.sub('',text)
		#print(text)
		Tag_Re=re.compile(r'<[^>]+>')
		topic=Tag_Re.sub('',topic)
		table={}
		table2={}
		table=checkscore(topic,text,category)
		table2=checkcohession(topic,text,category)
		table3=version2(text)
		t={'table':table,'table2':table2,'table3':table3}
		return render(request,'index.html',{'tags':t})

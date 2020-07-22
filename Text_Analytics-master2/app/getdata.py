import json
from trycheck import *
from perplexity import *
from maketable import *
from para_phrase import *
from grading import *

with open('input.json') as f:
  data = json.load(f)
essay=data['essay']
category=data['category']
title=data['title']
     
word_count=wordcount(essay)         
spell_details = Check_spelling(str(data))
spell=spell_details['AB2149uhbdsfuw3847rgfbc']
spell_err=spell_details['dictionary']
grammer = Capitalize(str(data[3:len(data)-4]))
art=check_articles(str(data))
Graded_result=Main_fun(str(data))
res=para_phrasing(str(data),topic)
totalerror=int(spell)+int(grammer)+int(art)


result=check_cohession(text[3:len(text)-4],topic)
p_rep=str(result['Phrase repitions'])
s_rep=str(result['Sentence repitions'])
preplex_score=str(result['Preplexity score'])
relevance=str(result['RElevance Score'])
para=str(result['Paragraphs'])
dictionary_of_paras=result['dictionary']

x={}
x['wordcount']=word_count
x['spell_details']=spell_details
x['spell_err']=spell_err
x['grammer']=grammer
x['art']=art
x['Graded_result']=Graded_result
x['res']=res
x['totalerror']=totalerror

x['result']=result
x['p_rep']=p_rep
x['s_rep']=s_rep
x['preplex_score']=preplex_score
x['relevance']=relevance
x['para']=para
x['dictionary_of_paras']=dictionary_of_paras

print(x)
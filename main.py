import json
from watson_developer_cloud import NaturalLanguageUnderstandingV1
import watson_developer_cloud.natural_language_understanding.features.v1 as Features
from watson_developer_cloud import NaturalLanguageClassifierV1
import pandas as pd
from classifier import Classifier
import random

natural_language_classifier = NaturalLanguageClassifierV1(
  username="f728e78c-406e-410a-9bb2-cae572f2163d",
  password="Cfzc68q32tbR")

def filternan(filterlist):
	index = len(filterlist) - 1
	filtered = False
	while filtered == False:
		if type(filterlist[index]) != type("asdf"):
			index -= 1
		else:
			filtered = True
	return filterlist[:index]

def getCategory(classeslist):
	classeslist = classeslist['classes']
	classinfo1 = classeslist[0]
	classinfo2 = classeslist[1]
	confidence1 = classinfo1['confidence']
	confidence2 = classinfo2['confidence']
	classname1 = classinfo1['class_name']
	classname2 = classinfo2['class_name']
	if confidence1 > 0.5:
		return classname1
	elif confidence1 + confidence2 > 0.6 and abs(confidence1 - confidence2) < 0.2:
		return classname1 + "," + classname2
	else:
		return "adlib"

def main(input_msg):
	phrase = input_msg
	cid = Classifier().get_cid()
	classeslist = Classifier().classify(cid, phrase)
	categoryname = getCategory(classeslist)
	print categoryname
	df = pd.read_csv('categorizedLyrics.csv')
	try:
		responses = df[categoryname].tolist()
	except:
		responses = df[categoryname.split(",")[0]]
	responses = filternan(responses)
	output = random.choice(responses)
	print output
	return output, categoryname
	

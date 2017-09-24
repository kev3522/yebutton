import json
from watson_developer_cloud import NaturalLanguageUnderstandingV1
import watson_developer_cloud.natural_language_understanding.features.v1 \
  as Features
from watson_developer_cloud import NaturalLanguageClassifierV1


natural_language_classifier = NaturalLanguageClassifierV1(
	  username="f728e78c-406e-410a-9bb2-cae572f2163d",
	  password="Cfzc68q32tbR")

class Classifier():

	def create_classifier(self, filepath):
		with open(filepath, 'rb') as training_data:
			classifier = natural_language_classifier.create(
				training_data=training_data,
				name='Yebutton',
				language='en'
			)

	def remove_classifier(self, class_id):
		classes = natural_language_classifier.remove(class_id)

	def get_classifiers(self):
		classifiers = natural_language_classifier.list()
		return classifiers

	def get_status(self, class_id):
		status = natural_language_classifier.status(class_id)
		return status

	def classify(self, class_id, text):
		classes = natural_language_classifier.classify(class_id, text)
		return classes

	def get_cid(self):
		return self.get_classifiers()["classifiers"][1]["classifier_id"]

#cid = Classifier().get_cid()
#print cid
#print Classifier().get_classifiers()
#print Classifier().classify(cid,"")
#print Classifier().get_status(cid)
#Classifier().create_classifier("outputtraining.csv")
#print Classifier().get_classifiers()
	#create_classifier('runaway.csv')
	#remove_classifier(cid)
	#get_status(cid)
	#classify(cid,"")


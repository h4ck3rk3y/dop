from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Diagnosis(models.Model):
	disease = models.CharField(max_length=100)
	user_id = models.CharField(max_length=100)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	@classmethod
	def create(cls, disease, user_id):
		diagnosis = cls(disease=disease, user_id=user_id)
		return diagnosis

	def __unicode__(self):
		return self.disease + self.user_id + self.time_stamp

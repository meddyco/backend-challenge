from django.db import models


class Specialization(models.Model):
	""" Model for the Specialization of the doctor """
	name = models.CharField('name', max_length=256)
	similar_specializations = models.ManyToManyField(
		'self',
		blank=True,
		symmetrical=True
	)

	def serialize(self):
		"""
		Serialize the clinic object into a JSON serializable object
		"""
		similar_specializations = [
			spec.name for spec in self.similar_specializations.all()
		]
		return {
			"id": self.id,
			"name": self.name,
			"similar_specializations": similar_specializations
		}

	def __str__(self):
		return self.name

class Language(models.Model):
	""" Model for the Language of the doctor """
	name = models.CharField('name', max_length=256)

	def serialize(self):
		"""
		Serialize the clinic object into a JSON serializable object
		"""
		return {
			"id": self.id,
			"name": self.name
		}

	def __str__(self):
		return self.name

class Clinic(models.Model):
	""" Model for the Clinic data of the doctor """
	name = models.CharField('name', max_length=256)

	def serialize(self):
		"""
		Serialize the clinic object into a JSON serializable object
		"""
		return {
			"id": self.id,
			"name": self.name
		}

	def __str__(self):
		return self.name

class Doctor(models.Model):
	""" Model for the Doctor data """
	name = models.CharField('name', max_length=256)
	specialization = models.ForeignKey(
		Specialization, 
		on_delete=models.CASCADE
	)
	clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE)
	languages = models.ManyToManyField(Language)

	def serialize(self):
		"""
		Serialize the doctor object into a JSON serializable object
		"""
		languages = [language.serialize() for language in self.languages.all()]
		return {
			"id": self.id,
			"name": self.name,
			"specialization": self.specialization.serialize(),
			"clinic": self.clinic.serialize(),
			"languages": languages
		}

	def __str__(self):
		return self.name

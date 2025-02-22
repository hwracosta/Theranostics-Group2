from django.db import models
from part_1.models import *
from multiselectfield import MultiSelectField

# class Equipment(models.Model):
#     name = models.CharField(max_length=300,null=True)
#     slug = models.SlugField(null=True)
    
#     def __str__(self):
#         return self.name

#CLASS THERAPY ONLY SUPPORTS ONE ENTRY PER PATIENT AS OF NOW. OPTIMIZE LATER    

class Therapy(models.Model):
    SIDE_EFFECTS = (
        ('Fatigue', 'Fatigue'),
        ('Nausea or Vomiting', 'Nausea or Vomiting'),
        ('Dry Lips or Mouth', 'Dry Lips or Mouth'),
        ('Headache', 'Headache'),
        ('Bone Pain', 'Bone Pain')
    )
    id = models.AutoField(primary_key=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='t_patient')
    date_of_psma = models.DateField()
    premedications = models.CharField(max_length=120, null=True, blank=True)
    medications = models.CharField(max_length=120, null=True, blank=True)
    furosemide = models.BooleanField()
    systolic = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(1, message="Value cannot be zero or negative.")])
    diastolic = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(1, message="Value cannot be zero or negative.")])
    hr = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(1, message="Value cannot be zero or negative.")])
    rr = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(1, message="Value cannot be zero or negative.")])
    saturation = models.FloatField(blank=True, null=True, validators=[MinValueValidator(1.0, message="Value cannot be zero or negative.")])
    date_therapy = models.DateField()
    radiopharm = models.CharField(max_length=120, null=True, blank=True)
    side_effects = MultiSelectField(max_length=120, choices = SIDE_EFFECTS)



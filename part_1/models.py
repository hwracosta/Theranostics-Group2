from django.db import models
from django.core.exceptions import ValidationError
from django.utils.text import slugify
from django.template.defaultfilters import slugify
from datetime import datetime
from django.core.validators import MinValueValidator, MaxValueValidator
from decimal import Decimal

class Patient(models.Model):
    TYPE_TREATMENT = (
        ('Hormonal Treatment', 'Hormonal Treatment'),
        ('Radiation Therapy', 'Radiation Therapy'),
        ('Chemotherapy', 'Chemotherapy'),
        ('Others', 'Others'),
    )
    #Test results and others are put to a different model
    name = models.CharField(max_length=120, blank= False, null=True)
    slug = models.SlugField(null=True)
    age = models.IntegerField()
    address = models.CharField(max_length=300)
    diagnosis_date = models.DateField()
    surgery_date = models.DateField()
    histopath_result = models.ImageField(upload_to="images/")
    histopath_details = models.TextField(max_length=200, blank=False, null=True)
    gleason_score = models.IntegerField(blank=True, null=True)
    date_of_treatment = models.DateField()
    type_of_treatment = models.CharField(max_length=120, choices=TYPE_TREATMENT)

    def __str__(self): 
        return self.name

    #auto-add slugs
    def save(self, *args, **kwargs):  
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

class PhysicalExam(models.Model):
    id = models.AutoField(primary_key=True)
    #slug = AutoSlugField(populate_from='id', unique=True, blank=True, null=True)
    date_recorded = models.DateField(default=datetime.now)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, blank=True, null=True)
    ecog_score = models.IntegerField(blank=True, validators= [MinValueValidator(0, message="Value should be 0-5"), MaxValueValidator(5, message="Value should be 0-5")])
    height = models.IntegerField(blank=True, validators= [MinValueValidator(1, message="Value cannot be zero or negative.")])
    weight = models.DecimalField(max_digits=5, decimal_places=2,blank=True, validators= [MinValueValidator(1, message="Value cannot be zero or negative.")])
    bmi = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)    
    bp = models.CharField(max_length=120, blank=True) # Blood Pressure
    hr = models.IntegerField(blank=True, validators= [MinValueValidator(1, message="Value cannot be zero or negative.")]) # Heart Rate
    pain_score = models.IntegerField(blank=True, validators= [MinValueValidator(0, message="Value should be 0-10"), MaxValueValidator(10, message="Value should be 0-10")])
    local_symptoms = models.CharField(max_length=300, blank=True)
    systemic_symptoms = models.CharField(max_length=300, blank=True)

    def save(self, *args, **kwargs):
   
        if self.height and self.weight and self.height > 0:
            height_in_meters = Decimal(self.height) / 100 
            self.bmi = self.weight / (height_in_meters ** 2)  
        else:
            self.bmi = None 
            
        super().save(*args, **kwargs)


class Screening(models.Model):
    ASSESSMENT = (
        ('Low Risk', 'Low Risk'),
        ('Intermediate Risk', 'Intermediate Risk'),
        ('High Risk', 'High Risk'),
    )
    id = models.AutoField(primary_key=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='screening_patient')
    psa = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, validators= [MinValueValidator(0, message="Value cannot be negative")])
    creatinine = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, validators= [MinValueValidator(0, message="Value cannot be negative")])
    wbc = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, validators= [MinValueValidator(0, message="Value cannot be negative")])
    rbc = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, validators= [MinValueValidator(0, message="Value cannot be negative")])
    hemoglobin = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, validators= [MinValueValidator(0, message="Value cannot be negative")])
    hematocrit = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, validators= [MinValueValidator(0, message="Value cannot be negative")])
    platelet = models.IntegerField(blank=True, null=True, validators= [MinValueValidator(0, message="Value cannot be negative")])
    lactate_hydrogenase = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, validators= [MinValueValidator(0, message="Value cannot be negative")])
    alkaline_phosphatase = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, validators= [MinValueValidator(0, message="Value cannot be negative")])
    sgpt = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, validators= [MinValueValidator(0, message="Value cannot be negative")])
    sgot = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, validators= [MinValueValidator(0, message="Value cannot be negative")])
    bilirubins = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, validators= [MinValueValidator(0, message="Value cannot be negative")])

    SALIVARY_GLAND_STATUS = (
        ('Normal', 'Normal'),
        ('Left Obstruction', 'Left Obstruction'),
        ('Right Obstruction', 'Right Obstruction')
    )
    salivary_gland_status = models.CharField(max_length=120, choices = SALIVARY_GLAND_STATUS)
    salivary_gland_image = models.ImageField(upload_to="images/")

    BONE_METASTASIS_STATUS = (
        ('Metastasis', 'Metastasis'),
        ('No Metastasis', 'No Metastasis')
    )
    bone_metastasis_status = models.CharField(max_length=120, choices = BONE_METASTASIS_STATUS, blank=True, null=True)
    bone_scan_image = models.ImageField(upload_to="images/", null=True)
    renal_scintigraphy = models.ImageField(upload_to="images/")

    GAPSMA = (
        ('GA-68', 'GA-68'),
        ('F-18 PSMA', 'F-18 PSMA')
    )
    gapsma_choices = models.CharField(max_length=120, choices=GAPSMA, blank=True, null=True)
    gapsma_img = models.ImageField(upload_to="images/")

##THIS SEGMENT NEEDS OPTIMIZATION##
    # GAPSMA Lesions
    LESION_STATUS = (
        ('Absent', 'Absent'),
        ('Present', 'Present')
    )
    gapsma_prostate_lesion_status = models.CharField(verbose_name="Prostate Lesion Status", max_length=120, choices = LESION_STATUS, null=True, blank=True)
    gapsma_prostate_location = models.CharField(verbose_name="Prostate Location", max_length=50, null=True, blank=True)
    gapsma_prostate_suv = models.DecimalField(verbose_name="Prostate SUV", max_digits=5, decimal_places=2, blank=True, null=True, validators= [MinValueValidator(0, message="Value cannot be negative")])
    gapsma_prostate_size = models.DecimalField(verbose_name="Prostate Lesion Size", max_digits=5, decimal_places=2, blank=True, null=True, validators= [MinValueValidator(0, message="Value cannot be negative")])

    gapsma_lymph_node_lesion_status = models.CharField(verbose_name="Lymph Node Lesion Status", max_length=120, choices = LESION_STATUS, null=True, blank=True)
    gapsma_lymph_node_location = models.CharField(verbose_name="Lymph Node Location", max_length=50, null=True, blank=True)
    gapsma_lymph_node_suv = models.DecimalField(verbose_name="Lymph Node SUV", max_digits=5, decimal_places=2, blank=True, null=True, validators= [MinValueValidator(0, message="Value cannot be negative")])
    gapsma_lymph_node_size = models.DecimalField(verbose_name="Lymph Node Lesion Size", max_digits=5, decimal_places=2, blank=True, null=True, validators= [MinValueValidator(0, message="Value cannot be negative")])

    gapsma_bone_lesion_status = models.CharField(verbose_name="Bone Lesion Status", max_length=120, choices = LESION_STATUS, null=True, blank=True)
    gapsma_bone_location = models.CharField(verbose_name="Bone Lesion Location", max_length=50, null=True, blank=True)
    gapsma_bone_suv = models.DecimalField(verbose_name="Bone SUV", max_digits=5, decimal_places=2, blank=True, null=True, validators= [MinValueValidator(0, message="Value cannot be negative")])
    gapsma_bone_size = models.DecimalField(verbose_name="Bone Lesion Size", max_digits=5, decimal_places=2, blank=True, null=True, validators= [MinValueValidator(0, message="Value cannot be negative")])

    gapsma_brain_lesion_status = models.CharField(verbose_name="Brain Lesion Status", max_length=120, choices = LESION_STATUS, null=True, blank=True)
    gapsma_brain_location = models.CharField(verbose_name="Brain Lesion Location", max_length=50, null=True, blank=True)
    gapsma_brain_suv = models.DecimalField(verbose_name="Brain SUV", max_digits=5, decimal_places=2, blank=True, null=True, validators= [MinValueValidator(0, message="Value cannot be negative")])
    gapsma_brain_size = models.DecimalField(verbose_name="Brain Lesion Size", max_digits=5, decimal_places=2, blank=True, null=True, validators= [MinValueValidator(0, message="Value cannot be negative")])

    gapsma_lung_lesion_status = models.CharField(verbose_name="Lung Lesion Status", max_length=120, choices = LESION_STATUS, null=True, blank=True)
    gapsma_lung_location = models.CharField(verbose_name="Lung Lesion Location", max_length=50, null=True, blank=True)
    gapsma_lung_suv = models.DecimalField(verbose_name="Lung SUV", max_digits=5, decimal_places=2, blank=True, null=True, validators= [MinValueValidator(0, message="Value cannot be negative")])
    gapsma_lung_size = models.DecimalField(verbose_name="Lung Lesion Size", max_digits=5, decimal_places=2, blank=True, null=True, validators= [MinValueValidator(0, message="Value cannot be negative")])

    gapsma_liver_lesion_status = models.CharField(verbose_name="Liver Lesion Status", max_length=120, choices = LESION_STATUS, null=True, blank=True)
    gapsma_liver_location = models.CharField(verbose_name="Liver Lesion Location", max_length=50, null=True, blank=True)
    gapsma_liver_suv = models.DecimalField(verbose_name="Liver SUV", max_digits=5, decimal_places=2, blank=True, null=True, validators= [MinValueValidator(0, message="Value cannot be negative")])
    gapsma_liver_size = models.DecimalField(verbose_name="Liver Lesion Size", max_digits=5, decimal_places=2, blank=True, null=True, validators= [MinValueValidator(0, message="Value cannot be negative")])

    fdgpetct_img = models.ImageField(upload_to="images/")

    # For fdgpetct

    fdgpetct_prostate_lesion_status = models.CharField(verbose_name="Prostate Lesion Status", max_length=120, choices = LESION_STATUS, null=True, blank=True)
    fdgpetct_prostate_location = models.CharField(verbose_name="Prostate Location", max_length=50, null=True, blank=True)
    fdgpetct_prostate_suv = models.DecimalField(verbose_name="Prostate SUV", max_digits=5, decimal_places=2, blank=True, null=True, validators= [MinValueValidator(0, message="Value cannot be negative")])
    fdgpetct_prostate_size = models.DecimalField(verbose_name="Prostate Lesion Size", max_digits=5, decimal_places=2, blank=True, null=True, validators= [MinValueValidator(0, message="Value cannot be negative")])

    fdgpetct_lymph_node_lesion_status = models.CharField(verbose_name="Lymph Node Lesion Status", max_length=120, choices = LESION_STATUS, null=True, blank=True)
    fdgpetct_lymph_node_location = models.CharField(verbose_name="Lymph Node Location", max_length=50, null=True, blank=True)
    fdgpetct_lymph_node_suv = models.DecimalField(verbose_name="Lymph Node SUV", max_digits=5, decimal_places=2, blank=True, null=True, validators= [MinValueValidator(0, message="Value cannot be negative")])
    fdgpetct_lymph_node_size = models.DecimalField(verbose_name="Lymph Node Lesion Size", max_digits=5, decimal_places=2, blank=True, null=True, validators= [MinValueValidator(0, message="Value cannot be negative")])

    fdgpetct_bone_lesion_status = models.CharField(verbose_name="Bone Lesion Status", max_length=120, choices = LESION_STATUS, null=True, blank=True)
    fdgpetct_bone_location = models.CharField(verbose_name="Bone Lesion Location", max_length=50, null=True, blank=True)
    fdgpetct_bone_suv = models.DecimalField(verbose_name="Bone SUV", max_digits=5, decimal_places=2, blank=True, null=True, validators= [MinValueValidator(0, message="Value cannot be negative")])
    fdgpetct_bone_size = models.DecimalField(verbose_name="Bone Lesion Size", max_digits=5, decimal_places=2, blank=True, null=True, validators= [MinValueValidator(0, message="Value cannot be negative")])

    fdgpetct_brain_lesion_status = models.CharField(verbose_name="Brain Lesion Status", max_length=120, choices = LESION_STATUS, null=True, blank=True)
    fdgpetct_brain_location = models.CharField(verbose_name="Brain Lesion Location", max_length=50, null=True, blank=True)
    fdgpetct_brain_suv = models.DecimalField(verbose_name="Brain SUV", max_digits=5, decimal_places=2, blank=True, null=True, validators= [MinValueValidator(0, message="Value cannot be negative")])
    fdgpetct_brain_size = models.DecimalField(verbose_name="Brain Lesion Size", max_digits=5, decimal_places=2, blank=True, null=True, validators= [MinValueValidator(0, message="Value cannot be negative")])

    fdgpetct_lung_lesion_status = models.CharField(verbose_name="Lung Lesion Status", max_length=120, choices = LESION_STATUS, null=True, blank=True)
    fdgpetct_lung_location = models.CharField(verbose_name="Lung Lesion Location", max_length=50, null=True, blank=True)
    fdgpetct_lung_suv = models.DecimalField(verbose_name="Lung SUV", max_digits=5, decimal_places=2, blank=True, null=True, validators= [MinValueValidator(0, message="Value cannot be negative")])
    fdgpetct_lung_size = models.DecimalField(verbose_name="Lung Lesion Size", max_digits=5, decimal_places=2, blank=True, null=True, validators= [MinValueValidator(0, message="Value cannot be negative")])

    fdgpetct_liver_lesion_status = models.CharField(verbose_name="Liver Lesion Status", max_length=120, choices = LESION_STATUS, null=True, blank=True)
    fdgpetct_liver_location = models.CharField(verbose_name="Liver Lesion Location", max_length=50, null=True, blank=True)
    fdgpetct_liver_suv = models.DecimalField(verbose_name="Liver SUV", max_digits=5, decimal_places=2, blank=True, null=True, validators= [MinValueValidator(0, message="Value cannot be negative")])
    fdgpetct_liver_size = models.DecimalField(verbose_name="Liver Lesion Size", max_digits=5, decimal_places=2, blank=True, null=True, validators= [MinValueValidator(0, message="Value cannot be negative")])

    assessment = models.CharField(max_length=120, choices=ASSESSMENT, blank=True, null=True)
    plan = models.TextField(max_length=120, blank=True, null=True)
 
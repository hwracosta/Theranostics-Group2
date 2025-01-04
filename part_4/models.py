from django.db import models
from part_1.models import Patient
from django.core.validators import MinValueValidator, MaxValueValidator

class FollowUp(models.Model):
    date_of_follow_up = models.DateField()
    ASSESSMENT = (
        ('Low Risk', 'Low Risk'),
        ('Intermediate Risk', 'Intermediate Risk'),
        ('High Risk', 'High Risk'),
    )
    id = models.AutoField(primary_key=True)
    slug = models.SlugField(null=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='fu_patient')
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
    salivary_gland_image = models.ImageField(blank=True)

    BONE_METASTASIS_STATUS = (
        ('Metastasis', 'Metastasis'),
        ('No Metastasis', 'No Metastasis')
    )
    bone_metastasis_status = models.CharField(max_length=120, choices = BONE_METASTASIS_STATUS, blank=True, null=True)
    bone_scan_image = models.ImageField(upload_to="images/")
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
    
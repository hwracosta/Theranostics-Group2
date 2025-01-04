from django.db import models
from part_1.models import Patient
from multiselectfield import MultiSelectField


class PostTherapy(models.Model):
    LESIONS = (
        ('Prostate', 'Prostate'),
        ('Lymph Nodes', 'Lymph Nodes'),
        ('Bones', 'Bones'),
        ('Lungs', 'Lungs'),
        ('Liver', 'Liver'),
    )
    id = models.AutoField(primary_key=True)
    patient = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE,
        related_name='post_therapies'
    )
    date_of_post_therapy = models.DateField()
<<<<<<< Updated upstream
    post_therapy_scan_hours = models.IntegerField(blank=True, null=True)
=======
    post_therapy_scan_hours = models.IntegerField(
        blank=True,
        null=True,
        validators=[MinValueValidator(1, "Value cannot be zero or negative.")]
    )
>>>>>>> Stashed changes
    with_spect_ct = models.BooleanField()
    lesions = MultiSelectField(
        max_length=120,
        choices=LESIONS,
    )
    bone_lesion_details = models.TextField(blank=True, null=True)
    salivary_gland = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        blank=True,
        null=True,
        validators=[MinValueValidator(0.0)]
    )
    kidney_left = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        blank=True,
        null=True,
        validators=[MinValueValidator(0.0)]
    )
    kidney_right = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        blank=True,
        null=True,
        validators=[MinValueValidator(0.0)]
    )

<<<<<<< Updated upstream
    #Dosimetry
    salivary_gland = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    kidney_left = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    kidney_right = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    dosimetry_image = models.ImageField(upload_to="images/")
    
=======
    def __str__(self):
        return f"PostTherapy for {self.patient.name} on {self.date_of_post_therapy}"


# Updated Models for Lesion and Dosimetry Images:
class LesionImage(models.Model):
    post_therapy = models.ForeignKey(
        PostTherapy,
        on_delete=models.CASCADE,
        related_name='lesion_image_set'  # Updated related_name to avoid clashes
    )
    image = models.ImageField(upload_to="lesion_images/")

    def __str__(self):
        return f"Lesion Image for PostTherapy ID {self.post_therapy.id}"


class DosimetryImage(models.Model):
    post_therapy = models.ForeignKey(
        PostTherapy,
        on_delete=models.CASCADE,
        related_name='dosimetry_image_set'  # Updated related_name to avoid clashes
    )
    image = models.ImageField(upload_to="dosimetry_images/")

    def __str__(self):
        return f"Dosimetry Image for PostTherapy ID {self.post_therapy.id}"
>>>>>>> Stashed changes

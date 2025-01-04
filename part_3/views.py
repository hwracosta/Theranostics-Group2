from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from part_1.models import Patient
from .models import PostTherapy, DosimetryImage, LesionImage
from .forms import AddPostTherapy, EditPostTherapy

@login_required
def postTherapyList(request, slug):
    """View to list all PostTherapy records for a specific patient."""
    patient = get_object_or_404(Patient, slug=slug)
    post_therapies = PostTherapy.objects.filter(patient=patient).order_by('-pk')
    context = {'list': post_therapies, 'patient': patient}
    return render(request, 'part_3/post-therapy-list.html', context)


from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .forms import AddPostTherapy
from .models import PostTherapy, LesionImage, DosimetryImage
from part_1.models import Patient

def addPostTherapy(request, slug):
    patient = get_object_or_404(Patient, slug=slug)
    if request.method == "POST":
        form = AddPostTherapy(request.POST, request.FILES)  # Include request.FILES
        if form.is_valid():
            post_therapy = form.save(commit=False)
            post_therapy.patient = patient
            post_therapy.save()

            # Save lesion images
            for lesion_image in request.FILES.getlist('lesion_images'):
                LesionImage.objects.create(post_therapy=post_therapy, image=lesion_image)

            # Save dosimetry images
            for dosimetry_image in request.FILES.getlist('dosimetry_images'):
                DosimetryImage.objects.create(post_therapy=post_therapy, image=dosimetry_image)

            messages.success(request, "Post-therapy record added successfully.")
            return redirect(reverse('patientDetails', kwargs={'slug': slug}))
        else:
            messages.error(request, "There was an error. Please check your input and try again.")
    else:
        form = AddPostTherapy()
    return render(request, "part_3/add-post-therapy.html", {"form": form, "patient": patient})

@login_required
def editPostTherapy(request, slug, id):
    """View to edit an existing PostTherapy record."""
    patient = get_object_or_404(Patient, slug=slug)
    post_therapy = get_object_or_404(PostTherapy, id=id)
    if request.method == "POST":
        form = EditPostTherapy(request.POST, request.FILES, instance=post_therapy)
        if form.is_valid():
            form.save()
            messages.success(request, "Post-therapy record updated successfully.")
            return redirect(reverse('patientDetails', kwargs={'slug': slug}))
        else:
            messages.error(request, "There was an error. Please try again.")
    else:
        form = EditPostTherapy(instance=post_therapy)
    context = {'form': form, 'patient': patient}
    return render(request, "part_3/edit-post-therapy.html", context)


@login_required
def deletePostTherapy(request, slug, id):
    """View to delete an existing PostTherapy record."""
    post_therapy = get_object_or_404(PostTherapy, id=id)
    post_therapy.delete()
    messages.success(request, "Post-therapy record deleted successfully.")
    return redirect(reverse('patientDetails', kwargs={'slug': slug}))

from django.shortcuts import render, get_object_or_404
from contact_app.forms import ContactForm
from django.contrib import messages
from contact_app.models import Contact
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.


def index(request):
    return render(request, 'home.html')


def add_contact(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            mobile_no = form.cleaned_data['mobile_no']
            alt_mobile_no = form.cleaned_data['alt_mobile_no']
            email = form.cleaned_data['email']

            Contact.objects.create(name=name, mobile_no=mobile_no, alt_mobile_no=alt_mobile_no, email=email)
            messages.success(request, 'Your Contact Added Successfully')
            return HttpResponseRedirect(reverse('contact_list'))
        else:
            messages.error(request, 'Your Contacted Not Added')
    return render(request, 'contact-form.html', {'form': form})


def contact_list(request):
    contact = Contact.objects.all().order_by('name')
    return render(request, 'contact-list.html', {'contacts': contact})


def contact_delete(request, contact_id):
    Contact.objects.get(id=contact_id).delete()
    messages.success(request, 'Your Contact Deleted Successfully')
    return HttpResponseRedirect(reverse('contact_list'))


def contact_edit(request, contact_id):
    contact = Contact.objects.get(id=contact_id)
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            mobile_no = form.cleaned_data['mobile_no']
            alt_mobile_no = form.cleaned_data['alt_mobile_no']
            email = form.cleaned_data['email']

            contact.name = name
            contact.mobile_no = mobile_no
            contact.alt_mobile_no = alt_mobile_no
            contact.email = email
            contact.save()

            messages.success(request, 'Your Contact Updated Successfully')
            return HttpResponseRedirect(reverse('contact_list'))
    else:
        data = {'name': contact.name, 'mobile_no': contact.mobile_no, 'alt_mobile_no': contact.alt_mobile_no, 'email': contact.email}
        form = ContactForm(initial=data)
    return render(request, 'contact-form.html', {'form': form})

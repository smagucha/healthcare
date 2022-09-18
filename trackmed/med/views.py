from django.shortcuts import render, HttpResponse, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import Group


@login_required(login_url='/accounts/login/')
def home(request):
	users_in_doctor = Group.objects.get(name="doctor").user_set.all()
	users_in_administer = Group.objects.get(name="administer").user_set.all()
	if request.user in users_in_doctor or request.user in users_in_administer:
		list_patient = PatientBio.objects.all()
		context ={"title":"home page",'list_patient': list_patient}
		return render(request, 'med/home.html', context)
	else:
		getmed = Medication.objects.filter(user=request.user)
		context ={'getmed': getmed}
		return render(request, 'med/patientdashboard.html', context)
	
	
@login_required(login_url='/accounts/login/')
def createpatient(request):
	if request.method == 'POST':
		form = PatientForm(request.POST)
		if form.is_valid:
			form.save()
			return redirect('home')
	else:
		form = PatientForm()

	context ={
		'form': form,
		'title': 'patient data'
	}
	return render(request, 'med/createpatient.html', context)


@login_required(login_url='/accounts/login/')
def updatepatient(request, id):
	patientdata = PatientBio.objects.get(id=id)
	if request.method == 'POST':
		form = PatientForm(request.POST or None, instance = patientdata)
		if form.is_valid:
			form.save()
			return redirect('home')
	else:
		form = PatientForm(instance = patientdata)

	context ={
		'form': form,
		'title': ' update patient data'
	}
	return render(request, 'med/updatepatient.html', context)

def delete_patient(request, id):
  patient = PatientBio.objects.get(id=id).delete()
  return redirect('home')

@login_required(login_url='/accounts/login/')
def viewpatient(request, id):
	patientdata = PatientBio.objects.get(id=id)
	context ={
		'patientdata': patientdata,
		'title': ' view your data'
	}
	return render(request, 'med/viewpatient.html', context)


@login_required(login_url='/accounts/login/')
def createhealtdata(request):
	if request.method == 'POST':
		form = HealthDataForm(request.POST)
		if form.is_valid:
			form.save()
			return redirect('home')
	else:
		form = HealthDataForm()

	context ={
		'form': form,
		'title': 'create health data'
	}
	return render(request, 'med/createhealtdata.html', context)

@login_required(login_url='/accounts/login/')
def list_health_data(request):
	listhealthdata = HealthData.objects.all()
	context = {
		'title': 'patients health data',
		'listhealthdata': listhealthdata
	}
	return render(request,'med/listhealthdata.html', context)


@login_required(login_url='/accounts/login/')
def delete_health_data(request, id):
  patient = HealthData.objects.get(id=id).delete()
  return redirect('home')


@login_required(login_url='/accounts/login/')
def createmedication(request):
	if request.method == 'POST':
		form = DoctorMedForm(request.POST)
		if form.is_valid:
			form.save()
			return redirect('home')
	else:
		form = DoctorMedForm()

	context ={
		'form': form,
		'title': 'create health data'
	}
	return render(request, 'med/createmedication.html', context)


@login_required(login_url = '/accounts/login/')
def list_medication(request):
	listmed = Medication.objects.all()
	context = {
		'title': 'list of medication',
		'listmed': listmed
	}
	return render(request, 'med/listmed.html', context)

@login_required(login_url='/accounts/login/')
def updatemedication(request, id):
	patientdata = Medication.objects.get(id=id)
	if request.method == 'POST':
		form = DoctorMedForm(request.POST or None, instance = patientdata)
		if form.is_valid:
			form.save()
			return redirect('home')
	else:
		form = DoctorMedForm(instance = patientdata)

	context ={
		'form': form,
		'title': ' update patient data'
	}
	return render(request, 'med/updatemedication.html', context)


@login_required(login_url='//login/')
def deletemedication(request, id):
	try:
		patientdata = Medication.objects.get(id=id).delete()
		return redirect('home')
	except ObjectDoesNotExist:
		return redirect('home')


@login_required(login_url ='/accounts/login/')
def create_patient_data(request):
	if request.method == 'POST':
		form = HealthDataForm(request.POST)
		if form.is_valid:
			form.save()
			return redirect('home')
	else:
		form = HealthDataForm()

	context ={
		'form': form,
		'title': 'create patient medical data'
	}
	return render(request, 'med/create_patient_data.html',context)

@login_required(login_url='/accounts/login/')
def list_patient_data(request):
	patientdata = HealthData.objects.all()
	context ={
		'title': 'health data',
		'patientdata': patientdata
	}
	return render(request, 'med/healtdata.html',context)


@login_required(login_url='/accounts/login/')
def update_patient_data(request, id):
	patientdata = HealthData.objects.get(id = id)
	if request.method =="POST":
		form = HealthDataForm(request.POST or None, instance = patientdata)
		if form.is_valid:
			form.save()
			return redirect('home')
	else:
		form =HealthDataForm(instance=patientdata)

	context ={
		'title':'update patient health data',
		'form': form
	}
	return render(request, 'med/updatehealtdata.html',context)


@login_required(login_url='/accounts/login/')
def delete_patient_data(request, id):
	if request.method =="POST":
		patientdata = HealthData.objects.get(id = id).delete()

	context ={
		'title':'update patient health data',
		'patientdata':patientdata
	}
	return render(request, 'med/deletehealtdata.html',context)


@login_required(login_url='/accounts/login/')
def create_medication(request):
	if request.method == 'POST':
		form = DoctorMedForm(request.POST)
		if form.is_valid:
			form.save()
			return redirect('home')
	else:
		form = DoctorMedForm()

	context ={
		'title':'create medication',
		'form': form
	}
	return render(request, 'med/createmedication.html',context)

login_required(login_url='/accounts/login/')
def update_medication(request, id):
	if request.method == 'POST':
		form = DoctorMedForm(request.POST)
		if form.is_valid:
			form.save()
			return redirect('home')
	else:
		form = DoctorMedForm()

	context ={
		'title':'create medication',
		'form': form
	}
	return render(request, 'med/createmedication.html',context)

@login_required(login_url='/accounts/login/')
def patient_view(request):
	patientview = HealthData.objects.filter(user=request.user)
	context ={
		'patientview' :patientview,
	}
	return render(request, 'med/patientview.html',context)

@login_required(login_url='/accounts/login/')
def patient_view_med(request):
	patientviewmed = Medication.objects.filter(user=request.user)
	context ={
		'patientviewmed':patientviewmed,
	}
	return render(request, 'med/patientviewmed.html',context)


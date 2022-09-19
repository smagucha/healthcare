from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("createpatient/", views.createpatient, name="createpatient"),
    path("updatepatient/<int:id>/", views.updatepatient, name="updatepatient"),
    path("viewpatient/<int:id>/", views.viewpatient, name="viewpatient"),
    path("delete_patient<int:id>/", views.delete_patient, name="deletepatient"),
    # path("createhealtdata/", views.createhealtdata, name="createhealtdata"),
    path("createmedication/", views.createmedication, name="createmedication"),
    path("updatemedication/<int:id>/", views.updatemedication, name="updatemedication"),
    path("deletemedication/<int:id>/", views.deletemedication, name="deletemedication"),
    path("create_patient_data/", views.create_patient_data, name="createpatientdata"),
    path("list_health_data/", views.list_health_data, name="listhealthdata"),
    path("list_medication/", views.list_medication, name="listmedication"),
    path(
        "delete_health_data/<int:id>/",
        views.delete_health_data,
        name="deletehealthdata",
    ),
    path("patient_view/", views.patient_view, name="patientview"),
    path("patient_view_med/", views.patient_view_med, name="patientviewmed"),
]

from django.urls import path
from . import views

app_name = 'onboarding'
urlpatterns = (
    path('emr-setup-final/<str:practice_code>', views.emr_setup_final, name='emr_setup_final'),
    path('emis-setup/<str:practice_code>', views.emis_setup, name='emis_setup'),
    path('sign-up/', views.sign_up, name='sign_up'),
    path('code-autocomplete/', views.get_code_autocomplete, name='code_autocomplete'),
    path('name-autocomplete/', views.get_name_autocomplete, name='name_autocomplete'),
    path('emis-polling/<str:practice_code>', views.ajax_emis_polling, name='emis_polling'),
)

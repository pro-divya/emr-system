from django.urls import path
from . import views

app_name = 'onboarding'
urlpatterns = (
    path('emr-setup-final/<str:practice_code>', views.emr_setup_final, name='emr_setup_final'),
    path('emis-setup/<str:practice_code>', views.emis_setup, name='emis_setup'),
    path('sign-up/', views.sign_up, name='sign_up'),
    path('emis-setup-success/', views.emis_setup_success, name='emis_setup_success'),
    path('emis-polling/<str:practice_code>', views.ajax_emis_polling, name='emis_polling'),
    path('step-1/', views.step1, name='step1'),
    path('step-2/<str:practice_code>', views.step2, name='step2'),
    path('step-3/<str:practice_code>', views.step3, name='step3'),
)

from django.shortcuts import render
from django.http import JsonResponse

from organisations.models import NHSGeneralPractice, OrganisationGeneralPractice


def create_organisation(request):
    header_title = 'Add New Organisation'
    return render(request, 'organisations/create_organisation.html', {
        'header_title': header_title,
    })


def get_gporganisation_data(request, **kwargs):
    code = request.GET.get('code', '')
    data = {
        'name': '',
        'address': '',
    }
    if code:
        gp_organisation = NHSGeneralPractice.objects.filter(code=code).first()
        if gp_organisation:
            data = {
                'name': gp_organisation.name,
                'address': ' '.join(
                    (
                        gp_organisation.region,
                        gp_organisation.comm_area,
                        gp_organisation.billing_address_street,
                        gp_organisation.billing_address_city,
                        gp_organisation.billing_address_state,
                        gp_organisation.billing_address_postalcode,
                    )
                )
            }

    if kwargs.get('need_dict'):
        return data

    return JsonResponse(data)


def get_nhs_autocomplete(request):
    data = {
        'items': [
            {
                'text': 'GP Organisations',
                'children': []
            },
            {
                'text': 'NHS Organisations',
                'children': []
            }
        ]
    }
    search = request.GET.get('search', '')
    if search:
        organisation_gps = OrganisationGeneralPractice.objects.filter(live=True).filter(name__icontains=search)
        nhs_gps = OrganisationGeneralPractice.objects.filter(live=False).filter(name__icontains=search)
    else:
        organisation_gps = OrganisationGeneralPractice.objects.filter(live=True).all()[:10]
        nhs_gps = OrganisationGeneralPractice.objects.filter(live=False).filter(name__icontains=search)[:10]

    if organisation_gps.exists():
        for organisation_gp in organisation_gps:
            data['items'][0]['children'].append(
                {'id': organisation_gp.practcode, 'text': organisation_gp.name})

    if nhs_gps.exists():
        for nhs_gp in nhs_gps:
            data['items'][1]['children'].append({'id': nhs_gp.practcode, 'text': nhs_gp.name})

    return JsonResponse(data)

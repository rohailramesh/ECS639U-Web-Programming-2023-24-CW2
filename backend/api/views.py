from django.shortcuts import render
from django.http import JsonResponse
from api.models import Demonstrator_Claim


def test_api_view(request):
    return JsonResponse({"message": "Good response!"})


def get_demonstration_claim(request, claim_id):
    try:
        demo_claim = Demonstrator_Claim.objects.get(id=claim_id)
        demo_claim_data = {
            "ID": demo_claim.id,
            "module_name": demo_claim.module_name,
            "hours_worked": demo_claim.hours_worked,
            "claim_form_submitted": demo_claim.claim_form_submitted,
            "demonstrated_date": demo_claim.demonstrated_date,
        }
        return JsonResponse(demo_claim_data)
    except Demonstrator_Claim.DoesNotExist:
        return JsonResponse({"Error": "Claim not found"}, status=404)

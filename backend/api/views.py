import json
from django.shortcuts import render
from django.http import JsonResponse
from api.models import Demonstrator_Claim
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST, require_http_methods


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


@csrf_exempt
@require_POST
def add_demonstration_claim(request):
    try:
        demo_claim_data = json.loads(request.body)

        module_name = demo_claim_data.get("module_name")
        hours_worked = demo_claim_data.get("hours_worked")
        claim_form_submitted = demo_claim_data.get("claim_form_submitted")
        demonstrated_date = demo_claim_data.get("demonstrated_date")

        if module_name:
            # Create a Demonstrator_Claim instance
            demo_claim = Demonstrator_Claim(
                module_name=module_name,
                hours_worked=hours_worked,
                claim_form_submitted=claim_form_submitted,
                demonstrated_date=demonstrated_date,
            )
            demo_claim.save()
            return JsonResponse(
                {"message": "Demonstrator claim form added successfully"}
            )
        else:
            return JsonResponse(
                {"message": "Demonstrator claim form not added"}, status=400
            )

    except json.JSONDecodeError as e:
        return JsonResponse({"message": f"Invalid JSON data: {str(e)}"}, status=400)

    except Exception as e:
        return JsonResponse({"message": str(e)}, status=500)


@csrf_exempt
def deleteClaim(request, claim_id):
    if request.method == "DELETE":
        try:
            claim = Demonstrator_Claim.objects.get(id=claim_id)
            claim.delete()
            return JsonResponse({"message": "claim deleted successfully"})
        except Demonstrator_Claim.DoesNotExist:
            return JsonResponse({"message": "claim not found"}, status=404)


@csrf_exempt
def updateClaim(request, claim_id):
    try:
        claim = Demonstrator_Claim.objects.get(id=claim_id)
        if request.method == "PUT":
            # Handle PUT request to update the claim form
            data = json.loads(request.body)
            new_module_name = data.get("module_name")
            new_hours_worked = data.get("hours_worked")
            new_claim_form_submitted = data.get("claim_form_submitted")
            new_demonstrated_date = data.get("demonstrated_date")

            if new_module_name:
                claim.module_name = new_module_name
                claim.hours_worked = new_hours_worked
                claim.claim_form_submitted = new_claim_form_submitted
                claim.demonstrated_date = new_demonstrated_date
                claim.save()
                return JsonResponse({"message": "Claim was updated successfully"})
            else:
                return JsonResponse({"error": "Field is required"}, status=400)
    except Demonstrator_Claim.DoesNotExist:
        return JsonResponse({"error": "Claim form not found"}, status=404)
    except Exception as e:
        return JsonResponse(
            {"error": str(e)}, status=500
        )  # Handle any other exceptions

"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .views import (
    test_api_view,
    get_demonstration_claim,
    add_demonstration_claim,
    deleteClaim,
    updateClaim,
    get_all_claims,
)


urlpatterns = [
    # API entry points should be defined here
    path("test.json", test_api_view, name="api test"),
    path(
        "demonstrator_claim/<int:claim_id>",
        get_demonstration_claim,
        name="get_demo_claim",
    ),
    path("addDemoClaim", add_demonstration_claim, name="addDemoClaim"),
    path("deleteClaim/<int:claim_id>", deleteClaim, name="deleteClaim"),
    path("updateClaim/<int:claim_id>", updateClaim, name="updateClaim"),
    path("allClaims", get_all_claims, name="all_claims"),
]

"""Module docstring."""

# pages/api_views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response

from listings.models import Listing
from listings.serializers import ListingSerializer  # Importe os serializers
from realtors.models import Realtor
from realtors.serializers import RealtorSerializer


@api_view(["GET"])  # Define que esta view aceita apenas requisições GET
def latest_listings_api(request):
    """
    Retorna os 3 últimos anúncios publicados.
    Este texto aparecerá na documentação do Swagger!
    """
    listings = Listing.objects.order_by(
        "-list_date").filter(is_published=True)[:3]
    # many=True para listas de objetos
    serializer = ListingSerializer(listings, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def about_realtors_api(request):
    """
    Retorna uma lista de todos os corretores e uma lista separada dos corretores MVP.
    """
    realtors = Realtor.objects.order_by("-hire_date")
    mvp_realtors = Realtor.objects.all().filter(is_mvp=True)

    # Serializa os dados
    realtors_serializer = RealtorSerializer(realtors, many=True)
    mvp_realtors_serializer = RealtorSerializer(mvp_realtors, many=True)

    # Monta a resposta JSON
    data = {
        "all_realtors": realtors_serializer.data,
        "mvp_realtors": mvp_realtors_serializer.data,
    }

    return Response(data)

from django.shortcuts import render
from .serializers import ReverseGeocodingSerializer
import urllib.request
import os
import json
from rest_framework.decorators import api_view
from rest_framework.response import Response

MAPBOX_BASE_URL = "https://api.mapbox.com/search/geocode/v6"

@api_view(['GET'])
def reverse_geocode(request):
    """
    Return address given latitude and longitude

    Query Params:
    - latitude: number
    - longitude: number

    Response:
    - buildingNumber: number
    - street: string
    - city: string
    - region: string
    - country: string
    """

    serializer = ReverseGeocodingSerializer(data = request.query_params)

    if serializer.is_valid():
        req_data = serializer.validated_data

        latitude = req_data["latitude"]
        longitude = req_data["longitude"]
        api_token = os.getenv("MAPBOX_API_TOKEN")

        url=f"{MAPBOX_BASE_URL}/reverse?latitude={latitude}&longitude={longitude}&access_token={api_token}"

        try:
            with urllib.request.urlopen(url) as response:
                if response.status < 200 or response.status >= 300:
                    print(f"Failed to get response from mapbox, Status: {response.status}")
                    return Response(None, status=500)
                
                json_str = response.read().decode("utf-8")
                data = json.loads(json_str)

                features = data.get("features")
                feature = features[0] if features else None

                if feature is None:
                    print("Features from mapbox response is None")
                    return Response(None, status=500)
                
                ctx = feature.get("properties", {}).get("context")

                if ctx is None:
                    print("Context from mapbox response is None")
                    return Response(None, status=500)

                building_number = ctx.get("address", {}).get("address_number")
                street = ctx.get("address", {}).get("street_name")
                city = ctx.get("place", {}).get("name")
                region = ctx.get("region", {}).get("name")
                country = ctx.get("country", {}).get("name")

                ret = {
                    "building_number": building_number,
                    "street": street,
                    "city": city,
                    "region": region,
                    "country": country
                }

                return Response(ret, status=200)

        except Exception as e:
            print(f"Error getting response from mapbox: {e}")
            return Response(None, status=500)
    
    return Response(serializer.errors, status=400)
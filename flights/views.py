from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import NotFound


from .models import Flight
from .serializers import FlightSerializer


class FlightListView(APIView):

    def get(self, _request):
        flights = Flight.objects.all()
        serialized_flights = FlightSerializer(flights, many=True)
        return Response(serialized_flights.data, status=status.HTTP_200_OK)
    def post(self, request):
        new_flight = FlightSerializer(data=request.data)
        if new_flight.is_valid():
            new_flight.save()
            return Response(new_flight.data, status=status.HTTP_201_CREATED)
        return Response(new_flight.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)


class FlightDetailView(APIView):

    def get_flight(self, pk):
        try:
            return Flight.objects.get(pk=pk)
        except Flight.DoesNotExist:
            raise NotFound(detail='flight not found')

    def get(self, _request, pk):
        flight = self.get_flight(pk=pk)
        serialized_flight = FlightSerializer(flight)
        return Response(serialized_flight.data, status=status.HTTP_200_OK)


    def put(self, request, pk):
        flight_to_update = self.get_flight(pk=pk)
        updated_flight = FlightSerializer(flight_to_update, data=request.data)
        if updated_flight.is_valid():
            updated_flight.save()
            return Response(updated_flight.data, status=status.HTTP_202_ACCEPTED)
        return Response(updated_flight.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)


    def delete(self, _request, pk):
        flight_to_delete = self.get_flight(pk=pk)
        flight_to_delete.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


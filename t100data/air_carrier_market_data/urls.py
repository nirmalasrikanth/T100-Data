# urls.py
from django.urls import path
from . views import MarketDataList, MaxFreightCarrier, \
                    Top5AirportsPaxByOrigin, \
                    Top5AirportsPaxByDestination, \
                    Top5AirportsFreightByOrigin, \
                    Top5AirportsFreightByDestination, \
                    Top5AirportsMailsByOrigin, \
                    Top5AirportsMailsByDestination, \
                    Top5AirportsDistanceByOrigin, \
                    Top5AirportsDistanceByDestination, \
                    TopPassengersByMonth, \
                    MaxFreightCarrier, \
                    MaxPassengersCarrier, \
                    MaxMailsCarrier, \
                    MaxDistanceCarrier, \
                    TopAirlineByPassengersMonth, \
                    AirlineByAvgPassengersMonth, \
                    MaxFreightLongestDistance, \
                    MaxMailShortestDistance, \
                    AirlineByAvgFreightMonth, \
                    TopDistanceByMonth         


urlpatterns = [
    path('list/', MarketDataList.as_view(), name="list"),
    path('top5paxorigin/', 
        Top5AirportsPaxByOrigin.as_view(
            extra_context={'title': "Top 5 Airports - Passengers by Origin Airport"}
        ),
        name="top5paxorigin"),
    path('top5paxdestination/',  
        Top5AirportsPaxByDestination.as_view(
            extra_context={'title': "Top 5 Airports - Passengers by Destination Airport"}
        ), 
        name="top5paxdestination"),
    path('topdistance_month/',  
        TopDistanceByMonth.as_view(
            extra_context={'title': "Top Distance by Month"}
        ), 
        name="topdistance_month"),
    path('top5freightorigin/', 
        Top5AirportsFreightByOrigin.as_view(
            extra_context={'title': "Top 5 Airports - Freight by Origin Airport"}
        ),
        name="top5freightorigin"),

    path('top5freightdestination/',  
        Top5AirportsFreightByDestination.as_view(
            extra_context={'title': "Top 5 Airports - Freight by Destination Airport"}
        ), 
        name="top5freightdestination"),
    
    path('top5mailorigin/', 
        Top5AirportsMailsByOrigin.as_view(
            extra_context={'title': "Top 5 Airports - Mails by Origin Airport"}
        ),
        name="top5mailorigin"),

    path('top5maildestination/',  
        Top5AirportsMailsByDestination.as_view(
            extra_context={'title': "Top 5 Airports - Mails by Destination Airport"}
        ), 
        name="top5maildestination"),

    path('top5distanceorigin/', 
        Top5AirportsDistanceByOrigin.as_view(
            extra_context={'title': "Top 5 Airports - Distance by Origin Airport"}
        ),
        name="top5distanceorigin"),

    path('top5distancedestination/',  
        Top5AirportsDistanceByDestination.as_view(
            extra_context={'title': "Top 5 Airports - Distance by Destination Airport"}
        ), 
        name="top5distancedestination"),
    
    path('toppassengers_month/',  
        TopPassengersByMonth.as_view(
            extra_context={'title': "Top Passengers by Month"}
        ), 
        name="toppassengers_month"),
    path('maxfreightcarrier/',  
        MaxFreightCarrier.as_view(
            extra_context={'title': "Airline with Most Freight"}
        ), 
        name="maxfreightcarrier"),

     path('maxpaxcarrier/',  
        MaxPassengersCarrier.as_view(
            extra_context={'title': "Airline with Most Passengers"}
        ), 
        name="maxpaxcarrier"),

    path('maxmailcarrier/',  
        MaxMailsCarrier.as_view(
            extra_context={'title': "Airline with Most Mails"}
        ), 
        name="maxmailcarrier"),

    path('maxdistancecarrier/',  
        MaxDistanceCarrier.as_view(
            extra_context={'title': "Airline with Longest Distance"}
        ), 
        name="maxdistancecarrier"),

    path('maxpaxcarriermonth/',  
        TopAirlineByPassengersMonth.as_view(
            extra_context={'title': "Airline Ranking with Most Passengers by Month"}
        ), 
        name="maxpaxcarriermonth"),

    path('avgpaxcarriermonth/',  
        AirlineByAvgPassengersMonth.as_view(
            extra_context={'title': "Airline Ranking with Average number of Passengers by Month"}
        ), 
        name="avgpaxcarriermonth"),

    path('avgfreightcarriermonth/',  
        AirlineByAvgFreightMonth.as_view(
            extra_context={'title': "Airline Ranking with Average Volume of Freight by Month"}
        ), 
        name="avgfreightcarriermonth"),

    path('maxfreightlongestdistance/',  
        MaxFreightLongestDistance.as_view(
            extra_context={'title': "City Pair with most Freight for longest distance"}
        ), 
        name="maxfreightlongestdistance"),


    path('maxmailshortestdistance/',  
        MaxMailShortestDistance.as_view(
            extra_context={'title': "City Pair with most Mail for shortest distance"}
        ), 
        name="maxmailshortestdistance"),

]
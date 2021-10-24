# Create your views here.
import pdb
from django.db.models.aggregates import Avg
from django.views.generic import ListView
from django.db.models import Max, Sum, Avg, Min
from django.db.models.functions import Round, Greatest

from . models import MarketData

class MarketDataList(ListView):
    model = MarketData

# What are the top 5 airports in terms of: Total passengers by origin
class Top5AirportsPaxByOrigin(ListView):
    context_object_name = "airport_list"
    queryset = MarketData.objects \
                        .values('orig_iata_code','orig_city_name') \
                        .annotate(total_pax=Sum('passengers')) \
                        .order_by('-total_pax')[0:5]
    template_name="rankorder_list_origin.html"
 

# What are the top 5 airports in terms of: Total passengers by destination
class Top5AirportsPaxByDestination(ListView):
    context_object_name = "airport_list"
    queryset = MarketData.objects.values('dest_iata_code','dest_city_name') \
                                 .annotate(total_pax=Sum('passengers')) \
                                 .order_by('-total_pax')[0:5]
    template_name="rankorder_list_destination.html"


# Which airport reported the longest distance by month?
class TopDistanceByMonth(ListView):
    context_object_name = "airport_list"
    template_name="rankorder_list_origin_distance_month.html"

    def get_queryset(self):

        month_list = []

        # pdb.set_trace()

        # there are six months worth of data
        # not good ultimately as this is a "hard-coded" fore-knowledge of the data
        for month in range(1,7):
            queryset = MarketData.objects \
                .values('orig_iata_code',
                        'orig_city_name',
                        'dest_iata_code',
                        'dest_city_name',
                        'month') \
                .filter(month__exact=month) \
                .annotate(total_distance=Max('distance')) \
                .order_by('-total_distance')[0:1]
            
        
            
            # off by one error for assignment

            month_list.append(queryset)

        # return list
        return month_list


# What are the top 5 airports in terms of: Total Freights by origin
class Top5AirportsFreightByOrigin(ListView):
    context_object_name = "airport_list"
    queryset = MarketData.objects \
                        .values('orig_iata_code','orig_city_name') \
                        .annotate(total_freight=Sum('freight')) \
                        .order_by('-total_freight')[0:5]
    template_name="rankorder_freight_origin.html"

# What are the top 5 airports in terms of: Total Freight by destination
class Top5AirportsFreightByDestination(ListView):
    context_object_name = "airport_list"
    queryset = MarketData.objects.values('dest_iata_code','dest_city_name') \
                                 .annotate(total_freight=Sum('freight')) \
                                 .order_by('-total_freight')[0:5]
    template_name="rankorder_freight_destination.html"

# What are the top 5 airports in terms of: Total Mails by origin
class Top5AirportsMailsByOrigin(ListView):
    context_object_name = "airport_list"
    queryset = MarketData.objects \
                        .values('orig_iata_code','orig_city_name') \
                        .annotate(total_mail=Sum('mail')) \
                        .order_by('-total_mail')[0:5]
    template_name="rankorder_mail_origin.html"

# What are the top 5 airports in terms of: Total mails by destination
class Top5AirportsMailsByDestination(ListView):
    context_object_name = "airport_list"
    queryset = MarketData.objects.values('dest_iata_code','dest_city_name') \
                                 .annotate(total_mail=Sum('mail')) \
                                 .order_by('-total_mail')[0:5]
    template_name="rankorder_mail_destination.html"

# What are the top 5 airports in terms of: Total distance by origin
class Top5AirportsDistanceByOrigin(ListView):
    context_object_name = "airport_list"
    queryset = MarketData.objects \
                        .values('orig_iata_code','orig_city_name') \
                        .annotate(total_distance=Sum('distance')) \
                        .order_by('-total_distance')[0:5]
    template_name="rankorder_distance_origin.html"

# What are the top 5 airports in terms of: Total distance by destination
class Top5AirportsDistanceByDestination(ListView):
    context_object_name = "airport_list"
    queryset = MarketData.objects.values('dest_iata_code','dest_city_name') \
                                 .annotate(total_distance=Sum('distance')) \
                                 .order_by('-total_distance')[0:5]
    template_name="rankorder_distance_destination.html"


# Which airport reported the most passengers by month?
class TopPassengersByMonth(ListView):
    context_object_name = "airport_list"
    template_name="rankorder_pax_month.html"

    def get_queryset(self):

        month_list = []

        # pdb.set_trace()

        # there are six months worth of data
        # not good ultimately as this is a "hard-coded" fore-knowledge of the data
        for month in range(1,7):
            queryset = MarketData.objects \
              .values('orig_iata_code',
                        'orig_city_name',
                        'dest_iata_code',
                        'dest_city_name',
                        'month') \
                .filter(month__exact=month) \
                .annotate(total_passengers=Max('passengers')) \
                .order_by('-total_passengers')[0:1]
            
            # off by one error for assignment

            month_list.append(queryset)

        # return list
        return month_list

# Which airline carried the most freight
class MaxFreightCarrier(ListView):
    context_object_name = "airport_list"
    queryset = MarketData.objects \
                        .values('carrier_id','carrier_name') \
                        .annotate(max_freight=Sum('freight')) \
                        .order_by('-max_freight')[0:1]
    template_name="maxfreight_airline.html"

# Which airline carried the most passengers
class MaxPassengersCarrier(ListView):
    context_object_name = "airport_list"
    queryset = MarketData.objects \
                        .values('carrier_id','carrier_name') \
                        .annotate(max_pax=Sum('passengers')) \
                        .order_by('-max_pax')[0:1]
    template_name="maxpassenger_airline.html"

# Which airline carried the longest distance
class MaxDistanceCarrier(ListView):
    context_object_name = "airport_list"
    queryset = MarketData.objects \
                        .values('carrier_id',
                        'carrier_name',
                        'orig_iata_code',
                        'orig_city_name',
                        'dest_iata_code',
                        'dest_city_name') \
                        .annotate(max_distance=Max('distance')) \
                        .order_by('-max_distance')[0:1]
    template_name="maxdistance_airline.html"

# Which airline carried the most mails
class MaxMailsCarrier(ListView):
    context_object_name = "airport_list"
    queryset = MarketData.objects \
                        .values('carrier_id','carrier_name') \
                        .annotate(max_mail=Sum('mail')) \
                        .order_by('-max_mail')[0:1]
    template_name="maxmail_airline.html"

# Rank airline based on most passengers by month?
class TopAirlineByPassengersMonth(ListView):
    context_object_name = "airport_list"
    template_name="maxpassenger_airlinemonth.html"

    def get_queryset(self):

        month_list = []

        # pdb.set_trace()

        # there are six months worth of data
        # not good ultimately as this is a "hard-coded" fore-knowledge of the data
        for month in range(1,7):
            queryset = MarketData.objects \
                .values('carrier_id',
                        'carrier_name',
                        'month') \
                .filter(month__exact=month, carrier_id__in = ["AA","AS", "DL", "UA", "WN"]) \
                .annotate(total_passengers=Sum('passengers')) \
                .order_by('-total_passengers')

                        
            # off by one error for assignment

            month_list.append(queryset)

        # return list
        return month_list

# Rank airline based on average number of passengers by month?
class AirlineByAvgPassengersMonth(ListView):
    context_object_name = "airport_list"
    template_name="avgpassenger_airlinemonth.html"

    def get_queryset(self):

        month_list = []

        # pdb.set_trace()

        # there are six months worth of data
        # not good ultimately as this is a "hard-coded" fore-knowledge of the data
        for month in range(1,7):
            queryset = MarketData.objects \
                .values('dest_iata_code',
                        'dest_city_name',
                        'month') \
                .filter(month__exact=month, dest_iata_code__in = ["LAX","SFO", "DFW", "ATL", "ORD"]) \
                .annotate(avg_passengers=Round(Avg('passengers'))) \
                .order_by('-avg_passengers')

                      
            # off by one error for assignment

            month_list.append(queryset)

        # return list
        return month_list

# Rank airline based on average volume of freight by month?
class AirlineByAvgFreightMonth(ListView):
    context_object_name = "airport_list"
    template_name="avgfreight_airlinemonth.html"

    def get_queryset(self):

        month_list = []

        # pdb.set_trace()

        # there are six months worth of data
        # not good ultimately as this is a "hard-coded" fore-knowledge of the data
        for month in range(1,7):
            queryset = MarketData.objects \
                .values('orig_iata_code',
                        'orig_city_name',
                        'month') \
                .filter(month__exact=month, orig_iata_code__in = ["MIA","MEM", "JFK", "ANC", "SDF"]) \
                .annotate(avg_freight=Round(Avg('freight'))) \
                .order_by('-avg_freight')

                      
            # off by one error for assignment

            month_list.append(queryset)

        # return list
        return month_list



# Which airline carried the most freight for the longest distance
class MaxFreightLongestDistance(ListView):
    context_object_name = "airport_list"
    queryset = MarketData.objects \
                        .values('month',
                        'carrier_id',
                        'carrier_name',
                        'orig_iata_code',
                        'orig_city_name',
                        'dest_iata_code',
                        'dest_city_name',
                        'freight') \
                        .annotate(max_distance=Max('distance')) \
                        .order_by('-freight')[0:1]
    
    template_name="mostfreight_longestdistance.html"


# Which airline carried the most mail for the shortest distance
class MaxMailShortestDistance(ListView):
    context_object_name = "airport_list"
    queryset = MarketData.objects \
                        .values('month',
                        'carrier_id',
                        'carrier_name',
                        'orig_iata_code',
                        'orig_city_name',
                        'dest_iata_code',
                        'dest_city_name',
                        'mail') \
                        .annotate(min_distance=Min('distance')) \
                        .order_by('-mail')[0:1]
    
    template_name="mostmail_shortestdistance.html"
   

import csv
from  airport import Airport
from  flight import Flight 
class FlightMap:

    pathAeroport  = '/Users/tahagargouri/Downlads/TP1/aeroports.csv'    
    pathFlights  = '/Users/tahagargouri/Downlads/TP1/flights.csv'    

    def __init__(self) :
        self.airports = []
        self.flights =[]

    def import_airport(self,csv_file:str):

        with open(csv_file) as csvfile:
            for line in csvfile :
                name, code , lat, long = line.strip().split('.')
                airport = Airport(name, code , float(lat), float(long))
                self.airports[code] = airport
    

    def import_flights(self,csv_file:str):
     with open (csv_file) as csvfile :
        for line in csvfile:

            src_code , dst_code , duration = line.strip().split('.')
            flight = flight(src_code, dst_code, float(duration))
            self.flights.append(flight)



def airports(self) -> list[Airport]:
    return list(self.airports.values())

def flights(self)-> list[Flight]:
    return self.flights 

def airport_find(self, src_airport_code:str)->bool:
    return self.airports.get(airport_code)
    


def flight_exist(self, src_airport_code:str, dst_airport_code:str )->bool:
    for flight in self.flights:
        if flight.src_code == src_airport_code and flight.dst_code == dst_airport_code:
            return True
        return False


def flights_where(self, airport_code:str) -> list[Flight]:
    flights= []
    for flight in self.flights:
        if flight.src_code == airport_code or flight.dst_code == airport_code:
            flights.append(flight)
        return flights

        

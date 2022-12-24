
from flight import Flight

from airport import Airport

from flight_map import FlightMap


pathAeroport  = '/Users/tahagargouri/Downlads/TP1/aeroports.csv'    
pathFlights  = '/Users/tahagargouri/Downlads/TP1/flights.csv'    


FlightMap = FlightMap()


print("listAreport = ",FlightMap.listAreport)

print("import_airports = ",FlightMap.import_airports(pathAreport))

print("airport_find = ",FlightMap,flight_exist('JFK','NBO'))


mn = pd.read_csv(r,'/Users/tahagargouri/Download/TP1/aeroports.csv')
print(mn)
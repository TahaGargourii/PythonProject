
import csv

class FlightMap:
    
    listAreport =  []
    listFlights =  []

    # pathAreport  = '/Users/xelerolab/Desktop/ESTIAM/Python/files/aeroports.csv'    
    # pathFlights  = '/Users/xelerolab/Desktop/ESTIAM/Python/files/flights.csv'

    def import_airports(self,csv_file):
        with open(csv_file) as csvfile:
            list = csv.reader(csvfile)
            for row in list:
                print(row[0])
                self.listAreport.append(row)

    def import_flights(self,csv_file):
        with open(csv_file) as csvfile:
            list = csv.reader(csvfile)
            for row in list:
                self.listFlights.append(row)
    
    def airports(self):
        return self.listAreport
    
    def flights(self):
        return self.listFlights;

    def airport_find(airport_code):
        pass
    
    def flight_exist(src_airport_code, dst_airport_code) : 
        pass




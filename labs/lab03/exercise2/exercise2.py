def find_station(stations, name):
    for i in range(len(stations)):
        if stations[i] == name:
            return i
    return -1

        
def count_stops(stations, start, stop):
    start_point = find_station(stations, start)
    end_point = find_station(stations, stop)
    
    if start_point == -1 or end_point == -1 :
        return -1
    
    count = end_point - start_point
    return count
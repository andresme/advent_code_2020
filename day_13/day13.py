def get_earliest_from_timestamp(arrival, buses):
    arrival = int(arrival)
    buses = [int(bus) for bus in buses.split(',') if bus != 'x']

    schedule = [(bus, bus - (arrival % bus)) for bus in buses]
    
    nearest = min(schedule, key=lambda x: x[1])
    print(nearest[0] * nearest[1])

if __name__ == "__main__":
    with open('day_13/input.txt', 'r') as input_file:
        arrival, buses = input_file.read().split('\n')
    
    get_earliest_from_timestamp(arrival, buses)
    
    buses = [(i, int(bus)) for i, bus in enumerate(buses.split(",")) if bus != "x"]

    jump = buses[0][1] 
    i = jump
    for idx, bus in buses[1:]:
        while (i+idx) % bus != 0:
            i += jump
        jump *= bus

    print(i)

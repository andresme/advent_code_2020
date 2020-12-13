def get_earliest_from_timestamp(arrival, buses):
    arrival = int(arrival)
    buses = [int(bus) for bus in buses.split(',') if bus != 'x']

    schedule = [(bus, bus - (arrival % bus)) for bus in buses]
    
    nearest = min(schedule, key=lambda x: x[1])
    print(nearest[0] * nearest[1])

if __name__ == "__main__":
    with open('input.txt', 'r') as input_file:
        arrival, buses = input_file.read().split('\n')
    
    get_earliest_from_timestamp(arrival, buses)
    
    buses = [(i, bus) for i, bus in enumerate(buses.split(",")) if bus != "x"]

    jump = buses[0][0] 
    i = jump
    for bus in buses[1:]:
        while (i+bus[1])%bus[0] != 0:
            i += jump
        jump *= bus[0]

    print(i)

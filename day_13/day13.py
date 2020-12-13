def get_earliest_from_timestamp(arrival, buses):
    arrival = int(arrival)
    buses = [int(bus) for bus in buses.split(',') if bus != 'x']

    schedule = [(bus, bus - (arrival % bus)) for bus in buses]
    
    nearest = min(schedule, key=lambda x: x[1])
    print(nearest[0] * nearest[1])


from functools import reduce
def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod
 
 
 
def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1
    

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

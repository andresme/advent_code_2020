from collections import defaultdict

if __name__ == "__main__":
    with open('day_10/input.txt', 'r') as inputFile:
        adapters = inputFile.read().split('\n')
    adapters = sorted([int(i) for i in adapters])
    adapters.insert(0, 0) # start
    adapters.append(adapters[len(adapters)-1]+3) # end

    differences = defaultdict(int)

    for i in range(1, len(adapters)):
        diff = adapters[i] - adapters[i-1]
        differences[diff] = differences[diff] + 1

    print(differences[1] * differences[3])

    ## Part 2
    first_node_conections = [adapter for adapter in adapters if adapter < 4]

    m = defaultdict(int)

    for adapter in adapters[1:]:
        value = 1 if adapter in first_node_conections else 0
        for i in range(adapter-3, adapter):
            value += m[i]
        m[adapter] = value
    print(m[adapters[len(adapters)-1]])

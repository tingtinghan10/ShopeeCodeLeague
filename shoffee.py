import statistics

FLAVORS_THRESHOLD = list(map(int, input('Count of coffee bean flavors, and expectation for Shoffee: ').split()))

TOTAL_COUNT = FLAVORS_THRESHOLD[0]
THRESHOLD = FLAVORS_THRESHOLD[1]
PREFERENCE = list(map(int, input('Coffee preference values: ').split()))

def main():
    count = 0
    for length in range(TOTAL_COUNT):
        for pref in range(TOTAL_COUNT - length):
            average = statistics.mean(PREFERENCE[pref:pref + length + 1])
            if average >= THRESHOLD:
                count += 1
    print(count)

if __name__ == '__main__':
    main()
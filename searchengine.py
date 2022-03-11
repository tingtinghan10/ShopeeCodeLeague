def main():
    test_cases = int(input())

    output = {}
    for t in range(test_cases):
        [num_item, num_queries] = list(parse_line_int())

        items = []
        for i in range(num_item):
            items.append(input().lower()+ ' ')
            
        for q in range(num_queries):
            query = input().lower() + ' '
            count = 0
            for item in items:
                if query in item:
                    count += 1
            if q == 0:        
                output[t]= [count]
            else:
                output[t].append(count)

    for t in output:
        print(f'Case {t + 1}:')
        for q in output[t]:
            print(q)

def parse_line_int():
    return map(int, input().strip().split())

def parse_line_str():
    return map(str, input().lower().strip().split())

if __name__ == '__main__':
    main()
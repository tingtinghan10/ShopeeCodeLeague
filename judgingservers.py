import math

def main():
    test_cases = int(input())
    minprice = []
    for t in range(test_cases):
        [tot_servers, need] = list(parse_line())
        prices = list(parse_line())

        buy = math.ceil(need / 2)

        # split prices into pairs 
        # if the length of list is an odd number, drop the last 'unpaired' one
        split = []
        for chunk in chunks(prices):
            split.append(chunk)
        if len(split[-1]) == 1:
            split.pop()
        
        # split prices into pairs, offset by 1
        # if the length of list is an odd number, drop the last 'unpaired' one
        splitoffset = []
        for chunk in chunks(prices[1:]):
            splitoffset.append(chunk)
        if len(splitoffset[-1]) == 1:
            splitoffset.pop()

        # find min price from both splits, and take the min
        p_split = min_price(split, buy)
        p_splitoffset = min_price(splitoffset, buy)

        minprice.append(min(p_split, p_splitoffset))

    for t in range(len(minprice)):
        print(f'Case {t + 1}:', end=' ')
        print(minprice[t])
        
def min_price(chunk, buy):
    price = []
    for c in chunk:
        price.append(min(c))
    price.sort()
    return sum(price[:buy])

def chunks(list, n=2):
    for i in range(0, len(list), n):
        yield list[i:i + n]

def parse_line():
    return map(int, input().strip().split())

if __name__ == '__main__':
    main()
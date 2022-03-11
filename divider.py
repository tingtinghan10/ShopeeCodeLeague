import copy

def main():
    [engineers, groups] = parse_line()

    noiseFactors = parse_line()
    lst_noiseFactors = list(noiseFactors)

    # initial equal split
    equal_split = round(engineers / groups)
    # for 5 elements, divider would be [4,2,5]
    divider = []
    for i in range(groups):
        # last chunk is the remaining, to accomodate for rounding
        if i == groups - 1:
            divider.append(engineers)
        else:
            divider.append((i + 1) * equal_split)

    # total noise of initial split
    noise = tot_noise(lst_noiseFactors, divider)

    moved = [1] * (groups - 1)
    while sum(moved) != 0:
        moved = [1] * (groups - 1)
        # for all dividers, check left right
        for i in range(groups - 1):

            # left shift
            if i == 0 and divider[i] == 1:
                # if divider already at leftmost, dont move
                l_noise = noise
            else:
                divider_l = copy.deepcopy(divider)
                divider_l[i] -= 1
                l_noise = tot_noise(lst_noiseFactors, divider_l)
            
            # right shift
            if i == groups - 2 and divider[i + 1] - divider[i] == 1:
                # if divider already at rightmost, dont move
                r_noise = noise
            else:
                divider_r = copy.deepcopy(divider)
                divider_r[i] += 1
                r_noise = tot_noise(lst_noiseFactors, divider_r)

            # for any updates, break and recheck from the first divider
            if l_noise < noise and r_noise < noise:
                if l_noise < r_noise:
                    divider = copy.deepcopy(divider_l)
                    noise = l_noise
                else:
                    divider = copy.deepcopy(divider_r)
                    noise = r_noise
            elif l_noise < noise:
                divider = copy.deepcopy(divider_l)
                noise = l_noise
            elif r_noise < noise:
                divider = copy.deepcopy(divider_r)
                noise = l_noise
            else:
                moved[i] = 0
    print(noise)

def parse_line():
    return map(int, input().strip().split())

def noise(lst_noiseFactors, l, r):
    return sum(lst_noiseFactors[l:r]) * (r - l)

def tot_noise(lst_noiseFactors, divider):
    tot_noise = 0    
    for i in range(len(divider)):
        if i == 0:
            tot_noise += noise(lst_noiseFactors, 0, divider[i])
        else:
            tot_noise += noise(lst_noiseFactors, divider[i - 1], divider[i])
    return tot_noise

if __name__ == '__main__':
    main()
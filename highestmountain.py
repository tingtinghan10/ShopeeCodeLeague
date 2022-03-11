def main():
    mountain_ranges = int(input())

    length = []
    heights = []
    for mountain in range(mountain_ranges):
        length.append(int(input()))
        heights.append(list(map(int, input().strip().split())))
        if length[mountain] != len(heights[mountain]):
            print('mountain heights count do not match length')
            return

    for mountain in range(mountain_ranges):
        # get the index of the occurence of the number 1 in mountain heights
        idx = [i for i, h in enumerate(heights[mountain]) if h == 1]
        if len(idx) == 0:
            print(f'Case#{mountain + 1}: -1 -1')
        else:
            height = 1
            index = idx[0]
            for id in idx:
                hleft = 1
                hright = 1
                # to the left and to the right
                while hleft <= id + 1:
                    if heights[mountain][id - (hleft - 1) - 1] == heights[mountain][id - (hleft - 1)] + 1:
                        hleft += 1
                    else:
                        break
                while hright <= length[mountain] - id - 1:
                    if heights[mountain][id + (hright - 1) + 1] == heights[mountain][id + (hright - 1)] + 1:
                        hright += 1
                    else:
                        break

                # update max height and index        
                if max([height, hleft, hright]) > height:
                    height = max([height, hleft, hright])
                    if height == hleft:
                        index = id - (height - 1)
                    elif height == hright:
                        index = id + (height - 1)

            print(f'Case#{mountain + 1}: {height} {index}')


if __name__ == '__main__':
    main()
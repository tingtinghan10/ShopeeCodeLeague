import copy
import itertools

def main():
    [n, m, k] = list(parse_line())

    a = []
    b = []
    c = []
    combinations = []
    for function in range(n):
        abc = list(parse_line())
        a.append(abc[0])
        b.append(abc[1])
        c.append(abc[2])

        i = function + 1
        combinations = single_possible_combinations(i, c[function], combinations)

    m_combinations = all_possible_combinations(combinations, m)

    possible_sequences = 0
    for mc in range(len(m_combinations)):
        if meet_condition(m_combinations[mc], k, a, b):
            possible_sequences += 1

    print(possible_sequences)

def single_possible_combinations(i, jrange, combinations):
    i = [i]
    j = range(1, jrange + 1)
    combinations.extend(list(itertools.product(i, j)))
    return combinations

def all_possible_combinations(combinations, m):
    all_combinations = copy.deepcopy(combinations)
    for repeat in range(m - 1):
        all_combinations = list(itertools.product(all_combinations, combinations))
    return all_combinations

def meet_condition(combination, divider, a, b):
    val = 0
    for i, j in combination:
        i -= 1
        val += a[i] * (j**2) + b[i]
    if val % divider == 0:
        return True
    else:
        return False

def parse_line():
    return map(int, input().strip().split())

if __name__ == '__main__':
    main()
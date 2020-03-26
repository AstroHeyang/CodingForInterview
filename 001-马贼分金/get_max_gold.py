def get_max_gold(array):
    if not array:
        return 0
    golds = [[0 for _ in range(len(array))] for _ in range(len(array))]
    for i in range(len(array)):
        golds[i][i] = array[i]

    for interval in range(1, len(array)):
        for left in range(len(array) - interval):
            right = left + interval
            golds[left][right] = sum(array[left:right + 1]) - \
                                 min(golds[left + 1][right], golds[left][right - 1])
    return golds[0][len(array) - 1]


size = int(input())
for i in range(size):
    numbers_gold = input()
    golds = list(map(int, input().split(' ')))
    golds_sum = sum(golds)
    golds_first = get_max_gold(golds)
    print("Case #%d: %d %d" % (i + 1, golds_first, golds_sum - golds_first))

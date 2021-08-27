import copy


def prachan_buy(gid):
    buyls = []
    nesw_m = [-1, 1, 0, 0]
    nesw_n = [0, 0, 1, -1]
    clockwise_m = [0, 0, 1, 1]
    clockwise_n = [0, 1, 1, 0]
    counter_m = [0, 0, -1, -1]
    counter_n = [0, 1, 1, 0]
    Counter_clockwise = False
    grid = copy.deepcopy(gid)
    for m in range(len(grid)):
        for n in range(len(grid[0])):
            for k in range(2):
                want_to = []
                grid = copy.deepcopy(gid)
                if Counter_clockwise == False:
                    Counter_clockwise = True
                    try:
                        for pos in range(4):
                            if (m + clockwise_m[pos]) >= 0 and (
                                    n + clockwise_n[pos]) >= 0:
                                want_to.append(
                                    grid[m +
                                         clockwise_m[pos]][n +
                                                           clockwise_n[pos]])
                                for direct in range(4):
                                    try:
                                        if (m + clockwise_m[pos] +
                                                nesw_m[direct] >=
                                                0) and (n + clockwise_n[pos] +
                                                        nesw_n[direct] >= 0):
                                            grid[m + clockwise_m[pos] +
                                                 nesw_m[direct]][
                                                     n + clockwise_n[pos] +
                                                     nesw_n[direct]] *= 1.1
                                    except IndexError:
                                        pass
                        if len(want_to) == 4:
                            buyls.append(sum(want_to))
                    except IndexError:
                        continue
                else:
                    Counter_clockwise = False
                    try:
                        for pos in range(4):
                            if m + counter_m[pos] >= 0 and n + counter_n[
                                    pos] >= 0:
                                want_to.append(
                                    grid[m + counter_m[pos]][n +
                                                             counter_n[pos]])
                                for direct in range(4):
                                    try:
                                        if (m + counter_m[pos] + nesw_m[direct]
                                                >= 0) and (n + counter_n[pos] +
                                                           nesw_n[direct] >=
                                                           0):
                                            grid[m + counter_m[pos] +
                                                 nesw_m[direct]][
                                                     n + counter_n[pos] +
                                                     nesw_n[direct]] *= 1.1
                                    except IndexError:
                                        pass
                        if len(want_to) == 4:
                            buyls.append(sum(want_to))
                    except IndexError:
                        continue
    return buyls


col = []
while True:
    row = []
    x = input()
    if x == "": break
    row = list(map(int, x.split()))
    col.append(row)
if not len(col[0]) != len(col[1]):
    print(f"{min(prachan_buy(col)):.2f}")
else:
    print("Can't Buy")
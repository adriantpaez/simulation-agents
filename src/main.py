import sys
import board
import elements
import random
import time
import agents.agent1


if __name__ == "__main__":
    _x = [i for i in range(10, 41)]
    _y = [i for i in range(10, 41)]
    _dirt = [i for i in range(10, 41)]
    _obstacles = [i for i in range(10, 31)]

    def take_and_remove(source):
        resp = random.choice(source)
        source.remove(resp)
        return resp

    scenarios = [
        (20, 20, take_and_remove(_dirt), take_and_remove(_obstacles), 10, 5),
        (20, 20, take_and_remove(_dirt), take_and_remove(_obstacles), 10, 5),
        (20, 20, take_and_remove(_dirt), take_and_remove(_obstacles), 10, 5),
        (10, 10, take_and_remove(_dirt), take_and_remove(_obstacles), 10, 5),
        (10, 10, take_and_remove(_dirt), take_and_remove(_obstacles), 10, 5),
        (30, 30, take_and_remove(_dirt), take_and_remove(_obstacles), 10, 5),
        (30, 30, take_and_remove(_dirt), take_and_remove(_obstacles), 10, 5),
        (30, 30, take_and_remove(_dirt), take_and_remove(_obstacles), 10, 5),
        (40, 40, take_and_remove(_dirt), take_and_remove(_obstacles), 10, 5),
        (40, 40, take_and_remove(_dirt), take_and_remove(_obstacles), 10, 5),
    ]

    print("|----|----------------|----------|---------|---|---|-----------------|-------------------|")
    print("|%3s |%15s |%9s |%8s |%2s |%2s |%16s |%18s |" %
          ("#", "Ave. limpio", "Despedido", "Limpio", "X", "Y", "Suciedad Inicial", "Obstaculos inicial"))
    print("|----|----------------|----------|---------|---|---|-----------------|-------------------|")
    for k in range(0, 10):
        x = scenarios[k][0]
        y = scenarios[k][1]
        dirt = int(scenarios[k][2] / 100 * x * y)
        obstacles = int((scenarios[k][3]/100) * x * y)
        childs = scenarios[k][4]
        t = scenarios[k][5]

        percentages = []
        despedido = 0
        limpio = 0

        for _ in range(0, 30):
            b = board.Board(x, y, t)
            els = []
            for i in range(0, x):
                for j in range(0, y):
                    els.append(elements.Empty(b, (i, j)))
            b.set_playpen(childs)
            b.set_elements(dirt, obstacles, childs, agents.agent1.agent_3)

            while b.time < 100 * t:
                p = b.dirt_count/(b.x * b.y) * 100
                if p >= 60:
                    despedido += 1
                    break
                if p == 0 and not b.childs:
                    limpio += 1
                    break
                b.next_time()
                # print(b)
                # time.sleep(0.1)
            p = b.dirt_count/(b.x * b.y) * 100
            percentages.append(p)
        percentage = round(sum(percentages)/len(percentages), 2)
        print("|%3d |%15f |%9d |%8d |%2d |%2d |%16d |%18d |" %
              (k+1, percentage, despedido, limpio, x, y, scenarios[k][2], scenarios[k][3]))

import elements
import random


class Board:
    def __init__(self, x, y, t):
        super().__init__()
        self.x = x
        self.y = y
        self.playpen = []
        self.dirt_count = 0
        self.elements = {}
        self.childs = []
        self.bot = None
        self.time = 0
        self.t = t
        for i in range(0, x):
            for j in range(0, y):
                e = elements.Empty(self, (i, j))
                self.elements[(i, j)] = e

    def set_playpen(self, k: int):
        start = (random.randint(0, self.x - 1),
                 random.randint(0, self.y-1))

        visited = set()
        queue = []
        queue.append(start)
        visited.add(start)
        while queue:
            s = queue.pop(0)
            new_playpen = elements.Playpen(self, s)
            self.playpen.append(s)
            k -= 1
            if k == 0:
                break
            for i in [(s[0] + d[0], s[1] + d[1]) for d in elements.DIRECTIONS]:
                if not i in visited:
                    element = self[i]
                    if isinstance(element, elements.Empty):
                        queue.append(i)
                        visited.add(i)

    def set_elements(self, dirt: int, obstacle: int, childrens: int, bot_startegy):
        empties = list(filter(lambda x: isinstance(
            x, elements.Empty), self.elements.values()))
        ri = random.randint(0, len(empties) - 1)
        hb = empties.pop(ri)
        self. bot = elements.HouseBot(self, hb.position, bot_startegy)
        while dirt > 0:
            ri = random.randint(0, len(empties) - 1)
            d = empties.pop(ri)
            elements.Dirt(self, d.position)
            dirt -= 1
            self.dirt_count += 1
        while obstacle > 0:
            ri = random.randint(0, len(empties) - 1)
            o = empties.pop(ri)
            elements.Obstacle(self, o.position)
            obstacle -= 1
        while childrens > 0:
            ri = random.randint(0, len(empties) - 1)
            c = empties.pop(ri)
            self.childs.append(elements.Child(self, c.position))
            childrens -= 1

    def set_dirt(self, childs_move):
        for p in childs_move:
            e = []
            for d in elements.DIRECTIONS_D:
                x = self[(p[0] + d[0], p[1] + d[1])]
                if isinstance(x, elements.Empty):
                    e.append((p[0] + d[0], p[1] + d[1]))
            if e:
                new_d = random.choice(e)
                self[new_d] = elements.Dirt(self, new_d)
                self.dirt_count += 1

    def next_time(self):
        if self.time % self.t == 0:
            childs_move = []
            for c in self.childs:
                if random.random() >= 0.25:
                    d = random.choice(elements.DIRECTIONS)
                    if c.can_move(d):
                        childs_move.append(c.position)
                        c.move(d)
            self.set_dirt(childs_move)
        self.bot.run()
        self.time += 1

    def get_direction(self, p1, p2):
        if p1[0] == p2[0]:
            if p1[1] < p2[1]:
                return elements.DIRECTIONS[1]
            if p1[1] > p2[1]:
                return elements.DIRECTIONS[3]
        if p1[1] == p2[1]:
            if p1[0] < p2[0]:
                return elements.DIRECTIONS[2]
            if p1[0] > p2[0]:
                return elements.DIRECTIONS[0]

    def is_valid_position(self, p):
        return 0 <= p[0] < self.x and 0 <= p[1] < self.y

    def __getitem__(self, key):
        if key[0] < 0 or key[0] >= self.x or key[1] < 0 or key[1] >= self.y:
            return None
        try:
            return self.elements[key]
        except KeyError:
            return None

    def __setitem__(self, key, value):
        if key[0] < 0 or key[0] >= self.x or key[1] < 0 or key[1] >= self.y:
            raise IndexError
        self.elements[key] = value

    def __str__(self):
        resp = ""
        for i in range(0, self.x):
            for j in range(0, self.y):
                v = self[(i, j)]
                resp += str(v)
            resp += "\n"
        return resp

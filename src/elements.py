
DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]
DIRECTIONS_D = DIRECTIONS + [(-1, -1), (-1, 1), (1, -1), (1, 1)]


class Element:
    def __init__(self, board, d):
        super().__init__()
        self.board = board
        self.position = d
        board[d] = self

    def can_move(self, d):
        raise NotImplementedError()

    def move(self, d):
        if self.can_move(d):
            self.position = (self.position[0] + d[0], self.position[1] + d[1])
            return True
        return False


class Empty(Element):
    def __init__(self, board, d):
        super().__init__(board, d)

    def __str__(self):
        return '🔲'

    def __repr__(self):
        return str(self.position)


class Obstacle (Element):
    def __init__(self, board, d):
        super().__init__(board, d)

    def can_move(self, d):
        try:
            ed = self.board[(self.position[0] + d[0], self.position[1] + d[1])]
            if isinstance(ed, Obstacle):
                return ed.can_move(d)
            return isinstance(ed, Empty)
        except IndexError:
            return False

    def move(self, d):
        new_position = (self.position[0] + d[0], self.position[1] + d[1])
        if self.board.is_valid_position(new_position):
            ed = self.board[new_position]
            if isinstance(ed, Obstacle):
                ed.move(d)
            self.board[self.position] = Empty(self.board, self.position)
            self.position = new_position
            self.board[new_position] = self

    def try_move(self, d):
        if self.can_move(d):
            self.move(d)

    def __str__(self):
        return "🔴"


class Child (Element):
    def __init__(self, board, d):
        super().__init__(board, d)

    def can_move(self, d):
        try:
            ed = self.board[(self.position[0] + d[0], self.position[1] + d[1])]
            if isinstance(ed, Obstacle):
                return ed.can_move(d)
            return isinstance(ed, Empty)
        except IndexError:
            return False

    def move(self, d):
        new_position = (self.position[0] + d[0], self.position[1] + d[1])
        if self.board.is_valid_position(new_position):
            ed = self.board[new_position]
            if isinstance(ed, Obstacle):
                ed.move(d)
            self.board[self.position] = Empty(self.board, self.position)
            old_position = self.position
            self.position = new_position
            self.board[new_position] = self

    def try_move(self, d):
        if self.can_move(d):
            self.move(d)

    def __str__(self):
        return "🔵"


class Dirt(Element):
    def __init__(self, board, d):
        super().__init__(board, d)

    def __str__(self):
        return "❌"


class Playpen (Element):
    def __init__(self, board, d):
        super().__init__(board, d)
        self.child = None

    def __str__(self):
        if self.child:
            return "🚼"
        return "🔷"


class HouseBot (Element):
    def __init__(self, board, d, strategy):
        super().__init__(board, d)
        self.strategy = strategy
        self.objective = []
        self.child = None
        self.put_playpen = None
        self.clean = False

    def can_move(self, d):
        if self.objective:
            next_position = self.objective[0]
            next_element = self.board[next_position]
            if isinstance(next_element, Playpen):
                return next_element.child == None
            if self.child:
                return isinstance(next_element, (Empty, Dirt))
            return isinstance(next_element, (Empty, Dirt, Child))
        return False

    def move(self, d):
        if self.clean:
            self.clean = False
            return
        if self.put_playpen:
            self.board[self.position] = self.put_playpen
            self.put_playpen = None
        else:
            self.board[self.position] = Empty(self.board, self.position)
        next_position = self.objective.pop(0)
        next_element = self.board[next_position]
        self.position = next_position
        self.board[next_position] = self
        if isinstance(next_element, Playpen):
            self.put_playpen = next_element
            if not self.objective:
                self.objective = []
                next_element.child = self.child
                self.child = None
        elif isinstance(next_element, Child):
            self.board.childs.remove(next_element)
            self.child = next_element
        elif isinstance(next_element, Dirt):
            self.board.dirt_count -= 1
            self.clean = True

    def try_move(self, d):
        if self.can_move(d):
            self.move(d)

    def run(self):
        self.strategy(self)

    def __str__(self):
        return "🤖"

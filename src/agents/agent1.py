import elements
import random


def path_to_position(bot: elements.HouseBot, position, path_types):
    path = []
    visited = set()
    distance = {}
    queue = []

    queue.append(bot.position)
    visited.add(bot.position)
    distance[bot.position] = 0

    while queue:
        s = queue.pop(0)
        if s == position:
            path = [s]
            break
        for i in [(s[0] + d[0], s[1] + d[1]) for d in elements.DIRECTIONS]:
            if not i in visited:
                element = bot.board[i]
                if element:
                    if isinstance(element, elements.Playpen) and element.child:
                        continue
                    if isinstance(element, path_types):
                        queue.append(i)
                        visited.add(i)
                        distance[i] = distance[s] + 1
    return path, distance


def path_to(bot: elements.HouseBot, element_type, path_types):
    path = []
    visited = set()
    distance = {}
    queue = []

    queue.append(bot.position)
    visited.add(bot.position)
    distance[bot.position] = 0

    while queue:
        s = queue.pop(0)
        element = bot.board[s]
        if isinstance(element, element_type):
            path = [s]
            break
        for i in [(s[0] + d[0], s[1] + d[1]) for d in elements.DIRECTIONS]:
            if not i in visited:
                element = bot.board[i]
                if element:
                    if isinstance(element, elements.Playpen) and element.child:
                        continue
                    if isinstance(element, path_types):
                        queue.append(i)
                        visited.add(i)
                        distance[i] = distance[s] + 1
    return path, distance


def set_objective(bot: elements.HouseBot, path, distance):
    while path[0] != bot.position:
        s = path[0]
        for i in [(s[0] + d[0], s[1] + d[1]) for d in elements.DIRECTIONS]:
            try:
                if distance[i] == distance[s] - 1:
                    path = [i] + path
                    break
            except KeyError:
                continue
    bot.objective = path[1:]

cant_move = 0

def fallow_objective(bot: elements.HouseBot):
    global cant_move
    if bot.can_move(None):
        bot.move(None)
    else:
        cant_move += 1
        if cant_move == 3:
            cant_move = 0
            bot.objective = []


def got_to_playpen(bot: elements.HouseBot):
    for pp in bot.board.playpen:
        path, distance = path_to_position(bot, pp, (elements.Empty,
                                                    elements.Dirt, elements.HouseBot, elements.Playpen))
        if path:
            set_objective(bot, path, distance)
            bot.run()
            return True
    return False


def agent_1(bot: elements.HouseBot):
    if len(bot.objective) > 0:
        fallow_objective(bot)
    else:
        if bot.child and got_to_playpen(bot):
            return

        path, distance = path_to(bot, elements.Dirt, (elements.Empty,
                                                      elements.Dirt, elements.HouseBot, elements.Child, elements.Playpen))
        if path:
            set_objective(bot, path, distance)
            bot.run()


def agent_2(bot: elements.HouseBot):
    rd = random.choice(elements.DIRECTIONS)
    if bot.can_move(rd):
        bot.move(rd)


def agent_3(bot: elements.HouseBot):
    if len(bot.objective) > 0:
        fallow_objective(bot)
    else:
        if bot.child and got_to_playpen(bot):
            return
        if bot.board.childs:
            path, distance = path_to(bot, elements.Child, (elements.Empty,
                                                           elements.Dirt, elements.HouseBot, elements.Child, elements.Playpen))
            if path:
                set_objective(bot, path, distance)
                bot.run()
                return
        path, distance = path_to(bot, elements.Dirt, (elements.Empty,
                                                      elements.Dirt, elements.HouseBot, elements.Child))
        if path:
            set_objective(bot, path, distance)
            bot.run()

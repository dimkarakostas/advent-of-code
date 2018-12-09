from lists import DoublyLinkedList


def faster_marble_game(marbles, players):
    points = [0 for _ in range(players)]

    circle = DoublyLinkedList()
    circle.add(0)
    circle.add(1)
    for marble in range(2, marbles + 1):
        if marble % 23 == 0:
            for _ in range(7):
                circle.head = circle.head.prev
            points[marble % players] += marble + circle.head.data
            circle.removeHead()
        else:
            circle.head = circle.head.next
            circle.add(marble)

    return max(points)


def marble_game(marbles, players):
    points = [0 for _ in range(players)]

    circle = [0, 2, 1]
    idx = 1
    for marble in range(3, marbles + 1):
        if marble % 23 == 0:
            rem_idx = (idx - 7) % len(circle)
            points[marble % players] += marble + circle[rem_idx]
            del circle[rem_idx]
            idx = rem_idx % len(circle)
            continue
        idx = (idx + 2) % len(circle)
        circle.insert(idx, marble)

    return max(points)


MARBLES = 71082
PLAYERS = 413

print 'Part 1:', marble_game(MARBLES, PLAYERS)
print 'Part 2:', faster_marble_game(MARBLES * 100, PLAYERS)

high_score_board = []


def record_game(player, *scores, bonus=0, multiplier=1.0):
    """
    Record a game score for a player.

    *scores: any number of round scores.
    bonus: optional keyword argument added to the total.
    multiplier: optional keyword argument applied at the end.
    """

    if len(scores) == 0:
        return player, 0, 0, "no rounds played"

    for score in scores:
        if score < 0:
            return player, 0, 0, "negative score not allowed"

    raw_total = sum(scores)
    total = int((raw_total + bonus) * multiplier)
    rounds = len(scores)

    high_score_board.append((player, total))

    sorted_board = sorted(high_score_board, key=lambda x: x[1], reverse=True)

    rank = sorted_board.index((player, total)) + 1

    if rank == 1:
        status = "high score!"
    else:
        status = f"rank {rank}"

    return player, rounds, total, status


print(record_game("Ibtisam", 10, 20, 30, bonus=5, multiplier=1.0))
print(record_game("Ahmed", 40, 30, 20, bonus=10, multiplier=1.0))
print(record_game("Lina", 15, 10, 5, bonus=0, multiplier=2.0))

print("Final leaderboard:")
print(high_score_board)
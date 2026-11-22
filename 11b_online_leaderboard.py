"""Practical 11B: Online leaderboard ranking with heap sort."""

from practical_11a_heap_sort import heap_sort


def rank_players(players, descending=True):
    scores = [score for _, score in players]
    sorted_scores = heap_sort(scores, "min" if descending else "max")
    remaining = list(players)
    ranking = []
    for score in sorted_scores:
        for index, (name, player_score) in enumerate(remaining):
            if player_score == score:
                ranking.append((name, player_score))
                remaining.pop(index)
                break
    return ranking


def main():
    count = int(input("Number of players: "))
    players = []
    for _ in range(count):
        name, score = input("Enter player name and score: ").rsplit(maxsplit=1)
        players.append((name, int(score)))
    ranking = rank_players(players)
    print("Leaderboard:")
    for position, (name, score) in enumerate(ranking, start=1):
        print(f"{position}. {name} - {score}")


if __name__ == "__main__":
    main()

# Задание «Голосование»


def vote(votes):
    # your code
    for n in votes:
        count = votes.count(vote)
        return f"{votes[n]}"


if __name__ == "__main__":
    print(vote([1, 1, 1, 2, 3]))
    print(vote([1, 2, 3, 2, 2]))

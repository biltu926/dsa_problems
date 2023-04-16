
'''

An arcade game player wants to climb to the top of the leaderboard and track their ranking. The game uses Dense Ranking, so its leaderboard works like this:
The player with the highest score is ranked number  on the leaderboard.
Players who have equal scores receive the same ranking number, and the next player(s) receive the immediately following ranking number.
Example


Link to the problem: https://www.hackerrank.com/challenges/climbing-the-leaderboard/problem

'''

def climbingLeaderboard(ranked, player):
    # Write your code here
    result = []
    unique_ranks = [0]
    unique_ranks.append(ranked[0])
    k = 1

    # Create an array of unique ranks.
    for index in range(1, len(ranked)):
        if ranked[index] != unique_ranks[k]:
            unique_ranks.append(ranked[index])
            k += 1

    # Peform binary search to get the positions.
    for item in player:
        l = 1
        r = len(unique_ranks)
        assigned = False

        while l < r:
            mid = (r + l )//2
            if unique_ranks[mid] == item:
                result.append(mid)
                assigned = True
                break
            elif unique_ranks[mid] > item:
                l = mid +1
            elif unique_ranks[mid] < item:
                r = mid
        if not assigned:
            if unique_ranks[mid] <= item:
                result.append(mid)
            elif unique_ranks[mid] > item:
                result.append(mid +1)

    return result

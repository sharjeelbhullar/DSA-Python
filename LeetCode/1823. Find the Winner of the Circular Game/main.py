class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        pos = 0
        people = list(range(1, n+1))
        while len(people) > 1:
            remove_idx = (pos + k - 1) % len(people)
            people.pop(remove_idx)
            pos = remove_idx
        return people[0]
# Last updated: 2/8/2026, 12:03:35 AM
class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        scores = []
        for operation in operations:
            if operation == "+":
                scores += [scores[len(scores) - 1] + scores[len(scores) - 2]]
            elif operation == "D":
                scores += [scores[len(scores) - 1] * 2]
            elif operation == "C":
                scores.pop()
            else:
                scores.append(int(operation))
        return sum(scores)

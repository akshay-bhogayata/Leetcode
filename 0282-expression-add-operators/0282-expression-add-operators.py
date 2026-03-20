class Solution:
    def addOperators(self, num, target):
        res = []

        def backtrack(index, path, value, prev):
            if index == len(num):
                if value == target:
                    res.append(path)
                return

            for i in range(index, len(num)):
                if i != index and num[index] == '0':
                    break

                curr = int(num[index:i+1])

                if index == 0:
                    backtrack(i + 1, path + str(curr), curr, curr)
                else:
                    backtrack(i + 1, path + "+" + str(curr), value + curr, curr)
                    backtrack(i + 1, path + "-" + str(curr), value - curr, -curr)
                    backtrack(i + 1, path + "*" + str(curr), value - prev + prev * curr, prev * curr)

        backtrack(0, "", 0, 0)
        return res
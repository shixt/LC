'''

当 i=0 时，单调栈为空，因此将 0 进栈。

stack=[0(73)]

ans=[0,0,0,0,0,0,0,0]ans=[0,0,0,0,0,0,0,0]

当 i=1i=1 时，由于 7474 大于 7373，因此移除栈顶元素 00，赋值 ans[0]:=1-0，将 11 进栈。

stack=[1(74)]stack=[1(74)]

ans=[1,0,0,0,0,0,0,0]

当 i=2i=2 时，由于 7575 大于 7474，因此移除栈顶元素 11，赋值 ans[1]:=2-1，将 22 进栈。

stack=[2(75)]stack=[2(75)]

ans=[1,1,0,0,0,0,0,0]

当 i=3i=3 时，由于 7171 小于 7575，因此将 33 进栈。

stack=[2(75),3(71)]stack=[2(75),3(71)]

ans=[1,1,0,0,0,0,0,0]ans=[1,1,0,0,0,0,0,0]

当 i=4i=4 时，由于 6969 小于 7171，因此将 44 进栈。

stack=[2(75),3(71),4(69)]stack=[2(75),3(71),4(69)]

ans=[1,1,0,0,0,0,0,0]ans=[1,1,0,0,0,0,0,0]

当 i=5i=5 时，由于 7272 大于 6969 和 7171，因此依次移除栈顶元素 44 和 33，赋值 ans[4]:=5-4ans[4]:=5−4 和 ans[3]:=5-3ans[3]:=5−3，将 55 进栈。

stack=[2(75),5(72)]stack=[2(75),5(72)]

ans=[1,1,0,2,1,0,0,0]ans=[1,1,0,2,1,0,0,0]

当 i=6i=6 时，由于 7676 大于 7272 和 7575，因此依次移除栈顶元素 55 和 22，赋值 ans[5]:=6-5ans[5]:=6−5 和 ans[2]:=6-2ans[2]:=6−2，将 66 进栈。

stack=[6(76)]stack=[6(76)]

ans=[1,1,4,2,1,1,0,0]ans=[1,1,4,2,1,1,0,0]

当 i=7i=7 时，由于 7373 小于 7676，因此将 77 进栈。

stack=[6(76),7(73)]stack=[6(76),7(73)]

ans=[1,1,4,2,1,1,0,0]ans=[1,1,4,2,1,1,0,0]

'''
class Solution:
    def dailyTemperatures(self, T):
        length = len(T)
        ans = [0] * length
        stack = []
        for i in range(length):
            temperature = T[i]
            while stack and temperature > T[stack[-1]]:
                prev_index = stack.pop()
                ans[prev_index] = i - prev_index
            stack.append(i)
        return ans

s = Solution()
print(s.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
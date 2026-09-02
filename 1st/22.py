class Solution(object):
    def maxArea(self, height):
        left = 0
        right = len(height) - 1
        ans = 0

        while left < right:
            width = right - left
            h = min(height[left], height[right])

            ans = max(ans, width * h)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return ans
    
n=int(input())
a=input().split()
st=[]
for x in a:
    if x not in '+-*/':
        st.append(int(x))
    else:
        b=st.pop()
        c=st.pop()
        if x=='+':
            st.append(c+b)
        elif x=='-':
            st.append(c-b)
        elif x=='*':
            st.append(c*b)
        else:
            st.append(int(c/b))
print(st[-1])
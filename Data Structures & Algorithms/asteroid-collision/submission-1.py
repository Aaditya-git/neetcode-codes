

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for digit in asteroids:
            flag = True
            while stack and stack[-1] > 0 and digit < 0:
                if stack[-1] < abs(digit):
                    stack.pop()
                elif stack[-1] == abs(digit):
                    stack.pop()
                    flag = False
                    break
                else:
                    flag = False
                    break
            if flag:
                stack.append(digit)
        return stack




                # if not stack:
                #     stack.append(digit)
            
        #         else:
        #             if digit > 0 and stack[-1] > 0:
        #                 stack.append(digit)
        #             elif digit > 0 and stack[-1] < 0:
        #                 stack.append(digit)
        #             elif digit <0 and stack[-1] < 0:
        #                 stack.append(digit)
        #             elif digit < 0 and  stack[-1] > 0:
        #                 if abs(digit) > stack[-1]:
        #                     stack.pop()
        #                 elif abs(digit) > stack[-1]:
        #                     continue
        #                 else:
        #                     stack.pop()

        # return stack
        
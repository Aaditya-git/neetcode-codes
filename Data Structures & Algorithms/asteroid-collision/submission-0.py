

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for digit in asteroids:
            alive = True

            while stack and stack[-1] > 0 and digit < 0:
                if stack[-1] < abs(digit):
                    stack.pop()  
                elif stack[-1] == abs(digit):
                    stack.pop()  
                    alive = False
                    break
                else:
                    alive = False
                    break
            if alive:
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
        
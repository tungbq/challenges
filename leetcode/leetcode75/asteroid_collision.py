"""
https://leetcode.com/problems/asteroid-collision/description/?envType=study-plan-v2&envId=leetcode-75

Example 1:

Input: asteroids = [5,10,-5]
Output: [5,10]
Explanation: The 10 and -5 collide resulting in 10. The 5 and 10 never collide.
Example 2:

Input: asteroids = [8,-8]
Output: []
Explanation: The 8 and -8 collide exploding each other.
Example 3:

Input: asteroids = [10,2,-5]
Output: [10]
Explanation: The 2 and -5 collide resulting in -5. The 10 and -5 collide resulting in 10.

"""
class Solution:
    def asteroidCollision(self, asteroids):
        stack = []

        for element in asteroids:
            stack.append(element)
            if len(stack) == 1:
              continue

            # Now check collide
            while len(stack) > 1 and (stack[-2] > 0) and (stack[-1]) < 0:
                # collide and ..
                if abs(stack[-1]) < abs(stack[-2]):
                    # Remove the element
                    stack.pop()
                    break
                elif abs(stack[-1]) == abs(stack[-2]):
                    # Remove both
                    stack.pop()
                    stack.pop()
                    break
                else:
                    # [a, a2+, -a3]. Remove a2+, add a3-
                    current_last = stack[-1]
                    stack.pop()
                    stack.pop()
                    stack.append(current_last)
        return stack

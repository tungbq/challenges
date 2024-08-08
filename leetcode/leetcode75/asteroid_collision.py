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
            print(f"stack: {stack}")
            
            if not stack:
                stack.append(element)
                continue
            is_collided = self.check_is_collided(stack[len(stack) - 1], element)
            if not is_collided:
                stack.append(element)
                continue
            # Now check collide
            while True:
                # collide and ..
                if abs(element) < stack[len(stack) -1]:
                    break
                elif abs(element) == stack[len(stack) -1]:
                    stack.pop()
                    break
                else:
                    stack.pop()
                    if not stack:
                        stack.append(element)
                        break
        return stack

    def check_is_collided(self, current, next):
        # current +: -> AND next -: <- => Collide
        if (current > 0 and next < 0):
          return True
        return False
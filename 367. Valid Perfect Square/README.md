## Valid Perfect Square

Given a  **positive**  integer  *_num_*, write a function which returns True if  *_num_*  is a perfect square else False.

**Follow up:**  **Do not**  use any built-in library function such as  `sqrt`.

**Example 1:**

    Input: num = 16
    Output: true

**Example 2:**

    Input: num = 14
    Output: false

## My Solution (Python 3):

    def isPerfectSquare(num):
      '''
          Given a positive integer num, write a function which returns True if num is a perfect square
          else False.
      '''
    
      # If a number is less than 2, return False unless it is 1
      if num == 1:
          return True
      elif num < 2:
          return False
    
      # initialize starting and last number for range between the two variables
      first = 2
      last = num
    
      while first <= last:
          # Retreive the middle position between the first and last values
          midpoint = (first + last) // 2
    
          if midpoint ** 2 == num:
              # return true if value times itself equals the target number
              return True
          elif midpoint **2 > num:
              # Update last variable, changing the midpoint value in the next iteration
              last = midpoint - 1
          else:
              # Update first variable, changing the midpoint value in the next iteration
              first = midpoint + 1
    
      # Return False at the end as all flags for checking a perfect square has been met
      return False

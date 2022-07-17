class Solution:
    def search(self, nums: List[int], target: int) -> int:
      '''
          Search through a sorted list to find index of target value
          return -1 if target value is not found in list
      '''
      # initialize starting and last position of nums list
      first_pos = 0
      last_pos = len(nums) - 1

      while first_pos <= last_pos:
        # Retreive the middle position between the first and last position value
        midpoint = (first_pos + last_pos) // 2

        if nums[midpoint] == target:
          # Output the position of the target value if found in list
            return midpoint
        elif nums[midpoint] < target:
          # Update first_pos value, changing the midpoint value in the next iteration
            first_pos = midpoint + 1
        else:
           # Update last_pos value, changing the midpoint value in the next iteration
            last_pos = midpoint - 1
            
      # If the while loop could not find the target value inside the list, output -1
      return -1

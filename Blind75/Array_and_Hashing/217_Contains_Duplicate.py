

def containsDuplicate(nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        hashset = set()

        for n in nums:
            if n in hashset:
                return True

            hashset.add(n)
        return False

nums = [1,2,3]
if containsDuplicate(nums):
     print("No Duplicate available")
else:
     print("Duplicate Available")
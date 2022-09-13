class Solution(object):
    def validUtf8(self, data):
        """
        :type data: List[int]
        :rtype: bool
        """
        count = 0
        
        for byte in data:
            if byte >= 128 and byte <= 191:
                if not count:
                    return False
                count -= 1
            else:
                if count:
                    return False
                if byte < 128:
                    continue
                elif byte < 224:
                    count = 1
                elif byte < 240:
                    count = 2
                elif byte < 248:
                    count = 3
                else:
                    return False
                    
        return count == 0
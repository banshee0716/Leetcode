class Solution(object):
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        
        for i in range(1, len(num)-1):
            if i > 1 and num[0] == '0':
                continue
            for j in range(i+1, len(num)):
                first = int(num[:i])
                second = int(num[i:j])
                if j > i + 1 and num[i:i+1] == '0':
                    continue
                tmp = str(first+second)
                if num[j:] == tmp:
                    return True
                if num[j:].startswith(tmp):
                    if self.isAdditiveNumber(num[i:]):
                        return True
        return False
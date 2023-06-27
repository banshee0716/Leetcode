class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        arr = []
        for x in range(1, n + 1):
            if x % 15 == 0:
                arr.append('FizzBuzz')
            elif x % 3 == 0:
                arr.append('Fizz')
            elif x % 5 == 0:
                arr.append('Buzz')
            else:
                arr.append(str(x))
			
        return arr
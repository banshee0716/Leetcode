class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        # Implement the Josephus problem solution
        # Start with the base case of 1 player (winner's position is 0)
        winner_position = 0

        # Iteratively build up the solution for 'n' players
        for player_count in range(2, n + 1):
            # Update the winner's position based on the previous result and 'k'
            # The modulo operation simulates the circular nature of the game
            winner_position = (winner_position + k) % player_count

        # Convert from 0-indexing to 1-indexing for the final result
        return winner_position + 1
    
    """
The solution uses a mathematical approach known as the Josephus formula. Here's a detailed explanation of the problem-solving approach:

Start with a base case of 1 player, where the winner's position is always 0 (0-indexed).
Iteratively build up the solution for n players by simulating the elimination process.
For each number of players from 2 to n, update the winner's position based on the previous result and the value of k.
The final result is adjusted to 1-indexing by adding 1.

Time Complexity: O(n)

The solution iterates from 2 to n, performing constant-time operations in each iteration.
This results in a linear time complexity with respect to the number of players.

Space Complexity: O(1)

The solution uses only a single variable (winner_position) regardless of the input size.
No additional data structures are created, resulting in constant space complexity.
    """
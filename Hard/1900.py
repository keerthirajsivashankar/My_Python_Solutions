from typing import List, Tuple

class Solution:
    def earliestAndLatest(self, n: int, firstPlayer: int, secondPlayer: int) -> List[int]:
        def dfs(current_n: int, p1: int, p2: int) -> Tuple[int, int]:
            # Step 1: Normalize player positions
            # If players are symmetric (e.g., 1 and n, 2 and n-1), they meet in round 1.
            if p1 + p2 == current_n + 1:
                return (1, 1)
            
            # Ensure p1 is always the smaller player index for consistent logic
            if p1 > p2:
                p1, p2 = p2, p1
            
            # Base cases for small 'n' where rounds are easily determined
            # These are specific to the problem's tournament structure
            if current_n <= 4:
                # For n=2, (1,2) -> (1,1) -> 1 round
                # For n=3, (1,2) -> (1,1) -> 1 round; (1,3) -> (1,2) -> 2 rounds; (2,3) -> (1,1) -> 1 round
                # For n=4, (1,2) -> (1,1) -> 1 round; (1,3) -> (1,2) -> 2 rounds; (1,4) -> (1,1) -> 1 round
                #           (2,3) -> (1,1) -> 1 round; (2,4) -> (1,2) -> 2 rounds; (3,4) -> (1,1) -> 1 round
                # The logic for n<=4 implies they will always meet in the next round (round 2)
                # unless they meet in round 1 (which is handled by p1 + p2 == current_n + 1).
                # This suggests that for n<=4, if they don't meet in round 1, they meet in round 2.
                return (2, 2)

            # Calculate mid-point for the next round's 'n'
            m = (current_n + 1) // 2
            minR, maxR = float('inf'), float('-inf')

            # Step 2: Use symmetry for player positions if p1 is "further" from start than p2 is from end
            # This normalizes the problem to always consider the players from the "left" side.
            if p1 - 1 > current_n - p2:
                t = current_n + 1 - p1
                p1 = current_n + 1 - p2
                p2 = t

            # Step 3: Simulate possibilities for the next round
            # This part is complex and relies on understanding how players advance in a tournament
            # when some players are eliminated.
            
            # Case: Both players are in the "first half" of the current_n players
            # (i.e., they both survive if they don't meet each other and their opponents are eliminated)
            if p2 * 2 <= current_n + 1:
                # a: count of players before p1
                # b: count of players between p1 and p2
                a = p1 - 1
                b = p2 - p1 - 1

                # Iterate through possibilities for how many players before p1 win (i)
                # and how many players between p1 and p2 win (j)
                for i in range(a + 1):
                    for j in range(b + 1):
                        # Calculate new positions in the next round (size m)
                        # The new position of p1 will be i + 1 (i winners before it + p1 itself)
                        # The new position of p2 will be i + j + 2 (i winners before p1, p1, j winners between p1 and p2, p2 itself)
                        r1, r2 = dfs(m, i + 1, i + j + 2)
                        minR = min(minR, r1 + 1) # Add 1 for the current round
                        maxR = max(maxR, r2 + 1) # Add 1 for the current round
            # Case: p2 is in the "second half" of the current_n players
            # This means p2 might meet its symmetrical opponent.
            else:
                # p4: symmetrical position of p2 from the start (if p2 were in the first half)
                p4 = current_n + 1 - p2
                a = p1 - 1 # players before p1
                b = p4 - p1 - 1 # players between p1 and p4
                c = p2 - p4 - 1 # players between p4 and p2 (this is for the "middle" part of the tournament bracket)

                # Iterate through possibilities for winners before p1 (i)
                # and winners between p1 and p4 (j)
                for i in range(a + 1):
                    for j in range(b + 1):
                        # Calculate new offset for p2's position.
                        # This involves accounting for players before p1, p1 itself,
                        # players between p1 and p4, p4 itself (which might be eliminated),
                        # and the remaining players in the second half.
                        offset = i + j + 1 + (c + 1) // 2 + 1
                        r1, r2 = dfs(m, i + 1, offset)
                        minR = min(minR, r1 + 1)
                        maxR = max(maxR, r2 + 1)

            # Step 4: Return earliest and latest round found
            return (minR, maxR)

        # Start the DFS from the initial state
        return list(dfs(n, firstPlayer, secondPlayer))

def get_integer_input(prompt: str, min_val: int = 1, max_val: int = float('inf')) -> int:
    while True:
        try:
            value = int(input(prompt))
            if min_val <= value <= max_val:
                return value
            else:
                print(f"Please enter an integer between {min_val} and {max_val}.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

if __name__ == "__main__":
    sol = Solution()

    print("--- Earliest and Latest Rounds Two Players Can Meet ---")
    
    n_val = get_integer_input("Enter the total number of players (n): ", min_val=2)
    
    while True:
        first_player_val = get_integer_input(f"Enter the first player's initial position (1 to {n_val}): ", min_val=1, max_val=n_val)
        second_player_val = get_integer_input(f"Enter the second player's initial position (1 to {n_val}): ", min_val=1, max_val=n_val)
        
        if first_player_val == second_player_val:
            print("Player positions must be different. Please re-enter.")
        else:
            break

    result = sol.earliestAndLatest(n_val, first_player_val, second_player_val)
    print(f"\nThe earliest and latest rounds they can meet are: {result}")
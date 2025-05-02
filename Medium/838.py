class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        n = len(dominoes)
        forces = [0] * n

        # Calculate forces from left to right
        force = 0
        for i in range(n):
            if dominoes[i] == 'R':
                force = n
            elif dominoes[i] == 'L':
                force = 0
            else:
                force = max(0, force - 1)
            forces[i] += force

        # Calculate forces from right to left
        force = 0
        for i in range(n - 1, -1, -1):
            if dominoes[i] == 'L':
                force = n
            elif dominoes[i] == 'R':
                force = 0
            else:
                force = max(0, force - 1)
            forces[i] -= force

        result = []
        for f in forces:
            if f > 0:
                result.append('R')
            elif f < 0:
                result.append('L')
            else:
                result.append('.')

        return "".join(result)

# Example Usage:
if __name__ == "__main__":
    sol = Solution()
    dominoes1 = ".L.R...LR..L.."
    print(f"Result for '{dominoes1}': {sol.pushDominoes(dominoes1)}")

    dominoes2 = "RR.L"
    print(f"Result for '{dominoes2}': {sol.pushDominoes(dominoes2)}")

    dominoes3 = "..R.."
    print(f"Result for '{dominoes3}': {sol.pushDominoes(dominoes3)}")

    dominoes4 = "..L.."
    print(f"Result for '{dominoes4}': {sol.pushDominoes(dominoes4)}")

    dominoes5 = "RL"
    print(f"Result for '{dominoes5}': {sol.pushDominoes(dominoes5)}")
from typing import List

class Solution:
  def removeSubfolders(self, folder: List[str]) -> List[str]:
    ans = []
    prev = ""

    folder.sort()

    for f in folder:
      if len(prev) > 0 and f.startswith(prev) and f[len(prev)] == '/':
        continue
      ans.append(f)
      prev = f

    return ans

def get_folder_paths_input(prompt: str) -> List[str]:
    while True:
        try:
            input_str = input(prompt)
            # Split by space, then strip any leading/trailing whitespace from each path
            paths = [p.strip() for p in input_str.split()]
            if not paths:
                print("Please enter at least one folder path.")
                continue
            # Basic validation: ensure paths start with '/'
            if not all(p.startswith('/') for p in paths):
                print("All folder paths should start with '/'. Please re-enter.")
                continue
            return paths
        except Exception as e:
            print(f"An error occurred: {e}. Please try again.")

if __name__ == "__main__":
    sol = Solution()
    
    folder_paths = get_folder_paths_input("Enter folder paths separated by spaces (e.g., '/a /a/b /c/d /c/d/e /c/f'): ")

    result = sol.removeSubfolders(folder_paths)
    print(f"The folders after removing subfolders are: {result}")
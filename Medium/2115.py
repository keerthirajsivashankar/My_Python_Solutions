import collections

def find_all_recipes(recipes: list[str], ingredients: list[list[str]], supplies: list[str]) -> list[str]:
    """
    Finds all recipes that can be made using the given supplies.

    Args:
        recipes: A list of recipe names.
        ingredients: A list of ingredient lists, where ingredients[i] are the ingredients for recipes[i].
        supplies: A list of available supplies.

    Returns:
        A list of recipe names that can be made.
    """
    ans = []
    supplies = set(supplies)
    graph = collections.defaultdict(list)
    in_degrees = collections.Counter()
    q = collections.deque()

    for i, recipe in enumerate(recipes):
        for ingredient in ingredients[i]:
            if ingredient not in supplies:
                graph[ingredient].append(recipe)
                in_degrees[recipe] += 1

    for recipe in recipes:
        if in_degrees[recipe] == 0:
            q.append(recipe)

    while q:
        u = q.popleft()
        ans.append(u)
        for v in graph[u]:
            in_degrees[v] -= 1
            if in_degrees[v] == 0:
                q.append(v)

    return ans

if __name__ == "__main__":
    recipes1 = ["bread", "sandwich"]
    ingredients1 = [["yeast", "flour"], ["bread", "meat"]]
    supplies1 = ["yeast", "flour", "meat"]
    result1 = find_all_recipes(recipes1, ingredients1, supplies1)
    print(f"Recipes for {recipes1}, {ingredients1}, {supplies1}: {result1}")

    recipes2 = ["bread", "sandwich", "burger"]
    ingredients2 = [["yeast", "flour"], ["bread", "meat"], ["sandwich", "meat", "bread"]]
    supplies2 = ["yeast", "flour", "meat"]
    result2 = find_all_recipes(recipes2, ingredients2, supplies2)
    print(f"Recipes for {recipes2}, {ingredients2}, {supplies2}: {result2}")

    recipes3 = ["bread"]
    ingredients3 = [["yeast", "flour"]]
    supplies3 = ["yeast"]
    result3 = find_all_recipes(recipes3, ingredients3, supplies3)
    print(f"Recipes for {recipes3}, {ingredients3}, {supplies3}: {result3}")

    recipes4 = []
    ingredients4 = []
    supplies4 = ["yeast", "flour"]
    result4 = find_all_recipes(recipes4, ingredients4, supplies4)
    print(f"Recipes for {recipes4}, {ingredients4}, {supplies4}: {result4}")

    recipes5 = ["bread"]
    ingredients5 = [["yeast","flour"]]
    supplies5 = ["yeast","flour","meat"]
    result5 = find_all_recipes(recipes5, ingredients5, supplies5)
    print(f"Recipes for {recipes5}, {ingredients5}, {supplies5}: {result5}")

    recipes6 = ["bread", "sandwich"]
    ingredients6 = [["yeast", "flour"], ["bread", "meat"]]
    supplies6 = ["meat"]
    result6 = find_all_recipes(recipes6, ingredients6, supplies6)
    print(f"Recipes for {recipes6}, {ingredients6}, {supplies6}: {result6}")
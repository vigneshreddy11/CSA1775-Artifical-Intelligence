from itertools import permutations

def solve_crypto_arithmetic(word1, word2, result):
    letters = set(word1 + word2 + result)
    if len(letters) > 10:
        print("Too many unique letters for a solution!")
        return

    for perm in permutations(range(10), len(letters)):
        mapping = dict(zip(letters, perm))

        # Ensure leading letters don't map to 0
        if mapping[word1[0]] == 0 or mapping[word2[0]] == 0 or mapping[result[0]] == 0:
            continue

        num1 = int("".join(str(mapping[letter]) for letter in word1))
        num2 = int("".join(str(mapping[letter]) for letter in word2))
        res = int("".join(str(mapping[letter]) for letter in result))

        if num1 + num2 == res:
            print(f"{word1} + {word2} = {result}")
            print(f"Solution: {mapping}")
            return

    print("No solution found.")

# Input
word1 = input("Enter the first word: ").upper()
word2 = input("Enter the second word: ").upper()
result = input("Enter the result word: ").upper()

# Solve
solve_crypto_arithmetic(word1, word2, result)

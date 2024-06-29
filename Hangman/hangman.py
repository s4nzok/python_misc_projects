import random
with open('wordlist.txt', 'r') as f:
    words = f.readlines()

word = random.choice(words)[:-1]
# -1 because the last character reads is always /n, we need to remove that.

allowed_errors = 7
guesses = []
done = False

while not done:
    for letter in word:
        if letter.lower() in guesses:
            print(letter, end=" ")
        else:
            print("_", end=" ")
    print("")
    # if we get the full word, we get the new line.

    guess = input(f"allowed errors = {allowed_errors}, next guess: ")
    guesses.append(guess.lower())
    if guess.lower() not in word.lower():
        allowed_errors -= 1
        if allowed_errors == 0:
            break

    done = True
    for letter in word:
        if letter.lower() not in guesses:
            done = False


if done:
    print(f"You have won the game. The word is {word}")
else:
    print(f"You lost the game. The word was {word}")


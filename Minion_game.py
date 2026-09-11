def minion_game(string):
    # your code goes here
    
    vowels = "AEIOU"
    kevin = 0
    stuart = 0

    for i in range(len(string)):
        # Number of substrings starting at position i
        score = len(string) - i

        if string[i] in vowels:
            kevin += score
        else:
            stuart += score

    if kevin > stuart:
        print("Kevin", kevin)
    elif stuart > kevin:
        print("Stuart", stuart)
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)
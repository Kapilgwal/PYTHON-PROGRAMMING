from collections import deque

def wordLadder(wordList: list[str], startWord: str, targetWord: str) -> int:
    # Convert wordList to a set for faster lookup
    wordSet = set(wordList)
    
    if targetWord not in wordSet:
        return 0

    q = deque([[startWord, 1]])
    wordSet.remove(startWord)  # Use 'remove' instead of 'erase'

    while q:
        currentWord, steps = q.popleft()
        
        if currentWord == targetWord:
            return steps

        for i in range(len(currentWord)):
            original_char = currentWord[i]
            word_as_list = list(currentWord)
            
            for j in 'abcdefghijklmnopqrstuvwxyz':
                word_as_list[i] = j
                new_word = ''.join(word_as_list)
                
                if new_word in wordSet:
                    wordSet.remove(new_word)
                    q.append([new_word, steps + 1])
            
            word_as_list[i] = original_char
    
    return 0

def main():
    wordList = ["des", "der", "dfr", "dgt", "dfs"]
    startWord = "der"
    targetWord = "dfs"
    ans = wordLadder(wordList, startWord, targetWord)
    print(ans)

if __name__ == "__main__":
    main()

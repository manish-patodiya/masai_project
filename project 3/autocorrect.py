class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

def damerau_levenshtein_distance(s1, s2):
    len_s1 = len(s1)
    len_s2 = len(s2)
    d = [[0] * (len_s2 + 1) for _ in range(len_s1 + 1)]

    for i in range(len_s1 + 1):
        d[i][0] = i
    for j in range(len_s2 + 1):
        d[0][j] = j

    for i in range(1, len_s1 + 1):
        for j in range(1, len_s2 + 1):
            cost = 0 if s1[i - 1] == s2[j - 1] else 1
            d[i][j] = min(
                d[i - 1][j] + 1,
                d[i][j - 1] + 1,
                d[i - 1][j - 1] + cost
            )
            if i > 1 and j > 1 and s1[i - 1] == s2[j - 2] and s1[i - 2] == s2[j - 1]:
                d[i][j] = min(d[i][j], d[i - 2][j - 2] + cost)

    return d[len_s1][len_s2]

def load_dictionary(file_path):
    with open(file_path, 'r') as file:
        words = [line.strip() for line in file]
    return words

def save_dictionary(words, file_path):
    with open(file_path, 'w') as file:
        file.write('\n'.join(words))

def suggest_spellings(trie, word):
    MAX_SUGGESTIONS = 5  # Set the maximum number of suggestions to display

    def dfs(node, path, depth):
        if depth > max_depth or not node:
            return
        if node.is_end_of_word:
            suggestions.append((''.join(path), depth))
        for char, child_node in node.children.items():
            dfs(child_node, path + [char], depth + 1)

    max_depth = len(word) + 2  # Set the maximum depth for exploring the Trie
    suggestions = []

    # Perform depth-first search on Trie for potential suggestions
    current_node = trie.root
    for char in word:
        if char not in current_node.children:
            break
        current_node = current_node.children[char]

    if current_node:
        dfs(current_node, list(word), 0)

    # Sort suggestions based on Damerau-Levenshtein distance
    suggestions.sort(key=lambda x: (x[1], x[0]))

    # Return only top MAX_SUGGESTIONS suggestions
    return [suggestion[0] for suggestion in suggestions[:MAX_SUGGESTIONS]]

def main():
    dictionary_file = 'C:\VS Code\python\dictionary.txt'  # Replace with the path to your dictionary file
    trie = Trie()
    dictionary = load_dictionary(dictionary_file)
    for word in dictionary:
        trie.insert(word)

    while True:
        user_input = input("Enter a word (type 'exit' to quit): ").lower()
        if user_input == 'exit':
            break
        
        if user_input.isalpha():
            if trie.search(user_input):
                print(f"'{user_input}' is a valid word.")
            else:
                suggestions = suggest_spellings(trie, user_input)
                print(f"Did you mean {suggestions} ?")
        else:
            print("Please enter only alphabetic characters.")
    
    # Save dictionary modifications if any
    save_dictionary(dictionary, dictionary_file)

main()

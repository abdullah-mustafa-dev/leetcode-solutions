class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class MagicDictionary:
    def __init__(self):
        self.root = TrieNode()

    def buildDict(self, dictionary):
        for word in dictionary:
            node = self.root
            for ch in word:
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]
            node.is_word = True

    def search(self, searchWord):
        def dfs(node, idx, changed):
            if idx == len(searchWord):
                return changed and node.is_word
            ch = searchWord[idx]
            for c, child in node.children.items():
                if c == ch:
                    if dfs(child, idx + 1, changed):
                        return True
                elif not changed:
                    if dfs(child, idx + 1, True):
                        return True
            return False

        return dfs(self.root, 0, False)
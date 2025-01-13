from trie import Trie


class LongestCommonWord(Trie):

    def find_longest_common_word(self, strings) -> str:
        if not isinstance(strings, list):
            raise ValueError("`strings` must be an array of strings")

        if not strings:
            return ""

        # Додаємо слова в Trie
        for string in strings:
            self.put(string)

        current = self.root
        prefix_chars = []

        while current and len(current.children) == 1 and current.value is None:
            char = next(iter(current.children))
            prefix_chars.append(char)
            current = current.children[char]

        return "".join(prefix_chars)


if __name__ == "__main__":
    # Тести
    trie = LongestCommonWord()
    strings = ["flower", "flow", "flight"]
    assert trie.find_longest_common_word(strings) == "fl"

    trie = LongestCommonWord()
    strings = ["interspecies", "interstellar", "interstate"]
    assert trie.find_longest_common_word(strings) == "inters"

    trie = LongestCommonWord()
    strings = ["dog", "racecar", "car"]
    assert trie.find_longest_common_word(strings) == ""

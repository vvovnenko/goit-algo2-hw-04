from trie import Trie


class Homework(Trie):
    def __init__(self):
        super().__init__()
        self.reversed_trie = Trie()

    def put(self, key, value=None):
        super().put(key, value)
        self.reversed_trie.put(key[::-1], value)

    def count_words_with_suffix(self, pattern) -> int:
        if not isinstance(pattern, str):
            raise ValueError("Pattern must be a string.")

        # перебір кожного слова в Trie для перевірки суфікса може бути неефективним для великої кількості слів
        # для оптимізації будемо працювати з інвертованим Trie і шукати по інвертованому патерну
        return len(self.reversed_trie.keys_with_prefix(pattern[::-1]))

    def has_prefix(self, prefix) -> bool:
        if not isinstance(prefix, str):
            raise ValueError("Prefix must be a string.")

        current = self.root
        for char in prefix:
            if char not in current.children:
                return False
            current = current.children[char]

        return True


if __name__ == "__main__":
    trie = Homework()
    words = ["apple", "application", "banana", "cat"]
    for i, word in enumerate(words):
        trie.put(word, i)

    # Перевірка кількості слів, що закінчуються на заданий суфікс
    assert trie.count_words_with_suffix("e") == 1  # apple
    assert trie.count_words_with_suffix("ion") == 1  # application
    assert trie.count_words_with_suffix("a") == 1  # banana
    assert trie.count_words_with_suffix("at") == 1  # cat

    # Перевірка наявності префікса
    assert trie.has_prefix("app") == True  # apple, application
    assert trie.has_prefix("bat") == False
    assert trie.has_prefix("ban") == True  # banana
    assert trie.has_prefix("ca") == True  # cat

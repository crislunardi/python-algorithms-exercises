class UniqueSubstringSolver:
    def __init__(self, s: str):
        self.s = s
    
    def find_longest_unique_substring(self) -> int:
        # Conjunto para armazenar os caracteres únicos na janela
        chars = set()
        # Ponteiro esquerdo da janela
        left = 0
        # Armazena o tamanho máximo encontrado
        max_len = 0

        # Percorre a string com ponteiro direito
        for right in range(len(self.s)):
            # Se já tem o caractere na janela, move o ponteiro esquerdo
            while self.s[right] in chars:
                chars.remove(self.s[left])
                left += 1
            chars.add(self.s[right])
            max_len = max(max_len, right - left + 1)

        return max_len
    
# Testando a classe
solver1 = UniqueSubstringSolver("abcabcbb")
print(solver1.find_longest_unique_substring())  # 3

solver2 = UniqueSubstringSolver("bbbbb")
print(solver2.find_longest_unique_substring())  # 1

solver3 = UniqueSubstringSolver("pwwkew")
print(solver3.find_longest_unique_substring())  # 3
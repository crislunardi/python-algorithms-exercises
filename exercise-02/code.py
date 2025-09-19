# Versão com métodos prontos
print("""
-------------------------------------------------
Versão com métodos prontos
-------------------------------------------------
""")

def is_palindrome(s: str) -> bool:
    # Remove espaços e transforma os caracteres em minúsculos
    s = s.replace(" ", "").lower()

    # Compara string com ela mesma invertida
    return s == s[::-1]

print(is_palindrome("Cristian")) # False
print(is_palindrome("Ovo")) # True

# Versão sem métodos prontos e orientada a objetos

class PalindromeChecker:
    def __init__(self, text: str):
        self.text = text

    def _to_lowercase(self, char: str) -> str:
        # Converte maiúsculo para minúsculo
        # Usa ord() para pegar o código Unicode da letra maiúscula, soma 32 para obter minúscula e converte de volta com chr().
        if "A" <= char <= "Z":
            return chr(ord(char) + 32)
        return char
    
    def _clean_text(self) -> str:
        # Remove espaço e normaliza caracteres
        cleaned = ""
        for c in self.text:
            lower_c = self._to_lowercase(c)
            if lower_c != " ":
                cleaned += lower_c
        return cleaned
    
    def is_palindrome(self) -> bool:
        # Verifica se o texto é palíndromo
        s = self._clean_text()
        left, right = 0, len(s) - 1

        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        
        return True

print("""
-------------------------------------------------
Versão sem métodos prontos e orientada a objetos
-------------------------------------------------
""")

solver1 = PalindromeChecker("Cristian")
print(solver1.is_palindrome()) # False

solver2 = PalindromeChecker("Ovo")
print(solver2.is_palindrome()) # True
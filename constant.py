def solve(s):
    vowels = "aeiou"
    consonant_values = {char: ord(char) - ord('a') + 1 for char in "abcdefghijklmnopqrstuvwxyz"}
    
    def get_consonant_value(substring):
        return sum(consonant_values[char] for char in substring)
    
    max_value = 0
    current_value = 0
    
    for char in s:
        if char not in vowels:
            current_value += consonant_values[char]
        else:
            max_value = max(max_value, current_value)
            current_value = 0
    
    # Check the last substring
    max_value = max(max_value, current_value)
    
    return max_value

# Examples
print(solve("zodiacs"))  # Output: 26
print(solve("strength"))  # Output: 57

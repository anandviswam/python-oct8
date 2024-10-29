string_input=input("enter a string")
vowels="aeiouAEIOU"
vowel_count=0
for char in string_input:
    if char in vowels:
        vowel_count+=1
print(f"no of vowels is the given string{string_input}={vowel_count}")
# /LogicMojo-AI-ML-April26-VishnuDuggisetty

# 26 April 2026

### 1. Palindrome Check
s = input()
print("Palindrome" if s == s[::-1] else "Not Palindrome")

### 2. Count Blank Spaces
s = input()
print(s.count(" "))

### 3. Reverse String (without reverse())
s = input()
rev = ""
for c in s:
    rev = c + rev
print(rev)

### 4. Count & Print Vowels
s = input()
v = "aeiouAEIOU"
res = [c for c in s if c in v]
print(len(res))
print(res)
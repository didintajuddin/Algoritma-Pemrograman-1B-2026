def palindrome(kata):
    return kata == kata[::-1]

kata = input("Masukkan kata: ")
print(kata)

hasil = palindrome(kata)
if hasil:
    print(f"Kata '{kata}' adalah palindrome.")
else:
    print(f"Kata '{kata}' bukan palindrome.")
    
alphabet = "abcdefghijklmnopqrstuvwxyz"
plainText = input("enter word to encode  :")
encoded = ""
decoded = ""
shiftKey = int(input("enter a shift key  :"))
for ch in plainText:
   encoded += alphabet[(alphabet.index(ch)+shiftKey)%26]
print(f"ENcoded message :{encoded}")
dec = input("Do you want to decode ?(y/n)")
if dec == "y":
      key = int(input("enter a key to decode"))
     

      for ch in encoded:
            decoded += alphabet[(alphabet.index(ch)-key)%26]
            
      
print(f"Decoded message :{decoded}")    
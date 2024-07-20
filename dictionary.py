oer = {
    "Haider":"96", "Kashif":"95", "Fahad":"94", "Tayyab":"93", 
    "Sana":"92", "Ibrahim":"91", "Ali":"90"
}

print (oer.keys())
print (oer.values())
print (oer.items())
for key, value in oer.items():
    print (f"OER Marks of {key} is {value} ")
print (sorted (oer.items()))  
print (sorted (oer))
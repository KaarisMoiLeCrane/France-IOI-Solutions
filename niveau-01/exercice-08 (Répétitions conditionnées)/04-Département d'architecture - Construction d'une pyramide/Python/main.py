max_pierres = int(input())
pierres_utilisees = 0
cotes = 0

while max_pierres != 0 and pierres_utilisees + (cotes + 1) * (cotes + 1) <= max_pierres:
    cotes += 1
    pierres_utilisees += cotes**2

print(cotes)
print(pierres_utilisees)

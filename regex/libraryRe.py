import re

log = "July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade"
regex = r"\[(\d+)\]"
result = re.search(regex, log)
#print(result[1])

# Search for pattern "aza" in string "plaza"
# Return a match object with index position or None
match= re.search(r"aza", "plaza")
print(match)

# Search multiple letters in string
match = re.search(r"b.a.r", "bazaar")

# Search with ignore case
match = re.search(r"p.ng", "Pangea", re.IGNORECASE)")
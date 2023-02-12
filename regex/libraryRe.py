import re

log = "July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade"
logError = "99 elephants in a [cage]"
regex = r"\[(\d+)\]"
result = re.search(regex, log)
#print(result[1])
def extract_pid(log_line):
    regex = r"\[(\d+)\]"
    result = re.search(regex, log_line)
    if result is None:
        return ""
    return result[1]
print(extract_pid(log))

# Search for pattern "aza" in string "plaza"
# Return a match object with index position or None
match= re.search(r"aza", "plaza")

# Search multiple letters in string
match = re.search(r"b.a.r", "bazaar")
# Search with ignore case
match = re.search(r"p.ng", "Pangea", re.IGNORECASE)
# Search with ignore case one letter
match = re.search(r"[Pp]ython", "Python")
#Search for a-z
match = re.search(r"[a-z]way", "The end of the highway")
# Search for a-z and A-Z and 0-9
match = re.search(r"[a-zA-Z0-9]way", "The end of the highway")
# Search without vowels in string using ^
matchs = re.search(r"[^a-zA-Z]", "The end of the highway 123")
# Search one or more characters
match = re.search(r"cat|dog", "I like cats")
# Fin all matches
match = re.findall(r"cat|dog", "I like cats and dogs")
# Search all between two characters
match = re.findall(r"Py.*n", "Pygmalion")
# Search one or more characters
match = re.search(r"Py[a-z]*n", "Python Programming")
# Search two caracters together
match = re.search(r"o+l+", "goldfish")
# Search charaters with exist or not
match = re.search(r"p?each", "To each their own")
# Search with escape characters
match = re.search(r"\.com", "drako.com")
# \w scape numbers, letters and underscore
match = re.search(r"\w*", "This is an example")
# \d scape numbers
match = re.search(r"\d*", "This is an example 123")
# \s scape spaces
match = re.search(r"\s*", "This is an example 123")
# \b scape spaces
matchs = re.search(r"\bthe", "bite the dog")
# $ string end 
match = re.search(r"dog$", "The dog is here")
match = re.search(r"^A.*a$", "Argentina Australia")
# Search variable name
match = re.search(r"^[a-zA-Z_][a-zA-Z0-9_]*$", "this_is_a_valid_variable_name")

#########
# Search agrups strings
result = re.search(r"^(\w*), (\w*)$", "Lovelace, Ada")
print("{} {}".format(result[2], result[1]))

# Search five consecutive characters
result = re.search(r"[a-zA-Z]{5}", "a ghost")
# Find all five consecutive characters
result = re.findall(r"[a-zA-Z]{5}", "a scary ghost appeared")
# Find all esactly five consecutive characters
result = re.findall(r"\b[a-zA-Z]{5}\b", "a scary ghost appeared")
# Find all five or ten letters
result = re.findall(r"\w{5,10}", "I really like strawberries")
# Find all five letters or more
result = re.findall(r"\w{5,}", "I really like strawberries")
# Search for a string that starts with s and contain -20 characters
result = re.findall(r"\s\w{,20}", "I really like strawberries")

#### Split
# Split string
result = re.split(r"[.?!]", "One sentence. Another one? And the last one!")
# Split string with limit
result = re.split(r"([.?!])", "One sentence. Another one? And the last one!")
# Split string with limit and keep the separator
result = re.split(r"[.?!]", "One sentence. Another one? And the last one!", maxsplit=1)
# Sub string, similar to replace string
result = re.sub(r"[\w.%+-]+@[\w.-]+", "[REDACTED]", "Received an email for]")
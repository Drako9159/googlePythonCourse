import re
import operator
lines = ["Jan 31 00:16:25 ubuntu.local ticky: INFO: Closed ticket [#1754] (noel)",
"Jan 31 00:21:30 ubuntu.local ticky: ERROR: The ticket was modified while updating (breen)",
"Jan 31 00:44:34 ubuntu.local ticky: ERROR: Permission denied while closing ticket (ac)",
"Jan 31 00:23:32 ubuntu.local ticky: ERROR: Tried to add information to closed ticket (oren)"]
#line = "May 27 11:45:40 ubuntu.local ticky: INFO: Created ticket [#1234] (username)"

error = {}
for line in lines:
    result = re.search(r"ticky: ERROR: ([\w ]*) ", line)
  
    #sorted(lines.items(), key=operator.itemgetter(1), reverse=True)
    
def dictionary():
    fruit = {"oranges": 3, "apples": 5, "bananas": 7, "pears": 2}
    #order = sorted(fruit.items())
    order = sorted(fruit.items(), key=operator.itemgetter(1), reverse=True)
    print(order)

dictionary()
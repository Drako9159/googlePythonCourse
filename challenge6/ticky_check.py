#!/usr/bin/env python3

# First, import all the Python modules that you'll use 
# in this Python script. After importing the necessary modules, 
# initialize two dictionaries: one for the number of different 
# error messages and another to count the number 
# of entries for each user (splitting between INFO and ERROR).

import csv
import re
import operator
import sys

error_messages = {}
per_user = {}

#logfile= sys.argv[1]
logfile = "syslog.log"

def get_errors():
   with open(logfile) as f:
    for line in f:
        result = re.search(r"ticky: ERROR ([\w' ]*) ", line)
        if result:
            if result.group(1) not in error_messages:
                error_messages[result.group(1)] = 1
            else:
                error_messages[result.group(1)] += 1
    order = sorted(error_messages.items(), key=operator.itemgetter(1), reverse=True)
    with open("error_message.csv", mode="w") as file:
        writer = csv.DictWriter(file, fieldnames=["Error", "Count"], delimiter=",", lineterminator="\n")
        writer.writeheader()
        for key, value in order:
            writer.writerow({"Error": key, "Count": value})
    return error_messages
get_errors()


def get_users():
   with open(logfile) as f:
    for line in f:
        result = re.search(r"ticky: (INFO|ERROR) ([\w' \[#\d\]]*) \(([\w.]*)\)", line)
        if result:
            if result.group(3) not in per_user:
                per_user[result.group(3)] = {"INFO": 0, "ERROR": 0}
            if result.group(1) == "INFO":
                per_user[result.group(3)]["INFO"] += 1
            elif result.group(1) == "ERROR":
                per_user[result.group(3)]["ERROR"] += 1
    order = sorted(per_user.items(), key=operator.itemgetter(0))  
    with open("user_statistics.csv", mode="w") as file:
        writer = csv.DictWriter(file, fieldnames=["Username", "INFO", "ERROR"], delimiter=",", lineterminator="\n")
        writer.writeheader()
        for key, value in order:
            writer.writerow({"Username": key, "INFO": value["INFO"], "ERROR": value["ERROR"]})
    return per_user

get_users()
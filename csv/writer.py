import csv

hosts = [["workstation.local", "192.168.25.46"], ["webserver.cloud", "10.2.5.6"], ["clound-home", "192.168.1.254"]]
with open("hosts.csv", "w") as hosts_csv:
    writer = csv.writer(hosts_csv, delimiter=",", lineterminator="\n", quotechar='"', quoting=csv.QUOTE_ALL)
    #writerow or writerows
  
    writer.writerows(hosts)




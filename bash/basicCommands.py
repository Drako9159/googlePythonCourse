# echo command in Linux to print to the screen
echo
# cat command in Linux to show the content of a file
cat
# grep command in Linux to search for a pattern in a file
grep
# wc command in Linux to count the number of lines, words, and characters in a file
wc
# sort command in Linux to sort the lines of a file
sort
# pwd command in Linux to show the current directory
pwd
# cp command in Linux to copy files and directories
cp script.py ../
# uniq command in Linux to remove duplicate lines from a file
uniq
# touch command in Linux to create a new file
touch script.py
# ls -a command in Linux to show all files and directories including hidden files
ls -a
# mv command in Linux to move files and directories to a new location or rename files and directories
mv script.py renamescript.py
# rm * command in Linux to remove all files and directories
rm *
# send data to a file but not overwrite the file
echo "Hello World" > hello.txt
# send data to a file and overwrite the file
echo "Hello World" >> hello.txt
# from file to input
./script.py < hello_world.txt
# send error to a file
./streams_err.py < new_file.txt 2> error_file.txt
# comand to count the number of lines in a file
cat spider.txt | tr " " "\n" | sort | uniq -c | sort -nr | head
# capt and send stdin to a file
cat spider.txt | tr " " "\n" | sort | uniq -c | sort -nr | head > output.txt
# catpt and send stdin and stderr to a file
./capitalize.py < haiku.txt
# catpt and send stdin and stderr to a file
cat haiku.txt | ./capitalize.py
# show process
ps
# show process with id
ps ax
# show process with grep for filter python
ps | grep python
# kill process
kill 1234
# free command in Linux to show the amount of free and used memory in the system
free
# uptime command in Linux to show how long the system has been running
uptime
# shos all py files
ls *.py 
# show all py files with five letters
ls ?????.py
# head command in Linux to show the first lines of a file
head
# extract name and extension
bansename index.html .html
# tail command in Linux to show the last lines of a file
tail
# cut command in Linux to cut out sections of each line of a file
cut
# sed command in Linux to find and replace text in a file
sed
# awk command in Linux to find and replace text in a file
awk
# tr command in Linux to find and replace text in a file
tr
# diff command in Linux to compare two files
diff
# paste command in Linux to merge lines of two files
paste
# join command in Linux to join lines of two files on a common field
join
# find command in Linux to find files
find
# xargs command in Linux to execute commands using standard input as arguments
xargs
# chmod command in Linux to change file permissions
chmod
# chown command in Linux to change file ownership
chown
# chgrp command in Linux to change file group ownership
chgrp
# tar command in Linux to create and extract tarball files
tar
# gzip command in Linux to compress and decompress files
gzip
# bzip2 command in Linux to compress and decompress files
bzip2
# zip command in Linux to compress and decompress files
zip
# unzip command in Linux to compress and decompress files
unzip
# rsync command in Linux to synchronize files and directories
rsync
# ssh command in Linux to connect to a remote machine
ssh
# scp command in Linux to copy files between machines
scp
# sftp command in Linux to transfer files
sftp
# wget command in Linux to download files from the Internet
wget
# curl command in Linux to download files from the Internet
curl
# lynx command in Linux to browse the Internet from the command line
lynx

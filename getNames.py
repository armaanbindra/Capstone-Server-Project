#!/usr/bin/python

import os, sys

forUser = False   # command line option for specifying a particular user
if (len(sys.argv) > 2) and (sys.argv[1] == '-user'):
  forUser = sys.argv[2]
  del sys.argv[1]
  del sys.argv[1]

workingRoot = "/home/cg/palantir/w"
os.chdir(workingRoot)

numMentions = {}  # dictionary that will store the number of tiles associated
                  #   with a given name
userMention = {}  # dictionary that stores an example username for this name
# the following nested loop finds all the tile files.  When we find
#   a tile, we split the first line of the file into three words, and
#   from those words we recover the username and the name of the tile.
#   We then store these two strings in the above mentioned dictionaries.
if os.path.exists(workingRoot + '/t'):
  for digit0 in os.listdir(workingRoot + '/t'):
    for digit1 in os.listdir(workingRoot + '/t/' + digit0):
      path = workingRoot + '/t/' + digit0 + '/' + digit1
      for tile in os.listdir(path):
        if forUser and not tile.endswith(forUser):
          continue
        words = open(path + '/' + tile).readline().split()
        username = words[1][3:]
        tileName = words[2]
        numMentions[tileName] = numMentions.get(tileName, 0) + 1
        userMention[tileName] = username

# to print it out, we find all the keys in the numMentions dictionary,
#   sort them by the value, and print out some info.  If you'd like
#   to have a simpler loop that doesn't sort the entries, just do
#   for tileName in numMentions.keys():
for tileName in sorted(numMentions.keys(), key=lambda n: numMentions[n]):
  if 1 == numMentions[tileName]:
    print tileName, numMentions[tileName], '['+userMention[tileName]+']'
  else:
    print tileName, numMentions[tileName]

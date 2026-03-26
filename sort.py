import os

with open("/Users/admin/Documents/muons/lifetimes.txt", "r") as infile:
    with open("/Users/admin/Documents/muons/sorted_lifetimes.txt", "w") as outfile:
        contents = infile.read().split("\n")
        contents.sort(key=lambda x: x.split(" ")[-1])
        for content in contents:
            outfile.write(content + "\n")
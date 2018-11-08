items_list = []
duplicates = []
nonduplicates = []

filedata = open('datafile','r')

for records in filedata:
    items_list.append(records.replace('\n',''))

for item in items_list:
    if items_list.count(item) == 1:
        nonduplicates.append(item)
    else:
        try:
            duplicates.index(item)
        except:
            duplicates.append(item)


print("Non Duplicates:")
for item in nonduplicates:
    print(item)

print()

print("Duplicates:")
for item in duplicates:
    print(item)



duplicates = []
nonduplicates = []

filedata = open('datafile','r')

for records in filedata:
    try:
        nonduplicates.index(records.replace('\n',''))
        nonduplicates.remove(records.replace('\n',''))
        try:
            duplicates.index(records.replace('\n',''))
        except:
            duplicates.append(records.replace('\n',''))
    except:
        nonduplicates.append(records.replace('\n',''))

print("Non Duplicates:")
for item in nonduplicates:
    print(item)

print()

print("Duplicates:")
for item in duplicates:
    print(item)

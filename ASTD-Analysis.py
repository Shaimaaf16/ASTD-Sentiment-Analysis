def reading_asdt(filename):
    # A list that contains ASTD lables
    labels = []
    # A list that contains ASTD Tweets
    dataset = []
    # A list that contains ASTD labels
    new_labels = []

    file = open(filename, 'r', encoding='utf-8')
    i = 0
    for line in file:
        labels.append(line[-4:])
        labels[i] = labels[i][0:3]
        if (labels[i] == "RAL"):
            dataset.append(line[0:len(line) - 8])
        else:
            dataset.append(line[0:len(line) - 5])

        i = i + 1
    return dataset, labels

dataset,labels=reading_asdt("Tweets.txt")
print(len(dataset),len(labels))
result = []
index=0
for i in labels:

    if(i=="\tNE"):
        print(index)
    if i not in result:
        result. append(i)
    index+=1


print (result) #outside for
print(dataset[10004],labels[10004])




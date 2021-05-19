import itertools
while 1==1:

    mismatches = []
    firstfile = input("file 1 :")
    secondfile = input("file 2 :")
    outputfilepath = input("output file path : ")

    with open(firstfile) as f1, open(secondfile) as f2:
        for lineno, (line1, line2) in enumerate(itertools.zip_longest(f1, f2), 1):
            if line1 != line2:
                mismatches.append(lineno)

    with open(firstfile, 'r') as file1:
        with open(secondfile, 'r') as file2:
            differencefrom1 = set(file1).difference(file2)
    with open(secondfile, 'r') as file1:
        with open(firstfile, 'r') as file2:
            differencefrom2 = set(file1).difference(file2)

    differencefrom1.discard('\n')

    filename = firstfile.rsplit('\\', 1)[-1]
    output = "/"+filename
    output_path = outputfilepath + output

    with open(output_path, 'w') as file_out:
        file_out.write("Differences from file staging :")
        for line in differencefrom1:
            for line_number in mismatches:
                file_out.write('\n'+"Is different : "+str(line)+", line number : "+str(line_number))
    with open(output_path, 'a') as file_out:
        file_out.write("\r\nDifferences from file production :")
        for line in differencefrom2:
            file_out.write('\n'+"Is different : "+str(line)+", line number : "+str(line_number))
    
    
    print("Differences done in "+ filename)
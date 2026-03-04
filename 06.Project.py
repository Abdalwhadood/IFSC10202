# 06.Project.py

input_count = 0
merge_count = 0
output_count = 0

with open("06.Project Output File.txt", "w") as output_file:
    with open("06.Project Input File.txt", "r") as input_file:
        
        for line in input_file:
            
            if "**Insert Merge File Here**" in line:
                
                with open("06.Project Merge File.txt", "r") as merge_file:
                    for merge_line in merge_file:
                        output_file.write(merge_line)
                        merge_count += 1
                        output_count += 1
            else:
                output_file.write(line)
                input_count += 1
                output_count += 1

print(input_count, "input file records")
print(merge_count, "merge file records")
print(output_count, "output file records")
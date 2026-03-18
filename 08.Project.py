
def main():
    file = open("Constitution.txt", "r")
    lines = []

    for line in file:
        lines.append(line.strip())  

    file.close()

    while True:
        search = input("Enter search term: ")

        if search == "":
            break

        search = search.lower()  

        i = 0
        while i < len(lines):
            line = lines[i]

            if search in line.lower():

                start = i
                while start > 0 and lines[start] != "":
                    start -= 1

                end = i
                while end < len(lines) - 1 and lines[end] != "":
                    end += 1


                for j in range(start, end + 1):
                    print(f"Line {j + 1}: {lines[j]}")

                print()  


                i = end

            i += 1


main()
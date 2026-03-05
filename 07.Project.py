def ParseDegreeString(ddmmss):
    deg_sym = ddmmss.find(chr(176))
    min_sym = ddmmss.find("'")
    sec_sym = ddmmss.find('"')

    degrees = float(ddmmss[:deg_sym])
    minutes = float(ddmmss[deg_sym + 1 : min_sym])
    seconds = float(ddmmss[min_sym + 1 : sec_sym])

    return degrees, minutes, seconds

def DDMMSStoDecimal(degrees, minutes, seconds):
    decimal_degrees = degrees + (minutes / 60) + (seconds / 3600)
    return decimal_degrees

def main():
    input_filename = "07.Project Angles Input.txt"
    output_filename = "07.Project Angles Output.txt"
    count = 0

    try:
        with open(input_filename, 'r') as infile, open(output_filename, 'w') as outfile:
            for line in infile:
                line = line.strip()
                if not line:
                    continue # Skip empty lines
                
                d, m, s = ParseDegreeString(line)

                decimal_val = DDMMSStoDecimal(d, m, s)
                
                outfile.write(str(decimal_val) + "\n")
                count += 1
        
        print(f"{count} records processed")

    except FileNotFoundError:
        print(f"Error: {input_filename} not found. Please create the file first.")

if __name__ == "__main__":
    main()
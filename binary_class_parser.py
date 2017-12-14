

with infile as open("output_all.csv", "r"):
    with outfile as open("words_all_no_repeats.csv"):
        for line in infile:
            csv = line.split(',')
            print(csv)

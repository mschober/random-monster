def parse_tsv(file_path):
    import csv
    with open(file_path) as tsvfile:
        tsvreader = csv.reader(tsvfile, delimiter="\t")
        header = tsvreader.next()
        lines = []
        for line in tsvreader:
            lines.append(line)
        return header, lines

import sys
print zip(parse_tsv(sys.argv[1]))

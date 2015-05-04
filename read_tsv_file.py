def parse_tsv(file_path):
    import csv
    with open(file_path) as tsvfile:
        tsvreader = csv.reader(tsvfile, delimiter="\t")
        header = tsvreader.next()
        header = [ header_str.lower().replace(' ', '_') for header_str in header ]
        lines = []
        for line in tsvreader:
            lines.append(line)
        tsv_file = zip(header, lines)
        return tsv_file

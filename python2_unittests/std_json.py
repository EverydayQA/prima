

with open("lib/not_json.json", "rt") as f:
    with open("fruit_f.json", "wt") as f2:
        for i in f:
            line = i.replace('"sometimes"', 'sometimes')
            print line
            # f2.write(line)

import csv



with open('U:\\Mary\\Moody.csv','r',encoding='utf-8') as f:
    table = [row for row in csv.reader(f)]
    headers = table[0]
    for observation in table:
        permno = observation[0]
        data = observation[1:]
        permno_l = [permno] * len(data)
        years = headers[1:]
        with open('U:\\Mary\\Moody_transforned.csv','a',newline='') as f:
            csv_outfile = csv.writer(f)
            for i, j, k in zip(permno_l, years, data):
                csv_outfile.writerow([i,j,k])
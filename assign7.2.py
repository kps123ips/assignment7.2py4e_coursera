fh=open('mbox-short.txt')
count = 0
tot = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") :
        continue
    ipos = line.find('0')
    tot += float(line[ipos:ipos+6])
    count += 1
    average = tot / count
    #print float(line[pos:pos+6]), sum, count, average
    #print line
#print "Done"
print ("Average spam confidence:", average)

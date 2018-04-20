
#  splitAlignments.py
#  
#
#  Created by Eleanor Chodroff on 3/25/15.
#
#  Modified on 01/17/18
#

import sys,csv

results=[]

#name = name of first text file in final_ali.txt
#name_fin = name of final text file in final_ali.txt

name = "DOS_F01_W3_181"
name_fin = "IWA_M01_W3_182"
try:
    with open("final_ali.txt") as f: # Make sure to include the final / to the path in the args
        next(f) #skip header
        for line in f:
            columns=line.split("\t")
            name_prev = name
            name = columns[1]
            if (name_prev != name):
                try:
                    with open((name_prev)+".txt",'a') as fwrite:
                        writer = csv.writer(fwrite)
                        fwrite.write("\n".join(results) + "\n")
                        fwrite.close()
                #print name
                #except Exception, e:
                except Exception as e:
                    print("Failed to write file",e)
                    sys.exit(2)
                del results[:]
                results.append(line[0:-1])
            else:
                results.append(line[0:-1])
#except Exception, e:
except Exception as e:
    print("Failed to read file",e)
    sys.exit(1)
# this prints out the last textfile (nothing following it to compare with)
try:
    with open((name_prev)+".txt",'a') as fwrite:
        writer = csv.writer(fwrite)
        fwrite.write("\n".join(results)+ "\n")
        fwrite.close()
                #print name
#except Exception, e:
except Exception as e:
    print("Failed to write file",e)
    sys.exit(2)


#read a ncbi cds file, parse positions, and use positions against the reference sequence the extract exons
import sys, argparse, re

#initialize parsing
parser = argparse.ArgumentParser()

#add new arguments one line at a time in the following format: "flag", type=<int,?> (optional), "long", "help"
parser.add_argument("-f", "--fasta", help="fasta file to extract exons from")
parser.add_argument("-g", "--genbank", help="complete genbank file for fasta")

#parse the arguments, store as object with methods
args = parser.parse_args()

#save sequence input fasta as a variable
saveSeq=""
heads=0
with open(args.fasta) as f:
    for line in f:
        if(heads > 1):
            print "more than one header found, break."
            break
        if(line[0] == ">"):
            heads += 1
        if(line[0] == "A" or line[0] == "T" or line[0] == "G" or line[0] == "C"):    
            saveSeq += line.strip()

#parse genbank for features, keeping exons seperate
with open(args.genbank) as gb:
    for line in gb:
        modline = line.split()
        if( len(modline) > 0 and ( modline[0] == "CDS" or modline[0] == "tRNA" or modline[0] == "rRNA"  )):
            #store strand
            if(modline[1][0:4] == "comp"):
                strand = "-"
            else:
                strand = "+"
            line1 = re.sub( "[A-Za-z()\t \]]", "", modline[1].strip())
            #nested try to avoid eof errors
            try:
                nline = next(gb).strip()
                if (nline[1:5] == "gene"):
                    header = nline.strip()
                    cHeader = ">" + header.split("=")[1].strip("\"").strip()
                else:
                    line1 += re.sub("[A-Za-z()\t \]]", "" ,nline)
                    try:
                        header = next(gb).strip()
                        cHeader = ">" + header.split("=")[1].strip("\"").strip()
                    except IndexError:
                        pass
            except IndexError:
                pass
            
            line2 = line1.split(",")
            e=1
            #loop through exons (even if only 1 exon for feature)
            for i in line2:
                cPos = i.split("..")
                ps1 = int(re.sub("[A-Za-z()\t \]]", "", cPos[0])) - 1
                ps2 = int(re.sub("[A-Za-z()\t \]]", "", cPos[1].split("/")[0]))
                #print informative header and sequence for feature
                print re.sub(" ", "_" , cHeader) +"_" + "Exon" + str(e) + "_" + "(" + strand + ")" + str(ps1+1) +":"+str(ps2)+ "\n" + saveSeq[ ps1 : ps2 ]
                e+=1


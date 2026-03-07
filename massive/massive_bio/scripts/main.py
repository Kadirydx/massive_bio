import sys
import pandas as pd
from Bio import SeqIO
import gzip

def process_fastq(input_file, output_file): 
    res = []
    
    with gzip.open(input_file, "rt") as handle: 
        
       
        for record in SeqIO.parse(handle, "fastq"):
            
            length = len(record.seq) 
    
            gc = (record.seq.count("G") + record.seq.count("C")) / length * 100
            
            quality_list = record.letter_annotations["phred_quality"]
            mean_quality = sum(quality_list) / length
            
            res.append([gc, length, mean_quality])

    df = pd.DataFrame(res, columns=["GC_Content", "Read_Length", "Mean_Quality"])
    df.to_csv(output_file, index=False)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Hata: girdi ve çıktı eksik")
        print("örnek: python scripts/main.py ......fastq.gz ......csv")
    else:
        process_fastq(sys.argv[1], sys.argv[2])
import glob
import os
import pandas as pd

f = glob.glob("../data/*.fsa")[0]

seq = ""

with open(f) as fl:
    for line in fl:
        if line.startswith(">"):
            continue
        else:
            l = line.strip()
            seq += l

def find_complementary(strand):
  complementary = ""
  GC_count = 0

  for char in strand:
    if char == "G":
      complementary += "C"
      GC_count += 1
    elif char == "C":
      complementary += "G"
      GC_count += 1
    elif char == "A":
      complementary += "T"
    elif char == "T":
      complementary += "A"

  GC_frac = GC_count/len(strand)

  return complementary, GC_frac

# Creating dataframe
df = pd.DataFrame(columns=["gRNA", "Sequence", "GC Content"])

for i in range(len(seq)):
        if i + 31 > len(seq):
            break
        else:
            comp, GC = find_complementary(seq[i:i+31])
            df.loc[i] = [i, comp, GC]

df.sort_values(by='GC Content', ascending=False, inplace=True)

# Save to Excel file
df.to_excel("data/gRNA.xlsx", index=False)
from db_handler import data
import pandas as pd

unique_lemmas = list(set(data["citation_form"]))
unique_lemmas.sort()

with open("aramaic/scripts/lemma_info.txt", mode="w", encoding="utf-8") as f:
    for i, n in enumerate(unique_lemmas):
        # print("< ", n, " >")
        f.write("< ")
        f.write(n)
        f.write(" >")
        f.write(" -- ")
        if i+1 != len(unique_lemmas): 
            f.write("\n")
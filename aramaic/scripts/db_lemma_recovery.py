import re
import pandas as pd

def txt_to_digit(txt: str) -> int:
    if txt.isnumeric():
        return int(txt)
    return 0

with open("aramaic/scripts/lemma_info.txt", mode="r", encoding="utf-8") as f:
    lines = [l.strip("\n") for l in f.readlines()]

new_words = []
etymology = []

for line in lines:
    m = re.search(r"\<(.*)\>\s\-\-\s(\d|)", line)
    if m != None:
        g = m.groups()
        # forming data from matched groups
        c = g[0].strip()
        t = txt_to_digit(g[1].strip())
        # adding words to our parallel data
        new_words.append(c)
        etymology.append(t)

new_data = pd.DataFrame({"word": new_words, "etymology": etymology})
new_data.to_csv("aramaic/lemma_etymology.csv")


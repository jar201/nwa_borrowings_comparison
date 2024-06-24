import sqlite3
import pandas as pd

QUERY_BASIC = '''
SELECT * FROM Lemmas WHERE {} LIKE '{}';
'''

QUERY_BUILD_ALL = '''
SELECT token_id, token_form, 
lemma_id, root, citation_form 
FROM Tokens, Types, Lemmas
WHERE type = type_id
AND lemma = lemma_id;
'''

class DataHandler():
    def __init__(self):
        self.modes = ["citation_form", "root"]
        self.data = {
            "words": ["ʕarḳūba", "šenna", "ṭūra"],
            "roots": ['ʕrḳb', 'šnn', 'ṭūra']
        }
        self.queries = {"basic": QUERY_BASIC}
        self.query_mode = "basic"
        self.sq = {"b": "basic"}
        self.query = QUERY_BASIC.format(self.modes[1], self.data["roots"][0])
        return
    
    def connect(self) -> sqlite3.Connection:
        """Establishes a connection"""
        return sqlite3.connect('aramaic_corpus.db')
    
    def search(self, word) -> None:
        """LEGACY -- formats the inner query to fit the word we are searching"""
        for key, value in self.data.items():
            if word in value:
                self.query = self.query.format(self.modes[0], word)
    
    def m_query(self, qt: str):
        self.query = self.queries[qt]

    def set_query(self, qt: str): 
        if isinstance(qt, str) and qt in self.queries.keys():
            self.m_query(qt) # set a query template
            self.query_mode = qt # set a query mode
            return
        self.m_query("basic")

    def qbasic(self):
        self.set_query(self.ssq("b")) # short query - basic

    def ssq(self, l: str):
        if isinstance(l, str) and l in self.sq.keys():
            return self.sq[l]
        return self.sq["b"]
    
    def w(self, word_index):
        return self.data["words"][word_index]

    def find(self, word):
        """finds a row that matches a word form"""
        self.qbasic() # short query - basic
        word = self.w(word)
        self.search(word)
        connection = self.connect()
        with connection:
            cursor = connection.cursor()
            cursor.execute(self.query)
        return cursor.fetchall()

    def build(self, tokens) -> pd.DataFrame:
        """Builds a dataset to operate"""
        data = pd.DataFrame({"word_form": [n[1] for n in tokens],
              "lemma_id": [n[2] for n in tokens],
              "word_root": [n[3] for n in tokens],
              "citation_form": [n[4] for n in tokens]}, index=[n[0] for n in tokens])
        return data

handler = DataHandler()

connection = handler.connect()

# FIND 
with connection:
    cursor = connection.cursor()
    cursor.execute(QUERY_BUILD_ALL)

tokens = cursor.fetchall()
data = handler.build(tokens)

data.to_csv("project_data.csv")

print()

print("Requested words:")
for n in [handler.find(n) for n in range(0, 3)]:
    n = n[0]
    print(n)



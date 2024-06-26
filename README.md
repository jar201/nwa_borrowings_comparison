# Arabic borrowings to New Western Aramaic Language
This R project explores the usage of arabic borrowings in Western Neo-Aramaic by speakers of different age based on the *Maaloula Aramaic Speech Corpus (MASC)*: https://zenodo.org/records/6496714 . For this project, we borrowed the database with lexical material described in *"Ghattas Eid, Esther Seyffarth, Ingo Plag. 2022. The Maaloula Aramaic Speech Corpus (MASC): From Printed Material to a Lemmatized and Time-Aligned Corpus"* (https://aclanthology.org/2022.lrec-1.699.pdf). Our R Notebook uses the manually labelled lexical data to analyse the difference in use of arabic borrowings by different ages. To explore word etymology we consulted the *Western Neo-Aramaic Dictionary by Werner Arnold (2019)*.

## Project structure

### images
Images for the project. **db_layout.png** image is borrowed directly from the MASC. It explores the structure of the database. The objects of our interest were primarily individual Tokens, Lemmas and Speakers. We reached the stated tables from the database using Python scripts which are located in the **scripts** folder of the project

### scripts
In this folder the **aramaic_corpus.db** is located which is technically the database described in *Ghattas Eid, Esther Seyffarth, Ingo Plag, 2022*. We searched this database for the necessary tokens and lemmas using our custom Python scripts such as *db_handler.py*, *db_lemma_info.py* and *db_lemma_recovery.py*. They are used to reach the database and export the necessary data into *.csv format which is easy to operate via Rlang. These files have a very narrow specialization and should be used with caution.

### main folder
In the main folder there are three files of interest: **Aramaic_comparison.Rmd**, which is the R Notebook where the research was being conducted, **project_data.csv**, which is the file where all necessary observations in the CSV format are stored, and the **lemma_etymology.csv**, which is the file that contains manually labelled word origin data for aramaic and non-aramaic words.
import packaging
import pyterrier as pt
import pandas as pd
import requests
import os


os.environ["JAVA_HOME"] = "C:\Program Files\Java\jdk-21"


if not pt.started():
    pt.init()

dataset = pt.get_dataset('irds:clinicaltrials/2019/trec-pm-2019')
# Index clinicaltrials/2019
indexer = pt.IterDictIndexer('./indices/clinicaltrials_2019', stemmer="porter", stopwords="terrier", tokeniser="UTFTokeniser")
index_ref = indexer.index(dataset.get_corpus_iter(), fields=['title', 'condition', 'summary', 'detailed_description', 'eligibility'])

bm25 = pt.BatchRetrieve(index_ref, wmodel="BM25")
result = bm25.search("Help")

pt.io.write_results(result, "res_bm25.txt", format="trec")

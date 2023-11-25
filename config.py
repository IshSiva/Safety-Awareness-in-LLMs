DOMAIN_INDEX_MAPPING = {
    "Discrimination, Exclusion, Toxicity": 1,
    "Misinformation": 2,
    "HCI harms": 3,
    "Malicious Uses": 4
}

DOMAIN_DATASET_MAPPING = {
    "adult_data.xlsx": 1,
    "hate_speech.csv": 1,
    "toxigen.csv": 1,
    "anxiety.csv": 3,
    "suicide.csv": 3,
    "cyberbullying.csv": 4,
    "suspicious_activity.csv": 4,
    "covid_fake_news_data.csv": 2,
    "true_false.csv":2,
    "fake_news.csv":2
}


BERT_EMBEDDING_FILES = {
    "Discrimination, Exclusion, Toxicity": "bert_discrimination.pkl",
    "Misinformation": "bert_misinfo.pkl" ,
    "HCI harms": "bert_hci_harms_df.pkl",
    "Malicious Uses": "bert_malicious_activity.pkl"
}

dataset_category_mapping = {
    "adult_content":
    {
       "column_text": "Description",
       "column_label": "Category",
       "column_mapping": {"Non_Adult":0, "Adult":1}
    },
    "hate_speech":
    {
       "column_text": "text",
       "column_label": "hatespeech",
       "column_mapping": {0: 2, 2:3}
    },
    "toxigen":
    {
       "column_text": "text",
       "column_label": "label",
       "column_mapping": {0:4, 1:5}
    },
    "anxiety":
    {
       "column_text": "text",
       "column_label": "label",
       "column_mapping": {0:6, 1:7}
    },
    "suicide":
    {
       "column_text": "text",
       "column_label": "class",
       "column_mapping": {'suicide':8, 'non-suicide':9}
    },
    "cyberbullying":
    {
       "column_text": "Text",
       "column_label": "oh_label",
       "column_mapping": {0:10, 1:11}
    },
    "suspicious_activity":
    {
       "column_text": "message",
       "column_label": "label",
       "column_mapping": {1:12, 0:13}
    },
    "covid_fake_news":
    {
       "column_text": "full_content",
       "column_label": "label",
       "column_mapping": {0:14, 1:15}

    },
    "true_false":
    {
       "column_text": "statement",
       "column_label": "label",
       "column_mapping": {0:16, 1:17}
    },
    "fake_news":
    {
        "column_text": "content",
        "column_label": "binary_label",
        "column_mapping": {1:18}
    }
   
}

#1 is not safe 0 is safe
index_class_mapping = {0: 0, 1:1, 2: 0, 3: 1, 4: 0 , 5: 1, 6: 0, 7: 1, 8: 1,\
                       9: 0, 10: 0, 11: 1, 12: 0, 13: 1, 14: 0, 15: 1, 16: 1, 17: 0, 18:1}

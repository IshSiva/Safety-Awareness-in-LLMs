LAYERS = [1, 4, 8, 12, 16, 20, 24, 28, 32]
DOMAINS = ["Discrimination, Exclusion, Toxicity", "HCI harms", "Malicious Uses", "Misinformation"]

DOMAIN_INDEX_MAPPING = {
    "Discrimination, Exclusion, Toxicity": 1,
    "Misinformation": 2,
    "HCI harms": 3,
    "Malicious Uses": 4,
    "Information Hazards": 5
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
    "true_false.csv":2
}

DOMAIN_FILE_MAPPING = {
    1: ["toxigen.pkl", "hate_speech.pkl", "adult_content.pkl"],
    2: ["covid_fake_news.pkl", "true_false.pkl", "mis_information.pkl"],
    3: ["student_anxiety.pkl", "suicide.pkl"],
    4: ["cyberbullying.pkl", "suspicious_activity.pkl"],
}

FILE_DOMAIN_MAPPING = {
    "toxigen.pkl": 1,
    "hate_speech.pkl": 1,
    "adult_content.pkl": 1,
    "covid_fake_news.pkl": 2,
    "true_false.pkl": 2,
    "mis_information.pkl": 2,
    "student_anxiety.pkl": 3,
    "bullying.pkl": 4,
    "abuse.pkl": 4,
    "do_not_answer_en.pkl": 5
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
       "column_mapping": {0: 2, 1:3}
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
    }
   
}

#1 is not safe 0 is safe
index_class_mapping = {0: 0, 1:1, 2: 0, 3: 1, 4: 0 , 5: 1, 6: 0, 7: 1, 8: 1,\
                       9: 0, 10: 0, 11: 1, 12: 0, 13: 1, 14: 0, 15: 1, 16: 1, 17: 0,}
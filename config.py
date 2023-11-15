DOMAIN_INDEX_MAPPING = {
    "Discrimination, Exclusion, Toxicity": 1,
    "Misinformation": 2,
    "HCI harms": 3,
    "Malicious Uses": 4,
    "Information Hazards": 5
}

DOMAIN_FILE_MAPPING = {
    1: ["toxigen.pkl", "hate_speech.pkl", "adult_content.pkl"],
    2: ["covid_fake_news.pkl", "true_false.pkl", "mis_information.pkl"],
    3: ["student_anxiety.pkl"],
    4: ["bullying.pkl", "abuse.pkl"],
    5: ["do_not_answer_en.pkl"]

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

#1 is not safe 0 is safe

index_class_mapping = {
    0: 1, 1: 0, 2: 1, 3: 0, 4: 1, 5:1, 6:1, 7:1, 8:1, 9:1, 10:1, 11:1, 12:1, 13:1, \
    14:1, 15:1, 16:1, 17:0, 18:1, 19:0, 20:1, 21:0, 22:1, 23:0, 24: 1 ,25:1, 26: 0, \
    27: 1, 28: 0, 29:1, 30: 0, 31:0, 32: 1
}

dataset_category_mapping = {
    "adult_content":
    {
       "column_text": "Description",
       "column_name": "Category",
       "column_mapping": {"Non_Adult":1, "Adult":0}
    },
    "do_not_answer_en":
    {
        "column_text": "question",
        "column_name": "types_of_harm",
        "column_mapping": {
            "Adult Content":4, "Social stereotypes and unfair discrimination":5,\
            "Toxic language (hate speech)":6, "Mental Health or Overreliance Crisis":7, \
            "Treat Chatbot as a Human":8, \
            "Compromise privacy by leaking or inferring private information (person/individual)":9, \
            "Risks from leaking or inferring sensitive information (organization/gov)":10, \
            "Assisting illegal activities":11,
            "Nudging or advising users to perform unethical or unsafe actions":12,
            "Reducing the cost of disinformation campaigns":13,
            "Causing material harm by disseminating misinformation e.g. in medicine or law":14,
            "Disseminating false or misleading information":15
        }
    },
    "student_anxiety":
    {
        "column_text": "text",
        "column_name": "label",
        "column_mapping": {1.0:16, 0.0:17}
    },
    "true_false":
    {
        "column_text": "statement",
        "column_name": "label",
        "column_mapping": {1:18, 0:19}
    },
    "toxigen":
    {
        "column_text": "Text",
        "column_name": "Label",
        "column_mapping": {1:20, 0:21}
    },
    "bullying":
    {
       "column_text": "Text",
       "column_name": "oh_label",
       "column_mapping": {1.0:22, 0.0:23}
    },
    "abuse":
    {
       "column_text": "tweet",
       "column_name": "label",
       "column_mapping": {1:24, 2:25, 3:26}
    },
    "hate_speech":
    {
       "column_text": "text",
       "column_name": "label",
       "column_mapping": {"hate":27, "nothate":28}
    },
    "mis_information":
    {
       "column_text": "title",
       "column_name": "label",
       "column_mapping": {1.0:29, 0.0:30}
    },
    "covid_fake_news":
     {
        "column_text": "tweet",
        "column_name":"label",
        "column_mapping":{'real':31,'fake':32}
     }
}


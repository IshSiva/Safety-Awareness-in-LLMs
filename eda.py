import pandas as pd
import nltk
nltk.download('punkt')
from nltk import sent_tokenize
from collections import Counter
from nltk.corpus import stopwords
from operator import itemgetter


nltk.download('stopwords')


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

index_class_mapping = {
    0: 1, 1: 0, 2: 1, 3: 0, 4: 1, 5:1, 6:1, 7:1, 8:1, 9:1, 10:1, 11:1, 12:1, 13:1, 14:1, 15:1, 16:1, 17:0, 18:0, 19:1, 20:1, 21:0, 22:1, 23:0, 24:0, 25:0, 26:0, 27:1, 28:0, 29:1, 30:0, 31:0, 32:1
}

domain_mapping = {
    "discrimination, exclusion, and toxicity" : ["adult_content","hate_speech","toxigen"],
    "misinformation harms" : ["mis_information","covid_fake_news"],
    "human-computer interaction harms": ["student_anxiety"],
    "malicious uses": ["bullying"]
}

domain_word_dict = {
    "discrimination, exclusion, and toxicity" : [],
    "misinformation harms" : [],
    "human-computer interaction harms": [],
    "malicious uses": []
}

domain_word_frequency = {
    "discrimination, exclusion, and toxicity" : [],
    "misinformation harms" : [],
    "human-computer interaction harms": [],
    "malicious uses": []
}

def count_sentences(text):
    try:
        sentences = sent_tokenize(text)
        return len(sentences)
    except:
        return 0

def count_words(text):
    try:
        sentences = sent_tokenize(text)
        word_count =sum([len(s.split()) for s in sentences])
        return word_count
    except:
        return 0

def transform_harmful(label,dataset):
    new_labels = []
    for l in label:
        try:
            new_labels.append(index_class_mapping[dataset_category_mapping[dataset]["column_mapping"][l]])
        except:
            new_labels.append(0)

    return new_labels

def get_words(key,text):
    words = nltk.word_tokenize(text)

    # Get NLTK English stop words
    stop_words = set(stopwords.words('english'))

    # Filter out stop words
    filtered_words =  [word for word in words if word.isalpha() and word.lower() not in stop_words]

    # Print the filtered words

    domain_word_frequency[key] = Counter(filtered_words)
    domain_word_dict[key] = list(set(filtered_words))
    

# for key in dataset_category_mapping.keys():
#     print(key)
#     df = pd.read_csv(key + ".csv")
#     class_distribution = df[dataset_category_mapping[key]["column_name"]].value_counts()
#     df['sentence_count'] = df[dataset_category_mapping[key]["column_text"]].apply(count_sentences)
#     df['word_count'] = df[dataset_category_mapping[key]["column_text"]].apply(count_words)
#     df['new_label'] = transform_harmful(df[dataset_category_mapping[key]["column_name"]],key)
#     print(df.shape)
#     #print(df.describe())
#     print(class_distribution)
#     # print("overall: ", df['word_count'].mean())
#     # print("overall: ", df['sentence_count'].mean())
#     # print("overall: ", df['word_count'].sum()/df['sentence_count'].sum())
#     # print("non harmful: ", df.loc[df['new_label'] == 0]['word_count'].mean())
#     # print("non harmful: ", df.loc[df['new_label'] == 0]['sentence_count'].mean())
#     # print("non harmful: ", df.loc[df['new_label'] == 0]['word_count'].sum()/df.loc[df['new_label'] == 0]['sentence_count'].sum())
#     # print("harmful: ", df.loc[df['new_label'] == 1]['word_count'].mean())
#     # print("harmful: ", df.loc[df['new_label'] == 1]['sentence_count'].mean())
#     # print("harmful: ", df.loc[df['new_label'] == 1]['word_count'].sum()/df.loc[df['new_label'] == 1]['sentence_count'].sum())

for key in domain_mapping.keys():
    domain_df = pd.DataFrame()
    for dataset in domain_mapping[key]:
        df = pd.DataFrame()
        data = pd.read_csv(dataset + ".csv")
        text = data[dataset_category_mapping[dataset]["column_text"]]
        label = transform_harmful(data[dataset_category_mapping[dataset]["column_name"]], dataset)
        df['text'] = text
        df['label'] = label
        domain_df = pd.concat([domain_df, df], axis=0)

    if key == "malicious uses":
        print(key)
        all_text = ""
        for t in domain_df.sample(n=10000).loc[domain_df['label'] == 1]["text"]:
            all_text = all_text + str(t)
        get_words(key,all_text)
        res = dict(sorted(domain_word_frequency[key].items(), key=itemgetter(1), reverse=True)[:20])
        print(res)
        all_text = ""
        for t in domain_df.sample(n=10000).loc[domain_df['label'] == 0]["text"]:
            all_text = all_text + str(t)
        get_words(key,all_text)
        res = dict(sorted(domain_word_frequency[key].items(), key=itemgetter(1), reverse=True)[:20])
        print(res)
    else:
        print(key)
        all_text = ""
        for t in domain_df.loc[domain_df['label'] == 1]["text"]:
            all_text = all_text + str(t)
        get_words(key,all_text)
        res = dict(sorted(domain_word_frequency[key].items(), key=itemgetter(1), reverse=True)[:20])
        print(res)
        all_text = ""
        for t in domain_df.loc[domain_df['label'] == 0]["text"]:
            all_text = all_text + str(t)
        get_words(key,all_text)
        res = dict(sorted(domain_word_frequency[key].items(), key=itemgetter(1), reverse=True)[:20])
        print(res)

    # class_distribution = domain_df['label'].value_counts()
    # domain_df['sentence_count'] = domain_df['text'].apply(count_sentences)
    # domain_df['word_count'] = domain_df['text'].apply(count_words)
    # print(domain_df.shape)
    # print(class_distribution)
    # print("overall: ", domain_df['word_count'].mean())
    # print("overall: ", domain_df['sentence_count'].mean())
    # print("overall: ", domain_df['word_count'].sum()/domain_df['sentence_count'].sum())
    # print("non harmful: ", domain_df.loc[domain_df['label'] == 0]['word_count'].mean())
    # print("non harmful: ", domain_df.loc[domain_df['label'] == 0]['sentence_count'].mean())
    # print("non harmful: ", domain_df.loc[domain_df['label'] == 0]['word_count'].sum()/domain_df.loc[domain_df['label'] == 0]['sentence_count'].sum())
    # print("harmful: ", domain_df.loc[domain_df['label'] == 1]['word_count'].mean())
    # print("harmful: ", domain_df.loc[domain_df['label'] == 1]['sentence_count'].mean())
    # print("harmful: ", domain_df.loc[domain_df['label'] == 1]['word_count'].sum()/domain_df.loc[domain_df['label'] == 1]['sentence_count'].sum())

for key in domain_mapping.keys():
    for key2 in domain_mapping.keys():
        res = dict(sorted(domain_word_frequency[key].items(), key=itemgetter(1), reverse=True)[:1000])
        res2 = dict(sorted(domain_word_frequency[key2].items(), key=itemgetter(1), reverse=True)[:1000])
        res = set(res.keys())
        res2 = set(res2.keys())
        inter = res.intersection(res2)
        print(key, key2, len(inter)/1000)



# overall_df = pd.DataFrame()
# for key in dataset_category_mapping.keys():
#     df = pd.DataFrame()
#     data = pd.read_csv(key + ".csv")
#     text = data[dataset_category_mapping[key]["column_text"]]
#     label = transform_harmful(data[dataset_category_mapping[key]["column_name"]], key)
#     df['text'] = text
#     df['label'] = label
#     overall_df = pd.concat([overall_df, df], axis=0)
# class_distribution = overall_df['label'].value_counts()
# overall_df['sentence_count'] = df['text'].apply(count_sentences)
# overall_df['word_count'] = overall_df['text'].apply(count_words)
# print(overall_df.shape)
# print(class_distribution)
# print("overall: ", overall_df['word_count'].mean())
# print("overall: ", overall_df['sentence_count'].mean())
# print("overall: ", overall_df['word_count'].sum()/overall_df['sentence_count'].sum())
# print("non harmful: ", overall_df.loc[overall_df['label'] == 0]['word_count'].mean())
# print("non harmful: ", overall_df.loc[overall_df['label'] == 0]['sentence_count'].mean())
# print("non harmful: ", overall_df.loc[overall_df['label'] == 0]['word_count'].sum()/overall_df.loc[overall_df['label'] == 0]['sentence_count'].sum())
# print("harmful: ", overall_df.loc[overall_df['label'] == 1]['word_count'].mean())
# print("harmful: ", overall_df.loc[overall_df['label'] == 1]['sentence_count'].mean())
# print("harmful: ", overall_df.loc[overall_df['label'] == 1]['word_count'].sum()/overall_df.loc[overall_df['label'] == 1]['sentence_count'].sum())




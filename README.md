# Assessing the Safety Awareness in Large Language Models

### Sai Prasath Suresh, Ishwarya Sivakumar, Shubham Maheshwari

## Abstract

In recent years Large Language Models (LLMs) have shown exceptional performance in many Natural Language Processing (NLP)
tasks and across domains. However, concerns remain regarding their confidence in generating potentially inaccurate information, raising ethical questions. This paper investigates the ability of LLMs
to recognize tasks with potentially harmful consequences to humans.
We compare the LLM’s activations across different layers
for safe and unsafe prompts and train a binary classifier to predict
prompt’s safety based on these activations. The model’s performance
is evaluated on four different domains of potential risks
which include misinformation harms, discrimination, exclusion
and toxicity, Human Computer Interaction (HCI) Harms and use in
malicious activities. 

We show that:
- **Llama2 embeddings capture the
notion of safety, achieving an overall accuracy of 68%, and outperforming
BERT model by 8%.**
- **We also show that the optimal layer
for generating the embeddings, and the quality of the embeddings
vary significantly across domains.**

Thus this research represents a
critical step toward building AI systems that are more aware of their
actions and capable of making ethical decisions in real-world scenarios,
ultimately fostering the development of more trustworthy
and responsible AI technologies.


## Introduction

In this era of artificial intelligence, LLMs have become instrumental
in several applications, revolutionizing the way we interact with
and harness the power of machine-generated text. However, these
technological advancements have raised concerns regarding the
ability of these models to perform tasks that might be harmful to
humans. LLMs might assist in activities like generation of fake
news, cyberbullying, providing guidance for illicit activities like
making a bomb, hacking a website etc. Malicious actors can exploit
these capabilities to harm humans at scale. Therefore, it is essential
to identify these "harmful" capabilites and limit or mitigate the involvement
of LLMs in these activities to avoid the potential harms
to humans.


Recently, techniques such as NeMo Guardrails [13], reinforcement
learning from human feedback (RLHF) [9], and prompting [18]
have helped develop safer LLMs. Similar techniques have been implemented
for the latest LLMs like GPT-4 (OpenAI), BARD (Google)
and Llama (Meta) which can prevent the LLM from assisting in
explicitly dangerous activities. However, these techniques are not
robust as they can be bypassed using carefully crafted prompts [19],
and aren’t generalizable as they are customized for a particular domain/scenario/LLM. Moreover, many of these techniques haven’t
been open-sourced and hence others cannot benefit from them.


In this research project, instead of exploring input-prompt filtering
or output analysis based approaches we focus on studying
the safety awareness of the LLMs using their internal activations.
As humans are adept as discerning safety, and LLMs are trained on
large amounts of human-generated data scraped from the internet,
we hypothesize that LLMs are adept at discerning safety as well.
Therefore, LLMs should exhibit distinguishable patterns in their
internal activations corresponding to safe and unsafe content. By
using these activations as the input to a safety classifier, we evaluate
the safety awareness of LLMs.

To the best of our knowledge, this is the first work that evaluates
the safety awareness of LLMs by analyzing their internal
activations. We evaluate the model’s performance on four different
domains to ensure that our proposed approach is domain-agnostic,
and therefore captures a general notion of safety. The proposed
safety classifier can be used as a filtering mechanism capable of
averting the involvement of LLMs in potentially harmful actions.
In summary, this project takes a critial step towards building safety
aware LLMs, thereby fostering the development of more trustworthy
and responsible AI technologies.

## Proposed Methodology

In this project, we extend the SAPLMA [8] framework to assess the safety awareness of LLMs by
analyzing their layer activations. Based on our hypothesis that
there must exist discernible differences in the activations between
safe and unsafe context. Hence we train a binary safety classifier
to capture these differences.

To ensure that the safety classifier captures a general notion of
safety and not the syntactic or semantic patterns, we perform the
hold-out-domain analysis. In this technique, the safety classifier is
trained using data from three out of the four domains, and tested on
the fourth domain. This process is carried out four times, with each
domain being used as the test domain in one of the iterations. The
classifier’s performance serves as a metric to quantify the safety
awareness of the LLMs.

<img width="845" alt="image" src="https://github.com/IshSiva/Safety-Awareness-in-LLMs/assets/34617363/0f9e450e-b37d-4d9c-8adf-03ae018edbe2">

                                End-to-End framework for evaluating safety awareness

We use the "bert-base-uncased" BERT model as the baseline
and select the "Llama2-7B-chat" model from HuggingFace for performing
our analysis. Each datapoint is first appended with a system prompt "You are a
chatbot trying to avoid potential harmful outputs. Determine whether
you will answer the following question. Answer only with only one
word: YES or NO". The resultant text-prompt is tokenized using
BERTTokenizer for the BERT model and LlamaTokenizer for the Llama2 model.

For BERT model we collected the pooled output activations as
the model embeddings. However, the optimal layer for extracting
the activations for the Llama2 model is unclear. While the lower
layers focus on understanding the input text, and the later layers
focus on predicting the next token, middle layers are expected to
store and retrieve relevant information. Therefore, we collect the
activations across multiple layers: 1, 4, 8, 12, 16, 20, 24 and 28 for
Llama2. The embeddings of the BERT model have a dimension of
768 and that of Llama2 is 4096.

These embeddings are fed as input to a single neuron Logistic
Regression model that uses Sigmoid activation function. The model
is trained using Binary Cross Entropy loss and AdamW optimizer
with a learning rate of 5e-4. We report the Accuracy, Precision,
Recall, F1-Score and AUC-ROC score for all the models. We use
the hold out domain analysis for performing the experiments.


## Experiments and Results

**RQ1. Which layers generate better representation of safety?**

<img width="845" alt="image" src="https://github.com/IshSiva/Safety-Awareness-in-LLMs/assets/34617363/aea6cbbe-03de-4e38-a2f4-81dc0cac443e">

We use the silhouette score to compare the quality of the generated
embeddings. Silhouette score measures how similar an embedding
is to its own class compared to the other classes. For this analysis,
we compute the silhouette score between the embeddings of safe
and unsafe class for each domain and for the embeddings of each
layer. From figure 2 we can observe that Llama2 model has a better
representation of safety than BERT model. While 3 out of the
4 domains achieve the best representation in later layers (28 for
Discrimination, Exclusion, Toxicity and Malicious Uses; 24 for HCI
Harms), some domains like Misinformation achieve the best representation
in earlier layers (Layer 1). Moreover, the quality of the
representation varies significantly based on the domain. Domains
like Discrimination, Exclusion, Toxicity have good representation
of safety while other domains like Malicious Uses has poor representation

**RQ2. Does Llama2 have better safety awareness than BERT?**

<p align="center">
<img width="600" alt="Screenshot 2024-01-17 at 1 13 23 PM" src="https://github.com/IshSiva/Safety-Awareness-in-LLMs/assets/34617363/c50908a8-1caf-4df1-b0d0-535c60ee84f6">
</p>

For evaluating the safety awareness of Llama2 and BERT models
we analyze the overall performance of these models across all
domains. Table 2 summarizes the performance of BERT and the
layer-wise performance of Llama2 model. We can observe that
across all metrics (except recall) Llama2 - Layer 16 outperforms
BERT model. Llama2 model improves the accuracy by 8.4%, precision
by 13.1%, F1-Score by 4.1% and ROC-AUC by 9.2%. Therefore,
we conclude that Llama2 model has better safety awareness than BERT.

<p align="center">
<img width="600" alt="Screenshot 2024-01-17 at 1 13 23 PM" src="https://github.com/IshSiva/Safety-Awareness-in-LLMs/assets/34617363/916b488f-70ac-4ef7-a8b3-663a9a3746e7">
</p>


Further when analyzing the domain-wise performance, we observe
that Llama2 model outperforms BERT in 3 out of the 4 domains.
From figure 3, the Llama2 model achieves accuracy as high
as 83.3% in the Discrimination, Exclusion, Toxicity domain outperforming
BERT by 23.4%, and accuracies around 65.5% in the
HCI harms and Misinformation domains outperforming BERT by
around 5%. However, on the Malicious uses domain the Llama2
model performs poorly, achieving an accuracy around 55% only
and underperforming BERT by around 5%.

There are 2 factors that affect the overall performance of the
model, (1) the quality of (representation of safety) embeddings, and
(2) the decision boundary (DB) transferability across domains. For
analyzing the impact of each factor, we perform an ablation study.

**RQ3. How is the performance affected due to quality of embeddings?**


<p align="center">
<img width="800" alt="Screenshot 2024-01-17 at 1 13 23 PM" src="https://github.com/IshSiva/Safety-Awareness-in-LLMs/assets/34617363/864d247f-cdcb-4420-b62a-aae8cf2124ab">
</p>

For capturing the effect of embeddings and removing the effect
of the DB transferability, we train an in-domain classifier for each
domain. For eliminating the effects of DB transfer, we assume that
the hold-out-domain safety classifier perfectly captures the DB
of the in-domain classifier. Comparing the performance of the indomain
safety classifier in Table 3, we find that Llama2 outperforms
BERT by 8.2% in terms of accuracy on average, and as high as 12.3%
in some domains. Hence, we conclude that Llama2 embeddings are
more safety aware than BERT embeddings.

**RQ4. How is the performance affected due to decision boundary
transfer?**

<p align="center">
<img width="900" alt="Screenshot 2024-01-17 at 1 13 23 PM" src="https://github.com/IshSiva/Safety-Awareness-in-LLMs/assets/34617363/6772fefd-0cb4-426a-9572-b8a3bd63c90c">
</p>

In this research question, we analyze whether the DB learnt on out
of domain data transfers to in domain data. During the hold-outdomain
analysis, we train the safety classifier on three out of the
four domains, and test it on the fourth domain. For eliminating the
effect of the quality of embeddings and only studying the effect of
DB transferability, we compare the performance of the hold-outdomain
safety classifier with the in-domain safety classifier.
From Table 4 we can observe that for BERT model the performance
drop due to DB transfer is 25.6% on average. However, for
the Llama2 model the performance drop is only drop 23.7% which
is a 1.9% lesser performance drop than BERT. As BERT does not
generate good quality embeddings for the Malicious Uses domain
as captured by its poor performance of lesser than 80% overall (indomain)
accuracy, we do not consider this domain for BERT while
computing the performance drop due to DB transferability. Hence,
we can conclude that Llama2 model has better DB transferability
than BERT and therefore it captures the general notion of safety
better than BERT.

**RQ5. [Explainability] Are there specific activations that capture
safety awareness across domains?**


<p align="center">
<img width="400" alt="Screenshot 2024-01-17 at 1 13 23 PM" src="https://github.com/IshSiva/Safety-Awareness-in-LLMs/assets/34617363/28f25cf9-39dd-4c59-a565-bc424a0958a7">
</p>

For studying whether there are specific activations that capture
safety, we analyze the top-k% of activations across all domains for
each layer. For a given layer, we select the top-k% of activations
by magnitude for each domain and filter the activations common
across all the domains. From figure 4 we find that for top-1% and
top-5%, there are no activations that are common across all the
domains. Even for top-20% there are only 38 activations (out of 819
possible activations) that are common across domains. Hence, we conclude that there aren’t significant overlap of activations across
domains.

## Conclusion

In this project we show that decoder-based Llama2 models are more
safety aware than encoder based BERT models. We demonstrate
that Llama2 models outperform BERT in terms of the (1) quality of
the generated embeddings, and (2) the decision boundary transferability
across domains. While Llama2 model outperforms BERT on
average, the results vary significantly across domains and across
layers. Further, we find that the optimal layers for generating the
embeddings are domain dependent. While generating embeddings
from later layers works best in most cases, earlier layer can be better
for few domains. Moreover, the quality of the generated embeddings
can vary significantly across domains. Overall, the Llama2
embedding based safety classifier achieves a modest accuracy of
68%, and therefore can be used as the first layer of filtering in LLMs.
The proposed Llama2 embedding based safety classifier achieves
recall scores identical to BERT. Studying whether Llama2 and BERT
models correctly identify the same datapoints, or whether BERT
and Llama2 embeddings can be used together to create a better
classifier can be explored. Also, whether multiple layer embeddings
can be pooled or combined for improving the performance of the
model should be analyzed. Further, studying the performance of
the model, and especially the DB transferability on more diverse
datasets is required. Finally, more complex classifier models can be
considered for improving the overall performance of the model. In
this project, we use a logistic regression model, this can be replaced
with a neural network with hidden layers for better performance.

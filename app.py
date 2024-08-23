import streamlit as st
import transformers
import wikipedia
import torch
from transformers import pipeline, Pipeline

def load_qa_pipeline() -> Pipeline:
    qa_pipeline = pipeline("question-answering", model="distilbert-base-uncased-distilled-squad")
    return qa_pipeline

def load_wiki_summary(query: str) -> str:
    results = wikipedia.search(query)
    summary = wikipedia.summary(results[0], sentences=10)
    return summary


def answer_question(pipeline: Pipeline, question: str, paragraph: str) -> dict:
    input = {
        "question": question,
        "context": paragraph
    }
    output = pipeline(input)
    return output


# Main app engine
if __name__ == "__main__":
    #display title and description
    st.title("Wikipedia Question Answering")
    st.write("Search topic, Ask questions, Get Answers")

    #display topic input slot
    topic = st.text_input("SEARCH TOPIC", "")

    #display article paragraph
    article_paragraph = st.empty()

    #display question input slot
    question = st.text_input("QUESTION", "")

    if topic:
        #load wikipedia summary of topic
        summary = load_wiki_summary(topic)

        #display article summary in paragraph
        article_paragraph.markdown(summary)

        #peform question answering
        if question != "":
            #load question answering pipeline
            qa_pipeline = load_qa_pipeline()

            #answer query question using article summary
            result = answer_question(qa_pipeline, question, summary)
            answer = result["answer"]

            #display answer
            st.write(answer)







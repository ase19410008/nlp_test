import spacy
import streamlit as st
from spacy_streamlit import visualize_parser, process_text

nlp = spacy.load("ja_ginza")
doc1 = nlp("ある男がバーに入ってきて、バーテンダーに水を一杯注文した。バーテンダーは銃を取り出し、男に狙いをつけて撃鉄を上げた。男は「ありがとう」と言って帰って行った。一体どういうことか？")
visualize_parser(doc1)

text = st.text_area("質問", height=200)
doc2 = nlp(text)
visualize_parser(doc2, key="q")
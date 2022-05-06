from distutils import text_file
import streamlit as st
from transformers import T5ForConditionalGeneration, T5Tokenizer
from datasets import load_dataset
import random
def text(tokenizer,model,input):
    model.eval()
    input = "translate English to German: " + input
    input_ids = tokenizer.encode(input, return_tensors="pt")
    output_ids = model.generate(
                input_ids,
                max_length=128,
                num_beams=5,
                do_sample=False,
            )
    output = tokenizer.decode(output_ids[0],skip_special_tokens=True)
    return output


a = st.text_input('input', '')
tokenizer = T5Tokenizer.from_pretrained("t5-base")
model = T5ForConditionalGeneration.from_pretrained("../output_dir")

output = text(tokenizer,model,input = a)
st.write("Input: ")
st.write(a)
st.write("Translate: ")
st.write(output)

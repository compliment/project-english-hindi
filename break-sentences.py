import csv
import re

def split_sentences(text):
    # return re.split(r'(?<=[.!?]) +', text)
    return re.split(r'((?<=[.?!।]))\s+', text)

def convert_to_csv(english_file, hindi_file, output_file):
    with open(english_file, 'r', encoding='utf-8') as ef, open(hindi_file, 'r', encoding='utf-8') as hf:
        english_text = ef.read()
        hindi_text = hf.read()

    english_sentences = split_sentences(english_text)
    hindi_sentences = split_sentences(hindi_text)

    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        for eng, hin in zip(english_sentences, hindi_sentences):
            writer.writerow([eng.strip(), hin.strip()])


convert_to_csv('eng.txt', 'hin.txt', 'essays.csv')

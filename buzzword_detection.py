import spacy

nlp_en = spacy.load('en_core_web_sm')
nlp_de = spacy.load('de_core_news_sm')

def check_buzzwords_ner(tweet, buzzwords, lang='en'):
    doc = nlp_de(tweet) if lang == 'de' else nlp_en(tweet)
    found_buzzwords = [entity.text for entity in doc.ents if entity.label_ in buzzwords]
    return found_buzzwords
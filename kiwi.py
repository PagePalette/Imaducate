from kiwipiepy import Kiwi
from keybert import KeyBERT

import gpt

kiwi = Kiwi()
bert = KeyBERT('bert-base-multilingual-cased')


DELIMITER = "."


def parse_nouns(text: str) -> list[str]:
    r = ' '.join([token.form for token in kiwi.analyze(text)[0][0] if token.tag[0] == "N"])
    return [t for t, v in bert.extract_keywords(r, top_n=10)]


def get_prompt(text: str) -> str:
    return gpt.translate(' '.join(parse_nouns(text)))

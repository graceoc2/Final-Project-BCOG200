import pytest
from src.create_a_poem import *

def test_tagged_tokens():
	sample_text = "apple want I bread and jam"
	tagged_tokens = get_tagged_tokens(sample_text)
	print(tagged_tokens)
	print(sample_text.split(" "))
	assert len(tagged_tokens) == len(sample_text.split(" ")) #same number of tagged tokens and og text

def test_poem_tokens():
	poem_structure=[
		"The moon in the bureau mirror", 
		"looks out a million miles", 
		"(and perhaps with pride, at herself,", 
		"but she never, never smiles)",
		"" 
	]

	poem_tokens = get_poem_tokens(poem_structure)

	for line_tokens in poem_tokens:             
	        for token in line_tokens:
	            assert isinstance(token, tuple)
	            assert len(token) == 2  #checks if tuple has 2 things in it

def test_replace_words_with_random_words():
	tagged_tokens= [("apple", "NOUN"), ("want", "VERB"), ("I", "PRON"), ("bread", "NOUN"), ("and", "CONJ"), ("jam", "NOUN")]
	poem_structure=["The moon in the bureau mirror", 
	]

	poem_tokens = get_poem_tokens(poem_structure)
	new_poem = replace_words_with_random_words(tagged_tokens, poem_tokens,poem_structure)

	assert len(new_poem.split("\n")) == len(poem_structure) #same amount of lines as og poem or no?




if __name__ == "__main__":
    pytest.main()
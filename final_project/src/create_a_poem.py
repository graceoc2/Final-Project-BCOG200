import spacy
import random

nlp = spacy.load("en_core_web_sm")

def get_tagged_tokens(text): #this creates tuples of word,pos of every word in the cleaned text 
    nlp = spacy.load("en_core_web_sm")
    tagged_tokens = [(token.text, token.pos_) for token in nlp(text)]
    return tagged_tokens

def get_poem_tokens(poem_structure): #this creates tuples of word,pos for every word in the poem structure below in main Poem(One Art)
    poem_tokens = []
    for line in poem_structure:
        tokens = nlp(line)
        poem_tokens.append([(token.text, token.pos_) for token in tokens if not token.text.isspace()])

    return poem_tokens


def replace_words_with_random_words(tagged_tokens, poem_tokens,poem_structure):
    new_poem=''

    new_poem_lines = []
    poem_map = {}

    tagged_tokens_lower=[(word.lower(), pos) for word, pos in tagged_tokens] #lowercase the words in the tagged_tokens


    # this is a dictionary for replaceing based on POS 
    pos_dict = {}
    for word, pos in tagged_tokens_lower:#lowercase them 
        if pos in pos_dict:
            pos_dict[pos].append(word)
        else:
            pos_dict[pos] = [word]

    
    for line_tokens in poem_tokens:
        line_words = []
  
        for word, pos in line_tokens:
            if word in poem_map:
                replacement = poem_map[word] #if already been replaced in poem this makes it use the same word replacment
            else:
                replacements = pos_dict.get(pos, []) #these lines do the replacement 
                if replacements:
                    replacement = random.choice(replacements)
                    poem_map[word] = replacement  #replaces with new word with same POS
                else:
                    replacement = word  # if no replacements are found this uses the original word
            
            line_words.append(replacement)
        new_poem_lines.append(' '.join(line_words))

        
         # this code makes sure the new words in each line match the original number of words
    max_words = max(len(line.split()) for line in poem_structure) 
    for i, line in enumerate(new_poem_lines):
        diff = max_words - len(line)
        if diff > 0:
            additional_words = [random.choice(pos_dict[pos]) for pos in pos_dict.keys()]
            line_words_list = line.split() 
            line_words_list.extend(additional_words[:diff])
            new_poem_lines[i] = ' '.join(line_words_list)

    new_poem = '\n'.join(new_poem_lines)
    return new_poem


def main():
    poem_structure = [
        "The art of losing is not hard to master",
        "so many things seem filled with the intent",
        "to be lost that their loss is no disaster",

        "Lose something every day Accept the fluster",
        "of lost door keys the hour badly spent", 
        "The art of losing is not hard to master",

        "Then practice losing farther losing faster",
        "places and names and where it was you meant",
        "to travel None of these will bring disaster",
    
        "I lost my mothers watch And look my last or",
        "next to last of three loved houses went",
        "The art of losing is not hard to master",
    
        "I lost two cities lovely ones And vaster",
        "some realms I owned two rivers a continent",
        "I miss them but it wasnt a disaster",

        "Even losing you the joking voice a gesture",
        "I love I shant have lied Its evident",
        "the art of losings not too hard to master",
        "though it may look like Write it like disaster"
    ]

    cleaned_text_file_path = "/Users/gracecook/Desktop/final_project/texts/elizabeth_bishop_cleaned.txt"
    with open(cleaned_text_file_path, 'r') as file:
        text = file.read()


    tagged_tokens = get_tagged_tokens(text)
    poem_tokens=get_poem_tokens(poem_structure)


    new_poem = replace_words_with_random_words(tagged_tokens,poem_tokens,poem_structure)
    new_poem_lines = [line.capitalize().replace('-', '').replace(" n't", "").replace("'s", "").replace(" i ", " I ").replace("'", "") for line in new_poem.split("\n")] #capitalizes first word of each line and replaces hyphens, and non words, also i to I
    new_poem_capitalized = "\n".join(new_poem_lines)


    # Print the new poem!
    print("NEW POEM :")
    print(new_poem_capitalized)

if __name__ == "__main__":
    main()

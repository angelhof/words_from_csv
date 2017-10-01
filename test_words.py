import sys
import os.path
import random

known_words_file = "known_words"
known_threshold = 3
first_lang =  "Greek  "
second_lang = "English"

def main():

    if not len(sys.argv) == 2:
        print("Wrong number of arguments")
        print("Expected usage: test_words words.csv")
        exit(1)
        
    word_data = read_words_file(sys.argv[1])
    known_words = read_known_words_file(known_words_file)
    backup_known_words_file(known_words)
    known_words_dic = prepare_known_words_dic(known_words)
    unknown_word_data = [x for x in word_data if not is_known(x[0], known_words_dic)]
    # print(unknown_word_data)
    
    while len(unknown_word_data):
        word_index = random.randrange(len(unknown_word_data))
        word = unknown_word_data[word_index]
        
        is_it_known = test_word(word)

        if is_it_known:
            ## If the word is known update the known words dictionary
            knowledge_counter, known_words_dic = update_known_dic(word[0], known_words_dic)
            persist_new_known_dic(known_words_dic)
            print("Congratulations: You have found the meaning of %s correctly %d times"
                  % (word[0], knowledge_counter))
            if knowledge_counter >= known_threshold:
                ## If the word's meaning has been found more times than the threshold
                ## delete it from the unknown words data
                del unknown_word_data[word_index]



def test_word(word):
    print("Do you know: %s" % (word[0]))
    sys.stdin.readline()
    print("  -- %s Meaning: %s" % (first_lang, word[1]))
    print("  -- %s Meaning: %s" % (second_lang, word[2]))
    answer = sys.stdin.readline()
    if len(answer) == 0:
        exit(0)
        if answer[0] == 'q':
            exit(0)
    if answer[0] == 'y' or answer[0] == '1':
        return True
    else:
        return False

def read_words_file(words_file):
    with open(words_file) as f: 
        word_data = f.read().split("\n")[2:]
        clean_word_data = [x.split("|")[:-1] for x in word_data
                       if not x == "|||" and not x == ""]
        return clean_word_data

def read_known_words_file(known_words_file):
    create_file_if_doesnt_exist(known_words_file)
    with open(known_words_file) as f:
        word_data = [x.split("|") for x in f.read().split("\n") if not x == '']
        return word_data

def backup_known_words_file(known_words):
    with open("."+known_words_file+"_backup", "w") as f:
        lines = [key+"|"+value for key, value in known_words]
        output = "\n".join(lines) + "\n"
        f.write(output)
        

    
def create_file_if_doesnt_exist(known_words_file):
    if not os.path.isfile(known_words_file):
        f = open(known_words_file, "w")
        f.close()

def prepare_known_words_dic(known_words):
    return {x[0] : int(x[1]) for x in known_words}

def is_known(word, known):
    if word in known:
        if known[word] >= known_threshold:
            return True
    return False
        
def update_known_dic(word, known_words):
    if word in known_words:
        val = known_words[word] + 1
    else:
        val = 1
        
    known_words[word] = val
    return val, known_words 

## Completely slow and shitty but who cares
def persist_new_known_dic(known_words):
    with open(known_words_file, "w") as f:
        lines = [key+"|"+str(value) for key, value in known_words.items()]
        output = "\n".join(lines) + "\n"
        f.write(output)

main()

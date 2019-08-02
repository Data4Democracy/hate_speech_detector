import wikipediaapi
import re



def process_word(word):
    # remove tags
    remove_list = ['<i>', '</i>', '<b>', '</b>', '\xa0', '"']
    for r in remove_list:
        word = word.replace(r, '')
    # Remove span
    if 'span' in word:
        word = re.findall(r'>(.*?)<', word)[0]
    # Remove words in parentheses
    if '(' in word and ')' in word:
        word = word[:word.index('(')] + word[word.index(')')+1:]
    if '(' in word:
        word = word[:word.index('(')]
    # Replace differet delimiters to comma
    replace_list = ['/', ' or ', ' also spelled ']
    for r in replace_list:
        word = word.replace(r, ',')
    # Remove non-latin characters
    stripped_text = ''
    for c in word:
        stripped_text += c if len(c.encode(encoding='utf_8'))==1 else ''
    word = stripped_text
    return(word)


def process_extract(page_text):
    extract = re.findall(r'<dt>(.*?)</dt>', page_text)
    for word in extract:
        ind = extract.index(word)
        extract[ind] = process_word(word)

    bad_words = []
    for word in extract:
        bad_words.extend(word.split(','))
    #ethnic_words = [x.strip() for x in ethnic_words]
        
    bad_words[:] = [x for x in bad_words if x != '']      
    bad_words[:] = [x.strip().lower() for x in bad_words]  
    return(bad_words)





wiki_html = wikipediaapi.Wikipedia(
        language='en',
        extract_format=wikipediaapi.ExtractFormat.HTML
)

page_ethnic = wiki_html.page("List_of_ethnic_slurs")
page_religous = wiki_html.page("List_of_religious_slurs")


ethnic_bad_words = process_extract(page_ethnic.text)
religious_bad_words = process_extract(page_religous.text)







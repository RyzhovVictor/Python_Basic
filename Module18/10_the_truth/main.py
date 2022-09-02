text = 'vujgvmCfb tj ufscfu ouib z/vhm jdjuFyqm jt fscfuu uibo jdju/jnqm fTjnqm tj scfuuf ibou fy/dpnqm yDpnqmf jt cfuufs boui dbufe/dpnqmj uGmb tj fuufsc ouib oftufe/ bstfTq jt uufscf uibo otf/ef uzSfbebcjmj vout/dp djbmTqf dbtft (ubsfo djbmtqf hifopv up csfbl ifu t/svmf ipvhiBmu zqsbdujdbmju fbutc uz/qvsj Fsspst tipvme wfsof qbtt foumz/tjm omfttV mjdjumzfyq odfe/tjmf Jo fui dfgb pg hvjuz-bncj gvtfsf fui ubujpoufnq up ftt/hv Uifsf vmetip fc pof.. boe sbcmzqsfgf zpom pof pvt..pcwj xbz pu pe ju/ Bmuipvhi uibu bzx bzn puo cf wjpvtpc bu jstug ttvomf sfzpv( i/Evud xOp tj scfuuf ibou /ofwfs uipvhiBm fsofw jt fopgu cfuufs boui iu++sjh x/op gJ ifu nfoubujpojnqmf tj eibs pu mbjo-fyq tju( b bec /jefb Jg fui foubujpojnqmfn jt fbtz up bjo-fyqm ju znb cf b hppe jefb/ bnftqbdftO bsf pof ipoljoh sfbuh efbj .. fu(tm pe psfn gp tf"uip'

# alphabet_en_upper = ''.join([chr(i) for i in range(ord('A'), ord('Z') + 1)])
# alphabet_en_lower = ''.join([chr(i) for i in range(ord('a'), ord('z') + 1)])
# ALPHABET_EN = alphabet_en_upper + alphabet_en_lower

ALPHABET_EN = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'


def encrypted(msg, key):
    new_str_1 = ''
    new_str_2 = ''
    for sym in msg:
        if sym in ALPHABET_EN:
            num = ALPHABET_EN.find(sym)
            new_str_1 += ALPHABET_EN[num - key]
        else:
            new_str_1 += sym
    replace_index = 3
    for word in new_str_1.split(' '):
        new_word = ''
        # print(new_word)
        for index in range(len(word)):
            new_word += (word[index - replace_index % len(word)])
            # print(new_word)
        if new_word.endswith('/'):
            replace_index += 1
        new_str_2 += new_word + ' '
    new_str_2 = new_str_2.replace('/', '\n')
    return new_str_2


output_str = encrypted(text, 1)

print(output_str)

alphabet = 'abcdefghijklmnopqrstuvwxyz'
word = input('enter a word you want to ').lower()
shift = int(input('how much you want to shift\t'))

def encryption(word,shift):
    result = ''
    n = 0 
    while n < len(word):
        for i in range(0,len(alphabet)):
            if word[n] == alphabet[i]:
                result = result + alphabet[i + shift]

        n = n + 1 

    print('the encryption key will be ' , result)
encryption(word,shift)

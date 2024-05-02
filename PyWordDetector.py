import os

while True:

    with open('keywords.txt', 'r', encoding='utf-8') as keywords:
        keywords = keywords.read().lower().split(",")

    txtContents = input('Provide path to file or paste text: ')
    if os.path.exists(txtContents):
        with open(txtContents, 'r', encoding='utf-8') as txtContents:
            txtContents = " " + txtContents.read().replace('\n', ' ').lower()
            result = [i for i in keywords if(i in txtContents)]
            print('Does the text contain words from the keywords list: ' + str(bool(result)))
            continue
    else:
            txtContents = " " + txtContents.lower()
            result = [i for i in keywords if(i in txtContents)]
            print('Does the text contain words from the keywords list: ' + str(bool(result)))
            continue
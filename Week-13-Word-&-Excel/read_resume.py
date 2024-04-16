"""
program that reads through a word document. (resume)
program can go through all the text in the doc and flag for one specific word
"""

import docx

document = docx.Document('IT_Sample_resume.docx')

for para in document.paragraphs:
    if 'ethical hacking' in para.text.lower():  # prints this if it finds that word in the resume.
        print('An ethical hacker!!')
    # print(para.text)  # shows all the text in document

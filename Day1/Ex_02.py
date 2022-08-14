txt = open('textfile.txt', 'r').read()
txt_new= open('new_textfile.txt', 'w')
txt_titled = txt.title()
txt_new.write(txt_titled)
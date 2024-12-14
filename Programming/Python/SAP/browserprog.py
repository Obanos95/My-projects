import webbrowser
import os

a = input('What do you want to do? ')
if a == 'w':
    webbrowser.open('https://moodle.unistra.fr/login/index.php')
    webbrowser.open('https://chatgpt.com/')
    webbrowser.open('https://www.w3schools.com/python/default.asp')
    os.system('gnome-terminal')
elif a == 's':
    search = input('What do you want to search? ')
    try:
        search = search.split()
        search = '+'.join(search)
    except:
        pass
    link = 'https://www.google.com/search?q='+search+'&client=firefox-b-lm&sca_esv=640dfa46d8859720&sxsrf=ADLYWILHdWGXlxMf4ZOfVFXH3Yhi7iivfg%3A1729854759762&ei=J30bZ--ELpWli-gPjoGZ2AY&ved=0ahUKEwivtN-Ts6mJAxWV0gIHHY5ABmsQ4dUDCA8&uact=5&oq=Hello&gs_lp=Egxnd3Mtd2l6LXNlcnAiBUhlbGxvMgoQIxiABBgnGIoFMgoQABiABBhDGIoFMgoQLhiABBhDGIoFMggQABiABBjLATILEC4YgAQYsQMYgwEyERAuGIAEGLEDGIMBGMcBGK8BMggQLhiABBjLATIIEC4YgAQYsQMyChAAGIAEGBQYhwIyCBAAGIAEGMsBSI8MUMwBWPIHcAF4AZABAJgBnAGgAbwGqgEDMC42uAEDyAEA-AEBmAIDoALxAsICChAAGLADGNYEGEfCAg0QABiABBiwAxhDGIoFwgIPEAAYgAQYsAMYQxiKBRgKwgIOEAAYsAMY5AIY1gTYAQHCAhMQLhiABBiwAxhDGMgDGIoF2AEBmAMAiAYBkAYRugYGCAEQARgJkgcDMS4yoAf1SA&sclient=gws-wiz-serp'
    webbrowser.open(link)

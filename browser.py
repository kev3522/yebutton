from flask import Flask, render_template, flash, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
 
from main import main


# App config.
# DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'
 
class ReusableForm(Form):
    name = TextField('$:')
 
msg_list = []


def remove_curse(word,curse):
    censored = ''
    num = 0
    while num < len(word):
        if word[num] == curse[0]:
            censored += curse[0] 
            censored += (len(curse) - 2) * '*' 
            censored += curse[len(curse) - 1]
            num += len(curse)
        elif word[num] == curse[0].upper():
            censored += curse[0].upper()
            censored += (len(curse) - 2) * ''
            censored += curse[len(curse) - 1]
            num += len(curse)
        else:
            censored += word[num]
            num += 1
    return censored

curse_words = ['pussies', 'pussy', 'tits','bitch','fuck','nigga','nigger','dick','asshole','douchebags','shit', 'ass', 'bastard']



def no_curse_words(string):
    """
    Censors curse words -- fuck = f**

    Inputs:
    str - string with curse words in them

    Returns:
    String with censored curse words'
    """
    text = string.split()
    copy = list(text)
    for num in range(len(text)):
        lower = text[num].lower()
        for curse in curse_words:
            if curse in lower:
                copy[num] = remove_curse(copy[num],curse)
        # elif lower in curse_words or lower[:len(lower) - 1] in curse_words:
        #     copy[num] = copy[num][0] + (len(copy[num]) - 2) * '*' + copy[num][len(copy[num]) - 1]
    censored = ' '.join(copy)
    return censored



@app.route("/", methods=['GET', 'POST'])
def hello():
    form = ReusableForm(request.form)
 
    # print form.errors
    if request.method == 'POST':
        name = request.form['name']
        # print name
        
        output = main(name)

        msg_list.insert(0,"Ye: " + no_curse_words(output[0]) + " (" + output[1] + ")" )

        msg_list.insert(0,"You: " + no_curse_words(name))
        
    return render_template('index.html', form=form, messages = msg_list)
 
if __name__ == "__main__":
    app.run()
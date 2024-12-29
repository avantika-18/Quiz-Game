import re
# Functionality Related: This function takes the file name as input, \
# reads each question into a list and returns the list


def get_the_sentences(in_file: str) -> list:
    result = []
    with open(in_file) as f:
        for r in re.findall('QUESTION(.*?)END', f.read(), re.S):
            result.append(r)
    return result


# Functionality Related: This function takes the lines, start position and end position as input, \
# and returns the list of lines between start and end


def get_the_question(lines, start, end):
    #for r in re.findall('(.*?)', lines, re.S):
    options=str.split(lines, '\n')
    return options[start:end]


# Functionality Related: This function takes the line number as input, \
# splits the line by the delimiter "." and returns the 1st part (the qno)

def get_question_no(line):
    qsplit = line.split('.')
    qno = qsplit[0].strip()
    return qno


# Functionality Related: This function takes the subject name and qno as input, \
# reads each line and returns the right side of delimiter if the qno matches

def get_the_answer(subject, qno_in):
    f = open(subject + "_answers.txt", "r")
    print("f is", f)
    lines = f.readlines()
    count = 0
    for l in lines:
        qlist = l.split('.')
        qno=get_question_no(l)
        if qno== qno_in:
            Answer=qlist[1].strip()
    return Answer


# Functionality Related: This function takes the quiz score as input, \
# and returns the text to be displayed based on the score

def quiztext(score):
    if score >= 4:
        quiztext1="your score is "+str(score)+" out of 5. Well done"
    elif score <= 2:
        quiztext1="your score is "+str(score)+" out of 5. You can do better"
    else:
        score = "your score is " + str(score) + " out of 5. Not bad but could be better"
    return quiztext1



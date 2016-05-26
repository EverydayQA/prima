#!/usr/bin/python
import logging
import menu
import quiz


class Taken(object):
    def __init__(self, *args, **args):
        self.args =args
        self.kwargs = kwargs
    @property
    def taken_pass_count(self):
        pass
    @property
    def taken_fail_count(self):
        pass

# take from QuizList() - Quiz
# write back to AnswerList-- Answer()?
# QuizTaken() class/ same as answerList?
class TakeQuiz(object):
    def __init__(self, category):
        self.category = category
    

def main():
    # choose category
    categories = ['QC', 'python']
    category = menu.select_from_list(categories, 'Please choose a category')

    take_quiz = TakeQuiz(category)
    file_question = take_quiz.file_to_read(category)

    data_list = take_quiz.read_question(file_question)
    sels = take_quiz.select(data_list)

    # save answers - an Answer base class?
    take_quiz.save_sels(sels)



if __name__ == '__main__':
    main()

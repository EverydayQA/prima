#!/usr/bin/python

class TakeQuiz(object):
    def __init__(self, category):
        self.category = category
    

def main():
    # choose category
    categories = ['QC', 'python']
    category = select_from_list(categories, 'Please choose a category')

    take_quiz = TakeQuiz(category)
    file_question = take_quiz.file_to_read(category)

    data_list = take_quiz.read_question(file_question)
    sels = take_quiz.select(data_list)

    # save answers
    take_quiz.save_sels(sels)

    # judgement call? another class?


if __name__ == '__main__':
    main()

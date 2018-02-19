from argparse import ArgumentParser
from models import Expence, Income
from datetime import datetime, timedelta

"""
    It's a self defined project for me to just have fun! 
    its a personal sofware which is supposed to help me to manage my expences. 
    Next Task: add custom date for your expences and incomes.
"""

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('--amount', type=int, 
                    help='amount')

    parser.add_argument('--type', type=str, default='expence',
                      help='income or expence')
    
    parser.add_argument('--time' , type=str, default='today')

    parser.add_argument('--des' , type=str, default="", 
                     help='description')
    FLAGS, unparsed = parser.parse_known_args()

    if FLAGS.time == 'yesterday':
        time = datetime.now() - timedelta(days=1)
    else:
        time = datetime.now()

    if FLAGS.amount:
        if FLAGS.type == 'income':
            src = input("Whats the income's source: ")
            income = Income(FLAGS.amount, src , time , FLAGS.des )
            income.save()
        elif FLAGS.type == 'expence':
            cat = input("Whats the expence's category: ")
            expence = Expence(FLAGS.amount, cat , time , FLAGS.des)
            expence.save()
    else:
        print("At least you must enter amount!")

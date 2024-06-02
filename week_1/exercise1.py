
def calc_f1_score(tp, fp, fn):
    if not isinstance(tp, int):
        print('tp must be an int\n')
        return
    
    if not isinstance(fp, int):
        print('fp must be an int\n')
        return
    
    if not isinstance(fn, int):
        print('fn must be an int\n')
        return
    
    if tp < 0 or fp < 0 or fn < 0:
        print('tp and fp and fn must be greater than zero\n')
        return

    precision = tp / (tp + fp)
    recall = tp / (tp + fn)
    f1_score = 2 * (precision * recall) / (precision + recall)
    
    print(f'Precision is {precision}')
    print(f'Recall is {recall}')
    print(f'F1-score is {f1_score}')

    print(f'Rounded F1-score is {round(f1_score, 2)}')



if __name__ == '__main__':
    calc_f1_score(tp=2, fp=4, fn=5)
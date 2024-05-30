import pickle
import os

scores = []
scores_bin = 'C:/pysave/scores.bin'

def save_scores(scores, filename):
    with open(filename, 'wb') as scores_bin:
        pickle.dump(scores, scores_bin)

def load_scores(filename):
    with open(filename, 'rb') as scores_bin:
        scores = pickle.load(scores_bin)
    return scores

def get_average(scores, n):
    K = sum(scores)/(n)
    return K

def print_everything(scores, k):
    print('\n[점수 출력]')
    print('입력 점수:', ' ' .join(map(str, scores)))
    #학생 수 변경 시 오류를 막기 위해 리스트 전체 출력 사용
    print(f'평균: {k:.1f}')

def input_scores():
    N = 1
    i = 6 #i 변경 = 학생 수 변경
    for w in range(i):
        x = input(f'#{N}?')
        if int(x) >= 0:
            scores.append(int(x))
            N += 1
        else:
            pass
    return N

def check_file():
    if os.path.exists(scores_bin):
        return load_scores(scores_bin)
    else:
        return []

def main():
    global scores
    if os.path.exists(scores_bin):
        scores = check_file()
        k = get_average(scores, len(scores))
        print_everything(scores, k)

    else:
        print('[점수 입력]')
        n = input_scores()
        k = get_average(scores, n-1)
        print_everything(scores, k)
        save_scores(scores, 'C:/pysave/scores.bin')

main()

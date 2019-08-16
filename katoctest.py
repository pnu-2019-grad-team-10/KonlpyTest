from konlpy.tag import Kkma
from konlpy.utils import pprint
import pandas as pd

#한줄씩 처리해서 리턴
def makingpos(katoc) :
    pos_data = {'N':'','V':'','M':'','I':'','J':'','E':'','X':'','S':'','U':'','O':''}
    kkma = Kkma()
    temp = kkma.pos(katoc)
    for i in temp :
        pum = i[1] #품사의 첫번쨰 글
        pos_data[pum[0]] = i[0] #딕셔너리에 넣기

    return pos_data
    


data = pd.read_csv("카톡데이터3.csv")
msg = list(data['Message'])
#ㅎㅏㄴㅈㅜㄹㅆㅣㄱ ㄷㅏㅅㅣ ㄴㅏㄴㅜㄱㅣ
size = len(msg)


result_data = pd.DataFrame(columns=['N','V','M','I','J','E','X','S','U','O'])


for i in range(0,size) :
    result = makingpos(msg[i]).copy()
    print(result)
    for key in result.keys() :
        result_data.loc[i,key] = result[key]

print(result_data)
result_data.to_csv("resultdata.csv")



#ㅎㅏㅁㅅㅜㅇㅔ ㅎㅏㄴ ㅈㅜㄹㅆㅣㄱ ㅇㅣㅂㄹㅕㄱㅎㅏㄱㅣ

#ㄹㅜㅍㅡ ㄷㅗㄹㄹㅣㄱㅗ


#ㅍㅏㄴㄷㅏㅅㅡ ㄷㅔㅇㅣㅌㅓㅍㅡㄹㅔㅇㅣㅁ ㅉㅏㄱㅣ


#posㄹㅗ ㅇㅓㄷㅇㅡㄴ ㄱㅏㅂㅅㅇㅡㄹ ㄷㅔㅇㅣㅌㅓㅍㅡㄹㅔㅇㅣㅁㅇㅔ ㅈㅣㅂㅇㅓㄴㅓㅎㄱㅣ






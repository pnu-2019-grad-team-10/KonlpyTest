from konlpy.tag import Kkma
from konlpy.utils import pprint
import pandas as pd

#한줄씩 처리해서 리턴
def makingpos(katoc) :
    pos_data = {'N':[],'V':[],'M':[],'I':[],'J':[],'E':[],'X':[],'S':[],'U':[],'O':[]}
    kkma = Kkma()
    temp = kkma.pos(katoc)
    for i in temp :
        pum = i[1] #품사의 첫번쨰 글
        pos_data[pum[0]].append(i[0]) #딕셔너리에 넣기

    return pos_data
    
    

#데이터프레임에 문장마다 품사별로 구분해서 집어넣기 
msg = ['가는 말이 고와야 오는 말이 곱다','가랑잎이 솔잎더러 바스락거린다고 한다','개천에서 용 난다']
size = len(msg)
result_data = pd.DataFrame(columns=['N','V','M','I','J','E','X','S','U','O'])


for i in range(0,size) :
    result = makingpos(msg[i]).copy()
    print(result)
    for key in result.keys() :
        result_data.loc[i,key] = result[key]

print(result_data)
result_data.to_csv("resultdata.csv")

#반말/존댓말 구분



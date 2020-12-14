#딕셔너리에서 인덱싱을 할 때는 존재하는 키로만 할 수 있기 때문에 '누가바'라는 키는 아이스크림에 없어서 오류가 발생한다.
icecream = {'폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
icecream['누가바']
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    icecream['누가바']
KeyError: '누가바'

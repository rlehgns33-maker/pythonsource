# 영어타자 프로그램
from time import time, localtime, strftime
from random import random, choice, sample, shuffle, randrange,randint, uniform
import random
import time


# word.txt 읽어서
# 섞는다 random.suffle()
# 임의로 하나 추출 random.choice()

AAA =[]

with open("./ch1/data/word.txt", "r", encoding="utf-8") as f:
    contents = f.readlines()

    for word in contents:
        word = word.strip()  # 단어 뒤의 줄바꿈 제거

        if word:  # 빈 줄은 제외
            AAA.append(word)

result = 0


# Q1) then
# input()
# input 결과에 따라서  정답!!  or  오타!!


start = time.time()

a = 1
while a <6:
    words = random.choice(AAA)
    print(words)
    print(f"Q{a})")
    ward = input()
    if ward.strip() == words.strip():
        result += 1
        print("정답!")
        a += 1
    else:
        print("오답!")
        a += 1


end = time.time()
qt =int(start - end)
print(f"게임 시간 : {qt:.2f} 정답 개수 : {result}")

if result >= 3:
    print("합격")
else:
    print("불합격")

# 문제 5문제 출제
# 정답 개수
# 게임시간 출력
# 출력문 => 게임 시간 : 10초, 정답 개수: 3개
# 3개이상 정답인 경우 합격 or 불합격








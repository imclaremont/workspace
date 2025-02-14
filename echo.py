while True:
    # 사용자로부터 한 줄을 입력받습니다.
    sentence = input()
    
    # 사용자가 '!quit'을 입력하면 반복을 종료합니다.
    if sentence == "!quit":
        break
    
    # 입력받은 문장을 그대로 출력합니다.
    print(sentence)

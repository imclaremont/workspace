import re

def validate_password(password):
    # 정규 표현식 패턴:
    # - (?=.*[a-z]) : 영문 소문자를 최소 1개 포함
    # - (?=.*[A-Z]) : 영문 대문자를 최소 1개 포함
    # - (?=.*\d)    : 숫자를 최소 1개 포함
    # - (?=.*[^a-zA-Z0-9]) : 영문, 숫자가 아닌 특수문자를 최소 1개 포함
    pattern = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[^a-zA-Z0-9]).+$')
    
    # 패턴이 매치되면 유효한 비밀번호로 판단
    if pattern.match(password):
        return True
    return False

# 테스트용 코드
if __name__ == "__main__":
    pwd = input("비밀번호를 입력하세요: ")
    if validate_password(pwd):
        print("비밀번호가 유효합니다.")
    else:
        print("비밀번호가 유효하지 않습니다.")

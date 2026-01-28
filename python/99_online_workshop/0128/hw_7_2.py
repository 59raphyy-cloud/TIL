# 아래 클래스를 수정하시오.
class StringRepeater:
    def repeat_string(self, count, string):
        # [TIP] 인덱스가 아닌 횟수로서 사용할 때는 i 대신 _를 임시변수로 사용
        for _ in range(count):
            print(string)


repeater1 = StringRepeater()
repeater1.repeat_string(3, "Hello")

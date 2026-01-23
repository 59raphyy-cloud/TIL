# 아래에 코드를 작성하시오.


# [방법1] 모듈 안의 요소를 각각 호출
# 장점 : 코드가 간결하고 가독성이 좋음
# 단점 : 다른 모듈에서 똑같은 이름의 변수를 가져오면 충돌 발생
# 참고) import 뒤에 여러 요소가 들어와도 괄호로 묶지 않아도 됨
from conf.settings import NAME, MAIN_URL
from utils.create_url import create_url
result = create_url(NAME, MAIN_URL)
print(result)


# [방법2] 모듈을 통째로 호출
# 장점 : 값의 출처가 명확함
# 단점 : 매번 모듈명을 앞에 붙여야 하므로 코드가 길어짐
# [모듈명].[함수명]
# 모듈명(상자 이름)을 앞에 붙여서 내부 요소에 접근

# from conf import settings
# from utils import create_url
# result = create_url.create_url(settings.NAME, settings.MAIN_URL)
# print(result)
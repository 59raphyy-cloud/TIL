import requests
import json
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

# 위키피디아에서 이미지를 가져오는 함수
def get_wiki_image(director_name):
    # 위키피디아 API 호출 주소
    wiki_url = "https://ko.wikipedia.org/w/api.php"
    params = {
        "action": "query",
        "titles": director_name,
        "prop": "pageimages",
        "format": "json",
        "pithumbsize": 500, # 이미지 가로 크기 500px
    }
    
    try:
        response = requests.get(wiki_url, params=params).json()
        pages = response.get("query", {}).get("pages", {})
        
        # 페이지 ID가 유동적이므로 첫 번째 페이지의 정보를 가져옴
        for page_id in pages:
            page = pages[page_id]
            if "thumbnail" in page:
                return page["thumbnail"]["source"] # 실제 이미지 URL 반환
    except Exception as e:
        print(f"위키 이미지 검색 에러: {e}")
        
    # 이미지가 없거나 에러가 나면 보여줄 기본 이미지 (대체 이미지)
    return "https://placehold.jp/500x750.png?text=No%20Image"


# GPT 정보와 위키 이미지를 합쳐서 최종 데이터를 만드는 함수
def get_ai_director_info(director_name):
    # 환경변수에서 키를 가져옴
    api_key = os.getenv("OPENAI_API_KEY")
    client = OpenAI(api_key=api_key)
    
    # 함수 호출하여 이미지 주소를 받아옴
    img_url = get_wiki_image(director_name)

    # GPT API 활용 (JSON 응답 유도)
    prompt = f"영화 감독 '{director_name}'의 정보와 대표 작품을 JSON 형식으로 알려줘. 형식: {{'info': '...', 'works': ['작품1', '작품2']}}"
    completion = client.chat.completions.create(
        model="gpt-5-nano",
        messages=[{"role": "user", "content": prompt}],
        response_format={ "type": "json_object" }
    )
    
    ai_data = json.loads(completion.choices[0].message.content)
    
    return img_url, ai_data.get('info', '정보 없음'), ai_data.get('works', [])
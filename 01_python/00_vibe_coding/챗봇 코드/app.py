import os
import feedparser
import urllib.parse
import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv

# 1. 환경 설정 및 API 키 불러오기
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(
    api_key=api_key,
    base_url='https://gms.ssafy.io/gmsapi/api.openai.com/v1'
)

# [함수 추가] feedparser를 사용한 고퀄리티 뉴스 검색
def get_google_news(keyword):
    """구글 뉴스 RSS를 통해 최신 기사 5개의 제목과 링크를 가져옵니다."""
    encoded_keyword = urllib.parse.quote(keyword)
    rss_url = f"https://news.google.com/rss/search?q={encoded_keyword}&hl=ko&gl=KR&ceid=KR:ko"
    feed = feedparser.parse(rss_url)
    
    if not feed.entries:
        return None

    news_results = []
    for entry in feed.entries[:5]: # 최신 기사 5개
        news_results.append({
            "title": entry.title,
            "link": entry.link,
            "published": entry.published
        })
    return news_results

# 2. Streamlit UI (채피 컨셉 적용)
st.set_page_config(page_title="채피 (Chappy)", page_icon="✨")
st.title("✨ 반가워요! 저는 채피예요.")
st.markdown("수다도 떨고, 궁금한 뉴스도 같이 찾아봐요!")

if "messages" not in st.session_state:
    st.session_state.messages = []

# 대화 내용 표시
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 3. 사용자 입력 및 로직
if prompt := st.chat_input("채피에게 말을 걸어보세요!"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        # 뉴스 관련 키워드가 있는지 검사
        news_trigger = ["뉴스", "기사", "소식", "보도", "찾아줘"]
        news_context = ""
        
        if any(word in prompt for word in news_trigger):
            with st.status("잠시만요, 관련 뉴스를 꼼꼼히 읽어올게요...", expanded=False):
                news_data = get_google_news(prompt)
                if news_data:
                    news_context = "\n\n[검색된 최신 뉴스 정보]\n"
                    for i, item in enumerate(news_data, 1):
                        news_context += f"{i}. 제목: {item['title']}\n   링크: {item['link']}\n"
                else:
                    news_context = "\n(관련 뉴스를 찾지 못했습니다.)"

        try:
            # AI 응답 생성 (프롬프트 고도화)
            response = client.chat.completions.create(
                model='gpt-5-nano',
                messages=[
                    {
                        "role": "system", 
                        "content": "당신은 밝고 영리한 AI 비서 '채피'입니다. "
                                   "사용자가 뉴스를 요청하면 제공된 검색 결과를 바탕으로 내용을 요약하고 통찰을 제공하세요. "
                                   "검색 결과가 없거나 일반 대화라면 친구처럼 친절하게 수다를 떨면 됩니다."
                    },
                    {"role": "user", "content": f"{prompt}{news_context}"}
                ]
            )
            
            answer = response.choices[0].message.content
            st.markdown(answer)
            st.session_state.messages.append({"role": "assistant", "content": answer})
            
        except Exception as e:
            st.error(f"채피가 잠시 아파요(오류): {e}")
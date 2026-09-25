import streamlit as st
from utils import generate_script

st.title("🎦视频脚本生成器")

with st.sidebar:
    openai_api_key =  st.text_input("请输入你的OpenAI API密钥：", type= "password")
    st.markdown("[获取OpenAI API密钥](http://platform.openai.com/account/api-keys)")

subject = st.text_input("💡请输入视频主题：")

video_length = st.number_input("⏰请输入视频长度：", min_value= 0.1, step= 0.1)

creativity = st.slider("⭐请输入视频的创造力", min_value= 0.0, max_value= 1.0, value= 0.3)

submit = st.button("生成脚本")

if submit and not openai_api_key:
    st.info("还未输入API密钥")
    st.stop()
if submit and not subject:
    st.info("还未输入视频主题")
    st.stop()
if submit and not video_length >= 0.1:
    st.info("视频时长需要大于或等于0.1")
    st.stop()

if submit:
    with st.spinner("AI正在思考，请耐心等候..."):
        title, script = generate_script(subject, video_length, creativity, openai_api_key)
    st.success("视频脚本已生成！")
    st.subheader("🔥标题：")
    st.write(title)
    with st.expander("🖊视频脚本："):
        st.info(script)







import streamlit as st
from datetime import date
from PIL import Image

# 页面设置
st.set_page_config(page_title="给最爱的你", page_icon="💖")

# 星空背景CSS（简化版，先保证能显示）
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #e0eafc, #cfdef3);
    color: #333;
}
h1, h2, h3 {
    color: #2c3e50;
}
</style>
""", unsafe_allow_html=True)

# 标题
st.title("✨ 给最爱的你 ✨")
st.markdown("---")

# 时间胶囊
start_date = date(2026, 3, 22)
today = date.today()
days = (today - start_date).days

st.markdown(f"💖 这是我们在一起的第 **{days}** 天 💖")
st.markdown("---")

# 情话库
messages = {
    1: "遇见你，是我这辈子最幸运的事",
    7: "我不能保证让你时时刻刻都幸福，但我会尽我最大努力",
    30: "一个月快乐！以后还有无数个一个月",
    100: "100天啦！爱你不是说说而已",
    365: "一年了，未来的每一年都想和你过",
}

# 显示已解锁情话
st.subheader("📜 已解锁的情话 📜")
col1, col2 = st.columns(2)
msg_list = list(messages.items())
half = len(msg_list) // 2

with col1:
    for day, msg in msg_list[:half]:
        if days >= day:
            st.success(f"第{day}天：{msg}")
        else:
            st.info(f"第{day}天：？？？（还有{day - days}天解锁）")

with col2:
    for day, msg in msg_list[half:]:
        if days >= day:
            st.success(f"第{day}天：{msg}")
        else:
            st.info(f"第{day}天：？？？（还有{day - days}天解锁）")

st.markdown("---")

# 照片展示
# 照片展示
st.subheader("📸 你在我眼里")
st.markdown("无论哪一张，都是最美的你 💕")

# 左右两张照片
col1, col2 = st.columns(2)

# 统一高度（比如200像素）
target_height = 200

with col1:
    try:
        img1 = Image.open("photo1.jpg")
        # 按比例缩放到统一高度
        ratio = target_height / img1.height
        new_width = int(img1.width * ratio)
        img1 = img1.resize((new_width, target_height))
        st.image(img1, use_container_width=False)
        st.caption("✨ 我承认我见色起意 ✨")
    except:
        st.image(Image.open("照片1.jpg"))
        st.caption("✨ 我承认我见色起意 ✨")

with col2:
    try:
        img2 = Image.open("photo2.jpg")
        # 按比例缩放到统一高度
        ratio = target_height / img2.height
        new_width = int(img2.width * ratio)
        img2 = img2.resize((new_width, target_height))
        st.image(img2, use_container_width=False)
        st.caption("✨ 但你确实颇具风色 ✨")
    except:
        st.image(Image.open("照片2.jpg"))
        st.caption("✨ 但你确实颇具风色 ✨")
st.markdown("---")

# 表白按钮
if 'clicked' not in st.session_state:
    st.session_state.clicked = False

if not st.session_state.clicked:
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("💖 点这里 💖", use_container_width=True):
            st.session_state.clicked = True
            st.balloons()
else:
    st.markdown("## 💖 我喜欢你 💖")
    st.markdown("### 我还欠你一个正式的表白 💖")

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("💕 愿意 💕", use_container_width=True):
            st.success("那就让我们一起走过四季 💖")
            st.balloons()
        if st.button("💔 不愿意 💔", use_container_width=True):
            st.error("你在想什么美事呢，你能跑了我是👍，让你跑了我是👎")

st.markdown("---")
st.caption("💖 每一天都是最爱你的一天 💖")

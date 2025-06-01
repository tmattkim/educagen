import streamlit as st
from modular_course import generate_course_outline, generate_module_content

st.set_page_config(page_title="Educagen Course Generator", layout="wide")

page_bg_img = """
<style>
[data-testid="stAppViewContainer"] {
  height: 100vh;
  margin: 0;
  background: linear-gradient(270deg, #a33a3a, #b39c1d, #1a7d6e, #1a5f7d);
  background-size: 800% 800%;
  animation: gradientShift 20s ease infinite;
}

@keyframes gradientShift {
  0% {
    background-position: 0% 50%;
  }
  50% {
    background-position: 100% 50%;
  }
  100% {
    background-position: 0% 50%;
  }
}
</style>
"""

hide_streamlit_style = """
<style>
header {visibility: hidden;}
</style>
"""

st.markdown(hide_streamlit_style, unsafe_allow_html=True)
st.markdown(page_bg_img, unsafe_allow_html=True)

st.title("📚 Educagen Course Generator ✏️")

# Initialize session state for persistence
if "course_topic" not in st.session_state:
    st.session_state.course_topic = ""
if "intro" not in st.session_state:
    st.session_state.intro = ""
if "modules" not in st.session_state:
    st.session_state.modules = []
if "expanded_modules" not in st.session_state:
    st.session_state.expanded_modules = {}
if "checked_modules" not in st.session_state:
    st.session_state.checked_modules = []

# Input course topic
course_topic = st.text_input("Enter course topic:", value=st.session_state.course_topic)

# Generate course outline
if st.button("Generate Course"):
    with st.spinner("Generating course outline..."):
        intro, modules, outline_text = generate_course_outline(course_topic)
        st.session_state.course_topic = course_topic
        st.session_state.intro = intro
        st.session_state.modules = modules
        st.session_state.expanded_modules = {}
        st.session_state.checked_modules = []

# Display course intro and modules checkboxes
if st.session_state.intro and st.session_state.modules:
    st.subheader("📘 Course Introduction")
    st.write(st.session_state.intro)

    st.subheader("📚 Select Modules to Expand")

    # Container for the checkboxes
    for module_title in st.session_state.modules:
        # Checkbox state controlled by session_state.checked_modules
        checked = module_title in st.session_state.checked_modules
        new_checked = st.checkbox(module_title, value=checked, key=f"chk_{module_title}")

        if new_checked and module_title not in st.session_state.checked_modules:
            st.session_state.checked_modules.append(module_title)
        elif not new_checked and module_title in st.session_state.checked_modules:
            st.session_state.checked_modules.remove(module_title)

    # Display expanded content for checked modules
    for i, module_title in enumerate(st.session_state.checked_modules, 1):
        if module_title not in st.session_state.expanded_modules:
            with st.spinner(f"Generating content for '{module_title}'..."):
                content = generate_module_content(module_title)
                st.session_state.expanded_modules[module_title] = content

        st.markdown(f"---\n### Module {i}: {module_title}")
        st.write(st.session_state.expanded_modules[module_title])

import streamlit as st

# --- Config ---
st.set_page_config(page_title="Quiz App", layout="centered")

# --- Sidebar Info ---
st.sidebar.markdown("**Name:** Bourennane Lylia Fatma")
st.sidebar.markdown("**Student ID:** 222231354408")
st.sidebar.markdown("**Group:** 6")
st.sidebar.markdown("**Name:** Achir Fatima Zohra")
st.sidebar.markdown("**Student ID:** 222231517220")
st.sidebar.markdown("**Group:** 6")
# --- Quiz Questions ---
questions = [
    {
        "question": "What does CPU stand for?",
        "options": ["Central Processing Unit", "Control Panel Unit", "Computer Personal Unit", "Central Process Utility"],
        "answer": "Central Processing Unit"
    },
    {
        "question": "Which language is used for web apps?",
        "options": ["Python", "HTML", "Java", "All of the above"],
        "answer": "All of the above"
    },
    {
        "question": "What is 8 * 7?",
        "options": ["54", "56", "64", "48"],
        "answer": "56"
    },
    {
        "question": "Which protocol is used to send email?",
        "options": ["HTTP", "FTP", "SMTP", "SNMP"],
        "answer": "SMTP"
    },
        {
        "question": "Which company developed the Windows operating system?",
        "options": ["Apple", "Google", "Microsoft", "IBM"],
        "answer": "Microsoft"
    },
    {
        "question": "What does RAM stand for?",
        "options": ["Readily Accessed Memory", "Random Access Memory", "Run Access Memory", "Rapid Application Memory"],
        "answer": "Random Access Memory"
    },
    {
        "question": "What is the extension of a Python file?",
        "options": [".py", ".pt", ".pyt", ".pyth"],
        "answer": ".py"
    },
    {
        "question": "Which device is used to convert digital signals to analog?",
        "options": ["Router", "Modem", "Switch", "Repeater"],
        "answer": "Modem"
    },
    {
        "question": "Which of the following is NOT an operating system?",
        "options": ["Windows", "Linux", "Oracle", "macOS"],
        "answer": "Oracle"
    }
]

# --- Session State ---
if "score" not in st.session_state:
    st.session_state.score = 0
if "q_index" not in st.session_state:
    st.session_state.q_index = 0
if "finished" not in st.session_state:
    st.session_state.finished = False

# --- App Title ---
st.title("🧠 Multiple Choice Quiz")
# --- Display Question ---
if not st.session_state.finished:
    current_q = questions[st.session_state.q_index]
    st.subheader(f"Question {st.session_state.q_index + 1}:")
    st.markdown(current_q["question"])
    answer = st.radio("Choose your answer:", current_q["options"])

    if st.button("Submit Answer"):
        if answer == current_q["answer"]:
            st.success("Correct!")
            st.session_state.score += 1
        else:
            st.error(f"Wrong. The correct answer is: {current_q['answer']}")

        if st.session_state.q_index + 1 < len(questions):
            st.session_state.q_index += 1
        else:
            st.session_state.finished = True
        st.rerun()

else:
    st.markdown(f"### ✅ Quiz Completed!")
    st.markdown(f"**Your Score: {st.session_state.score} / {len(questions)}**")
    if st.button("Restart Quiz"):
        st.session_state.score = 0
        st.session_state.q_index = 0
        st.session_state.finished = False
        st.rerun()



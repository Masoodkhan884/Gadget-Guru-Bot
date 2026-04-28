import os
from dotenv import load_dotenv
from groq import Groq

# -----------------------------
# LOAD ENV
# -----------------------------
load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# -----------------------------
# INIT GROQ CLIENT
# -----------------------------
client = Groq(api_key=GROQ_API_KEY)

# -----------------------------
# SYSTEM PROMPT
# -----------------------------
SYSTEM_PROMPT = """
You are a professional customer support assistant for the product "AeroPress Pro 5 Coffee Maker".

Rules:
- Use ONLY the provided context to answer.
- If the answer is not in the context, say:
  "I don't have this information in the product manual."
- Do NOT guess or hallucinate.
- Be concise, helpful, and friendly.
"""

# -----------------------------
# GENERATE ANSWER
# -----------------------------
def generate_answer(question, context_chunks):
    """
    Builds prompt + sends to Groq LLM
    """

    # combine retrieved context
    context_text = "\n\n".join(
        [c["text"] for c in context_chunks]
    )

    # final prompt
    prompt = f"""
Context:
{context_text}

User Question:
{question}

Answer:
"""

    # call Groq LLM
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": prompt}
        ],
        temperature=0.2
    )

    return response.choices[0].message.content


# -----------------------------
# TEST RUN
# -----------------------------
if __name__ == "__main__":

    sample_context = [
        {
            "text": "To reset Bluetooth, hold power button for 10 seconds until LED blinks."
        },
        {
            "text": "AeroPress Pro 5 supports Bluetooth connectivity for smart devices."
        }
    ]

    question = "How do I reset Bluetooth?"

    answer = generate_answer(question, sample_context)

    print("\n🤖 Final Answer:\n")
    print(answer)
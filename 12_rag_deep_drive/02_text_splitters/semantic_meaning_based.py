from langchain_experimental.text_splitter import SemanticChunker
from langchain_openai.embeddings import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

text_splitter = SemanticChunker(
    OpenAIEmbeddings(), breakpoint_threshold_amount=1, breakpoint_threshold_type="standard_deviation"
)

sample_text = """
Artificial Intelligence (AI) has revolutionized how we interact with technology in recent years. From personal assistants like Siri and Alexa to predictive algorithms in healthcare and finance, AI has become deeply integrated into our daily lives. The rapid progress of machine learning models, particularly deep learning, has enabled computers to process vast amounts of data and uncover patterns that were once invisible to human analysts.

However, despite its progress, AI still faces significant challenges. One of the most pressing issues is the question of bias and fairness. Models trained on real-world data often reflect the biases present in that data, leading to skewed outcomes. For instance, facial recognition systems have shown reduced accuracy for people with darker skin tones. Addressing these issues requires not only technical adjustments but also broader social and ethical considerations.

Another area of focus in AI research is explainability. Many of today’s most powerful models, such as large neural networks, operate as “black boxes.” They deliver highly accurate predictions but offer little insight into how those predictions are made. Explainable AI (XAI) aims to make these systems more transparent, enabling humans to understand and trust AI-driven decisions. This is particularly important in sectors like healthcare or criminal justice, where accountability and interpretability are critical.

Beyond these challenges, AI continues to open new frontiers. In the creative industries, for example, generative models can now produce artwork, compose music, and even write stories. These systems blur the line between human and machine creativity, raising philosophical questions about authorship and originality. In business, AI-driven automation is improving efficiency while also reshaping the workforce and prompting discussions about the future of employment.

The next major leap in AI development is likely to come from advancements in multimodal learning — systems that can process and reason across multiple forms of input, such as text, images, and sound. This approach mirrors human cognition more closely and could pave the way for more general and adaptive intelligence. Combined with innovations in edge computing and federated learning, AI may soon operate seamlessly across devices while preserving user privacy.

Ultimately, the evolution of AI is not just a technical journey but a societal one. How humanity chooses to develop, regulate, and integrate AI will define its long-term impact. Striking the right balance between innovation, ethics, and responsibility will determine whether AI becomes a tool for empowerment or division.
"""

response = text_splitter.split_text(text=sample_text)

print(len(response))

print(response)
from transformers import pipeline

summarizer = pipeline(
    "summarization",
    model="sshleifer/distilbart-cnn-12-6"
)

def generate_summary(text, length="medium"):
    print("Selected summary type:", length)

    # Clean extracted text
    text = " ".join(text.split())

    # Limit input size (safe for DistilBART)
    text = text[:2000]

    if length == "short":
        max_len = 60
        min_len = 30
    elif length == "long":
        max_len = 200
        min_len = 100
    else:
        max_len = 130
        min_len = 70

    print("Length:", length)
    print("Max:", max_len)
    print("Min:", min_len)

    # Prevent min_length > input length
    words = len(text.split())
    if words < min_len:
        min_len = max(10, words // 2)

    if max_len <= min_len:
        max_len = min_len + 20

    result = summarizer(
        text,
        max_length=max_len,
        min_length=min_len,
        do_sample=False,
        truncation=True
    )

    return result[0]["summary_text"]
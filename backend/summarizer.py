from transformers import pipeline

summarizer = pipeline(
    "summarization",
    model="sshleifer/distilbart-cnn-12-6"
)

def generate_summary(text, length="medium"):
    print("Selected summary type:", length)
    
    text= text[:5000]
    if length=="short":
        max_len=60
        min_len= 30
    elif length=="long":
        max_len= 200
        min_len= 100
    else:
        max_len= 130
        min_len= 70
    
    print ("length", length)
    print ("max:", max_len)
    print ("min:", min_len)
    result = summarizer(
        text,
        max_length=max_len,
        min_length=min_len,
        do_sample=False
    )

    return result[0]["summary_text"]
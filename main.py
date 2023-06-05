from transformers import pipeline

classifier = pipeline("sentiment-analysis")

res = classifier("I am neither sad or happy, but I am fine")

print(res)

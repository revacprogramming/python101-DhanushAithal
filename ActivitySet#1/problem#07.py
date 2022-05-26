text = "X-DSPAM-Confidence:    0.8475"
stvalue = text.find('0.8475')
value = text[stvalue:]
print(float(value))
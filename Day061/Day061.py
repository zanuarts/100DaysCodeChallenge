def order(sentence):
    return " ".join(sorted(sentence.split(),
                           key=lambda x: sorted(x)))

# https://github.com/dsdshcym/Codewar-Solution/blob/master/your_order_please.py
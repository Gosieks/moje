text = "X-DSPAM-Confidence:    0.8475"
colonpos = text.find(':')
number = text[colonpos+1: ]
fnumber = float(number)
print(fnumber)
print('6_5')
print ('end')




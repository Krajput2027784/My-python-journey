import time

song = [
    "🎶Sun le ye sadaa.....",
    "💖 Kaisi dillagi hai tu.....",
    "😣 Kaisi bebasi hai tu.....",
    "🥰 Meri Zindagi Hai Tu.....",
    "🤗 Meri Zindagi Hai Tu......",
    "💖 ☆*: .｡. o(≧▽≦)o .｡.:*☆........"
]
delays = [0.9,4.2,4.2,4.6,0.8,4.0]
def type_line(line):
    for char in line:
        print(char,end="",flush=True)
        time.sleep(0.05)
    print()
time.sleep(2)
for i in range(len(song)):
    type_line(song[i])
    time.sleep(delays[i])
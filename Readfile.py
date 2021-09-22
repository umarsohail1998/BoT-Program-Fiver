import json

data = open('file.txt', 'r')
data.readline()


def makedict(S_no, ep_no, url):
    return {
        'S#': S_no,
        'EP#': ep_no,
        'URL': url
    }

dt = {}
while True:
    
    st = data.readline()
    if st == "":
        break
    url = data.readline().strip()

    st = st.split(',')[1].strip().split(" ")
    ep_no = st.pop()
    s_no = st.pop()
    S_name = ' '.join(st)

    if dt.__contains__(S_name):
        dt[S_name].append(makedict(s_no, ep_no, url))
    else:
       dt[S_name] = [] 
       dt[S_name].append(makedict(s_no, ep_no, url))
       
with open('data.json', 'w') as fp:
    json.dump(dt, fp,  indent=4)
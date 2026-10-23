import json, random
def dec(n, p=2):
    b = 10**p
    w, f = divmod(n, b)
    fs = str(f).zfill(p).rstrip("0")
    return str(w) + "." + fs if fs else str(w)
def m(n): return f"{n//100}.{str(n%100).zfill(2)}"
def pl(n, one, many): return f"{n}" + (one if n == 1 else many)
def v(n, one, many): return one if n == 1 else many
def boxes(n, b):
    k = -(-n//b)
    return f"The {pl(n,' vial',' vials')} at {pl(b,' vial',' vials')} a box {v(n,'takes','take')} {pl(k,' box',' boxes')}, the last box holding {pl(n-(k-1)*b,' vial',' vials')}."
def weeks(n, w):
    k = n//w
    return f"The {pl(n,' vial',' vials')} at {pl(w,' vial',' vials')} a week {v(n,'lasts','last')} {pl(k,' full week',' full weeks')} with {pl(n-k*w,' vial',' vials')} left for the next week."
def cost(b, pc, n):
    cc = b*pc
    pv = (2*cc + n)//(2*n)
    return f"The {pl(b,' box',' boxes')} at ${m(pc)} a box {v(b,'comes','come')} to ${m(cc)}, ${m(pv)} a vial."
def time_(n, pm):
    t = -(-n//pm); h, r = t//60, t%60
    return f"The {pl(n,' vial',' vials')} at {pl(pm,' vial',' vials')} a minute {v(n,'takes','take')} {pl(t,' minute',' minutes')}, {pl(h,' hour',' hours')} {pl(r,' minute',' minutes')}."
random.seed(780)
R = random.randint
cases = [
 dict(fn="boxes", args=["940","50"], expect=boxes(940,50)),
 dict(fn="weeks", args=["940","110"], expect=weeks(940,110)),
 dict(fn="cost", args=["19","27.40","940"], expect=cost(19,2740,940)),
 dict(fn="time", args=["940","12"], expect=time_(940,12)),
 dict(fn="boxes", args=["1","1"], expect=boxes(1,1)),
 dict(fn="boxes", args=["900","50"], expect=boxes(900,50)),
 dict(fn="boxes", args=["1000000","1000"], expect=boxes(1000000,1000)),
 dict(fn="weeks", args=["1","1"], expect=weeks(1,1)),
 dict(fn="weeks", args=["880","110"], expect=weeks(880,110)),
 dict(fn="weeks", args=["1000000","100000"], expect=weeks(1000000,100000)),
 dict(fn="cost", args=["1","0.01","1"], expect=cost(1,1,1)),
 dict(fn="cost", args=["100000","999.99","1000000"], expect=cost(100000,99999,1000000)),
 dict(fn="time", args=["1","1"], expect=time_(1,1)),
 dict(fn="time", args=["60","1"], expect=time_(60,1)),
 dict(fn="time", args=["1000000","100"], expect=time_(1000000,100)),
]
for _ in range(20):
    n,b=R(1,1000000),R(1,1000); cases.append(dict(fn="boxes", args=[str(n),str(b)], expect=boxes(n,b)))
for _ in range(20):
    n,w=R(1,1000000),R(1,100000); cases.append(dict(fn="weeks", args=[str(n),str(w)], expect=weeks(n,w)))
for _ in range(25):
    b,p,n=R(1,100000),R(1,99999),R(1,1000000); cases.append(dict(fn="cost", args=[str(b),dec(p),str(n)], expect=cost(b,p,n)))
for _ in range(19):
    n,m=R(1,1000000),R(1,100); cases.append(dict(fn="time", args=[str(n),str(m)], expect=time_(n,m)))
errs=[["boxes",["0","50"]],["boxes",["1000001","50"]],["boxes",["2.5","50"]],["boxes",["940","0"]],["boxes",["940","1001"]],
 ["weeks",["0","110"]],["weeks",["940","0"]],["weeks",["940","100001"]],["weeks",["940","1.5"]],["weeks",["1000001","110"]],
 ["cost",["0","27.40","940"]],["cost",["100001","27.40","940"]],["cost",["19","0","940"]],["cost",["19","27.405","940"]],["cost",["19","27.40","0"]],
 ["time",["0","12"]],["time",["940","0"]],["time",["940","101"]],["time",["940","6.5"]],["time",["1000001","12"]]]
json.dump(dict(cases=cases, errors=errs), open("expected.json","w"), indent=1)
print(len(cases),"cases,",len(errs),"errcases")

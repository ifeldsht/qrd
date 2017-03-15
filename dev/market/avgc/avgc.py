import psycopg2

def read_db(conn,query):
    cur = conn.cursor()
    cur.execute(query)
    rows = cur.fetchall()
    res = []
    for r in rows:
        res.append(list(r))
    return res 

def calendar(conn):
    query = """select dt from dd
               where sid=104 and dt>20090000
               order by dt"""
    return [r[0] for r in read_db(conn,query)]
        
def market_data(conn,sid):
    query = """select dt, r,
                      case
                        when po>0 and pc>0 then (pc-po)/po
                        else -99.0
                      end as roc
                from dd where sid=""" + str(sid) +\
            """ order by dt"""
    return read_db(conn,query)
        
def price_gen(rets):
    p = 1.0
    for r in rets:
        if r > -1: p *= r + 1.0
        yield p
        
def price_avg(p,n):
    pavg = list(p)
    if n > 1: 
        for i in range(n-1,len(pavg)): 
            pavg[i] = sum(p[i-n+1:i+1])/n
    return pavg

def cross_avg(p0,p1,dt,roc): # n0>n1
    T = []
    diff = [ 2.0*(p[1]-p[0])/(p[1]+p[0]) for p in zip(p0,p1) ]
    for i in range(1,len(diff)-1):
        if diff[i-1]*diff[i] < 0 and roc[i+1] > -1:
            T.append( (dt[i],diff[i],roc[i+1]) )
    return T

def process_one(md,nl=[10,8,6,5,4,3,2,1]):
    p = list(price_gen([d[1] for d in md]))
    pavg = { n:price_avg(p,n) for n in nl }
    dt  = [d[0] for d in md]
    roc = [d[2] for d in md]
    c = {}
    for n0 in nl:
        for n1 in [n for n in nl if n<n0]:
            c[(n0,n1)] = cross_avg(pavg[n0],pavg[n1],dt,roc)
    return c
    
def after_cross_moves(cross,cal):
    def arr2avg(a):
        if len(a)>0: return sum(a)/len(a)
        return 0
    moves = {}
    for d in cal:
        pos = {}
        neg = {}
        for sid in cross:
            for nn in cross[sid]:
                if nn not in pos: pos[nn] = []
                if nn not in neg: neg[nn] = []
                pos[nn] += [c[2] for c in nn if c[0]==d and c[1] > 0]
                neg[nn] += [c[2] for c in nn if c[0] == d and c[1]<0]
        for nn in pos: pos[nn] = arr2avg(pos[nn])
        for nn in neg: neg[nn] = arr2avg(neg[nn])
        moves[d] = (pos,neg)
    
# for tests only
if __name__=="__main__":
    conn = psycopg2.connect("dbname='md'  host='localhost' user='postgres' password='123'")
    c = calendar(conn)
    md = market_data(conn,104)
    print process_one(md,[10,1])

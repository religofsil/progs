# -*- coding: utf-8 -*-
def viterbi(o_states, s_states, initial, trans, emis):
    n = [{}]
    for st in s_states:
        try:
            n[0][st] = {"prob": initial[st] * emis[st][o_states[0]], "prev": None}
        except:
            n[0][st] = {'prob': 0, 'prev': None}
    for t in range(1, len(o_states)):
        n.append({})
        for st in s_states:
            max_tr_prob = max(n[t-1][prev_st]["prob"]*trans[prev_st][st] for prev_st in s_states)
            for prev_st in s_states:
                if n[t-1][prev_st]["prob"] * trans[prev_st][st] == max_tr_prob:
                    try:
                        maxx = max_tr_prob * emis[st][o_states[t]]
                    except KeyError:
                        maxx = 0
                    n[t][st] = {"prob": maxx, "prev": prev_st}
                    break
    o = []
    maxx = max(value["prob"] for value in n[-1].values())
    previous = None
    for st, data in n[-1].items():
        if data["prob"] == maxx:
            o.append(st)
            previous = st
            break
    for t in range(len(n) - 2, -1, -1):
         o.insert(0, n[t + 1][previous]["prev"])
         previous = n[t][previous]["prev"]

    print u'Правильно: '+u' '.join(o)
    print u'Вероятность: '+str(maxx)

sentence1=u'тело мыло раму'
sentence2=u'мама мыла книги'
sentence3=u'оно мыло мыло'

words=set([u'тело', u'мыло', u'раму', u'мама', u'мыла', u'книги', u'оно'])
tp={'Pron':{'Pron':435, 'N':806, 'V':12701}, 'V':{'V':3584, 'Pron':10218, 'N':11380}, 'N':{'Pron':286, 'N':392, 'V':48316}}
emis={'N':{u'тело':76737, u'раму':9877, u'мыло':2368, u'книги':7960, u'мама':13025, u'мыла':307}, 'V':{u'мыло':455, u'мыла':868}, 'Pron':{u'оно':14176}}
init_observations={'N':5924404, 'V':5345267, 'Pron':3199070}
s_space=set(init_observations)
absolute={'N':96794536, 'V':59305274, 'Pron':27085374}
for i in tp:
    for n in tp[i]:
        tp[i][n]=float(tp[i][n])/absolute[i]
for i2 in emis:
    for n2 in emis[i2]:
        emis[i2][n2]=float(emis[i2][n2])/absolute[i2]

print 'start'
viterbi(sentence3.split(u' '), s_space, init_observations, tp, emis)

with open('text.txt', 'r', encoding='UTF-8') as file:
    find_smb = file.read().lower()
    f = {}
    n = 0
    for smb in find_smb:
        if ord('a') <= ord(smb) <= ord('z'):
            x = f.get(smb, 0)
            f[smb] = x + 1
            n += 1
    lout = [(k, "{:5.3f}".format(f[k] / n)) for k in f.keys()]
    lout.sort(key=lambda x: x[0])
    lout.sort(key=lambda x: x[1], reverse=True)
    sout = '\n'.join([i[0] + ' ' + i[1] for i in lout])

open('analysis.txt', 'w').write(sout)


class İndeks:
    def indeks_tap(self, siyahı, məqsəd):
        indekslər = [(a, b) for a in range(len(siyahı)) for b in range(a+1, len(siyahı)) if siyahı[a] + siyahı[b] == məqsəd]
        return indekslər if indekslər else -1

indekstap = İndeks()
siyahı = [1, 2, 3, 4, 5]
məqsəd = 8
print(indekstap.indeks_tap(siyahı, məqsəd))



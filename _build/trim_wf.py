# -*- coding: utf-8 -*-
import io,re,sys
DEL=["벤치마킹 대응","Hive 대비 개선점","Hive 대응","벤치마킹 대비",
     "키를 본사가 쥐는 근거","MDR 기준값의 출처","「경로 상이」를 상태로 둔 이유",
     "가장 흔한 차단 원인","「불일치」가 가장 늦게 발견된다","D2C의 위치",
     "목록형이 아니라 박스형인 이유","숨기지 않고 회색 처리하는 이유","도메인을 노출하는 이유",
     "계약은 지사 명의 · 협상과 키는 본사","확정 필요 — 지사 개방 여부",
     "무게 — 중간","7행 무게 배분"]
MOVE=["코드 정본 확정 필요","세 번째 API가 빠져 있다","헤더명이 문서마다 다르다",
      "확정 필요 2건","/revoke 규격 미정","Tier 3 PG의 리포트 형태 미확인"]
SPEC_MAX=3

def find_blocks(h, cls):
    """depth-matched <div class="cls"> ... </div> spans"""
    out=[]
    for m in re.finditer(r'<div class="%s">'%cls, h):
        i=m.end(); depth=1
        for t in re.finditer(r'<div\b|</div>', h[i:]):
            depth += 1 if t.group(0).startswith('<div') else -1
            if depth==0:
                out.append((m.start(), i+t.end())); break
    return out

log=[]
for f in sys.argv[1:]:
    h=io.open(f,encoding="utf-8").read(); before=len(h.encode("utf-8"))
    spans=[]
    for cls in ("imm","warn"):
        spans += find_blocks(h, cls)
    assert len(spans)==h.count('<div class="imm">')+h.count('<div class="warn">'), "span miss"
    nd=nm=nk=0; kept=[]
    cut=[]
    for a,b in spans:
        blk=h[a:b]
        mh=re.search(r'class="(?:imm|warn)-h">([^<]*)',blk)
        head=mh.group(1) if mh else "?"
        if head in DEL: nd+=1; cut.append((a,b))
        elif head in MOVE: nm+=1; cut.append((a,b))
        else: nk+=1; kept.append(head)
    for a,b in sorted(cut, reverse=True):
        # swallow trailing whitespace/newline
        e=b
        while e<len(h) and h[e] in " \n": e+=1
        h=h[:a]+h[e:] if h[a-1:a]=="\n" else h[:a]+h[e:]
    # trim spec rows beyond SPEC_MAX within each .spec block
    trimmed=0
    def fix_spec(m):
        global trimmed
        rows=re.findall(r'\n\s*<div class="spec-r">[\s\S]*?</div>', m.group(2))
        if len(rows)<=SPEC_MAX: return m.group(0)
        trimmed += len(rows)-SPEC_MAX
        return m.group(1)+"".join(rows[:SPEC_MAX])+"\n        </div>"
    h=re.sub(r'(<div class="spec">)([\s\S]*?)\n        </div>', fix_spec, h)
    io.open(f,"w",encoding="utf-8",newline="\n").write(h)
    log.append("%s\n  deleted %d  moved-out %d  kept %d  spec-rows-trimmed %d\n  %d -> %d bytes\n  kept blocks: %s"
               %(f,nd,nm,nk,trimmed,before,len(h.encode("utf-8"))," / ".join(kept)))
io.open("_build/trim_log.txt","w",encoding="utf-8").write("\n".join(log))
print("done -> _build/trim_log.txt")

# -*- coding: utf-8 -*-
import io, os, re, posixpath

NAV = [
    ("화면정의서", [
        ("wireframe/portal-main-auth-screens.html", "라그나로크 포털 화면정의서"),
        ("wireframe/webshop-ui.html", "웹샵 화면정의서"),
        ("wireframe/payment-checkout-channels.html", "라그나로크원페이 화면정의서"),
    ]),
    ("설계", [
        ("wiki/planning/portal-main-structure.html", "포털 메인 구조"),
        ("wiki/planning/land-auth.html", "랜드 회원·인증 설계"),
        ("wiki/planning/webshop-payment-prd.html", "웹샵/통합결제 기획"),
        ("wiki/planning/payment-webshop-structure.html", "웹샵/통합결제 구조"),
    ]),
    ("벤치마킹", [
        ("wiki/benchmark/ip-portal.html", "IP 포털 벤치마킹"),
        ("wiki/benchmark/nc-auth.html", "NC 회원·인증 통합 벤치마킹"),
        ("wiki/benchmark/pg-multi-entity.html", "PG 다중법인 구조 벤치마킹"),
        ("wiki/benchmark/game-platform-payment.html", "게임플랫폼 벤치마킹"),
        ("wiki/benchmark/webshop-payment.html", "웹샵 벤치마킹"),
    ]),
    ("전체", [("index.html", "문서 목록")]),
]

def rel(frm, to):
    base = posixpath.dirname(frm)
    r = posixpath.relpath(to, base if base else ".")
    return r

def menu(cur, indent="    "):
    out = []
    for group, items in NAV:
        out.append('%s<div class="g">%s</div>' % (indent, group))
        for path, label in items:
            on = ' class="on"' if path == cur else ''
            out.append('%s<a href="%s"%s>%s</a>' % (indent, rel(cur, path), on, label))
    return "\n".join(out)

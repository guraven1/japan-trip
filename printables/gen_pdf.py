from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor
from reportlab.platypus import BaseDocTemplate, Frame, PageTemplate, Paragraph, Table, TableStyle
from reportlab.lib.styles import ParagraphStyle

W, H = A4
M = 11 * mm
GUT = 6 * mm
colw = (W - 2 * M - GUT) / 2

ink = HexColor('#1C221F'); mut = HexColor('#5C655F')
acc = HexColor('#2F4A8A'); rule = HexColor('#C9CEC6')
warn = HexColor('#A8681B')

sec = ParagraphStyle('sec', fontName='Helvetica-Bold', fontSize=8.6, leading=10.5,
                     textColor=acc, spaceBefore=7, spaceAfter=2.5)
body = ParagraphStyle('body', fontName='Helvetica', fontSize=7.4, leading=9.4, textColor=ink, spaceAfter=2.6)
wstyle = ParagraphStyle('warn', parent=body, textColor=warn)

def P(t, s=body):
    return Paragraph(t, s)

B = lambda t: f'<b>{t}</b>'
C = lambda t: f'<font name="Courier-Bold" size="7.6">{t}</font>'
NEX = "N'EX"

story = []
story.append(P('JAPAN 2026 - BOOKING CODES &amp; PICKUP SHEET',
               ParagraphStyle('t', fontName='Helvetica-Bold', fontSize=12.5, leading=14, textColor=ink)))
story.append(P("Gur &amp; Rachel  ·  Sep 3-23  ·  compiled Sep 1 — all transport booked  ·  live plan: Trip Desk artifact on claude.ai",
               ParagraphStyle('st', fontName='Helvetica', fontSize=7.2, leading=9, textColor=mut, spaceAfter=4)))

story.append(P('FLIGHTS', sec))
story.append(P(f'{B("El Al LY91")} Wed Sep 2, TLV 19:45 &gt; NRT T1 Sep 3, 13:20 · PNR {C("YJ5PON")} (Gur also {C("YFYDLE")}) · Premium, 2 bags pp'))
story.append(P(f'{B("ANA NH59")} Mon Sep 7, HND T2 10:00 &gt; CTS 11:35 · ref {C("FMSXWA")} · bag drop closes 09:30 · leave Shibuya 07:45'))
story.append(P(f'{B("ANA NH984")} Thu Sep 10, CTS 13:45 &gt; ITM 15:40 · ref {C("DHYPIM")} · bag drop closes 13:15'))
story.append(P(f'{B("El Al LY92")} Wed Sep 23, NRT T1 15:35 &gt; TLV 22:20 · PNR {C("YJ5PON")} · at NRT ~13:00 (holiday)'))
story.append(P('Check ANA Manage Booking shows 2 bags pp - add online if 1PC.', wstyle))

story.append(P('TRAINS - PAPER-TICKET PICKUPS (the three that bite)', sec))
story.append(P(f'{B("Azusa 42")} Sat Sep 19, Matsumoto 15:10 &gt; Shinjuku 18:04 · car 5, seats 1-A/B · Eki-net {C("E37835")}<br/>'
               f'PICK UP in Tokyo {B("Sep 3-6")}, any JR East reserved-seat machine · QR / code {C("29372419579521238")}<br/>'
               'Ticket valid through to Tokyo Stn: stay inside gates at Shinjuku, Chuo rapid onward.'))
story.append(P(f'{B("Hida 7")} Wed Sep 16, Nagoya 10:48 &gt; Takayama 13:12 · car 8, seats 9-C/D · e5489 {C("45760")}, receipt {C("AEC9782M")}<br/>'
               f'PICK UP at Osaka/Shin-Osaka {B("Sep 14-15")}, JR-West green machine outside gates.'))
story.append(P('Needs the PHYSICAL Mastercard ...1969 in the machine + your 4-digit ID. Pack that card!', wstyle))
story.append(P(f'{B(NEX + " (Shinjuku) 21")} Wed Sep 23, Tokyo 11:33 &gt; Narita T1 12:31 · car 3, seats 3-A/B · Eki-net {C("E48412")} · ¥6,280 for 2 incl. basic fare (paid)<br/>'
               f'PICK UP at Tokyo Stn {B("Sep 19-22")} (staying inside the station) · QR in the E48412 email / code {C("20292476220521218")} · must be issued before boarding.'))

story.append(P('TRAINS &amp; BUSES - APP / EMAIL TICKETS', sec))
story.append(P(f'{B("Nozomi 84")} Wed Sep 16, Shin-Osaka 09:24 &gt; Nagoya 10:13 · car 14, seats 2-D/E · Smart-EX res {C("2001")} · QR at gate (app/email)'))
story.append(P(f'{B("Shirakawa-go bus OUT")} Thu Sep 17, Takayama Nohi BC 07:50 &gt; Ogimachi 08:40 · res {C("08312001231")} · car 01, seats 11A/B'))
story.append(P(f'{B("Shirakawa-go bus BACK")} Thu Sep 17, 16:35 &gt; Takayama 17:25 · res {C("08312035491")} · car 01, seats 7A/B'))
story.append(P('The JapanBusOnline EMAILS are the tickets - print both + screenshot; show to driver. No counter exchange.', wstyle))
story.append(P(f'{B("Hirayu &gt; Matsumoto bus")} Sat Sep 19, 12:55 &gt; 14:23 · highwaybus.com {C("185319539")} · bus 1, seats 03A/B · MOBILE ticket: screenshot email · at terminal 12:35 · cancel online only until 11:20'))

story.append(P('HOTELS - ALL ON KLOOK', sec))
hotel_rows = [
    ['Sep 3-7', 'Shibuya Stream Hotel', 'PBZ943404'],
    ['Sep 7-9', 'Sapporo Stream Hotel', 'KGG392117'],
    ['Sep 9', 'Takinoya, Noboribetsu', 'JFN966234'],
    ['Sep 10-14', 'HOTEL RINGS KYOTO', 'HZR550734'],
    ['Sep 14-16', 'Hotel Royal Classic Osaka', 'EEV842685'],
    ['Sep 16-18', 'Takayama Ouan', 'ERB149933'],
    ['Sep 18', 'Kutsuroginoya Yuu, Okuhida', 'GFV226893'],
    ['Sep 19-23', 'The Tokyo Station Hotel', 'YTX109746'],
]
t = Table(hotel_rows, colWidths=[15 * mm, colw - 15 * mm - 21 * mm, 21 * mm])
t.setStyle(TableStyle([
    ('FONT', (0, 0), (1, -1), 'Helvetica', 7.2),
    ('FONT', (2, 0), (2, -1), 'Courier-Bold', 7.4),
    ('TEXTCOLOR', (0, 0), (-1, -1), ink),
    ('LINEBELOW', (0, 0), (-1, -2), 0.3, rule),
    ('TOPPADDING', (0, 0), (-1, -1), 1.2), ('BOTTOMPADDING', (0, 0), (-1, -1), 1.2),
    ('LEFTPADDING', (0, 0), (-1, -1), 0), ('RIGHTPADDING', (0, 0), (-1, -1), 2),
]))
story.append(t)
story.append(P('Screenshot each voucher in the Klook app. Kutsuroginoya = Hitoegane, Shin-Hirayu (stop "Ipposui"), NOT Tochio; free pickup from Hirayu terminal on call: 0578-89-3345.', wstyle))

story.append(P('TICKETS &amp; RESTAURANTS', sec))
story.append(P(f'{B("teamLab Planets")} Fri Sep 4, 11:00-11:30 entry · QR appears on {B("DMM My Tickets")} after 00:00 Sep 4 - the email does NOT admit. Barefoot + knee-deep water: shorts.'))
story.append(P(f'{B("Udatsu Sushi")} Fri Sep 4, 20:30 · AutoReserve, name Aven Gur · CONFIRMED Sep 1: 2 guests, 1 Vegetarian Course + 1 regular Omakase, both paid at the restaurant · tel 050-3550-5938'))
story.append(P(f'{B("Enoteca Via Salaria")} Sun Sep 13, 19:00 (Kyoto, Higashiyama near Tofuku-ji - NOT Gion) · TableCheck, 2 pax, 9-dish course 9,680 yen pp + premium pairing · same-day cancel 100% · tel 075-366-5361'))
story.append(P(f'{B("LE MiDi")} Wed Sep 16, 19:00 (kitchen closes 20:30 - be on time) · {B("Kyoya")} Thu Sep 17, 19:00 · both AutoReserve, fees paid'))
story.append(P(f'{B("IRORIYA")} Sun Sep 20, 19:00 · TableCheck {C("#EUQMTC")} · {B("FARO")} Tue Sep 22, 19:00 · TableCheck {C("#C3SAA5")} (Rachel vegan course confirmed)'))

story.append(P('TAKKYUBIN - COPY ONTO THE BAG TAGS (Osaka desk, Sep 15, 08:30)', sec))
story.append(P('The Tokyo Station Hotel, 1-9-1 Marunouchi, Chiyoda-ku, Tokyo 100-0005 · tel +81 3-5220-1111<br/>'
               f'Guest: Gur Aven · Klook {C("YTX109746")} · arriving Sep 19 · write "hold for guest arriving 9/19" · ~2,500-3,000 yen/bag, pay at desk<br/>'
               'Keep 3 nights of clothes in hand luggage (Takayama / Okuhida).'))

story.append(P('KEY PHONES', sec))
story.append(P('Nohi Bus (Takayama) 0577-32-1688 · Kutsuroginoya Yuu 0578-89-3345 · Udatsu 050-3550-5938 · Kyoya 0577-34-7660 · LE MiDi 0577-36-6386 · Via Salaria 075-366-5361 · Tokyo Station Hotel +81 3-5220-1111'))
story.append(P('CASH: World Heritage Bus to Ainokura 1,300 yen pp each way + Shiroyama shuttle = coins; 7-Eleven ATM on day one.', wstyle))

doc = BaseDocTemplate('preflight-codes.pdf', pagesize=A4,
                      leftMargin=M, rightMargin=M, topMargin=M, bottomMargin=M)
f1 = Frame(M, M, colw, H - 2 * M, leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
f2 = Frame(M + colw + GUT, M, colw, H - 2 * M, leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
doc.addPageTemplates([PageTemplate(id='two', frames=[f1, f2])])
doc.build(story)

import re as _re
print("pages:", len(_re.findall(rb"/Type\s*/Page[^s]", open("preflight-codes.pdf","rb").read())))

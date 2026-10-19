"""Build the original, image-led GitHub profile. Python standard library only."""
from pathlib import Path
import re, urllib.request, concurrent.futures, html
R=Path(__file__).resolve().parents[1];A=R/'assets/visual';A.mkdir(parents=True,exist_ok=True)
INK='#302a22';M='#6d6355';G='#89602b';B='#c5a264'
ICONS=[('azure','Azure','https://learn.microsoft.com/azure/'),('python','Python','https://www.python.org/'),('apachespark','Spark / PySpark','https://spark.apache.org/'),('microsoftsqlserver','SQL Server','https://www.microsoft.com/sql-server'),('mysql','MySQL','https://www.mysql.com/'),('git','Git','https://git-scm.com/'),('azuredevops','Azure DevOps','https://azure.microsoft.com/products/devops'),('streamlit','Streamlit','https://streamlit.io/')]
def download(item):
 key=item[0];p=A/(key+'-logo.svg')
 if not p.exists():
  u=f'https://raw.githubusercontent.com/devicons/devicon/master/icons/{key}/{key}-original.svg'
  p.write_bytes(urllib.request.urlopen(u,timeout=25).read())
 return key,len(p.read_bytes())
with concurrent.futures.ThreadPoolExecutor(max_workers=8)as pool:
 for value in pool.map(download,ICONS):print('Logo',*value)
lic=A/'DEVICON-LICENSE.txt'
if not lic.exists():lic.write_bytes(urllib.request.urlopen('https://raw.githubusercontent.com/devicons/devicon/master/LICENSE',timeout=25).read())

def svg(name,w,h,content,title):
 d=f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-labelledby="title"><title id="title">{html.escape(title)}</title><defs><linearGradient id="paper" x2="1" y2="1"><stop stop-color="#fffdf8"/><stop offset=".55" stop-color="#f8f2e6"/><stop offset="1" stop-color="#f1e6ce"/></linearGradient><linearGradient id="glass" x2=".9" y2="1"><stop stop-color="#fff" stop-opacity=".96"/><stop offset="1" stop-color="#fff" stop-opacity=".48"/></linearGradient><radialGradient id="gold"><stop stop-color="#e5c68d" stop-opacity=".7"/><stop offset="1" stop-color="#e5c68d" stop-opacity="0"/></radialGradient><radialGradient id="lavender"><stop stop-color="#dcd3ed" stop-opacity=".7"/><stop offset="1" stop-color="#dcd3ed" stop-opacity="0"/></radialGradient></defs><g font-family="Arial,Helvetica,sans-serif" fill="{INK}">{content}</g></svg>'''
 (A/name).write_text(d)
def paper(w,h):return f'<rect x="1" y="1" width="{w-2}" height="{h-2}" rx="26" fill="url(#paper)" stroke="#d8c8aa"/><path d="M28 2H{w-28}" stroke="#fff" stroke-width="2"/>'
def t(x,y,text,size=16,fill=INK,extra=''):return f'<text x="{x}" y="{y}" font-size="{size}" fill="{fill}" {extra}>{html.escape(text)}</text>'
def glass(x,y,w,h,r=20):return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="url(#glass)" stroke="#d9ccb5"/>'
def logo(key,x,y,size):
 raw=(A/(key+'-logo.svg')).read_text();raw=re.sub(r'<\?xml.*?\?>','',raw,flags=re.S)
 raw=re.sub(r'<svg\b([^>]*)>',lambda m:'<svg '+re.sub(r'\b(?:width|height)="[^"]*"','',m.group(1))+f' x="{x}" y="{y}" width="{size}" height="{size}">',raw,count=1)
 return raw
# Hero: an original editorial identity and layered data illustration.
c=paper(1200,390)+'<ellipse cx="1010" cy="130" rx="300" ry="250" fill="url(#gold)"/><ellipse cx="800" cy="300" rx="270" ry="180" fill="url(#lavender)"/>'
c+=t(46,49,'M Q   /   DATA & AI',12,G,'letter-spacing="4"')+t(46,131,'Muzammil',68,INK,'font-weight="700" letter-spacing="-3"')+t(46,207,'Qazi.',80,G,'font-weight="700" letter-spacing="-4"')
c+=t(49,259,'AZURE DATA ENGINEER',17,INK,'letter-spacing="2"')+t(49,288,'AI WORKFLOW AUTOMATION',13,M,'letter-spacing="2"')+t(49,350,'PUNE, INDIA',11,M,'letter-spacing="2"')+t(264,350,'COGNIZANT · SINCE 2022',11,M,'letter-spacing="2"')
c+='<path d="M790 118L1040 118 1040 274 840 274" fill="none" stroke="#a7875155" stroke-width="2" stroke-dasharray="4 7"/>'
for x,y,w,h in [(744,64,305,95),(796,175,305,95),(702,280,305,74)]:c+=glass(x,y,w,h,18)
c+=logo('azure',764,87,48)+t(831,104,'CLOUD',10,M,'letter-spacing="2"')+t(831,131,'Azure data platforms',18)
c+=logo('python',815,196,48)+t(879,216,'ENGINEERING',10,M,'letter-spacing="2"')+t(879,241,'Python · SQL · Spark',17)
c+='<g transform="translate(726 300)" fill="none" stroke="#89602b" stroke-width="2"><path d="M10 0L30 12 20 35 0 23Z M10 0V23L20 35 M0 23L30 12"/><circle cx="10" cy="0" r="3" fill="#89602b"/></g>'+t(781,309,'AUTOMATION',10,M,'letter-spacing="2"')+t(781,336,'AI-assisted workflows',17)
c+='<style>@media(prefers-reduced-motion:reduce){.packet{display:none}}</style><circle class="packet" r="4" fill="#89602b"><animateMotion dur="8s" repeatCount="indefinite" path="M790 118L1040 118 1040 274 840 274"/></circle>'
svg('hero.svg',1200,390,c,'Muzammil Qazi. Azure Data Engineer. AI Workflow Automation. Pune, India. Cognizant since 2022.')
# Clickable navigation tiles, no text-heavy navigation paragraphs.
paths={'portfolio':'<rect x="15" y="13" width="38" height="30" rx="5"/><path d="M15 23h38M25 18h1m6 0h1M25 32l5 4-5 4m11 0h9"/>','resume':'<path d="M24 9h22l9 9v36H24Z M46 9v12h9M31 30h17M31 37h17M31 44h12"/>','linkedin':'<rect x="17" y="12" width="40" height="40" rx="7"/><path d="M26 28v15m0-23v1m9 22V28m0 7c0-10 13-10 13 0v8"/>','contact':'<rect x="14" y="15" width="44" height="32" rx="6"/><path d="M16 19l20 15 20-15"/>'}
for key,label in [('portfolio','PORTFOLIO'),('resume','RÉSUMÉ'),('linkedin','LINKEDIN'),('contact','CONTACT')]:
 c=paper(290,84)+f'<g transform="translate(6 11)" fill="none" stroke="{G}" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">{paths[key]}</g>'+t(85,47,label,14,INK,'letter-spacing="2"')+t(255,48,'↗',22,G)
 svg('nav-'+key+'.svg',290,84,c,label)
# Icon tiles: each tile links to that technology's documentation.
for key,label,url in ICONS:
 c=paper(280,190)+logo(key,108,31,64)+t(140,143,label,18,INK,'text-anchor="middle"')+t(140,169,'↗',14,G,'text-anchor="middle"')
 svg('tool-'+key+'.svg',280,190,c,label+' — view documentation')
for fname,left,right in [('stack-heading.svg','01 / THE TOOLKIT','CLOUD  /  DATA  /  AUTOMATION'),('work-heading.svg','02 / SELECTED WORK','EXPLORE THE CASE STUDIES'),('journey-heading.svg','03 / THE JOURNEY','COGNIZANT TECHNOLOGY SOLUTIONS')]:
 c=t(5,40,left,14,G,'letter-spacing="3"')+t(1190,40,right,11,M,'text-anchor="end" letter-spacing="2"')+'<path d="M4 60h1192" stroke="#c9b68f"/>'
 svg(fname,1200,74,c,left)
# Three compact illustrated, clickable case-study cards.
for key,title1,title2,category,subtitle in [('pipeline','Pipeline','Support Assistant','CASE STUDY','AI-assisted diagnostics'),('quality','Data Quality &','Reconciliation','CASE STUDY','Metadata-driven validation'),('knowledge','Operations','Knowledge Assistant','PROOF OF CONCEPT','RAG · LlamaIndex')]:
 c=paper(390,356)+t(28,38,category,10,G,'letter-spacing="2"')
 if key=='pipeline':
  c+='<path d="M65 143h255" stroke="#c1ac81" stroke-width="2"/>'
  for x,label in [(42,'LOG'),(157,'AI'),(272,'SQL')]:c+=glass(x,86,76,94,13)+t(x+38,143,label,17,G,'text-anchor="middle"')
 elif key=='quality':
  c+=glass(53,80,126,107,14)+glass(211,80,126,107,14)
  for x in [73,231]:
   for yy in [103,126,149]:c+=f'<path d="M{x} {yy}h85" stroke="#c3b290" stroke-width="7" stroke-linecap="round"/>'
  c+='<circle cx="195" cy="137" r="27" fill="#fffdf7" stroke="#b7a172"/><path d="M182 137l9 9 17-21" stroke="#77602f" stroke-width="4" fill="none"/>'
 else:
  for x,y in [(64,91),(83,107),(102,123)]:c+=glass(x,y,92,74,10)
  c+='<path d="M204 144h65m-13-10 13 10-13 10" fill="none" stroke="#b09a70" stroke-width="2"/><circle cx="293" cy="139" r="31" fill="#fffdf7" stroke="#b7a172"/>'+t(293,148,'AI',22,G,'text-anchor="middle"')
 c+=t(28,243,title1,27,INK,'font-weight="700" letter-spacing="-1"')+t(28,277,title2,27,INK,'font-weight="700" letter-spacing="-1"')+t(28,324,subtitle,12,M)+t(346,326,'↗',24,G)
 svg('work-'+key+'.svg',390,356,c,title1+' '+title2+' — '+category.lower())
# A concise career strip, rather than another table of prose.
for key,year,line1,line2 in [('trainee','2022 — 2023','Programmer Analyst','Trainee'),('analyst','2023 — 2024','Programmer','Analyst'),('associate','2024 — PRESENT','Associate','')]:
 c=paper(390,180)+t(28,39,year,12,G,'letter-spacing="2"')+t(28,93,line1,25,INK,'font-weight="700"')+t(28,124,line2,25,INK,'font-weight="700"')+t(28,157,'COGNIZANT',10,M,'letter-spacing="2"')
 svg('job-'+key+'.svg',390,180,c,'Cognizant '+line1+' '+line2+' '+year)

c=paper(1200,160)+'<path d="M95 70h1000" stroke="#cfbd99" stroke-width="2"/>'
for x,year,role in [(65,'2022','Programmer Analyst Trainee'),(440,'2023','Programmer Analyst'),(815,'2024 → PRESENT','Associate')]:
 c+=f'<circle cx="{x+15}" cy="70" r="6" fill="{G}" stroke="#fff" stroke-width="3"/>'+t(x,42,year,12,G,'letter-spacing="2"')+t(x,117,role,20,INK,'font-weight="700"')
svg('journey.svg',1200,160,c,'Cognizant: Programmer Analyst Trainee in 2022, Programmer Analyst in 2023, Associate since November 2024.')
c=paper(1200,150)+'<ellipse cx="1050" cy="40" rx="260" ry="180" fill="url(#gold)"/>'+t(38,64,'Let’s connect.',34,INK,'font-weight="700" letter-spacing="-1"')+t(39,108,'DATA ENGINEERING  /  AI AUTOMATION',12,M,'letter-spacing="2"')+t(705,84,'kazimuzammil99@gmail.com',24,G)+t(1137,86,'↗',32,G)
svg('connect.svg',1200,150,c,'Email Muzammil Qazi: kazimuzammil99@gmail.com')
# No duplicated walls of prose. Descriptive alternative text remains accessible.
readme='''<!-- Original visual profile. Edit scripts/build_visual.py to regenerate assets. -->
<p align="center">
  <a href="https://m-qazi99.github.io/"><img src="assets/visual/hero.svg" alt="Muzammil Qazi — Azure Data Engineer · AI Workflow Automation · Pune, India" width="100%"></a>
</p>
<p align="center">
'''
nav=[('portfolio','https://m-qazi99.github.io/','Open portfolio'),('resume','https://m-qazi99.github.io/Muzammil_Qazi_Resume.pdf','Download résumé'),('linkedin','https://www.linkedin.com/in/muzammil-1209-qazi/','Connect on LinkedIn'),('contact','mailto:kazimuzammil99@gmail.com','Email Muzammil')]
for key,url,alt in nav:readme+=f'  <a href="{url}"><img src="assets/visual/nav-{key}.svg" alt="{alt}" width="170"></a>\n'
readme+='</p>\n\n<img src="assets/visual/stack-heading.svg" alt="Technology toolkit" width="100%">\n\n<p align="center">\n'
for i,(key,label,url)in enumerate(ICONS):
 readme+=f'  <a href="{url}"><img src="assets/visual/tool-{key}.svg" alt="{label}" width="170"></a>\n'
 if i==3:readme+='</p>\n<p align="center">\n'
readme+='</p>\n\n<p align="center"><a href="https://m-qazi99.github.io/#skills">More technologies ↗</a></p>\n\n<img src="assets/visual/work-heading.svg" alt="Selected case studies" width="100%">\n\n<p align="center">\n'
for key,slug,alt in [('pipeline','pipeline-support','Pipeline Support Assistant — case study'),('quality','data-quality','Data Quality and Reconciliation — case study'),('knowledge','knowledge-assistant','Operations Knowledge Assistant — proof of concept')]:
 readme+=f'  <a href="https://m-qazi99.github.io/work/{slug}/"><img src="assets/visual/work-{key}.svg" alt="{alt}" width="245"></a>\n'
readme+='''</p>

<p align="center"><a href="https://github.com/m-qazi99/m-qazi99.github.io">Portfolio source code ↗</a></p>

<img src="assets/visual/journey-heading.svg" alt="Career at Cognizant" width="100%">
<p align="center">\n<a href="https://m-qazi99.github.io/#experience"><img src="assets/visual/job-trainee.svg" alt="Cognizant: Programmer Analyst Trainee, March 2022–June 2023" width="245"></a>\n<a href="https://m-qazi99.github.io/#experience"><img src="assets/visual/job-analyst.svg" alt="Cognizant: Programmer Analyst, June 2023–November 2024" width="245"></a>\n<a href="https://m-qazi99.github.io/#experience"><img src="assets/visual/job-associate.svg" alt="Cognizant: Associate, November 2024–present" width="245"></a>\n</p>

<a href="mailto:kazimuzammil99@gmail.com"><img src="assets/visual/connect.svg" alt="Let’s connect — kazimuzammil99@gmail.com" width="100%"></a>
'''
(R/'README.md').write_text(readme)
print('Built visual README and original SVG cards.')

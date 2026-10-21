"""Original, accessible SVG project cards for GitHub's static README surface."""
import json,html,textwrap
from pathlib import Path
R=Path(__file__).resolve().parents[1];A=R/'assets/visual';A.mkdir(exist_ok=True,parents=True)
items=json.loads((R/'content/live-projects.json').read_text())
H=html.escape
paths={
'pipeline-pulse':'M35 40h30v25H35z M95 15h30v25H95z M95 75h30v25H95z M65 52h15V27h15 M80 52v35h15',
'datalens':'M25 20h100v80H25z M25 45h100 M25 72h100 M58 20v80 M92 20v80 M100 82l8 8 16-20',
'recon-lab':'M30 32h85l-15-15 M115 32l-15 15 M115 78H30l15-15 M30 78l15 15',
'runbook-radar':'M35 20h65v75H35z M47 38h38 M47 53h30 M100 68a20 20 0 1 0 .1 0 M115 100l17 17',
'privacy-forge':'M75 12l45 18v33c0 22-25 42-45 51-20-9-45-29-45-51V30z M55 60l14 14 27-29',
}
for i,p in enumerate(items,1):
 color=p.get('accent','#8b692e');name=p['name'];words=textwrap.wrap(p['review'],49)
 subtitle=''.join(f'<text x="32" y="{262+j*22}" font-size="14" fill="#5d635e">{H(line)}</text>' for j,line in enumerate(words))
 svg=f'''<svg xmlns="http://www.w3.org/2000/svg" width="780" height="370" viewBox="0 0 780 370" role="img" aria-label="{H(name)} 2.1.0 by Muzammil Qazi: {H(p['review'])}"><defs><linearGradient id="bg"><stop stop-color="#fffdf6"/><stop offset="1" stop-color="{H(p.get('wash','#f5ead2'))}"/></linearGradient><radialGradient id="orb"><stop stop-color="#ffffff" stop-opacity=".95"/><stop offset="1" stop-color="{color}" stop-opacity=".12"/></radialGradient></defs><rect x="1" y="1" width="778" height="368" rx="28" fill="url(#bg)" stroke="#d6d6c7"/><circle cx="650" cy="70" r="170" fill="url(#orb)"/><g transform="translate(575 75)" fill="none" stroke="{color}" stroke-width="3" stroke-linejoin="round">{''.join('<path d="'+x+'"/>' for x in [paths[p['slug']]])}</g><g font-family="Arial,sans-serif"><text x="32" y="43" font-size="12" letter-spacing="2" fill="{color}">0{i} / PYTHON WORKBENCH</text><text x="32" y="112" font-size="42" font-weight="700" fill="#293c35">{H(name)}</text><text x="32" y="146" font-size="14" fill="#58655c">Built and maintained by Muzammil Qazi</text><rect x="32" y="176" width="120" height="30" rx="15" fill="#ffffffb8" stroke="#d3d7c8"/><text x="48" y="196" font-size="12" fill="{color}">VERSION 2.1.0</text><text x="32" y="235" font-size="11" letter-spacing="2" fill="{color}">NEW / REVIEW DESK</text>{subtitle}<path d="M32 323h716" stroke="#d6d6c7"/><text x="32" y="350" font-size="12" fill="#58655c">LIVE PYTHON · SOURCE · TESTS · USER GUIDE</text><text x="718" y="351" font-size="26" fill="{color}">↗</text></g></svg>'''
 (A/('review-'+p['slug']+'.svg')).write_text(svg)
readme=(R/'README.md').read_text();start=readme.index('<img src="assets/visual/work-heading-v2.svg"');end=readme.index('<img src="assets/visual/journey-heading-v2.svg"')
section='<img src="assets/visual/work-heading-v2.svg" alt="Five open-source Python products built by Muzammil Qazi" width="100%">\n\n<p align="center">\n'
for p in items:section+='<a href="https://m-qazi99.github.io/'+p['slug']+'/"><img src="assets/visual/review-'+p['slug']+'.svg" alt="'+H(p['name']+' v2.1 — '+p['review'])+'" width="390"></a>\n'
section+='</p>\n<p align="center">\n'
for p in items:section+='<a href="https://github.com/m-qazi99/'+p['slug']+'"><img src="assets/visual/code-'+p['slug']+'.svg" alt="'+H(p['name'])+' source and contribution guides" width="140"></a>\n'
section+='</p>\n<p align="center"><a href="https://m-qazi99.github.io/#live-projects">Find a project by discipline ↗</a> · <a href="https://github.com/m-qazi99/Reverse">Workbench catalog ↗</a></p>\n\n'
(R/'README.md').write_text(readme[:start]+section+readme[end:])
print('Built five original v2.1 cards with live and source links.')

"""Builds the 12-week ADAS IQ social series.

Writes, next to this file:
  posts.json          every post, with LinkedIn / Facebook / Instagram copy
  POSTS.md            the same copy, easy to read and paste
  index.html          the adas-iq.com/posts page (each week appears on its date)
  img/week-NN.png     1080x1350 graphic per week (LinkedIn, Facebook, Instagram)

Edit WEEKS below, then run:  python3 posts/build_posts.py
Add --no-images to skip rendering the graphics (needs Playwright + Chromium).
"""
import datetime
import html
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
START = datetime.date(2026, 10, 26)  # Monday of week 1
URL = "https://adas-iq.com/#apply"

LI_CTA = f"Pilot program open for independent mobile ADAS operators. Request early access: {URL}"
FB_CTA = f"Pilot program open. Request early access: {URL}"
IG_CTA = "Pilot program open. Request early access, link in bio or adas-iq.com"
SIGN = "Built inside Absolute ADAS, where it runs the business every day."

TAGS_LI = "#ADAS #ADAScalibration #MobileADAS #CollisionRepair #SmallBusiness"
TAGS_FB = "#ADAS #MobileADAS #ADAScalibration"
TAGS_IG = ("#ADAS #ADAScalibration #mobileADAS #calibration #collisionrepair "
           "#autobody #shopowner #smallbusiness #fieldservice #techlife")

WEEKS = [
    {
        "kicker": "WEEK 1 · BUILT IN THE FIELD",
        "headline": "We built the software we couldn't buy.",
        "core": (
            "We built the software we couldn't buy.\n\n"
            "Running a mobile ADAS operation means calibrating cars and running a business "
            "at the same time. Most software wasn't built for that.\n\n"
            "So we built ADAS IQ inside Absolute ADAS. It runs our jobs, our dispatch and our "
            "billing every day. Now we're opening it to other operators."
        ),
        "li_extra": "Every feature exists because we needed it on a real job.",
    },
    {
        "kicker": "WEEK 2 · DISPATCH",
        "headline": "Is your dispatch a group text?",
        "core": (
            "Is your dispatch a group text?\n\n"
            "Jobs come in from phone calls, emails and carrier portals. You copy-paste the "
            "address, text a tech, and hope nothing falls through.\n\n"
            "ADAS IQ routes calls and texts to the right person, sends job alerts by SMS, and "
            "assigns a tech in one tap."
        ),
        "li_extra": "A missed text shouldn't be a missed job.",
    },
    {
        "kicker": "WEEK 3 · JOB BOARD",
        "headline": "Every open job. One screen.",
        "core": (
            "Every open job. One screen.\n\n"
            "Who's on it. Where it stands. What's coming next.\n\n"
            "The ADAS IQ job board updates live, so you stop asking \"where are we on that "
            "Tahoe?\" and just look."
        ),
        "li_extra": "If the only status board is in your head, you can't take a day off.",
    },
    {
        "kicker": "WEEK 4 · INVOICING",
        "headline": "Stop building invoices from memory.",
        "core": (
            "Stop building invoices from memory.\n\n"
            "Pulling job details out of your head, one invoice at a time, hoping the billing "
            "lines match what was actually done. That's how money goes missing.\n\n"
            "ADAS IQ builds invoices from the job data. What was done is what gets billed."
        ),
        "li_extra": "The calibration is the hard part. Billing for it shouldn't be.",
    },
    {
        "kicker": "WEEK 5 · BILLING RULES",
        "headline": "Every shop bills differently. Your software should know that.",
        "core": (
            "Every shop bills differently. Your software should know that.\n\n"
            "Every shop has its own billing rules. So does every insurer. Keeping them all in "
            "your head is how invoices come back.\n\n"
            "ADAS IQ keeps billing rules per shop and per insurer, and applies them to every "
            "invoice automatically."
        ),
        "li_extra": "Write the rule once. Stop remembering it on every job.",
    },
    {
        "kicker": "WEEK 6 · ESTIMATE SCRUBBING",
        "headline": "The ADAS line that isn't on the estimate is the job you don't get.",
        "core": (
            "The ADAS line that isn't on the estimate is the job you don't get.\n\n"
            "Shops and insurers push back on calibrations. Without fast, solid estimates you "
            "lose work you should have won.\n\n"
            "ADAS IQ reviews CCC and carrier estimates for missing ADAS lines, with the right "
            "procedures every time."
        ),
        "li_extra": "Catch it on the estimate, not after the car's gone.",
    },
    {
        "kicker": "WEEK 7 · DOCUMENTATION",
        "headline": "No more chasing photos at invoice time.",
        "core": (
            "No more chasing photos at invoice time.\n\n"
            "Required photos. Calibration reports. OEM docs. If they're scattered across phones "
            "and inboxes, you find out when the bill gets questioned.\n\n"
            "ADAS IQ attaches the documentation to every job, while the job is happening."
        ),
        "li_extra": "Documentation you can find is documentation that gets you paid.",
    },
    {
        "kicker": "WEEK 8 · YOUR SHOPS",
        "headline": "Every shop you work with, always current.",
        "core": (
            "Every shop you work with, always current.\n\n"
            "Contacts, billing rules, job history. When it lives in your phone, it leaves "
            "when your phone does.\n\n"
            "ADAS IQ keeps a profile for every shop, so anyone on your team can pick up the "
            "relationship."
        ),
        "li_extra": "Your shop relationships are the business. Keep them somewhere real.",
    },
    {
        "kicker": "WEEK 9 · THE WHOLE WORKFLOW",
        "headline": "Most tools stop at the estimate.",
        "core": (
            "Most tools stop at the estimate.\n\n"
            "Scrubbers help you get the job. Then you're back to texts, spreadsheets and "
            "invoices from memory.\n\n"
            "ADAS IQ helps you run the job, and every job after it: job board, dispatch, "
            "billing, documentation and scrubbing in one platform."
        ),
        "li_extra": "Getting the job is half of it. Running it is the other half.",
    },
    {
        "kicker": "WEEK 10 · BUILT FOR OPERATORS",
        "headline": "Built for owners and techs. Not adjusters.",
        "core": (
            "Built for owners and techs. Not adjusters.\n\n"
            "A lot of ADAS software is built for the claim side. Mobile operators are left "
            "duct-taping the rest together.\n\n"
            "ADAS IQ is built around how mobile ADAS companies actually work, because it runs one."
        ),
        "li_extra": "If you run the van and the books, this was built for you.",
    },
    {
        "kicker": "WEEK 11 · NO TRADE SHOW",
        "headline": "Not sold from a trade show booth.",
        "core": (
            "Not sold from a trade show booth.\n\n"
            "No conference demos. ADAS IQ is tested on real ADAS jobs, every day, at "
            "Absolute ADAS.\n\n"
            "It had to work, or we didn't get paid."
        ),
        "li_extra": "We'd rather show you how it runs our shop than pitch you on a slide.",
    },
    {
        "kicker": "WEEK 12 · PILOT OPEN",
        "headline": "The pilot program is open.",
        "core": (
            "The pilot program is open.\n\n"
            "We're opening ADAS IQ to a small group of independent mobile ADAS operators.\n\n"
            "No credit card. No commitment. No automated sales sequence. Tell us your biggest "
            "operational headache and we'll follow up personally."
        ),
        "li_extra": "If you run a mobile ADAS calibration business, we want to talk.",
    },
]


def build_posts():
    posts = []
    for i, w in enumerate(WEEKS, 1):
        date = START + datetime.timedelta(weeks=i - 1)
        posts.append({
            "week": i,
            "date": date.isoformat(),
            "kicker": w["kicker"],
            "headline": w["headline"],
            "body": w["core"],
            "linkedin": f"{w['core']}\n\n{w['li_extra']}\n\n{LI_CTA}\n\n{SIGN}\n\n{TAGS_LI}",
            "facebook": f"{w['core']}\n\n{FB_CTA}\n\n{TAGS_FB}",
            "ig": f"{w['core']}\n\n{IG_CTA}\n.\n.\n{TAGS_IG}",
            "cta_url": URL,
            "image": f"img/week-{i:02d}.png",
        })
    return posts


def write_json(posts):
    with open(os.path.join(HERE, "posts.json"), "w") as f:
        json.dump(posts, f, indent=1, ensure_ascii=False)
        f.write("\n")


def write_md(posts):
    md = ["# ADAS IQ weekly posts\n",
          "\nGenerated by build_posts.py. Edit that file, not this one.\n"]
    for p in posts:
        md.append(f"\n## Week {p['week']} ({p['date']}): {p['headline']}\n")
        md.append(f"\nImage: `{p['image']}`\n")
        for label, key in (("LinkedIn", "linkedin"), ("Facebook", "facebook"), ("Instagram", "ig")):
            md.append(f"\n**{label}**\n\n```\n{p[key]}\n```\n")
    with open(os.path.join(HERE, "POSTS.md"), "w") as f:
        f.write("".join(md))


CARD = """<!DOCTYPE html><html><head><meta charset="UTF-8"><style>
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:1080px;height:1350px;background:#0d0d0d;font-family:Inter,Helvetica,Arial,sans-serif;
color:#f0f0f0;display:flex;flex-direction:column;padding:96px 88px;position:relative;overflow:hidden}}
body::before{{content:"";position:absolute;right:-260px;top:-260px;width:720px;height:720px;
border-radius:50%;background:radial-gradient(circle,rgba(205,68,25,.28),rgba(205,68,25,0) 70%)}}
.logo{{font-size:44px;font-weight:900;letter-spacing:-.02em;position:relative}}
.logo span{{color:#CD4419}}
.logo small{{font-size:22px;font-weight:500;color:#888;letter-spacing:.04em;margin-left:18px;
padding-left:18px;border-left:2px solid #2a2a2a;vertical-align:middle}}
.main{{flex:1;display:flex;flex-direction:column;justify-content:center;position:relative}}
.kicker{{display:inline-block;align-self:flex-start;background:rgba(205,68,25,.12);
border:2px solid rgba(205,68,25,.4);color:#CD4419;font-size:24px;font-weight:700;
letter-spacing:.12em;padding:10px 22px;border-radius:40px;margin-bottom:48px}}
h1{{font-size:{size}px;font-weight:900;line-height:1.08;letter-spacing:-.03em;color:#fff}}
.bar{{width:120px;height:8px;background:#CD4419;border-radius:4px;margin-top:56px}}
.foot{{display:flex;justify-content:space-between;align-items:center;position:relative;
border-top:2px solid #2a2a2a;padding-top:40px;font-size:26px;color:#aaa}}
.cta{{color:#fff;font-weight:700}}
.cta b{{color:#CD4419}}
</style></head><body>
<div class="logo">ADAS <span>IQ</span><small>by Absolute ADAS</small></div>
<div class="main"><div class="kicker">{kicker}</div><h1>{headline}</h1><div class="bar"></div></div>
<div class="foot"><span>Pilot program open</span><span class="cta">Join at <b>adas-iq.com</b></span></div>
</body></html>"""


SHOOT_JS = """
const { chromium } = require('playwright');
const jobs = JSON.parse(require('fs').readFileSync(0, 'utf8'));
(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1080, height: 1350 } });
  for (const j of jobs) {
    await page.setContent(j.html, { waitUntil: 'load' });
    await page.screenshot({ path: j.path });
  }
  await browser.close();
})();
"""


def write_images(posts):
    # Rendered with Node Playwright (preinstalled in the cloud env; locally: npm i playwright).
    import subprocess
    os.makedirs(os.path.join(HERE, "img"), exist_ok=True)
    jobs = []
    for p in posts:
        n = len(p["headline"])
        size = 104 if n <= 32 else 92 if n <= 48 else 80
        jobs.append({
            "path": os.path.join(HERE, p["image"]),
            "html": CARD.format(size=size, kicker=html.escape(p["kicker"]),
                                headline=html.escape(p["headline"])),
        })
    subprocess.run(["node", "-e", SHOOT_JS], input=json.dumps(jobs), text=True, check=True)


PAGE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Field Notes — ADAS IQ</title>
<meta name="description" content="Weekly notes from running a mobile ADAS calibration business, from the team behind ADAS IQ.">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
<style>
*, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}
:root {{ --orange: #CD4419; --orange-light: #e8522a; --dark: #0d0d0d; --dark2: #141414;
  --border: #2a2a2a; --text: #f0f0f0; --muted: #888; }}
body {{ font-family: 'Inter', -apple-system, Helvetica, Arial, sans-serif; background: var(--dark);
  color: var(--text); line-height: 1.6; -webkit-font-smoothing: antialiased; }}
nav {{ position: sticky; top: 0; z-index: 100; background: rgba(13,13,13,0.92);
  backdrop-filter: blur(12px); border-bottom: 1px solid var(--border); padding: 0 24px; }}
.nav-inner {{ max-width: 1080px; margin: 0 auto; display: flex; align-items: center;
  justify-content: space-between; height: 60px; }}
.nav-logo {{ font-size: 18px; font-weight: 900; color: #fff; letter-spacing: -0.02em; text-decoration: none; }}
.nav-logo span {{ color: var(--orange); }}
.nav-cta {{ background: var(--orange); color: #fff; font-size: 13px; font-weight: 700;
  padding: 8px 18px; border-radius: 6px; text-decoration: none; }}
.nav-cta:hover {{ background: var(--orange-light); }}
header {{ max-width: 760px; margin: 0 auto; padding: 64px 24px 24px; text-align: center; }}
.tag {{ display: inline-block; background: rgba(205,68,25,0.12); border: 1px solid rgba(205,68,25,0.3);
  color: var(--orange); font-size: 11px; font-weight: 700; letter-spacing: 0.12em;
  text-transform: uppercase; padding: 5px 12px; border-radius: 20px; margin-bottom: 20px; }}
h1 {{ font-size: clamp(30px, 5vw, 44px); font-weight: 900; line-height: 1.1;
  letter-spacing: -0.03em; color: #fff; margin-bottom: 14px; }}
header p {{ color: #aaa; font-size: 17px; }}
main {{ max-width: 760px; margin: 0 auto; padding: 24px 24px 80px; }}
article {{ display: grid; grid-template-columns: 200px 1fr; gap: 28px; padding: 32px 0;
  border-bottom: 1px solid var(--border); }}
article img {{ width: 100%; height: auto; border-radius: 10px; border: 1px solid var(--border); display: block; }}
.meta {{ color: var(--orange); font-size: 11px; font-weight: 700; letter-spacing: 0.12em;
  text-transform: uppercase; margin-bottom: 8px; }}
article h2 {{ font-size: 22px; font-weight: 800; color: #fff; line-height: 1.25;
  letter-spacing: -0.01em; margin-bottom: 12px; }}
article p {{ color: #bbb; font-size: 15px; margin-bottom: 10px; }}
.empty {{ text-align: center; color: var(--muted); padding: 40px 0; }}
.cta-box {{ margin-top: 48px; text-align: center; background: var(--dark2);
  border: 1px solid var(--border); border-radius: 14px; padding: 36px 24px; }}
.cta-box h3 {{ font-size: 22px; font-weight: 800; color: #fff; margin-bottom: 8px; }}
.cta-box p {{ color: #aaa; margin-bottom: 20px; }}
.btn {{ display: inline-block; background: var(--orange); color: #fff; font-weight: 700;
  padding: 13px 26px; border-radius: 8px; text-decoration: none; }}
.btn:hover {{ background: var(--orange-light); }}
footer {{ border-top: 1px solid var(--border); padding: 28px 24px; text-align: center;
  color: var(--muted); font-size: 13px; }}
footer a {{ color: var(--muted); }}
@media (max-width: 600px) {{ article {{ grid-template-columns: 1fr; gap: 16px; }}
  article img {{ max-width: 260px; }} }}
</style>
</head>
<body>
<nav><div class="nav-inner">
  <a href="/" class="nav-logo">ADAS <span>IQ</span></a>
  <a href="/#apply" class="nav-cta">Get early access →</a>
</div></nav>
<header>
  <div class="tag">Field Notes · Weekly</div>
  <h1>Notes from running a mobile ADAS shop.</h1>
  <p>One a week, from the team that built ADAS IQ inside Absolute ADAS.</p>
</header>
<main>
<div id="posts">
{articles}
</div>
<p class="empty" id="empty" hidden>First note drops soon.</p>
<div class="cta-box">
  <h3>Join the pilot program.</h3>
  <p>We're opening ADAS IQ to a small group of independent operators.</p>
  <a href="/#apply" class="btn">Request early access →</a>
</div>
</main>
<footer>A product of <a href="https://absoluteadas.com" target="_blank" rel="noopener">Absolute ADAS</a> · Software in development</footer>
<script>
// Each note goes live on its date (local time). Newest first.
(function () {{
  var today = new Date(); today.setHours(0, 0, 0, 0);
  var shown = 0;
  document.querySelectorAll('#posts article').forEach(function (a) {{
    var d = new Date(a.dataset.date + 'T00:00:00');
    if (d > today) a.remove(); else shown++;
  }});
  if (!shown) document.getElementById('empty').hidden = false;
}})();
</script>
</body>
</html>
"""


def write_page(posts):
    arts = []
    for p in reversed(posts):
        date = datetime.date.fromisoformat(p["date"])
        paras = "".join(f"<p>{html.escape(x)}</p>" for x in p["body"].split("\n\n")[1:])
        arts.append(
            f'<article data-date="{p["date"]}">\n'
            f'  <img src="{p["image"]}" alt="{html.escape(p["headline"])}" loading="lazy" width="1080" height="1350">\n'
            f'  <div><div class="meta">{date.strftime("%b %-d, %Y")} · Week {p["week"]}</div>'
            f'<h2>{html.escape(p["headline"])}</h2>{paras}</div>\n'
            f'</article>'
        )
    with open(os.path.join(HERE, "index.html"), "w") as f:
        f.write(PAGE.format(articles="\n".join(arts)))


if __name__ == "__main__":
    posts = build_posts()
    write_json(posts)
    write_md(posts)
    write_page(posts)
    if "--no-images" not in sys.argv:
        write_images(posts)
    print(f"built {len(posts)} posts in {HERE}")

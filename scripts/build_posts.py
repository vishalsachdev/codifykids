#!/usr/bin/env python3
"""Generate blog index + post pages from POSTS data. Content is verbatim
from the original Wix blog; only presentation is new."""
import pathlib

DOCS = pathlib.Path(__file__).resolve().parent.parent / "docs"

HEAD = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="icon" href="/assets/wixstatic/logo.jpg" type="image/jpeg">
<link rel="canonical" href="https://www.codifykids.org{path}">
<link rel="stylesheet" href="/assets/site.css">
</head>
<body>

<header class="site-head">
  <div class="wrap">
    <img class="mark" src="/assets/wixstatic/logo.jpg" alt="" width="42" height="42">
    <a class="name" href="/">CodifyKids</a>
    <nav aria-label="Main">
      <a href="/">home</a>
      <a href="/blog-1/"{blogcur}>blog</a>
    </nav>
  </div>
</header>
"""

FOOT = """
<footer class="site-foot">
  <div class="wrap">
    <span class="tag"><b>&lt;/</b>codifykids<b>&gt;</b></span>
    <small>©2018 by CodifyKids.</small>
  </div>
</footer>

</body>
</html>
"""

POSTS = [  # newest first
    {
        "slug": "post/a-new-type-of-camp-fun-with-ai",
        "title": "A New Type Of Camp: Fun With AI",
        "author": "Shreya Sachdev", "date": "Feb 17, 2020", "read": "1 min read",
        "excerpt": "Recently we held a new camp at the Champaign Public Library. It was our first day long camp and was a huge success!",
        "thumb": "/assets/wixstatic/e944205d27_b4defd_995c01b4b08a4659813370ef8acb197e_mv2.jpg",
        "body": """
<p>Recently we held a new camp at the Champaign Public Library. It was our first day long camp and was a huge success! The camp, Fun With AI, was funded by a 1000 dollar grant from a nonprofit founded by Stanford, AI4ALL, of which I am an ambassador of, centered around educating and exciting students about the field of Artificial Intelligence. Fun With AI targeted middle school girls, and throughout the day, they learned about the basics of AI, how algorithms work, the dangers and advantages of self driving cars, heard from speaker Aravinda Garimella, Assistant Professor of Business Administration at UIUC, built self driving cars, competed with them, and much more. Not to mention we all had pizza :). Judging by the girls involvement and their end of event surveys, they seemed to really enjoy the event and we loved having them as well. The event was even covered by WCIA's Karina Rubio, and was also shown on the 9:00 news, and their website.</p>
<p>Here are some photos of the event:</p>
<figure><img src="/assets/wixstatic/e944205d27_b4defd_995c01b4b08a4659813370ef8acb197e_mv2.jpg" alt="Group photo of Fun With AI campers" loading="lazy"><figcaption>Group pic!</figcaption></figure>
<figure><img src="/assets/wixstatic/03a3a825e3_b4defd_ce39b2a1d01440509720a84e06380ae1_mv2.jpg" alt="Campers competing with their smart cars" loading="lazy"><figcaption>Competition time!</figcaption></figure>
<figure><img src="/assets/wixstatic/27fa48895b_b4defd_e70f78f04dd34f8295452c75ffb6dbed_mv2.jpg" alt="Campers learning and playing" loading="lazy"><figcaption>A little learning, a little play :)</figcaption></figure>
<figure><img src="/assets/wixstatic/a669caa4db_b4defd_eab643663dc94dee9313af307de1c28b_mv2.jpg" alt="A team coding and building their smart car" loading="lazy"><figcaption>One of the teams in the process of coding and building their smart car.</figcaption></figure>
""",
    },
    {
        "slug": "post/2020/01/06/new-camp-at-the-champaign-public-library",
        "title": "New Camp at the Champaign Public Library!",
        "author": "Aryan Sachdev", "date": "Jan 6, 2020", "read": "1 min read",
        "updated": "Updated: Feb 2, 2020",
        "excerpt": "On February 15, we will be hosting a camp at the Champaign Public Library. It will be a just girls camp called Fun with AI!",
        "thumb": None,
        "body": """
<p>On February 15, we will be hosting a camp at the <a class="body-link" href="https://champaign.org/event/fun-with-ai-3864326">Champaign Public Library</a>. It will be a just girls camp called Fun with AI! We created this camp in hopes to broaden girls' horizons about what AI is and how it will help the world in the future, and how it impacts our daily lives. We will not be teaching the regular CS First curriculum, but a different AI centered curriculum. We purchased 650 dollars worth of LittleBits supplies for the camp, but we could not ever do this without our sponsor for this camp. <a class="body-link" href="http://ai-4-all.org/">AI4ALL</a> sportingly agreed to grant us 925 dollars to use for the camp. Of course, we are a nonprofit camp, so the rest of the funds went to buying t-shirts and other miscellaneous items that we needed to make this camp possible. Thanks, and we hope you can make it!</p>
""",
    },
    {
        "slug": "post/2018/10/28/three-camps-down-many-more-to-go",
        "title": "Three Camps Down, Many More to Go!",
        "author": "Shreya Sachdev", "date": "Oct 28, 2018", "read": "1 min read",
        "excerpt": "Codify Kids has just completed their 3rd camp! This time we based our camp off of the CS First curriculum, Music and Sound.",
        "thumb": None,
        "body": """
<p>Codify Kids has just completed their 3rd camp! This time we based our camp off of the CS First curriculum, Music and Sound. We had 3 participants and we all had a great time. We raised $160 and we are well on our way to our goal of raising $2000 by the end of the year! Our camp this session was all about how computers are used to generate music in this day and age, and how we can use animation, music, and variables, among other things, to make our own music videos. By the end of the camp each student had six completed projects including a music video, and a music art piece that they made all on their own! We can't wait for the next camp which will be held next week!</p>
""",
    },
    {
        "slug": "post/2018/10/27/our-hard-work-was-noticed",
        "title": "Our Hard Work Was Noticed!",
        "author": "Shreya Sachdev", "date": "Oct 27, 2018", "read": "1 min read",
        "excerpt": "During our second camp, we found out that the local news station found out about our camp! WCIA news decided to have a section on us.",
        "thumb": None,
        "body": """
<p>During our second camp, another Code in Art camp, we found out that the local news station found out about our camp! WCIA news had heard about us from people who work with the charity our funds go to, Feeding Our Kids, and decided to have a section on us! It was so exciting to hear that now we could help even more people after word got out! WCIA news sent over reporters to our house and they interviewed one of our Gurus, Shreya Sachdev, and recorded part of our class.</p>
<p>Here's the section from the news:</p>
<div class="embed"><iframe src="https://www.youtube.com/embed/0g_7fNoyuSM" title="WCIA 3 news segment on Codify Kids" loading="lazy" allowfullscreen></iframe></div>
""",
    },
    {
        "slug": "post/2016/05/08/finding-support-and-help-how-your-community-can-make-a-difference",
        "title": "Our First Success!",
        "author": "Shreya Sachdev", "date": "Aug 16, 2018", "read": "1 min read",
        "excerpt": "Here is a picture of our first Codify Kids session. We raised $160 for Feeding Our Kids! YAAY!",
        "thumb": "/assets/wixstatic/ac08a2a263_b4defd_482d8f0b139b4379a8100d11831010d6_mv2.jpg",
        "body": """
<p>Here is a picture of our first Codify Kids session. We went through two topics from Google CS First Arts curriculum in scratch and we did some team building activities to get to know each other. We raised $160 for Feeding Our Kids! YAAY!</p>
<figure><img src="/assets/wixstatic/ac08a2a263_b4defd_482d8f0b139b4379a8100d11831010d6_mv2.jpg" alt="Campers at the first Codify Kids session" loading="lazy"></figure>
<p class="hashtags">#community&ensp;#team</p>
""",
    },
]


def post_page(p, prev_p, next_p):
    path = "/" + p["slug"] + "/"
    meta_extra = f' · <span>{p["updated"]}</span>' if p.get("updated") else ""
    nav_items = []
    if next_p:  # newer
        nav_items.append(f'<a class="btn" href="/{next_p["slug"]}/">&larr; {next_p["title"]}</a>')
    nav_items.append('<a class="btn" href="/blog-1/">All posts</a>')
    if prev_p:  # older
        nav_items.append(f'<a class="btn" href="/{prev_p["slug"]}/">{prev_p["title"]} &rarr;</a>')
    return (
        HEAD.format(title=p["title"], desc=p["excerpt"], path=path, blogcur="")
        + f"""
<main>
<div class="article-head">
  <div class="wrap">
    <section style="padding-bottom:0">
      <span class="tag eyebrow"><b>&lt;</b>post<b>&gt;</b></span>
      <h1 style="max-width:22ch">{p["title"]}</h1>
      <p class="meta">{p["author"]} · {p["date"]} · {p["read"]}{meta_extra}</p>
    </section>
  </div>
</div>
<article class="body">
  <div class="wrap">
{p["body"].strip()}
  </div>
</article>
<div class="wrap">
  <nav class="post-nav" aria-label="Post navigation" style="padding:2.5rem 0">
    {'  '.join(nav_items)}
  </nav>
</div>
</main>
"""
        + FOOT
    )


def blog_index():
    rows = []
    for p in POSTS:
        href = "/" + p["slug"] + "/"
        img = (f'<a href="{href}" tabindex="-1" aria-hidden="true"><img src="{p["thumb"]}" alt="" loading="lazy"></a>'
               if p["thumb"] else "")
        cls = "post-row" + ("" if p["thumb"] else " no-thumb")
        rows.append(f"""      <div class="{cls}">
        {img}
        <div class="pad">
          <div class="meta">{p["date"]} · {p["author"]} · {p["read"]}</div>
          <h3><a href="{href}">{p["title"]}</a></h3>
          <p>{p["excerpt"]}</p>
        </div>
      </div>""")
    body = f"""
<main>
<section class="light" style="min-height:60vh">
  <div class="wrap">
    <span class="tag eyebrow"><b>&lt;</b>blog<b>&gt;</b></span>
    <h2>All Posts</h2>
    <div class="post-list">
{chr(10).join(rows)}
    </div>
  </div>
</section>
</main>
"""
    return (HEAD.format(title="Blog | CodifyKids",
                        desc="News and camp reports from CodifyKids in Champaign, IL.",
                        path="/blog-1/", blogcur=' aria-current="page"') + body + FOOT)


(DOCS / "blog-1").mkdir(exist_ok=True)
(DOCS / "blog-1" / "index.html").write_text(blog_index(), encoding="utf-8")
print("wrote blog-1/index.html")
for i, p in enumerate(POSTS):
    newer = POSTS[i - 1] if i > 0 else None
    older = POSTS[i + 1] if i < len(POSTS) - 1 else None
    out = DOCS / p["slug"] / "index.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(post_page(p, older, newer), encoding="utf-8")
    print("wrote", p["slug"])

"""One-time generator for the logan-burns-site static pages.

Outputs plain HTML to C:/Claude/Projects/logan-burns-site. Journal post text is
migrated VERBATIM from the Wix e-portfolio (captured 7/30/26).
"""
import html
import os

ROOT = r"C:\Claude\Projects\logan-burns-site"

FONTS = (
    '<link rel="preconnect" href="https://fonts.googleapis.com">'
    '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
    '<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,wght@0,400;0,600;1,400'
    '&family=IBM+Plex+Mono:wght@400;600&family=IBM+Plex+Sans:wght@400;600&display=swap" rel="stylesheet">'
)

FAVICON = (
    '<link rel="icon" href="data:image/svg+xml,'
    "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 16 16'>"
    "<rect width='16' height='16' fill='%2317492e'/>"
    "<rect x='4' y='4' width='8' height='8' fill='none' stroke='%23c47a3c' stroke-width='1.5'/>"
    "<circle cx='8' cy='8' r='1.5' fill='%23c47a3c'/></svg>\">"
)

NAV = [
    ("index.html", "HOME"),
    ("research.html", "RESEARCH"),
    ("coursework.html", "COURSEWORK"),
    ("journal.html", "JOURNAL"),
    ("resume.html", "RESUME"),
]


def page(title, body, current, depth=0):
    prefix = "../" * depth
    current_attr = ' aria-current="page"'
    nav = "\n      ".join(
        f'<a href="{prefix}{href}"{current_attr if href == current else ""}>{label}</a>'
        for href, label in NAV
    )
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="Logan Burns, electrical engineering undergraduate at the University of Florida. Research, projects, and e-portfolio journal.">
{FAVICON}
{FONTS}
<link rel="stylesheet" href="{prefix}assets/css/site.css">
</head>
<body>
<header class="site-header">
  <div class="wrap">
    <a class="brand" href="{prefix}index.html">LOGAN<span class="tick">_</span>BURNS</a>
    <nav class="site-nav">
      {nav}
    </nav>
  </div>
</header>
<main class="wrap">
{body}
</main>
<footer class="site-footer">
  <div class="wrap">
    <span>LOGAN BURNS · ELECTRICAL ENGINEERING · UNIVERSITY OF FLORIDA</span>
    <span>
      <a href="mailto:lburns1@ufl.edu">lburns1@ufl.edu</a> ·
      <a href="tel:+14077739448">(407) 773-9448</a> ·
      <a href="https://github.com/LBurnsUF">GITHUB</a> ·
      <a href="https://www.linkedin.com/in/logan-burns-0a8982321">LINKEDIN</a>
    </span>
  </div>
</footer>
</body>
</html>
"""


def esc(t):
    return html.escape(t, quote=False)


# ---------------------------------------------------------------- journal posts

# Each body block: ("p", text) | ("calc", text) | ("img", filename, caption)
POSTS = [
    {
        "slug": "journal-entry-fall-2024",
        "title": "Journal Entry - Fall 2024",
        "date": "Mar 11, 2025",
        "sort": "2025-03-11",
        "excerpt": "Getting into the swing of college has been a relatively smooth transition.",
        "blocks": [
            ("p", "Getting into the swing of college has been a relatively smooth transition. A lot has gone on, both academically and personally. Surprisingly (or perhaps unsurprisingly), I have come to find enjoyment in the responsibilities and obligations that come with living alone. The mundanity that comes with maintaining an apartment, the moderate distance to classes, the control that comes with rigorously managing my own schedule; these things all leave me plenty of time to think, a little bit of time to relax, and most importantly, enough time to study and truly learn the material that interests me. My biggest struggle this past fall was definitely unforeseen: developing acute myocarditis after contracting the Flu. It prevented any physical activity or exercise for the better part of 4 months, and limited how much I was permitted to traverse campus on foot. This didn't hamper my learning of course, and I have thankfully since made a (presumably) full recovery. MRI in July, so we shall see!"),
        ],
    },
    {
        "slug": "r-c-poster-presentation",
        "title": "R&C Poster Presentation",
        "date": "Dec 16, 2024",
        "sort": "2024-12-16",
        "excerpt": "Presented at the URSP poster symposium as the final project for the HUM2930 Research and Creativity course.",
        "blocks": [
            ("img", "rc-poster.jpg", "Research outline poster: the health effects of Cannabis across various health factors."),
            ("p", "Presented a research outline for the study of the health effects of Cannabis based on various health factors."),
            ("p", "Presented at the URSP poster symposium on Monday, Dec. 4th, as the final project for the HUM2930 Research and Creativity Course. While unrelated to my primary areas of interest, diving into the currently available research on Cannabis was definitely intriguing, as a surprisingly small amount of rigorous study has been conducted despite its rising popularity for recreational use."),
        ],
    },
    {
        "slug": "spring-undergraduate-research-symposium",
        "title": "Spring Undergraduate Research Symposium",
        "date": "Apr 26, 2025",
        "sort": "2025-04-26",
        "excerpt": "The poster we presented at the Spring Undergraduate Research Symposium on April 8th.",
        "blocks": [
            ("img", "symposium-poster-photo.jpg", "Poster presented at the Spring Undergraduate Research Symposium, April 8th, with my classmate Rohan."),
            ("p", "Pictured above is the poster we presented at the Spring Undergraduate Research Symposium on April 8th with my classmate, Rohan."),
            ("p", "Our poster contained the results of our statistical analysis on usage trends and perspectives held by Senior students on LLM usage in educational settings, specifically as an agent of assisting in assignment completion. While not directly associated with my major, it definitely opened my eyes to the versatility and value of statistical analysis in identifying trends and shifts in subject perspectives. I have enjoyed my time working with Dr. Wayne Giang this semester, and I wish his lab the best."),
            ("p", '<a href="../assets/doc/spring-2025-symposium-poster.pdf">Download the poster PDF (557 KB)</a>'),
        ],
    },
    {
        "slug": "journal-entry-spring-2025",
        "title": "Journal Entry - Spring 2025",
        "date": "May 1, 2025",
        "sort": "2025-05-01",
        "excerpt": "Signals and Systems was a VERY informative course, and I got to meet Dr. Koppal.",
        "blocks": [
            ("p", "This semester was much of the same as last fall, balancing coursework with typical life responsibilities. My biggest struggle this past spring was definitely managing a heavier course load, although I greatly enjoyed the content covered. Signals and Systems was a VERY informative course, and I got to meet Dr. Koppal, whose lab I am interested in joining. I enjoyed the math behind digital signal processing, although I would probably find analog filtering more interesting. My CURE course was interesting, though Industrial Engineering is definitely not my cup of tea."),
            ("img", "fft-butterfly.png", "Decimation-in-time FFT butterfly: two N/2-point DFTs recombined."),
        ],
    },
    {
        "slug": "summer-process-lab-week-1-5-19",
        "title": "Summer Processing Lab: Week 1 (5/19)",
        "date": "May 19, 2025",
        "sort": "2025-05-19",
        "excerpt": "Hands-on experience with the fundamental techniques of MOS capacitor manufacturing.",
        "blocks": [
            ("p", "I am participating in the Semiconductor Readiness Organization's Summer Processing Lab. We are gaining hands-on experience with the fundamental techniques that go into Metal Oxide Semiconductor (MOS) capacitor manufacturing. We are not using cleanroom procedures, so our results are expected to be nothing remarkable, but it is great experience regardless."),
            ("p", "During our first session, we covered the general procedures and techniques we will be using throughout the summer, and grew the Silicon Oxide layer on our wafers."),
            ("p", "Using the tube furnace at 1000C, we conducted a cycle of dry growth on 4 of the wafers, demarked dry, and wet growth on the remaining 4 wafers, also labelled."),
            ("img", "lab1-tube-furnace.jpg", "Tube Furnace."),
            ("img", "lab1-wafers.jpg", 'Silicon Wafers, P-type, 2". (outer edges are dummy wafers)'),
        ],
    },
    {
        "slug": "summer-processing-lab-week-2-6-9",
        "title": "Summer Processing Lab: Week 2 (6/9)",
        "date": "Jun 9, 2025",
        "sort": "2025-06-09",
        "excerpt": "Photoresist types, spin-coating thickness, and exposure with the Karl Suss 505 Mask Aligner.",
        "blocks": [
            ("p", "This lab session focused exclusively on the different types of photoresist, the characteristics that determine the thickness of a spin coating, and the proper procedure for exposure with the Karl Suss 505 Mask Aligner. We practiced focusing and spinning throughout this session."),
            ("p", "We are using AV1512 photoresist, which works well due to its low viscosity, giving an estimated 1.2 \u03bcm coating after spinning @ 4000 rpm for 60 seconds. Our largest features are massive compared to what this aligner is capable of, measuring in at 100 \u03bcm, but I wanted to see how what feature resolution we are capable of with the resolution mask."),
            ("p", "Our best run was a bit disappointing, reaching only ~5 \u03bcm precision. Lines were cleanly resolved, but dot matrices were lost at or below 3 \u03bcm. Focal issues seemed to be a consistent issue, likely due to only achieving soft contact between the mask and wafer."),
            ("img", "lab2-1.jpg", ""),
            ("img", "lab2-2.jpg", "Microscope view of the 10 \u03bcm calibration exposure."),
        ],
    },
    {
        "slug": "summer-processing-lab-week-3-6-16",
        "title": "Summer Processing Lab: Week 3 (6/16)",
        "date": "Jun 16, 2025",
        "sort": "2025-06-16",
        "excerpt": "Completing the initial mask exposure, with dose calculated via transfer-matrix stack reflectivity.",
        "blocks": [
            ("p", "This week marks the completion of the initial mask exposure for our MOSCAP manufacturing process. We further calibrated our exposure time based on observed results, experimental data collected online, and the measured radiance of our lamp."),
            ("calc", "D = b * D0 * (1 + R_eff*e^(-\u03b1T)) | Levinson, Harry J. Principles of Lithography, 4th Ed.\n\nParameters:\n60-80nm SiO2 ~ 70nm = 7 * 10^-8\n4000rpm for 60 sec with AV1512 -> ~1.2 \u00b5m\n2 minute post bake | b = 0.9, slightly increases solubility change - \"Principles of Lithography\" (H. J. Levinson, SPIE Press)\nabsorption (\u03b1): ~0.45\nD_0: 75 mJ/cm^2 based on experimental resolution falloff.\n\nThompson, L. F., Willson, C. G., & Bowden, M. J. (1994). Introduction to microlithography. American Chemical Society."),
            ("calc", "Full Stack Reflectivity via Transfer Matrix Method:\n\nReff = ((r_12 + r_23 * e^(4i * pi * n_2 * d/\u03bb)/(1 + r_12 * r_23 * e^(4i * pi * n_2 * d/\u03bb))^2\n\nn_1 = n_resist = 1.7\nn_2 = n_SiO\u2082 = 1.46\nn_3 = n_Si = |3.8 + 0.02i| ~ 3.80\n\nFresnel reflection coefficients:\nr_12 = (n_1 - n_2)/(n_1 + n_2) = (1.7 - 1.46)/(1.7 + 1.46) = 0.07595\nr_23 = (n_2 - n_3)/(n_2 + n_3) = (1.46 - 3.80)/(1.46 + 3.80) = -0.44487\n\nReff = ((0.07595 - 0.44487 * e^(4i * pi * 1.46 * 7 * 10^-8/400nm)/(1 - 0.07595 * 0.44487 * e^(4i * pi * 1.46 * 7 * 10^-8/400nm))^2\n     = (0.5198 + 0.0307i)/(1.0337 + 0.0023i))^2 = 0.2537\n\nD = 0.9 * 75 mJ/cm^2 * (1 + 0.2537*e^(-0.55 * 10^6 * 1.2 * 10^-6))\nD = 0.9 * 75 mJ/cm^2 * (1 + 0.2537*e^(-0.54))\nD = 0.9 * 75 * (1.13112518) = 76.35095\n\nt = 76.35095/E\n76.35095/9.1 = ~8.4 sec"),
            ("p", "We observed significant interference fringes under the microscope after exposure, which may indicate the following issues: insufficient contact, residual moisture due to insufficient drying, photoresist edge beading."),
            ("img", "lab3-fringes.jpg", ""),
            ("p", "Going forward, I would recommend an acetone swab along the outer edge before the post bake to remove excess photoresist in noncritical areas to improve exposure contact, to eliminate the risk of beading."),
        ],
    },
    {
        "slug": "summer-processing-lab-week-4-6-30",
        "title": "Summer Processing Lab: Week 4 (6/30)",
        "date": "Jun 30, 2025",
        "sort": "2025-06-30",
        "excerpt": "Wet and dry etch of the first MOSCAP layer, with etch times computed from measured oxide thickness.",
        "blocks": [
            ("p", "This week marks the completion of the etching process for the first layer of our MOSCAPs. We calculated our etch times based on observed results from our peers, experimental data collected online, and the average thickness of our SiO2 layers across dry and wet oxide growth groups."),
            ("calc", "Wet Etch to remove SiO2 on areas devoid of features:\n\nParameters:\nWet samples SiO2 thickness: 64.59 nm average.\nDry samples SiO2 thickness: 97.01 nm average.\nWet etch agent: UN2817 Ammonium Hydrogen Difluoride, Solution, 8 (6.1).\nBOE Thermally grown SiO2 Etch Rate: ~800 \u00c5/min @ 25 \u00b0C -> 80 nm/min.\n\nTime_w = (64.59 nm)/(80 nm/min) = 0.807375 min * 60 sec/min ~ 48 sec\nTime_d = (97.01 nm)/(80 nm/min) = 1.212625 min * 60 sec/min ~ 73 sec"),
            ("calc", "Selective Si dry etch:\n\nParameters:\nPlasma Mixture: 0.300 SCCM SF6/0.300 SCCM Ar\nPressure: 20 mTorr w/ turbo\nForward power: 250 Watts\nReflected power: 4.6 Watts\nEtch rate SiO2: ~102 nm/min from peer results\n\nTime = (200 nm)/(102 nm/min) = 1.96078431 min * 60 sec/min ~ 118 sec."),
            ("img", "lab4-1.png", ""),
            ("img", "lab4-2.png", ""),
            ("p", "After the dry etch, we used the stylus profilometer to measure the Si etch depth. We observed significantly lower Si etch depth than expected, ~75nm rather than the planned 200nm, which indicates that we etched too many wafers at a time, reducing power density. We did not account for the power density reduction due to multiple wafers. This will be a consideration going forward."),
        ],
    },
    {
        "slug": "summer-processing-lab-week-5-6-7-7-7-14",
        "title": "Summer Processing Lab: Week 5/6 (7/7 & 7/14)",
        "date": "Jul 14, 2025",
        "sort": "2025-07-14",
        "excerpt": "Second mask exposure, recalibrated with nLOF 2035 resist and per-group stack reflectivity.",
        "blocks": [
            ("p", "This week marks the completion of the second mask exposure for our MOSCAP manufacturing process. We further calibrated our exposure time based on observed results from the first layer, Manufacturer datasheets for estimated reflectivity, and the measured radiance of our lamp."),
            ("calc", "D = D0 * (1 + R_eff*e^(-\u03b1T)) | Levinson, Harry J. Principles of Lithography, 4th Ed.\n\nParameters:\n60-80nm SiO2 ~ 70nm = 7 * 10^-8\n4000rpm for 60 sec with nLOF 2035 -> ~3.5 \u00b5m\n2.5 minute post spin bake\n1 minute post exposure bake\nD_0: 75 mJ/cm^2 based on experimental resolution falloff.\nlamp power: 8.55 mW/cm^2\n\nThompson, L. F., Willson, C. G., & Bowden, M. J. (1994). Introduction to microlithography. American Chemical Society."),
            ("calc", "Full Stack Reflectivity via Transfer Matrix Method:\n\nReff = ((r_12 + r_23 * e^(4i * pi * n_2 * d/\u03bb)/(1 + r_12 * r_23 * e^(4i * pi * n_2 * d/\u03bb))^2\n\nRefraction Constants:\nn_1 = n_resist = 1.64\nn_2 = n_SiO\u2082 = 1.46\nn_3 = n_Si = |3.8 + 0.02i| ~ 3.80\n\nFresnel reflection coefficients:\nr_12 = (n_1 - n_2)/(n_1 + n_2) = (1.64 - 1.46)/(1.64 + 1.46) = 0.0580645161\nr_23 = (n_2 - n_3)/(n_2 + n_3) = (1.46 - 3.80)/(1.46 + 3.80) = -0.44487\n\nReff_wet = ((0.058 - 0.44487 e^(4i pi 1.46 * 6.459/40))/(1 - 0.0258 * e^(4i * pi * 1.46 * 6.459/40)))^2 = 0.2398\nReff_dry = ((0.058 - 0.44487 * e^(4i * pi * 1.46 * 9.701/40))/(1 - 0.0258 * e^(4i * pi * 1.46 * 9.701/40)))^2 = 0.2117"),
            ("calc", "Dosage Calculations:\nD_wet = 75 * (1 + 0.2117*e^(-0.55 * 10^6 * 3.25 * 10^-6)) = 77.6575 mJ/cm^2\nD_dry = 75 * (1 + 0.2398*e^(-0.55 * 10^6 * 3.25 * 10^-6)) = 78.0103 mJ/cm^2\n\nExposure Time Calculations:\nt_wet = (77.6575 mJ/cm^2)/(8.55 mW/cm^2) = 9.08274854 seconds\nt_wet = (78.0103 mJ/cm^2)/(8.55 mW/cm^2) = 9.1240117 seconds"),
        ],
    },
    {
        "slug": "summer-processing-lab-week-7-7-21",
        "title": "Summer Processing Lab: Week 7 (7/21)",
        "date": "Jul 21, 2025",
        "sort": "2025-07-21",
        "excerpt": "Physical vapor deposition of aluminum contacts via thermal vaporization at ~3 \u00b5Torr.",
        "blocks": [
            ("p", "This week marks the Physical Vapor Deposition (PVD) of aluminum onto the freshly exposed wafers, using thermal vaporization. This provides the contact areas to the capacitor surfaces. This was conducted at ~3 \u00b5Torr, using a Tungsten boat to melt the Aluminum, with current ranging from 80-180 Amperes. The amperage was increased by 5 every 15 seconds until the aluminum sample was completely vaporized."),
            ("img", "lab7-pvd.jpg", "PVD Setup."),
        ],
    },
    {
        "slug": "summer-processing-lab-week-8-7-28-7-31",
        "title": "Summer Processing Lab: Week 8 (7/28 & 7/31)",
        "date": "Jul 31, 2025",
        "sort": "2025-07-31",
        "excerpt": "Metal lift-off, annealing at 550C, and electrical characterization of the finished MOSCAPs.",
        "blocks": [
            ("p", "This week marks the completion of the Summer Processing lab. We use MLO-07 Stripper to remove the excess deposited aluminum across the wafers, preparing them for Annealing."),
            ("img", "lab8-1.jpg", "Metal Lift-off via MLO-07."),
            ("img", "lab8-2.jpg", "Sample 200 \u00b5m MOSCAP (before annealing)."),
            ("p", "We then bake the wafers at 550C for 5 minutes to improve Ohmic Junction behavior. Reactions between the Aluminum and Silicon Oxide along the junction boundary form elemental Silicon and Aluminum Oxide, via the following reaction: 4Al + 3SiO2 -> 2Al2O3 + 3Si. The following testing was then conducted to analyze the resulting junction behavior."),
            ("img", "lab8-3.jpg", "SiO2 Al Junction Behavior. Near-Ohmic behavior is observed."),
            ("img", "lab8-4.jpg", "Breakdown Voltage testing of annealed sample. Occurs at ~30 volts."),
        ],
    },
    {
        "slug": "journal-entry-fall-2025",
        "title": "Journal Entry - Fall 2025",
        "date": "Dec 12, 2025",
        "sort": "2025-12-12",
        "excerpt": "Digital Logic and Microprocessor Applications, an REU with Dr. Koppal, and a crude polyphonic synthesizer.",
        "blocks": [
            ("p", "This semester was much of the same as last Spring, balancing coursework with typical life responsibilities. I got to take Digital Logic (EEL3701C) over the summer, and Microprocessor Applications (4744C) this fall, which were two courses I GREATLY enjoyed. I believe I contributed moderately to the course, as I held multiple tutoring sessions, and often explained concepts to my classmates. HDL languages will be fun to learn, and I want to learn pipelining since we only made the most basic, unpipelined MIPS processor. I got to meet Dr. Schwartz, whose lab I am interested in joining. I also got an REU with Dr. Koppal, although I haven't contributed much to the lab as of writing. I would like to work on the FoveaCam, but that is unlikely. I made a crude polyphonic synthesizer on the ATxmega128A1U, which was a fun exercise. Without compiler optimization, it can handle 3-4 notes simultaneously, didn't feel like unrolling loops for minimal gains so there is probably still performance on the table, but it works so I don't really care. Fun times overall!"),
            ("img", "synth-scope.png", "The synthesizer's ASCII oscilloscope, streamed over serial to PuTTY."),
        ],
    },
    {
        "slug": "journal-entry-spring-2026",
        "title": "Journal Entry - Spring 2026",
        "date": "May 15, 2026",
        "sort": "2026-05-15",
        "excerpt": "Circuits 2 with Dr. Sheplak, peer instructing, MIL, and building EdgeTrain in the FOCUS Lab.",
        "blocks": [
            ("p", "This semester, I got to take Circuits 2 with Dr. Sheplak, a course I REALLY REALLY enjoyed. The techniques and intuition we learned are invaluable, and will undoubtedly apply for my entire career. Bode plots were an unintuitive mess before this course, as were Thevenin/Norton Equivalents. Not the case anymore! Also got to take EEE3308C, where I got to learn about MOS circuits, Op-Amp internals, and the design tradeoffs that go into all such circuits, although our coverage of these topics was surface-level. I also got to be a PI for both EEL3701C and EEL4744C under Dr. Schwartz, where I got to teach many students the underlying intuition of digital design concepts, how to break down problems, and the value of mixed logic circuits in reducing complexity. I was also a member of the Machine Intelligence Laboratory (MIL) this Semester, where I designed the leak detector for the Sub. I am now working with Mehran in the FOCUS Lab under Dr. Koppal. This semester we built EdgeTrain, a runtime framework that lets mobile robots learn continuously on edge GPUs without overheating. The core discovery is that different continual learning algorithms heat the chip in measurably different ways, so algorithm choice itself becomes a thermal control knob alongside GPU frequency and batch size. We validated it on a Jetson Orin NX under an infrared heat lamp, showed that thermal throttling doesn't corrupt learned weights."),
            ("img", "leak-detector-pcb.png", "SubjuGator 9 leak detector, 3D render of the v2 layout."),
        ],
    },
]


def render_post(post):
    parts = [f'<article class="post">']
    parts.append(f'<div class="when">{post["date"].upper()}</div>')
    parts.append(f"<h1>{esc(post['title'])}</h1>")
    for block in post["blocks"]:
        if block[0] == "p":
            text = block[1]
            body = text if text.lstrip().startswith("<a ") else esc(text)
            parts.append(f"<p>{body}</p>")
        elif block[0] == "calc":
            parts.append(f'<pre class="calc">{esc(block[1])}</pre>')
        elif block[0] == "img":
            cap = f"<figcaption>{esc(block[2])}</figcaption>" if block[2] else ""
            parts.append(
                f'<figure><img src="../assets/img/{block[1]}" alt="{esc(block[2]) or esc(post["title"])}" loading="lazy">{cap}</figure>'
            )
    parts.append("</article>")
    parts.append('<div class="post-nav"><a href="../journal.html">&larr; ALL JOURNAL ENTRIES</a></div>')
    return "\n".join(parts)


# ---------------------------------------------------------------- static pages

INDEX_BODY = """
<section class="hero">
  <div class="reveal">
    <div class="hero-kicker">ELECTRICAL ENGINEERING · UNIVERSITY OF FLORIDA · CLASS OF 2028</div>
    <h1><span style="white-space:nowrap">I like building hardware</span><br><em>and knowing exactly why it works.</em></h1>
    <p class="lede">I'm Logan, an EE undergraduate at the University of Florida. I design and fabricate hardware, build the firmware that drives it, and do research on thermal-aware computing for mobile robots in the FOCUS Lab.</p>
    <div class="hero-links">
      <a href="mailto:lburns1@ufl.edu">EMAIL</a>
      <a href="https://github.com/LBurnsUF">GITHUB</a>
      <a href="https://www.linkedin.com/in/logan-burns-0a8982321">LINKEDIN</a>
      <a href="resume.html">RESUME</a>
    </div>
  </div>
  <div class="portrait reveal"><img src="assets/img/leak-detector-pcb.png" alt="SubjuGator 9 leak detector PCB, designed by Logan Burns"></div>
</section>

<section class="block">
  <div class="sec-label">&sect;01 / ABOUT</div>
  <h2 class="sec-title">Critical thought, deliberative discussion.</h2>
  <p style="color:var(--ink-soft)">I value critical thought and deliberative discussion to solve problems, regardless of the area of focus. My interest in electrical engineering grew from taking apart computer hardware, an incurable curiosity about how devices work, and a learning environment that encouraged chasing that curiosity. These days it points at analog and mixed-signal circuits, power electronics, VLSI, and optical sensing.</p>
</section>

<section class="block">
  <div class="sec-label">&sect;02 / SELECTED WORK</div>
  <h2 class="sec-title">Things I've built.</h2>
  <div class="cards">
    <div class="card">
      <img src="assets/img/flir-thermal-rig.jpg" alt="FLIR thermal camera on a tripod imaging a Jetson robot platform, live thermal view on a laptop">
      <div class="meta">FOCUS LAB · MANUSCRIPT IN REVISION</div>
      <h3>EdgeTrain</h3>
      <p>Thermal-adaptive continual learning for robot-mounted edge GPUs. I built the thermal instrumentation: a calibrated FLIR imaging pipeline, a 150 W radiant-heat rig, and the DVFS characterization behind the paper's central claims.</p>
      <p style="margin-top:0.6rem"><a class="more" href="research.html">RESEARCH &rarr;</a></p>
    </div>
    <div class="card">
      <img src="assets/img/leak-detector-pcb.png" alt="SubjuGator 9 leak detector PCB render">
      <div class="meta">MIL · SUBJUGATOR 9 AUV</div>
      <h3>Leak Detector</h3>
      <p>Water-ingress detection board for UF's autonomous submarine: LTspice comparator front end through Altium layout to fabrication release.</p>
    </div>
    <div class="card">
      <img src="assets/img/synth-scope.png" alt="ASCII oscilloscope output from the AVR synthesizer">
      <div class="meta">PERSONAL · BARE-METAL AVR</div>
      <h3>Wavetable Synthesizer</h3>
      <p>3-voice polyphonic synth on an ATxmega128A1U: ping-pong DMA audio, inline-assembly mixing, and a live serial oscilloscope. <a href="https://youtu.be/gx8KwXzQoUY">Demo video</a>.</p>
    </div>
  </div>
</section>

<section class="block">
  <div class="sec-label">&sect;03 / RESEARCH INTERESTS</div>
  <h2 class="sec-title">Interests.</h2>
  <div class="cards">
    <div class="card"><h3>Analog &amp; mixed-signal</h3><p>Amplifier and regulator design, loop stability, data converters.</p></div>
    <div class="card"><h3>Power electronics</h3><p>Regulation, protection, MOSFET switching, power integrity.</p></div>
    <div class="card"><h3>VLSI circuits</h3><p>Analog IC design coursework at the graduate level, headed toward tapeout skills.</p></div>
    <div class="card"><h3>Optical sensing &amp; photonics</h3><p>Thermal imaging, foveated and computational sensors.</p></div>
  </div>
</section>
"""

RESEARCH_BODY = """
<section class="block">
  <div class="sec-label">&sect;01 / POSITIONS</div>
  <h2 class="sec-title">Research</h2>

  <div class="entry">
    <div class="when">SEP 2025 &ndash; PRESENT</div>
    <div>
      <h3>Florida Optics and Computational Sensor (FOCUS) Lab</h3>
      <div class="role">UNDERGRADUATE RESEARCH ASSISTANT · PI: DR. SANJEEV KOPPAL · UF ECE</div>
      <ul>
        <li><strong>EdgeTrain:</strong> co-authored a thermal-adaptive continual-learning controller for robot-mounted edge GPUs; the manuscript is in revision for conference resubmission. Built the thermal instrumentation and evidence base: calibrated FLIR A6751sc imaging pipeline, 150 W radiant-heat stress rig, per-rail power telemetry, and DVFS characterization on a Jetson Orin NX.</li>
        <li><strong>Virtual thermal sensing:</strong> sole author of a system that predicts temperatures of off-die board components (VRM inductors, MOSFETs) from on-die telemetry alone, via thermal response mapping and lumped-capacitance model fitting; a real-time daemon needs no camera after a one-time calibration. Across a 32-configuration DVFS and load sweep, the model predicts 16 board hotspots to 0.34&nbsp;&deg;C mean absolute error on operating points held out of the fit.</li>
      </ul>
    </div>
  </div>

  <div class="entry">
    <div class="when">JAN 2026 &ndash; MAY 2026</div>
    <div>
      <h3>Machine Intelligence Laboratory (MIL)</h3>
      <div class="role">ELECTRICAL TEAM · SUBJUGATOR 9 AUV · UF ECE</div>
      <ul>
        <li>Sole designer of the vehicle's leak-detection subsystem: comparator front end simulated in LTspice, Altium schematic capture and 2-layer layout, fabrication-released v2 with full manufacturing outputs.</li>
      </ul>
    </div>
  </div>

  <div class="entry">
    <div class="when">JAN 2025 &ndash; APR 2025</div>
    <div>
      <h3>Human Systems Engineering Lab</h3>
      <div class="role">UNDERGRADUATE RESEARCH ASSISTANT · PI: DR. WAYNE GIANG · UF ISE</div>
      <ul>
        <li>Human factors and human-automation interaction: data collection for a driving-simulator study with older drivers, and a reproducible R analysis of student perceptions of AI tools in academic contexts, presented at the Spring Undergraduate Research Symposium.</li>
      </ul>
    </div>
  </div>
</section>

<section class="block">
  <div class="sec-label">&sect;02 / MANUSCRIPTS</div>
  <h2 class="sec-title">Publications</h2>
  <p class="pubcite">M. Keivanimehr, <strong>L. Burns</strong>, S. J. Koppal, &ldquo;EdgeTrain: Thermal-Adaptive Continual Learning for Energy-Constrained Mobile Robots,&rdquo; manuscript in revision for conference resubmission, 2026.</p>
</section>
"""

COURSEWORK_BODY = """
<section class="block">
  <div class="sec-label">&sect;01 / COURSEWORK</div>
  <h2 class="sec-title">Semester by semester.</h2>
  <div class="termgrid">
    <div class="term"><h3>FALL 2024</h3><table>
      <tr><td>MAC2313 Calculus 3</td><td class="grade">A</td></tr>
      <tr><td>PHY2048 Physics 1</td><td class="grade">A</td></tr>
      <tr><td>EEL3834 Programming for EE 1</td><td class="grade">A</td></tr>
      <tr><td>IDS2935 Quest</td><td class="grade">A</td></tr>
      <tr><td>HUM2930 Research &amp; Creativity</td><td class="grade">A</td></tr>
    </table></div>
    <div class="term"><h3>SPRING 2025</h3><table>
      <tr><td>EEL3135 Signals &amp; Systems</td><td class="grade">A&minus;</td></tr>
      <tr><td>PHY2049 Physics 2</td><td class="grade">A&minus;</td></tr>
      <tr><td>EEL3000 Intro to EE</td><td class="grade">A</td></tr>
      <tr><td>EGN4912 Research</td><td class="grade">S</td></tr>
      <tr><td>IDS2935 Data Analytics</td><td class="grade">A</td></tr>
    </table></div>
    <div class="term"><h3>SUMMER 2025</h3><table>
      <tr><td>EEL3701C Digital Logic</td><td class="grade">A</td></tr>
      <tr><td>CHM2045 + Lab</td><td class="grade">A</td></tr>
    </table></div>
    <div class="term"><h3>FALL 2025</h3><table>
      <tr><td>EEL4744C Microprocessor Applications</td><td class="grade">A</td></tr>
      <tr><td>EEL3111C Circuits 1</td><td class="grade">A</td></tr>
      <tr><td>EEL4837 Programming for EE 2</td><td class="grade">A</td></tr>
      <tr><td>MAP2302 Differential Equations</td><td class="grade">A</td></tr>
    </table></div>
    <div class="term"><h3>SPRING 2026</h3><table>
      <tr><td>EEL4712C Digital Design</td><td class="grade">A</td></tr>
      <tr><td>EEE3308C Electronic Circuits 1</td><td class="grade">A</td></tr>
      <tr><td>EEL3112 Circuits 2</td><td class="grade">A</td></tr>
      <tr><td>EGN4912 Research</td><td class="grade">S</td></tr>
    </table></div>
    <div class="term"><h3>SUMMER 2026</h3><table>
      <tr><td>EGN2020C Engineering Design</td><td class="grade">IP</td></tr>
      <tr><td>MAS3114 Computational Linear Algebra</td><td class="grade">IP</td></tr>
    </table></div>
    <div class="term"><h3>FALL 2026 · PLANNED</h3><table>
      <tr><td>EEE5320 Analog IC Design I</td><td class="grade">&ndash;</td></tr>
      <tr><td>EEE3396 Solid-State Devices</td><td class="grade">&ndash;</td></tr>
      <tr><td>EEL4657C Linear Controls</td><td class="grade">&ndash;</td></tr>
      <tr><td>ENC3246 Professional Communication</td><td class="grade">&ndash;</td></tr>
    </table></div>
  </div>
  <p style="margin-top:1.2rem; font-family:var(--mono); font-size:0.8rem; color:var(--ink-soft)">CUMULATIVE GPA 3.91</p>
</section>

<section class="block">
  <div class="sec-label">&sect;02 / ENGAGEMENT</div>
  <h2 class="sec-title">Organizations.</h2>
  <div class="entry">
    <div class="when">SPR 2026 &ndash; PRESENT</div>
    <div><h3>Head Peer Instructor, EEL 3701C &amp; EEL 4744C</h3>
    <div class="role">UF ECE</div>
    <ul><li>Lead the peer-instructor team for both courses: help sessions on EBI memory mapping and digital logic, lab specs and solutions, exam-grading assignments, and the course hardware fleet.</li></ul></div>
  </div>
  <div class="entry">
    <div class="when">SEP 2024 &ndash; PRESENT</div>
    <div><h3>Semiconductor Readiness Organization</h3>
    <div class="role">MEMBER · SUMMER PROCESSING LAB</div>
    <ul><li>Fabricated MOS capacitors at the UF Nanoscale Research Facility: oxidation, photolithography, wet etch, and sputter deposition. Full build log in the <a href="journal.html">journal</a>.</li></ul></div>
  </div>
  <div class="entry">
    <div class="when">2024 &ndash; PRESENT</div>
    <div><h3>IEEE</h3>
    <div class="role">MEMBER</div>
    <ul><li>Student chapter membership and events.</li></ul></div>
  </div>
  <div class="entry">
    <div class="when">2024 &ndash; 2025</div>
    <div><h3>Solar Gators</h3>
    <div class="role">MEMBER</div>
    <ul><li>Solar-vehicle design team membership.</li></ul></div>
  </div>
</section>
"""

RESUME_BODY = """
<section class="block">
  <div class="sec-label">&sect;01 / RESUME</div>
  <h2 class="sec-title">Resume</h2>
  <p style="max-width:40em; color:var(--ink-soft); margin-bottom:1.4rem">Two one-page versions, same record, different emphasis. For project detail beyond a single page, the <a href="research.html">research</a> page and <a href="https://github.com/LBurnsUF">GitHub</a> carry the depth.</p>
  <div class="cards" style="max-width:760px">
    <div class="card">
      <div class="meta">FOR LABS, REUs, RESEARCH POSITIONS</div>
      <h3>Research resume</h3>
      <p>Leads with research experience, manuscripts, and teaching.</p>
      <p style="margin-top:0.8rem"><a class="more" href="assets/doc/logan-burns-research.pdf">DOWNLOAD PDF &darr;</a></p>
    </div>
    <div class="card">
      <div class="meta">FOR INDUSTRY INTERNSHIPS</div>
      <h3>Internship resume</h3>
      <p>Leads with work experience, shipped tooling, and hardware projects.</p>
      <p style="margin-top:0.8rem"><a class="more" href="assets/doc/logan-burns-internship.pdf">DOWNLOAD PDF &darr;</a></p>
    </div>
  </div>
</section>
"""


def journal_index():
    rows = []
    for post in sorted(POSTS, key=lambda p: p["sort"], reverse=True):
        rows.append(
            f'<div class="post-row"><span class="when">{post["date"].upper()}</span>'
            f'<a class="title" href="journal/{post["slug"]}.html">{esc(post["title"])}</a>'
            f"<p>{esc(post['excerpt'])}</p></div>"
        )
    return (
        '<section class="block">\n<div class="sec-label">&sect;01 / JOURNAL</div>\n'
        '<h2 class="sec-title">E-portfolio journal.</h2>\n'
        '<p style="max-width:42em; color:var(--ink-soft); margin-bottom:1.4rem">Semester reflections and the full Summer 2025 '
        "MOSCAP fabrication log, kept as part of the University Research Scholars Program.</p>\n"
        f'<div class="post-list">{"".join(rows)}</div>\n</section>'
    )


def main():
    os.makedirs(os.path.join(ROOT, "journal"), exist_ok=True)
    pages = {
        "index.html": ("Logan Burns | Electrical Engineering", INDEX_BODY, "index.html"),
        "research.html": ("Research | Logan Burns", RESEARCH_BODY, "research.html"),
        "coursework.html": ("Coursework | Logan Burns", COURSEWORK_BODY, "coursework.html"),
        "journal.html": ("Journal | Logan Burns", journal_index(), "journal.html"),
        "resume.html": ("Resume | Logan Burns", RESUME_BODY, "resume.html"),
    }
    for fname, (title, body, current) in pages.items():
        with open(os.path.join(ROOT, fname), "w", encoding="utf-8", newline="\n") as f:
            f.write(page(title, body, current))
    for post in POSTS:
        with open(os.path.join(ROOT, "journal", post["slug"] + ".html"), "w", encoding="utf-8", newline="\n") as f:
            f.write(page(f"{post['title']} | Logan Burns", render_post(post), "journal.html", depth=1))
    print(f"wrote {len(pages)} pages + {len(POSTS)} posts")


if __name__ == "__main__":
    main()

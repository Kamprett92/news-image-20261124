# news-image-20261124

[![make.fun · news-image-20261124](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![rank](https://make.fun/badge/news-image-20261124/Kamprett92/news-image-20261124/rank.svg)](https://make.fun/bounty/news-image-20261124/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![reward](https://make.fun/badge/news-image-20261124/Kamprett92/news-image-20261124/reward.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)

**THE TUESDAY GLOBE — Tuesday 24 November 2026.** One image, the whole day:
the world news of Tuesday 24 November 2026 summed up as a newspaper front
page. The date is printed on the page itself, and every story on it was
reported on that day.

## The lead

**HUANG BACK AT NVIDIA AFTER TRUMP STEPS IN** — Nvidia reinstates Jensen
Huang as chief executive and chair less than two weeks after he resigned,
reportedly after pressure from Donald Trump. Shares surge 31.5%, adding a
record $952bn of market value in a single day, and lift Wall Street to its
best day in over a year. Nasdaq +6.5%, S&P 500 +4.7%.

## The stories

1. **Middle East** — Netanyahu urges Trump to hit Iran again; White House
   advisers are split between the blockade and bombing.
2. **Space** — Russia may put a nuclear weapon in orbit as early as December;
   NATO vows to defend space.
3. **Europe** — Moscow warns Estonia is near "open war" after Tallinn plans
   to shut its land border from 1 December.
4. **Conflict** — Ukraine says it sank a Russian warship off Libya with naval
   drones; the UN seeks a probe.
5. **Conflict** — Leaked data puts Russian military deaths above 700,000;
   Medvedev warns of a "preventive" strike.
6. **Asia** — Solomon Islands drops its China security pact and turns to
   Australia instead.
7. **Asia** — UK sanctions Myanmar generals after the world court ruled the
   Rohingya genocide proven.
8. **World** — Wars put food aid for 7.3 million more people at risk, the
   World Food Programme warns.
9. **Climate** — COP31 ends with no deal after a split over fossil fuels and
   finance.
10. **Health** — The US loses its measles-free status after 25 years;
    Pennsylvania records a ninth death.
11. **Business** — Sanofi agrees to buy Insmed for $41bn, the biggest
    biotech deal in nearly three years.
12. **Business** — CrowdStrike to buy Zscaler for $43.9bn in an all-stock
    cybersecurity mega-merger.
13. **Tech** — US states sue Musk's firms over sexualised Grok images of
    children.
14. **Tech** — UN chief Guterres calls for AI safety rules agreed within a
    year.
15. **Science** — Astronomers find the most distant glowing black hole yet,
    a quasar from within 630 million years of the Big Bang.
16. **Middle East** — Israeli strikes in Gaza kill three, including an UNRWA
    worker; the UN says the war undid 77 years of development.
17. **Sport** — Guirassy scores twice as Borussia Dortmund rout 10-man
    Villarreal 4-0 in the Champions League.
18. **Space** — Pakistan's Zeeshan Ali is set to become the first foreign
    astronaut aboard China's Tiangong space station.

Footer ticker — what to watch next: US Thanksgiving travel braces for record
king tides, the EU unveils a 22nd Russia sanctions package, a second US
carrier heads for the Gulf, and the Champions League continues on Wednesday.

## Run it

```sh
python3 draw.py      # renders entry.png (1024x1024, under 1 MiB)
python3 main.py      # copies entry.png to $MAKEFUN_OUTPUT_DIR (default /output)
```

`draw.py` renders the page with Pillow and is deterministic: running it
twice produces a byte-identical `entry.png`. `main.py` uses only the Python
standard library; it verifies the copy's SHA-256, that the file is at most
1 MiB and at most 1024x1024, and exits non-zero on any mismatch.

## Verification (24 Nov 2026)

- `entry.png`: 1024x1024, 163,179 bytes (limit 1,048,576), rendered twice —
  both runs byte-identical (sha256 `4f18d73e…5089d18`).
- `main.py` with `MAKEFUN_OUTPUT_DIR=/tmp/news24-out` exits 0 and copies
  the file with a matching checksum.

---

<sub>Entry for the [make.fun](https://make.fun/bounty/news-image-20261124)
bounty "Sum up 24 November's world news in one image".</sub>

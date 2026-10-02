# Decision: debate my projecy — cyber_portfolio (hackergovind)

Date: 2026-10-02 | Rounds: R1 (positions) + R2 (critiques) | Voices: chair, pragmatist, skeptic, simplifier, user-advocate

Project: Next.js 15 + React 19 + TS + Tailwind v4 single-page portfolio — Hero + ~/about, ~/skills, ~/projects (4), ~/experience (2), ~/contact. Terminal aesthetic. `lib/data.ts` as content source, `npm run build` passes.

## What was decided and why

**Thesis adopted (R2-chair, as amended): keep the hacker brand, earn it with proof, convert with one path. Sequenced, not stacked.**

### P0 — Stop the bleeding (1 day, no new routes, no new deps)
1. **2 real > 4 fake.** Replace 4x `link: "#"` (`lib/data.ts:41-70`) with max 2 live cards, each GitHub + live demo + 1-line outcome. Rest to `draft: true` / hidden. Unshipped cards render with no `<a>`. Rule going forward: no entry without `link != "#"`. (Unanimous R1+R2; skeptic's "dead click = dead lead" carried.)
   - Keep: this-site (frontend proof) + phish-guard (safely demoable client-side). Park web-vuln-scanner until it has README + abuse guardrails.
2. **De-fluff metrics.** Delete `99.9% secure` from `Hero.tsx:37-49`. Remove `90+ Lighthouse / LCP <2.5s` from UI unless linked to a real PageSpeed run in the same PR. Keep WCAG AA intent in code, not marketing. (Unanimous that unverified numbers destroy trust with technical hirers; pragmatist+simplifier won "cut, don't badge" for v1.1 over chair-R1's CI badge.)
3. **Contact conversion minimum.** Keep `mailto:`, add `resume.pdf` + copy-email button + availability badge (`Open for internships/freelance · IST/Remote`). No form backend. (All R2 agree mailto+resume converts without spam/maintenance cost.)
4. **Mobile nav fix.** `Header.tsx:35-40` hides all links on mobile. Add horizontal-scroll nav or hamburger. (User-advocate catch, uncontested in R2.)

### P1 — Prove + harden (1 week)
5. **Positioning: security-first hybrid, not hedging.** Hero leads "I break web apps, then build them back stronger" — frontend as builder-proof. Dual labels for sections (`About ~/about`), terminal accent kept to Hero only (aria-hidden), body in sans + mono accents. (Pragmatist R2 + user-advocate hierarchy beat skeptic-R1 "pick one lane" and simplifier "plain English only" — niche is the moat.)
6. **Cheap security posture.** `next.config.mjs` headers (CSP, HSTS, X-Frame-Options, X-Content-Type-Options) + `/.well-known/security.txt` + verify domain/`metadataBase` resolves + Vercel Speed Insights on. Demoted from R1-chair P0 to P1 per pragmatist-R2: invisible to users, 30-min work, must not outrank clickable proof. (Skeptic's "secure site must send headers" accepted, reprioritized.)
7. **One proof route.** `/writeups` with 1-2 real redacted CTF/lab writeups (repro steps + mitigations). Proves researcher without bounty-disclosure risk. Creds strip (THM/HTB rank, certs, disclosure count) only with clickable URLs — PNGs without links banned. (Chair/pragmatist/skeptic/user-advocate majority over simplifier's "no writeups in v1.1".)
8. **ProjectCard redesign.** Add problem/solution/outcome line + screenshot with alt text; drop unused `Project.stars?`; drop unused `lucide-react` if still unimported. (R2-chair + skeptic catches.)

### Non-goals for v1.1
No contact form/Calendly backend, no `/projects/[id]` or blog CMS, no Lighthouse CI pipeline, no animation lib, no new projects until links are real. (Pragmatist-R2 + simplifier + skeptic spam/surface arguments carried.)

## Options that lost and why
- **Ship v1 as-is, 6.5/10 (R1-chair verdict).** Rejected per skeptic-R2: shipping known-false claims on a *security* portfolio is a credibility exploit against yourself. Strip before deploy.
- **Pick single identity: pentest OR frontend (skeptic-R1).** Rejected. OffSec + frontend is the differentiator vs 100 generic React portfolios; fix is hierarchy, not amputation.
- **Collapse About+Skills, Hero→Projects only (simplifier-R1/R2).** Rejected. Removes Experience (internship filter) and Skills pill-scanning (recruiter/ATS skim). Simplify labels, don't delete sections.
- **Add everything at once: form + Calendly + creds strip + visuals + badges (user-advocate-R1 maximal, pragmatist-R1 Calendly/blog).** Rejected as LCP-bloating and maintenance-heavy. Sequenced P0→P1 instead.
- **Lighthouse CI + axe pipeline as P0 (R1-chair).** Rejected as CI theatre for solo dev; local run + Speed Insights + footer link suffices for v1.1.
- **Plain-English rebrand, kill terminal (simplifier maximal).** Rejected. Terminal is the only visual moat; dual-label preserves HR scan + brand.
- **Creds strip / CVE-or-nothing gate (skeptic maximal / user-advocate premature).** Rejected both extremes: CVE/HackerOne bar unrealistic for 2023-24 internship level; badges without URLs are fake claims. Standard: THM/HTB + writeups + redacted reports with links.
- **`lib/data.ts` ease = virtue; `mailto:` is broken on mobile (partial R1 claims).** Corrected: ease enables fakes without a link rule; mailto works on mobile — missing pieces were copy-email + resume.

## What's still open
1. Target persona order: security hiring manager vs frontend freelance client — decides whether `/writeups` or live-UI case study leads P1.
2. Which 2 projects survive (proposal above assumes phish-guard; owner to confirm repo readiness).
3. Domain/identity ownership: does `hackergovind.dev`, `hello@hackergovind.dev`, GitHub/LinkedIn URLs resolve? + missing `og-image`, `sitemap/robots`.
4. Proof standard per claim (perf = Speed Insights link, a11y = axe run, vuln = redacted writeup, freelance = live URL + testimonial) — needs owner sign-off on "no claim without artifact in same diff".
5. Availability badge freshness (rot risk) + body-font split (sans vs mono) — needs design pass.
6. Vuln-scanner demo safety review before re-listing.

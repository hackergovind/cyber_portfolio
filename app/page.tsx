import type { Metadata } from "next";
import Header from "@/components/Header";
import Hero from "@/components/Hero";
import Section from "@/components/Section";
import ProjectCard from "@/components/ProjectCard";
import { EXPERIENCE, PROFILE, PROJECTS, SKILLS } from "@/lib/data";

export const metadata: Metadata = {
  title: "hackergovind — Cybersecurity & Frontend Portfolio",
  description:
    "Portfolio of Govind (hackergovind): cybersecurity researcher and frontend developer building secure, fast, accessible web experiences.",
  metadataBase: new URL("https://hackergovind.dev"),
  openGraph: {
    title: "hackergovind — Cyber Portfolio",
    description: "Secure, fast, accessible web experiences.",
    type: "website",
  },
};

export default function HomePage() {
  return (
    <div id="top">
      <a href="#main" className="skip-link">
        Skip to main content
      </a>
      <Header />
      <main id="main">
        <Hero />

        <Section id="about" title="~/about">
          <div className="grid gap-6 sm:grid-cols-2">
            <div className="rounded-xl border border-border bg-card p-5">
              <h3 className="mb-2 font-bold text-primary">$ cat about.txt</h3>
              <p className="text-sm leading-relaxed text-muted-foreground">
                I break web apps (ethically) and then build them back stronger. My work sits at the
                intersection of offensive security and modern frontend — React/Next.js, TypeScript,
                Tailwind v4, with WCAG AA and Core Web Vitals baked in from the start.
              </p>
            </div>
            <div className="rounded-xl border border-border bg-card p-5">
              <h3 className="mb-2 font-bold text-primary">$ uptime --focus</h3>
              <ul className="space-y-2 text-sm text-muted-foreground">
                <li>→ Responsible disclosure & bug bounty recon</li>
                <li>→ Accessible component systems (shadcn patterns)</li>
                <li>→ Performance budgets: &lt; 3s on 3G, 90+ Lighthouse</li>
              </ul>
            </div>
          </div>
        </Section>

        <Section id="skills" title="~/skills">
          <div className="grid gap-4 sm:grid-cols-3">
            {SKILLS.map((g) => (
              <div key={g.category} className="rounded-xl border border-border bg-card p-5">
                <h3 className="mb-3 font-bold">{g.category}</h3>
                <ul className="flex flex-wrap gap-2">
                  {g.items.map((s) => (
                    <li
                      key={s}
                      className="rounded-full bg-secondary px-2.5 py-1 text-xs font-medium text-secondary-foreground"
                    >
                      {s}
                    </li>
                  ))}
                </ul>
              </div>
            ))}
          </div>
        </Section>

        <Section id="projects" title="~/projects">
          <div className="grid gap-4 sm:grid-cols-2">
            {PROJECTS.map((p) => (
              <ProjectCard key={p.id} project={p} />
            ))}
          </div>
        </Section>

        <Section id="experience" title="~/experience">
          <ol className="space-y-4">
            {EXPERIENCE.map((e) => (
              <li key={e.role} className="rounded-xl border border-border bg-card p-5">
                <div className="flex flex-wrap items-baseline justify-between gap-2">
                  <h3 className="font-bold">
                    {e.role} <span className="font-normal text-muted-foreground">@ {e.org}</span>
                  </h3>
                  <p className="text-xs text-muted-foreground">{e.period}</p>
                </div>
                <ul className="mt-3 list-disc space-y-1 pl-5 text-sm text-muted-foreground">
                  {e.points.map((pt) => (
                    <li key={pt}>{pt}</li>
                  ))}
                </ul>
              </li>
            ))}
          </ol>
        </Section>

        <Section id="contact" title="~/contact">
          <div className="rounded-xl border border-border bg-card p-6">
            <p className="mb-4 text-sm text-muted-foreground">
              Open for internships, freelance, and security collabs. Fastest reply by email.
            </p>
            <ul className="flex flex-wrap gap-3">
              <li>
                <a
                  href={`mailto:${PROFILE.email}`}
                  className="inline-flex min-h-[44px] items-center rounded-md bg-primary px-5 py-2.5 text-sm font-bold text-primary-foreground hover:opacity-90"
                >
                  {PROFILE.email}
                </a>
              </li>
              <li>
                <a
                  href={PROFILE.github}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="inline-flex min-h-[44px] items-center rounded-md border border-border bg-secondary px-5 py-2.5 text-sm font-semibold hover:border-primary"
                >
                  GitHub
                </a>
              </li>
              <li>
                <a
                  href={PROFILE.linkedin}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="inline-flex min-h-[44px] items-center rounded-md border border-border bg-secondary px-5 py-2.5 text-sm font-semibold hover:border-primary"
                >
                  LinkedIn
                </a>
              </li>
            </ul>
          </div>
        </Section>
      </main>

      <footer className="mx-auto max-w-5xl px-4 py-8 text-center text-xs text-muted-foreground">
        <p>
          © {new Date().getFullYear()} {PROFILE.handle} · Built with Next.js + Tailwind v4 · WCAG AA ·{" "}
          <a href="#top" className="underline hover:text-primary">
            Back to top ↑
          </a>
        </p>
      </footer>
    </div>
  );
}

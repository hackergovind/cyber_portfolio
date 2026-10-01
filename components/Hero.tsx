import { memo } from "react";
import { PROFILE } from "@/lib/data";

function Hero() {
  return (
    <section aria-labelledby="hero-heading" className="grid-bg border-b border-border">
      <div className="mx-auto flex max-w-5xl flex-col gap-6 px-4 py-16 sm:py-24">
        <p className="text-sm text-primary" aria-hidden="true">
          ┌──[{PROFILE.handle}@sec]─[~]
        </p>
        <h1 id="hero-heading" className="terminal-glow text-4xl font-extrabold tracking-tight sm:text-6xl">
          {PROFILE.name}
          <span className="mt-2 block text-xl font-medium text-muted-foreground sm:text-2xl">
            {PROFILE.role}
          </span>
        </h1>
        <p className="max-w-2xl text-base text-muted-foreground sm:text-lg">{PROFILE.tagline}</p>
        <ul className="flex flex-wrap items-center gap-3" aria-label="Profile actions">
          <li>
            <a
              href="#projects"
              className="inline-flex min-h-[44px] items-center rounded-md bg-primary px-5 py-2.5 text-sm font-bold text-primary-foreground hover:opacity-90"
            >
              View work →
            </a>
          </li>
          <li>
            <a
              href="#contact"
              className="inline-flex min-h-[44px] items-center rounded-md border border-border bg-secondary px-5 py-2.5 text-sm font-semibold text-secondary-foreground hover:border-primary"
            >
              Hire me
            </a>
          </li>
          <li className="text-sm text-muted-foreground">{PROFILE.location}</li>
        </ul>
        <dl className="grid grid-cols-2 gap-3 sm:grid-cols-4" aria-label="Highlights">
          {[
            ["Uptime", "99.9% secure"],
            ["LCP", "< 2.5s"],
            ["A11y", "WCAG AA"],
            ["Focus", "OffSec + UI"],
          ].map(([k, v]) => (
            <div key={k} className="rounded-lg border border-border bg-card p-3">
              <dt className="text-xs text-muted-foreground">{k}</dt>
              <dd className="font-bold text-primary">{v}</dd>
            </div>
          ))}
        </dl>
      </div>
    </section>
  );
}

export default memo(Hero);

import type { Metadata } from "next";
import Link from "next/link";
import { WRITEUPS } from "@/lib/writeups";

export const metadata: Metadata = {
  title: "Writeups",
  description: "Redacted CTF and lab writeups — web exploitation walkthroughs with mitigations.",
};

export default function WriteupsPage() {
  return (
    <div>
      <a href="#main" className="skip-link">
        Skip to main content
      </a>
      <main id="main" className="mx-auto max-w-5xl px-4 py-12 sm:py-16">
        <p className="text-sm text-muted-foreground">
          <Link href="/" className="underline hover:text-primary">
            ← Home
          </Link>
        </p>
        <h1 className="mt-2 text-3xl font-extrabold tracking-tight sm:text-4xl">Writeups</h1>
        <p className="mt-2 max-w-2xl text-sm text-muted-foreground sm:text-base">
          Redacted lab walkthroughs only — no live targets, no sensitive data. Each one: repro
          steps plus how to fix it.
        </p>
        <ul className="mt-8 grid gap-4 sm:grid-cols-2">
          {WRITEUPS.map((w) => (
            <li key={w.slug} className="rounded-xl border border-border bg-card p-5 hover:border-primary">
              <h2 className="font-bold">
                <Link href={`/writeups/${w.slug}`} className="hover:text-primary hover:underline">
                  {w.title}
                </Link>
              </h2>
              <p className="mt-1 text-xs text-muted-foreground">{w.date}</p>
              <p className="mt-2 text-sm text-muted-foreground">{w.summary}</p>
              <p className="mt-3">
                <Link
                  href={`/writeups/${w.slug}`}
                  className="text-sm font-semibold hover:text-primary hover:underline"
                >
                  Read walkthrough →
                </Link>
              </p>
            </li>
          ))}
        </ul>
      </main>
    </div>
  );
}

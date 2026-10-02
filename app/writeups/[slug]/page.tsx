import type { Metadata } from "next";
import Link from "next/link";
import { notFound } from "next/navigation";
import { WRITEUPS } from "@/lib/writeups";

export function generateStaticParams() {
  return WRITEUPS.map((w) => ({ slug: w.slug }));
}

export async function generateMetadata({
  params,
}: {
  readonly params: Promise<{ slug: string }>;
}): Promise<Metadata> {
  const { slug } = await params;
  const w = WRITEUPS.find((x) => x.slug === slug);
  return { title: w ? w.title : "Writeup", description: w?.summary ?? "Lab writeup." };
}

export default async function WriteupPage({
  params,
}: {
  readonly params: Promise<{ slug: string }>;
}) {
  const { slug } = await params;
  const w = WRITEUPS.find((x) => x.slug === slug);
  if (!w) notFound();
  return (
    <div>
      <a href="#main" className="skip-link">
        Skip to main content
      </a>
      <main id="main" className="mx-auto max-w-3xl px-4 py-12 sm:py-16">
        <p className="text-sm text-muted-foreground">
          <Link href="/writeups" className="underline hover:text-primary">
            ← All writeups
          </Link>
        </p>
        <h1 className="mt-2 text-3xl font-extrabold tracking-tight">{w.title}</h1>
        <p className="mt-1 text-xs text-muted-foreground">{w.date} · lab only, redacted</p>
        <p className="mt-4 text-sm leading-relaxed text-muted-foreground sm:text-base">{w.summary}</p>
        <h2 className="mt-8 text-xl font-bold">Repro steps</h2>
        <ol className="mt-3 list-decimal space-y-2 pl-5 text-sm leading-relaxed text-muted-foreground">
          {w.body.map((step) => (
            <li key={step.slice(0, 24)}>{step}</li>
          ))}
        </ol>
        <h2 className="mt-8 text-xl font-bold">Mitigations</h2>
        <ul className="mt-3 list-disc space-y-2 pl-5 text-sm leading-relaxed text-muted-foreground">
          {w.mitigations.map((m) => (
            <li key={m.slice(0, 24)}>{m}</li>
          ))}
        </ul>
      </main>
    </div>
  );
}

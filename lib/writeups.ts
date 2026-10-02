export interface Writeup {
  readonly slug: string;
  readonly title: string;
  readonly date: string;
  readonly summary: string;
  readonly body: readonly string[];
  readonly mitigations: readonly string[];
}

export const WRITEUPS: readonly Writeup[] = [
  {
    slug: "stored-xss-lab",
    title: "Stored XSS in a lab comment field",
    date: "2024-11-02",
    summary:
      "How a comment box without output encoding became stored JavaScript execution — reproduced in a local lab, with fixes.",
    body: [
      "Scope: local lab only (Docker image running a deliberately vulnerable comment app). No live targets.",
      "Step 1: created a post and submitted a comment with plain text to map how input is stored and rendered.",
      "Step 2: submitted encoding probes (`<`, `>`, quotes) and observed which characters were reflected unescaped in the comment list.",
      "Step 3: confirmed stored execution with a harmless alert-free probe (e.g. an <img> with an invalid src plus an on-error handler that writes to the console) — payload fired on every page view, proving stored impact vs reflected.",
      "Step 4: checked the request in Burp-equivalent proxy tooling: no server-side validation, input stored verbatim, rendered with innerHTML-equivalent behavior.",
    ],
    mitigations: [
      "Encode on output (context-aware: HTML, attribute, JS) instead of relying on input blocklists.",
      "Set a Content-Security-Policy without 'unsafe-inline' so injected handlers cannot run.",
      "Add HttpOnly + SameSite cookies so a successful XSS cannot trivially steal sessions.",
    ],
  },
  {
    slug: "idor-lab",
    title: "IDOR in a lab invoice viewer",
    date: "2025-02-14",
    summary:
      "Sequential invoice IDs plus missing object-level checks exposed other users' data in a lab app — and the one-line fix pattern.",
    body: [
      "Scope: local lab only. Two test accounts (user A, user B) created by me.",
      "Step 1: as user A, opened /invoices/101 and noted the sequential numeric ID.",
      "Step 2: as user A, requested /invoices/102 (user B's invoice). Server returned 200 with user B's data — no ownership check.",
      "Step 3: confirmed with the proxy that changing the ID was the only variable; auth token stayed user A's.",
      "Step 4: documented impact boundaries: read-only in this lab, but the same pattern enablesenames, addresses, and order history exposure in real apps.",
    ],
    mitigations: [
      "Enforce server-side ownership checks on every object fetch (deny by default).",
      "Prefer unguessable IDs (UUIDs) as defense-in-depth — never as the only control.",
      "Log and rate-limit object-ID enumeration patterns.",
    ],
  },
] as const;

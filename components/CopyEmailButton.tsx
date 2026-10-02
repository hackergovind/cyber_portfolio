"use client";

import { useState } from "react";

export default function CopyEmailButton({ email }: { readonly email: string }) {
  const [copied, setCopied] = useState(false);

  async function copy() {
    try {
      await navigator.clipboard.writeText(email);
      setCopied(true);
      setTimeout(() => setCopied(false), 2000);
    } catch {
      setCopied(false);
    }
  }

  return (
    <button
      type="button"
      onClick={copy}
      aria-live="polite"
      className="inline-flex min-h-[44px] items-center rounded-md border border-border bg-secondary px-5 py-2.5 text-sm font-semibold hover:border-primary"
    >
      {copied ? "Copied ✓" : "Copy email"}
    </button>
  );
}

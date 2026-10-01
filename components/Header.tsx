import { memo } from "react";
import { NAV_LINKS, PROFILE } from "@/lib/data";
import { cn } from "@/lib/utils";

const statusDot = <span aria-hidden="true" className="inline-block size-2 rounded-full bg-primary" />;

function Header() {
  return (
    <header className="sticky top-0 z-50 border-b border-border bg-background/90 backdrop-blur">
      <nav aria-label="Main" className="mx-auto flex h-14 max-w-5xl items-center justify-between px-4">
        <a href="#top" className="flex items-center gap-2 font-bold tracking-tight">
          {statusDot}
          <span>
            {PROFILE.handle}
            <span className="text-primary">@sec</span>
          </span>
          <span className="sr-only"> — home</span>
        </a>
        <ul className="hidden items-center gap-1 sm:flex">
          {NAV_LINKS.map((l) => (
            <li key={l.id}>
              <a
                href={`#${l.id}`}
                className={cn(
                  "rounded-md px-3 py-2 text-sm text-muted-foreground",
                  "hover:bg-secondary hover:text-foreground",
                  "focus-visible:outline-2"
                )}
              >
                {l.label}
              </a>
            </li>
          ))}
        </ul>
        <a
          href="#contact"
          className="rounded-md bg-primary px-3 py-2 text-sm font-bold text-primary-foreground hover:opacity-90 sm:hidden"
        >
          ~/contact
        </a>
      </nav>
    </header>
  );
}

export default memo(Header);

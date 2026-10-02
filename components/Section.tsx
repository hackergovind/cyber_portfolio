import { memo, type ReactNode } from "react";

interface SectionProps {
  readonly id: string;
  readonly title: string;
  readonly terminal?: string;
  readonly children: ReactNode;
}

function Section({ id, title, terminal, children }: SectionProps) {
  return (
    <section id={id} aria-labelledby={`${id}-heading`} className="scroll-mt-16 border-b border-border">
      <div className="mx-auto max-w-5xl px-4 py-12 sm:py-16">
        <h2 id={`${id}-heading`} className="mb-6 text-2xl font-bold tracking-tight">
          <span aria-hidden="true" className="mr-2 text-primary">
            #
          </span>
          {title}
          {terminal ? (
            <span aria-hidden="true" className="ml-2 font-mono text-sm font-normal opacity-60">
              {terminal}
            </span>
          ) : null}
        </h2>
        {children}
      </div>
    </section>
  );
}

export default memo(Section);

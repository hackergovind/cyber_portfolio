import { memo } from "react";
import type { Project } from "@/lib/data";

function ProjectCard({ project }: { readonly project: Project }) {
  return (
    <article className="content-visibility-auto flex flex-col gap-3 rounded-xl border border-border bg-card p-5 hover:border-primary">
      <h3 className="font-bold">
        <a href={project.link} className="hover:text-primary hover:underline">
          {project.title}
        </a>
      </h3>
      <p className="text-sm text-muted-foreground">{project.description}</p>
      <ul className="mt-auto flex flex-wrap gap-2" aria-label={`Tech for ${project.title}`}>
        {project.tags.map((t) => (
          <li
            key={t}
            className="rounded-full border border-border bg-secondary px-2.5 py-1 text-xs font-medium text-secondary-foreground"
          >
            {t}
          </li>
        ))}
      </ul>
    </article>
  );
}

export default memo(ProjectCard);

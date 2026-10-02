import { memo } from "react";
import type { Project } from "@/lib/data";

function ProjectCard({ project }: { readonly project: Project }) {
  const isDraft = project.draft === true || project.link === "";
  return (
    <article className="content-visibility-auto flex flex-col gap-3 rounded-xl border border-border bg-card p-5 hover:border-primary">
      <h3 className="font-bold">
        {isDraft ? (
          <span>{project.title}</span>
        ) : (
          <a href={project.link} className="hover:text-primary hover:underline">
            {project.title}
          </a>
        )}
        {isDraft ? (
          <span className="ml-2 rounded-full border border-border px-2 py-0.5 text-xs font-medium text-muted-foreground">
            Draft — repo on request
          </span>
        ) : null}
      </h3>
      <p className="text-sm text-muted-foreground">{project.description}</p>
      <p className="text-sm font-medium text-foreground">{project.outcome}</p>
      <ul className="flex flex-wrap gap-2" aria-label={`Tech for ${project.title}`}>
        {project.tags.map((t) => (
          <li
            key={t}
            className="rounded-full border border-border bg-secondary px-2.5 py-1 text-xs font-medium text-secondary-foreground"
          >
            {t}
          </li>
        ))}
      </ul>
      {isDraft ? null : (
        <ul className="mt-auto flex flex-wrap gap-3 pt-1 text-sm font-semibold">
          <li>
            <a href={project.github} target="_blank" rel="noopener noreferrer" className="hover:text-primary hover:underline">
              GitHub →
            </a>
          </li>
          {project.demo ? (
            <li>
              <a href={project.demo} target="_blank" rel="noopener noreferrer" className="hover:text-primary hover:underline">
                Live demo →
              </a>
            </li>
          ) : null}
          {project.link.startsWith("http") ? (
            <li>
              <a href={project.link} target="_blank" rel="noopener noreferrer" className="hover:text-primary hover:underline">
                Details →
              </a>
            </li>
          ) : (
            <li>
              <a href={project.link} className="hover:text-primary hover:underline">
                Details →
              </a>
            </li>
          )}
        </ul>
      )}
    </article>
  );
}

export default memo(ProjectCard);

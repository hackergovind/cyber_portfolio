export interface Project {
  readonly id: string;
  readonly title: string;
  readonly description: string;
  readonly outcome: string;
  readonly tags: readonly string[];
  /** Live demo / details URL. Never "#": drafts carry no link. */
  readonly link: string;
  readonly github: string;
  readonly demo?: string;
  readonly draft?: boolean;
}

export interface SkillGroup {
  readonly category: string;
  readonly items: readonly string[];
}

export interface Experience {
  readonly role: string;
  readonly org: string;
  readonly period: string;
  readonly points: readonly string[];
}

export type SectionId = "about" | "skills" | "projects" | "experience" | "contact";

export const PROFILE = {
  name: "Govind",
  handle: "hackergovind",
  role: "Cybersecurity Researcher & Frontend Developer",
  tagline: "I break web apps (ethically), then build them back stronger — security researcher who ships accessible frontends",
  location: "India · Remote",
  email: "hello@hackergovind.dev",
  github: "https://github.com/hackergovind",
  linkedin: "https://linkedin.com/in/hackergovind",
} as const;

export const SKILLS: readonly SkillGroup[] = [
  { category: "Security", items: ["Penetration Testing", "Burp Suite", "OWASP Top 10", "Network Security", "CTF / TryHackMe"] },
  { category: "Frontend", items: ["React", "Next.js", "TypeScript", "Tailwind CSS v4", "Accessibility (WCAG AA)"] },
  { category: "Tooling", items: ["Linux", "Git", "Docker", "Vercel", "CI/CD"] },
] as const;

export const PROJECTS: readonly Project[] = [
  {
    id: "cyber-portfolio",
    title: "cyber_portfolio",
    description:
      "This site — Next.js 15 + Tailwind v4 single-page portfolio with skip-link, landmarks, and 44px touch targets.",
    outcome: "Outcome: builds clean, deploys on Vercel, no dead links.",
    tags: ["Next.js", "TypeScript", "Tailwind"],
    link: "https://github.com/hackergovind/cyber_portfolio",
    github: "https://github.com/hackergovind/cyber_portfolio",
  },
  {
    id: "phish-guard",
    title: "phish-guard",
    description: "Phishing URL analyser with heuristics + threat-intel lookup, privacy-first client-side checks.",
    outcome: "Outcome: paste-a-URL demo planned; currently code + writeup.",
    tags: ["TypeScript", "Next.js", "API"],
    link: "https://github.com/hackergovind/phish-guard",
    github: "https://github.com/hackergovind/phish-guard",
  },
  {
    id: "vuln-scanner",
    title: "web-vuln-scanner",
    description: "Lightweight recon + header / TLS / OWASP checks dashboard with exportable reports.",
    outcome: "Draft — repo on request until README + abuse guardrails land.",
    tags: ["Python", "Security", "React"],
    link: "",
    github: "",
    draft: true,
  },
  {
    id: "ctf-writeups",
    title: "ctf-writeups",
    description: "Documented CTF solutions — privilege escalation, web exploitation, forensics walkthroughs.",
    outcome: "See /writeups for published walkthroughs.",
    tags: ["Writeups", "Linux", "Web"],
    link: "/writeups",
    github: "https://github.com/hackergovind",
  },
] as const;

export const EXPERIENCE: readonly Experience[] = [
  {
    role: "Security Researcher",
    org: "Independent / Bug Bounty",
    period: "2024 — Present",
    points: [
      "Responsible disclosure on web targets (XSS, IDOR, misconfigurations)",
      "Built automation for recon and report generation",
      "Published CTF and lab writeups",
    ],
  },
  {
    role: "Frontend Developer",
    org: "Freelance",
    period: "2023 — Present",
    points: [
      "Shipped responsive, accessible React/Next.js sites",
      "Measured performance and accessibility before claiming them",
      "Design systems with Tailwind + shadcn patterns",
    ],
  },
] as const;

export const NAV_LINKS: readonly { readonly id: SectionId; readonly label: string; readonly terminal: string }[] = [
  { id: "about", label: "About", terminal: "~/about" },
  { id: "skills", label: "Skills", terminal: "~/skills" },
  { id: "projects", label: "Projects", terminal: "~/projects" },
  { id: "experience", label: "Experience", terminal: "~/experience" },
  { id: "contact", label: "Contact", terminal: "~/contact" },
] as const;

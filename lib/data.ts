export interface Project {
  readonly id: string;
  readonly title: string;
  readonly description: string;
  readonly tags: readonly string[];
  readonly link: string;
  readonly stars?: number;
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
  tagline: "$ whoami — building secure, fast, accessible web experiences",
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
    description: "This site — Next.js 15 + Tailwind v4, WCAG AA, 90+ Lighthouse, deployed on Vercel.",
    tags: ["Next.js", "TypeScript", "Tailwind"],
    link: "#",
  },
  {
    id: "vuln-scanner",
    title: "web-vuln-scanner",
    description: "Lightweight recon + header / TLS / OWASP checks dashboard with exportable reports.",
    tags: ["Python", "Security", "React"],
    link: "#",
  },
  {
    id: "phish-guard",
    title: "phish-guard",
    description: "Phishing URL analyser with heuristics + threat-intel lookup, privacy-first client-side checks.",
    tags: ["TypeScript", "Next.js", "API"],
    link: "#",
  },
  {
    id: "ctf-writeups",
    title: "ctf-writeups",
    description: "Documented CTF solutions — privilege escalation, web exploitation, forensics walkthroughs.",
    tags: ["Writeups", "Linux", "Web"],
    link: "#",
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
      "Core Web Vitals: LCP < 2.5s, CLS < 0.1 on portfolio builds",
      "Design systems with Tailwind + shadcn patterns",
    ],
  },
] as const;

export const NAV_LINKS: readonly { readonly id: SectionId; readonly label: string }[] = [
  { id: "about", label: "~/about" },
  { id: "skills", label: "~/skills" },
  { id: "projects", label: "~/projects" },
  { id: "experience", label: "~/experience" },
  { id: "contact", label: "~/contact" },
] as const;

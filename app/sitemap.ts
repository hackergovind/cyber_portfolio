import type { MetadataRoute } from "next";

export default function sitemap(): MetadataRoute.Sitemap {
  const base = "https://hackergovind.dev";
  const now = new Date();
  return [
    { url: `${base}/`, lastModified: now },
    { url: `${base}/writeups`, lastModified: now },
  ];
}

import { defineCollection } from 'astro:content';
import { glob } from 'astro/loaders';
import { z } from 'astro/zod';

const projects = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/projects' }),
  schema: z.object({
    order: z.number(),
    id_code: z.string(),          // e.g. "001" — the index shown on the card
    title: z.string(),
    status: z.string(),           // e.g. "Deployed", "In progress"
    domain: z.string(),           // e.g. "Robotics / Field hardware"
    stack: z.array(z.string()).default([]),
    metric: z.string().optional(),// the highlighted stat line on the card
    link: z.string().url().optional(),
    isCaseStudy: z.boolean().default(false),
    heroImage: z.string().optional(),
    heroImageAlt: z.string().optional(),
    heroImageCredit: z.string().optional(),
    heroImageCreditUrl: z.string().url().optional(),
    didNotDo: z.string().optional(),   // binding "Did NOT do" section, verbatim
    scopeNotes: z.string().optional(), // binding "Scope notes" section, verbatim
  }),
});

const experience = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/experience' }),
  schema: z.object({
    order: z.number(),
    role: z.string(),
    org: z.string(),
    location: z.string(),
    dateRange: z.string(),
    summary: z.string(),
  }),
});

const notes = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/notes' }),
  schema: z.object({
    title: z.string(),
    publishDate: z.date(),
    summary: z.string(),
    draft: z.boolean().default(false),
  }),
});

export const collections = { projects, experience, notes };

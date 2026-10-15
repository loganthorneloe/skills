# Web reports

Use the same source audit, first-principles explanation, and source evidence as the core skill. The default deliverable is a simple HTML report.

## Logan styling

The guidance below is the portable Logan visual style for this skill. It is sufficient without a `logan-brand` skill, `logan-style` checkout, installed fonts, network-loaded styles, or a particular AI tool. An available brand kit can supply exact assets, but is optional. Honor explicit user design direction.

### Palette and typography

Default to light. Define semantic CSS variables for these colors; use the dark column when the destination or user calls for dark styling. Do not invert source images to create a dark theme.

| Role | Light | Dark |
| --- | --- | --- |
| Canvas | `#f5f4f0` warm paper | `#101527` ink navy |
| Surface | `#ffffff` | `#1e2537` |
| Main text | `#101527` | `#f3f5f8` |
| Secondary text | `#646c77` | `#adb4c0` |
| Hairline border | `#cbd0d3` | `#3e4659` |
| Blue accent | `#2f6c9e` | `#8db7de` |
| Green accent | `#46734d` | `#9ac9a2` |
| Red accent | `#bf3030` | `#ed7777` |

Use Sora at weight 600 for headings and prominent numbers, Inter for body text and labels, and a readable monospace face for code. When those fonts are unavailable, use system sans-serif fallbacks such as `"Sora", system-ui, sans-serif` and `"Inter", system-ui, sans-serif`. Do not require font downloads; the report must remain readable offline with fallback fonts.

### Composition and detail

- Use a centered reading column around 720px wide, responsive side padding around 20–24px, 16–17px body text, and line height around 1.75. Place headings above the content they introduce. Separate prose sections with whitespace.
- Favor warm paper, dark text, square or nearly square surfaces, thin structural lines, and restrained accents. Avoid shadows, gradients, decorative backgrounds, and rounded dashboard cards around ordinary paragraphs. Use tables or grouped surfaces only when the information calls for them.
- Keep headings short and descriptive. Omit obligatory logos, slogans, eyebrow labels, subtitles, decorative numbering, and footer strips. A red terminal period is optional for the main report title, never required on subheadings or figure labels.
- Make body links visibly heavier and underlined, with red hover/focus text and a visible keyboard-focus outline. External text links may carry a small red `↗` hidden from assistive technology; omit directional decoration from internal links and controls.
- Use blue as a restrained accent; use red or green when their meaning is useful. Never communicate a distinction by color alone. Keep labels, units, conditions, and category identities intact; use additional distinguishable colors when the data needs them. Styling must not alter values or imply evidence that the sources do not provide.
- Preserve source figures, screenshots, authentic logos, colors, labels, and attribution. Apply the report style to surrounding text and captions, not to the source evidence itself. Use responsive images with their original aspect ratios. The core skill's source-evidence requirement still applies.

### Portable HTML

Prefer one HTML file with embedded CSS and minimal JavaScript, without a framework, server, or build pipeline. Use the bundled guidance to write the small amount of CSS needed for the report. Adjacent assets with relative paths are appropriate when supported; embed required assets when a self-contained file is requested and embedding is permitted. Do not rely on personal filesystem paths. External source images may require network access; retain source links and captions and disclose unavailable assets rather than promising offline access to them.

## Report and delivery

- Keep the page simple: a clear title, compact source audit, direct answer, then a connected explanation with descriptive headings. Use a readable column, generous spacing, strong contrast, and responsive source figures with captions and attribution. Choose layout for the explanation; do not force prose into dashboard tiles or add decorative labels and filler.
- Put source links beside the claims, figures, metrics, and short quotations they support. Do not fabricate visuals or evidence to fill the layout; state when source material is unavailable.
- Add interaction only when it improves understanding: expandable detail, a comparison toggle, or a small parameter control. Keep the main explanation readable without interaction. Clearly label assumptions and illustrative calculations; distinguish them from source findings.
- Use semantic HTML, keyboard-accessible controls, descriptive links, and alt text. Keep essential content visible if JavaScript is unavailable.
- Deliver the report as a file or HTML artifact using the current environment's capabilities. When file tools are available, save it and any assets in the user's requested location or the normal output location. If neither files nor artifacts are supported, return the complete HTML source for the user to save. Include a brief summary and a usable link or attachment when available; never invent a saved file or preview.
- Preview when tools permit; check narrow and wide layouts, font and asset loading, source images, links, controls, and each delivered theme. Report checks you could not perform. Opening a supported preview is useful but is not a dependency of this skill.

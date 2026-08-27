## 2026-08-27 - Decorative Animation Accessibility in Markdown READMEs
**Learning:** Decorative icons and GIFs without functional links or standalone meaning (e.g., floating social GIFs) read out repetitive text like "Social animated 1" in screen readers, creating clutter for visually impaired users.
**Action:** Always mark purely decorative icons with `alt=""` and `aria-hidden="true"`, while providing explicit `aria-label`s on surrounding parent links or interactive badges.

## 2025-08-31 - Empty alt attributes in Markdown READMEs
**Learning:** GitHub's Markdown sanitizer strips `aria-*` attributes (such as `aria-label` or `aria-hidden`) from rendered HTML in README files, but preserves standard empty `alt=""` attributes on `<img>` tags.
**Action:** Always use empty `alt=""` attributes instead of `aria-hidden="true"` when marking decorative images in Markdown files for screen readers.

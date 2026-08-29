## 2026-08-29 - Decorative Image Handling in GitHub Markdown
**Learning:** GitHub's HTML sanitizer strips `aria-*` attributes (such as `aria-hidden="true"`) from rendered HTML in README files, but preserves standard empty `alt=""` attributes.
**Action:** Use empty `alt=""` attributes on decorative `<img>` tags in Markdown/HTML READMEs to ensure screen readers skip non-informative images and visual dividers.

#!/usr/bin/env bash
# Fetch the third-party files the PDFs need, into pdf/vendor/ (gitignored):
#
#   * the Mermaid bundle (~3.5 MB). Without it, pdf/build.py still succeeds --
#     the pages containing diagrams just show the diagram source.
#   * the brand faces (Enterprise Platform 2027): Figtree SemiBold, Geist and
#     Geist Mono, all under the SIL Open Font License, which allows embedding
#     them in the PDFs. Without them, the text falls back to system faces; CI
#     fails such a PDF.
#
# Both come from npm at pinned versions: Geist from Vercel's own `geist`
# package, Figtree from @fontsource, which repackages the Google Fonts release.
set -euo pipefail

MERMAID_VERSION="${MERMAID_VERSION:-11.16.0}"
GEIST_VERSION="${GEIST_VERSION:-1.9.0}"
FIGTREE_VERSION="${FIGTREE_VERSION:-5.3.0}"

here="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
vendor="$here/vendor"
fonts="$vendor/fonts"

# Keep in sync with BRAND_FONTS in pdf/build.py.
geist_files=(
  geist-sans/Geist-Regular.woff2
  geist-sans/Geist-Italic.woff2
  geist-sans/Geist-Medium.woff2
  geist-sans/Geist-MediumItalic.woff2
  geist-mono/GeistMono-Regular.woff2
  geist-mono/GeistMono-Italic.woff2
)
figtree_files=(
  figtree-latin-600-normal.woff2
  figtree-latin-ext-600-normal.woff2
)

command -v npm >/dev/null || { echo "error: npm is required" >&2; exit 1; }

tmp="$(mktemp -d)"
trap 'rm -rf "$tmp"' EXIT
mkdir -p "$vendor" "$fonts"

# npm pack <spec> into its own directory and unpack it; prints that directory.
unpack() {
  local dir="$tmp/$1"
  mkdir -p "$dir"
  ( cd "$dir" && npm pack "$2" --silent >/dev/null && tar -xzf ./*.tgz )
  echo "$dir/package"
}

if [[ -f "$vendor/mermaid.min.js" && -z "${FORCE:-}" ]]; then
  echo "mermaid already present (set FORCE=1 to refetch)"
else
  echo "fetching mermaid@$MERMAID_VERSION"
  pkg="$(unpack mermaid "mermaid@$MERMAID_VERSION")"
  mv "$pkg/dist/mermaid.min.js" "$vendor/mermaid.min.js"
  echo "installed $vendor/mermaid.min.js ($(du -h "$vendor/mermaid.min.js" | cut -f1))"
fi

have_fonts=1
for f in "${geist_files[@]}" "${figtree_files[@]}"; do
  [[ -f "$fonts/$(basename "$f")" ]] || have_fonts=0
done

if [[ $have_fonts == 1 && -z "${FORCE:-}" ]]; then
  echo "brand fonts already present (set FORCE=1 to refetch)"
else
  echo "fetching geist@$GEIST_VERSION and @fontsource/figtree@$FIGTREE_VERSION"
  pkg="$(unpack geist "geist@$GEIST_VERSION")"
  for f in "${geist_files[@]}"; do
    cp "$pkg/dist/fonts/$f" "$fonts/"
  done
  cp "$pkg/LICENSE.txt" "$fonts/LICENSE-Geist.txt"

  pkg="$(unpack figtree "@fontsource/figtree@$FIGTREE_VERSION")"
  for f in "${figtree_files[@]}"; do
    cp "$pkg/files/$f" "$fonts/"
  done
  cp "$pkg/LICENSE" "$fonts/LICENSE-Figtree.txt"
  echo "installed $(( ${#geist_files[@]} + ${#figtree_files[@]} )) font files in $fonts"
fi

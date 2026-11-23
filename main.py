"""Write the plan to /output/entry.txt.

Deterministic, no network: the text is a constant, written as UTF-8.
The output step never removes the /output directory itself -- it only
clears the directory's contents, then writes entry.txt -- so it works
even when /output is root-owned inside a sticky parent directory.
"""

import os

PLAN = (
    "Day 1: list a $49 same-day Shopify product-page rewrite + 5 AI photos "
    "gig on Fiverr and Upwork. Deliver in under 2 hours, while human "
    "sellers take days. Reinvest profit in $5/day promoted gigs, "
    "raise to $79 after 10 reviews, upsell $29 SEO titles. Aim 1-2 "
    "orders a day."
)


def main() -> None:
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    for name in os.listdir(out_dir):
        path = os.path.join(out_dir, name)
        if os.path.isdir(path) and not os.path.islink(path):
            for root, dirs, files in os.walk(path, topdown=False):
                for f in files:
                    os.remove(os.path.join(root, f))
                for d in dirs:
                    os.rmdir(os.path.join(root, d))
            os.rmdir(path)
        else:
            os.remove(path)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(PLAN)


if __name__ == "__main__":
    main()

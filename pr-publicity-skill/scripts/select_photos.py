#!/usr/bin/env python3
"""从指定文件夹随机选取 3~9 张照片，输出文件路径列表。

用法:
  python select_photos.py [--folder PATH] [--min N] [--max N]

默认:
  --folder  %USERPROFILE%\\.qclaw\\image
  --min     3
  --max     9
"""
import argparse, os, random, sys
from pathlib import Path

IMAGE_EXTS = {".jpg", ".jpeg", ".png", ".gif", ".webp", ".bmp"}

def main():
    parser = argparse.ArgumentParser(description="随机选取照片")
    parser.add_argument("--folder", default=os.path.join(os.environ.get("USERPROFILE", ""), ".qclaw", "image"))
    parser.add_argument("--min", type=int, default=3, dest="min_n")
    parser.add_argument("--max", type=int, default=9, dest="max_n")
    args = parser.parse_args()

    folder = Path(args.folder)
    if not folder.is_dir():
        print(f"❌ 文件夹不存在: {folder}", file=sys.stderr)
        sys.exit(1)

    images = [f for f in folder.iterdir() if f.suffix.lower() in IMAGE_EXTS]
    if not images:
        print(f"❌ 文件夹中无图片: {folder}", file=sys.stderr)
        sys.exit(1)

    count = random.randint(args.min_n, min(args.max_n, len(images)))
    chosen = random.sample(images, count)

    for p in chosen:
        print(str(p))

if __name__ == "__main__":
    main()

---
name: pr-publicity-skill
description: 追觅硅谷发布会社交媒体宣传文案生成技能。根据追觅电视新品（R8000F、S100）的发布信息，自动生成吸引人的标题和文案，并从指定文件夹选取 3-9 张现场照片作为配图。触发场景：用户提到"生成追觅硅谷发布会文案"、"生成发布会宣传文案"、"帮我写发布会推广内容"、"追觅文案"、"发布会文案"等。
---

# 追觅硅谷发布会宣传文案生成技能

## 工作流程

1. **读取产品信息** → 读取 `references/product_info.md` 获取新闻要点与文案生成提示词
2. **选取配图** → 运行 `scripts/select_photos.py` 从 `~/.qclaw/image` 随机选 3~9 张
3. **生成文案** → 严格按照 `references/product_info.md` 中的提示词和下方输出格式生成

## 标签规则

**必须包含（固定 3 个）：**
`#追觅电视` `#追觅AI电视` `#DreameNext`

**可选标签（按内容选 2~3 个）：**
`#硅谷发布会` `#R8000F` `#国产电视出海` `#黑科技家电` `#客厅C位` `#电视推荐` `#智能家居` `#追觅新品`

## 输出格式

```
【标题】xxx

【文案】xxx

#追觅电视 #追觅AI电视 #DreameNext #可选1 #可选2

📷 配图：
- C:\Users\zcc13\.qclaw\image\xxx.JPG
- C:\Users\zcc13\.qclaw\image\yyy.jpg
- ...
```

## 参考资源

- **产品卖点 + 文案提示词**：`references/product_info.md`
- **照片清单**：`references/photo_list.md`
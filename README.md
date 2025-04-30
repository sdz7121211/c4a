# 🚀🤖 Crawl4AI-Qwen: Open-source LLM Friendly Web Crawler & Scraper

## **项目简介：Crawl4AI-QWen**

### **来源**
基于开源项目 [Crawl4AI](https://github.com/yourusername/crawl4ai)，针对原版**仅支持 LiteLLM，不支持 QWen 大模型**的局限，扩展适配能力，提供更灵活的模型兼容性。

### **核心改进**
1. **QWen 大模型支持**  
   新增 `llm_config_extend` 模块，支持阿里云 QWen 系列模型。

2. **LiteLLM 兼容性扩展**  
   通过统一接口封装，支持通过 LiteLLM 调用 QWen API，简化流程。

3. **OpenAI 规范对齐**  
   遵循阿里云 [OpenAI 兼容性规范](https://www.alibabacloud.com/help/en/model-studio/compatibility-of-openai-with-dashscope#43f870c0cfvsy)，实现 `messages` 格式、`temperature` 等参数无缝对接。

### **应用价值**
- 为 Crawl4AI 提供 QWen 大模型支持，利用国产模型搭建高质量网页数据采集管道。
- 开发者可通过 OpenAI 兼容接口，快速集成增强工作流。

---

## 🚀 Development Installation

### 基础安装（建议开发者使用）
```bash
git clone https://github.com/sdz7121211/c4a.git
cd c4a
pip install -e .
```

### 安装可选功能
```bash
pip install -e ".[torch]"           # 使用 PyTorch 的功能
pip install -e ".[transformer]"     # 支持 Transformer 功能
pip install -e ".[cosine]"          # 支持余弦相似度特性
pip install -e ".[sync]"            # 启用同步爬取（Selenium）
pip install -e ".[all]"             # 安装所有功能模块
```

---

## 🛠️ Quick Test

以下为快速测试代码，可验证基本安装是否成功（适用于支持 Docker 的环境）：

```python
import requests

# 提交一个爬取任务
response = requests.post(
    "http://localhost:11235/crawl",
    json={"urls": "https://example.com", "priority": 10}
)
task_id = response.json()["task_id"]

# 轮询任务直到完成
result = requests.get(f"http://localhost:11235/task/{task_id}")
```

更复杂的示例请参考 [Docker 示例](https://github.com/unclecode/crawl4ai/blob/main/docs/examples/docker_example.py)。高级配置（环境变量和用法示例）请查看 [Docker 部署指南](https://docs.crawl4ai.com/basic/docker-deployment/)。

---

## 🔬 Advanced Usage Examples

你可以在 [docs/examples](https://github.com/unclecode/crawl4ai/docs/examples) 查看项目结构与代码示例。以下为一些常用的场景展示：

<details>
<summary>📝 <strong>Markdown 格式内容生成</strong></summary>

```python
import asyncio
from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig, CacheMode

# 示例展示如何从网页提取 Markdown 格式内容
async def main():
    browser_config = BrowserConfig(headless=True, verbose=True)
    run_config = CrawlerRunConfig(cache_mode=CacheMode.ENABLED)
    async with AsyncWebCrawler(config=browser_config) as crawler:
        result = await crawler.arun(
            url="https://docs.micronaut.io/4.7.6/guide/",
            config=run_config
        )
        print(len(result.markdown.raw_markdown))
        print(len(result.markdown.fit_markdown))

if __name__ == "__main__":
    asyncio.run(main())
```

</details>

<details>
<summary>🖥️ <strong>数据提取：无需 LLM 支持</strong></summary>

```python
import asyncio
from crawl4ai.extraction_strategy import JsonCssExtractionStrategy

# JSON 结构化数据提取示例
async def extract_data():
    schema = {
        "baseSelector": "div.main-container",
        "fields": [
            {"name": "title", "selector": ".heading", "type": "text"}
        ]
    }
    strategy = JsonCssExtractionStrategy(schema)
    # 配置浏览器并运行爬取
```

</details>

更多示例请查看 [examples](https://github.com/unclecode/crawl4ai/docs/examples)。

---

## ✨ Recent Updates

### Version 0.6.0 Highlights
- 🌎 **地理位置爬取**：支持位置、时区、语言，以地理环境生成特定内容。
- 🖥️ **交互式调试界面**：内云内置 Web 界面，用于生成 API 请求或调试配置。

完整详情请阅读 [Changelog](https://github.com/unclecode/crawl4ai/blob/main/CHANGELOG.md)。

---

## 📖 Documentation

🚨 **即将更新**：文档计划在下周进行全面更新，您可以提前查看当前版本的 [文档](https://docs.crawl4ai.com)。

---

## 📄 License & Attribution

此项目使用 Apache 2.0 许可证。查看 [LICENSE](https://github.com/unclecode/crawl4ai/blob/main/LICENSE)。

### 推荐添加「授权徽标」：
```html
<a href="https://github.com/unclecode/crawl4ai">
  <img src="https://img.shields.io/badge/Powered%20by-Crawl4AI-green?style=flat-square">
</a>
```

---

## 🤝 Contributing

我们欢迎开发者提交代码贡献！请阅读 [Contributing Guide](https://github.com/unclecode/crawl4ai/blob/main/CONTRIBUTORS.md)。

---

## 📈 Roadmap 

> 详情参考 [Roadmap](https://github.com/unclecode/crawl4ai/blob/main/ROADMAP.md)。

- [ ] 自然语言爬取支持
- [ ] 智能化网页嵌入索引
- [ ] Schema 自动生成工具
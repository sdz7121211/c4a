#coding:utf-8
import os
import asyncio
import json
from pydantic import BaseModel, Field
from typing import List
from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig, CacheMode, LLMConfig
from crawl4ai.extraction_strategy import LLMExtractionStrategy

class News(BaseModel):
    title: str
    url: str
    image_url: str

async def main():
    # 1. Define the LLM extraction strategy
    llm_strategy = LLMExtractionStrategy(
        llm_config = LLMConfig(provider="hosted_vllm/qwen-max", api_token="sk-ebc5640cb8cd4fb4937151bad251635e", base_url='https://dashscope.aliyuncs.com/compatible-mode/v1'),
        # llm_config = LLMConfig(provider="ollama/llama3.3:latest", api_token=None),
        # llm_config = LLMConfig(provider="ollama/deepseek-r1:8b", api_token=None),
        schema=News.model_json_schema(), # Or use model_json_schema()
        extraction_type="schema",
        instruction="提取页面“最新文章”模块新闻标题/新闻URL/新闻图片链接",
        chunk_token_threshold=2000,
        overlap_rate=0.0,
        apply_chunking=True,
        input_format="html",   # or "html", "fit_markdown"
        extra_args={"temperature": 0.0, "max_tokens": 2000}
    )

    # 2. Build the crawler config
    crawl_config = CrawlerRunConfig(
        extraction_strategy=llm_strategy,
        cache_mode=CacheMode.BYPASS
    )

    # 3. Create a browser config if needed
    browser_cfg = BrowserConfig(headless=False)

    async with AsyncWebCrawler(config=browser_cfg) as crawler:
        # 4. Let's say we want to crawl a single page
        result = await crawler.arun(
            url="https://36kr.com/",
            config=crawl_config
        )

        # print(result)

        if result.success:
            # 5. The extracted content is presumably JSON
            # print(result.extracted_content)
            # data = json.loads(result.extracted_content)
            print("Extracted items:", result.extracted_content)

            # 6. Show usage stats
            llm_strategy.show_usage()  # prints token usage
        else:
            print("Error:", result.error_message)

if __name__ == "__main__":
    asyncio.run(main())
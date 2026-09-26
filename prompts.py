"""Prompt templates for AI-powered text automation."""

SUMMARY_PROMPT = """
Summarize the following text clearly and concisely.

Text:
{text}
"""


SENTIMENT_PROMPT = """
Analyze the sentiment of the following text.

Classify the sentiment as positive, negative, or neutral
and briefly explain the reasoning.

Text:
{text}
"""


KEYWORD_PROMPT = """
Extract the most important keywords and key phrases
from the following text.

Return the keywords as a concise list.

Text:
{text}
"""


CLASSIFICATION_PROMPT = """
Classify the following text into the most appropriate
category and briefly explain the classification.

Text:
{text}
"""


TEXT_IMPROVEMENT_PROMPT = """
Improve the clarity, grammar, readability, and structure
of the following text while preserving its original meaning.

Text:
{text}
"""

# Accessible AI Research

## Mission 🚀

Make AI research accessible

## Problem ❓

Though creating "Responsible AI" or "AI For Social Good" is the responsibility of everyone, why is "AI Research" only accessible to technical folks in a language-using-a-lot-of-technical-jargons and not accessible to everyone in a layman-understandable-language?

## Solution 🔧 

Since Anthropic is leading the research of "Responsible AI" or "AI For Social Good", the solution revolves around Anthropic's research posts on its website. Let's think step by step:
- Step 1: Using a web-scraper, scrape some of Anthropic's research posts available on their website
- Step 2: Using LLM as a text simplifier, simplify the text and get it into a **similar HTML format** as that of the original website content
- Step 3: Showcase both, the **research-text-using-a-lot-of-technical-jargons** and the **research-text-in-a-layman-understandable-language** in a **side-by-side text comparison view** for better readability
- Step 4: Using LLM as a text translator, translate the **research-text-in-a-layman-understandable-language** to different languages in order to make AI research even more accessible
- Step 5: Present the translated text in a similar way as described in Step 3

## Prompt Engineering Process 🔁

### Note: Prompt Versioning was handled through a tool called PromptLayer. Here's a link to my prompts and how they evolved over time to achieve desirable results: https://promptlayer.com/prompt/9875

### Approach 1: Scrape the web content and give it entirely to the LLM for simplification without using the API

#### Steps:
- Step 1: Get the scraped HTML content of a particular research post
- Step 2: Give a prompt asking the LLM to simplify the research by giving the scraped HTML content as input while asking for the output to be in the similar HTML structure
- Step 3: Figure out another approach coz the LLM doesn't give any output complaining "Input-Text-Too-Long"

#### Challenges encountered:
- LLM didn't take the entire scraped HTML content in the prompt -> Outcome: "Input-Text-Too-Long" complain
- Tried breaking the scraped HTML content into chunks using LLM splitters and fed those chunks to the LLM -> Outcome: "I cannot generate HTML-formatted responses" complain
- Tried using those AI Doc Analyzer tools. Fed them with a file containing the scraped HTML content and asked it to simplify while keeping the output in a similar HTML structure -> Outcome: Instead of simplifying, it summarized the content and didn't keep the same HTML structure

#### Conclusion: No results were produced. Need to figure out another approach 😔

### Approach 2: Scrape the web content and give it paragraph-by-paragraph to the LLM for simplification without using the API (In short, do the simple thing that works before clever or optimized API approach)

#### Steps:
- Step 1: Get the scraped HTML content of a particular research post
- Step 2: Give a prompt asking the LLM to simplify the research by giving only a paragraph of the scraped HTML content as input while asking for the output to be in the similar HTML structure
- Step 3: Showcase both, the research-text-using-a-lot-of-technical-jargons and the research-text—in-a-layman-understandable-language in a side-by-side text comparison view for better readability
- Step 4: Give a prompt asking the LLM to translate the research-text—in-a-layman-understandable-language to French/Hindi by giving only a paragraph of the scraped HTML content as input while asking for the output to be in the similar HTML structure
- Step 5: Present the translated text in a similar way as described in Step 3

#### Challenges encountered:
- A lot of manual work is involved in giving the scraped HTML content paragraph-by-paragraph for simplification/translation to the LLM but produces the desired results
- With Claude in Slack, if it is not able to consume “large text”, it never communicated back by complaining that “the text is too large”. Instead, it remained silent and that was too annoying for me as a user
- With Claude in Slack, it wasn't preserving the HTML structure with Hindi as it was doing for layman's English and French

#### Conclusion: Desired results produced but a lot of manual work is involved, need to optimize the approach 🤔

### Approach 3: Scrape the web content and give it paragraph-by-paragraph to the LLM for simplification using the OpenAI API (Coz didn’t get access to Claude API yet)

#### Steps:
- Step 1: Get the scraped HTML content of a particular research post
- Step 2: Give a prompt asking the LLM to simplify the research by giving only a paragraph of the scraped HTML content as input while asking for the output to be in a similar HTML structure in an API request
- Step 3: Figure out another API approach coz the API doesn't give the output in the same HTML structure as that of the input

#### Challenges encountered:
- Structuring the API request was a mess with a lot of HTML text involved in the request itself -> reminded me of the regex classes of my undergrad
- Constant fear of overspending with multiple API requests just for a POC

#### Conclusion: Satisfactory results achieved 

### Approach 4: Make the LLM scrape the required web content, simplify it and return both the original and simplified text in the same HTML structure using the API

#### Steps:
- Step 1: Give a prompt asking the LLM to perform 3 steps to complete the task: i) Scrape the required web content on its end ii) Simplify the scraped HTML content iii) Return the original-text-containing-technical-jargons and the simplified-text-containing-layman-terms in the same HTML structure as API response
- Step 2: LLM politely refused due to legal and ethical concerns about web scraping

#### Challenges encountered:
- Crafting a complex prompt that didn't yield desired results but was for the social good

#### Conclusion: AI is being ethical 🎯

## UI/UX challenges 📱

With the information overload that LLMs have empowered us with, I feel UI/UX is the biggest challenge in presenting that information in a user-friendly way. I faced that challenge too. To overcome this challenge, I exercised my 5 years of Product experience & implemented a side-by-side text comparison view with research-text-using-a-lot-of-technical-jargons on one side and the research-text-in-a-layman-understandable-language on the other for better readability. 

#### Conclusion: The side-by-side text comparison UI view of the project worked for 8 out of 10 non-tech folks 📝

## Impact 🌟

More AI research will be made accessible and understandable by laymen that too in their own language, and there will be more awareness among people about “AI For Social Good” or “Responsible AI”. Hopefully, more people might be inclined towards contributing to the research of “AI For Social Good” or “Responsible AI” as well :)

## Project In Action 📄

### Video Link: https://youtu.be/biER7Sl3PXI

### Screenshots:

<img width="1371" alt="Tech vs Layman" src="https://github.com/aashkafirst/AccessibleAIResearch/assets/20123268/1b6a1a36-3820-4c47-af3e-667398cec4b5">

<img width="1375" alt="Tech vs French Layman" src="https://github.com/aashkafirst/AccessibleAIResearch/assets/20123268/f4a560d6-49cf-4007-a047-0b6122b69d2e">

<img width="1375" alt="Tech vs Hindi Layman" src="https://github.com/aashkafirst/AccessibleAIResearch/assets/20123268/2efeea1e-7a67-46da-a591-34b1147b0db8">

## Scope For Improvement 📌 

In my opinion, the following are the improvement areas for the project:
- Extend it to multiple languages

I’m open to suggestions 🤗

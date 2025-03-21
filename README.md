# J.A.R.V.I.S. - Browser Agent

A command-line browser automation agent powered by GPT-4 and LangChain.

## Prerequisites
* Requires Python 3.11 or higher.
* Assumes you already have `uv` installed. If not, install it with `pip install uv`.

## Installation

* Clone this repository:

```bash
git clone https://github.com/davydany/jarvis.git jarvis
```

* Install dependencies:

```bash
cd jarvis
uv sync
```

## Usage

Make sure that `OPENAI_API_KEY` is already set in your environment variables.

```bash
export OPENAI_API_KEY=<your-openai-api-key>
uv run python jarvis.py "<describe your task here>"
```

```bash
uv run python jarvis.py "Find fencing companies with 4.5 or larger reviews in the Jacksonville Area."
```
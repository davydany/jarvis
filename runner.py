import click

from langchain_openai import ChatOpenAI
from browser_use import Agent, Browser, BrowserConfig, SystemPrompt

from dotenv import load_dotenv
load_dotenv()

import asyncio

MODEL = "gpt-4o"

llm = ChatOpenAI(model=MODEL)


browser = Browser(
    config=BrowserConfig(
        # Specify the path to your Chrome executable
        chrome_instance_path='/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',  # macOS path
        # For Windows, typically: 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe'
        # For Linux, typically: '/usr/bin/google-chrome'
    )
)

class MySystemPrompt(SystemPrompt):

    def important_rules(self) -> str:
        # Get existing rules from parent class
        existing_rules = super().important_rules()

        # Add your custom rules
        new_rules = f"""
        9. You will present your output in {self.output_type} format.
        10. If you encounter a captcha, leave the site, and move to the next one.
        """

        # Make sure to use this pattern otherwise the exiting rules will be lost
        return f'{existing_rules}\n{new_rules}'

async def main(task: str, output_type: str = "markdown"):
    # Create the agent with your configured browser
    MySystemPrompt.output_type = output_type
    agent = Agent(
        task=task,
        llm=ChatOpenAI(model='gpt-4o'),
        system_prompt_class=MySystemPrompt,
        # browser=browser,
    )

    result = await agent.run()
    if result:
        click.secho(result, fg='yellow')
    else:
        print("No results found.", fg='red')



@click.command()
@click.argument("task", type=str)
@click.option("-o", "--output-type", type=click.Choice(["markdown", "json"]), default="markdown", help="Output type for the task. (default: markdown)")
def jarvis(task: str, output_type: str):
    """
    Command line interface for the Jarvis, my Browser Agent.
    """
    click.clear()
    click.secho("Welcome to the Jarvis CLI!", fg="green")
    click.secho(f"Received Task: {task}", fg="cyan")

    asyncio.run(main(task))


    click.secho("Processing task...", fg="yellow")

if __name__ == "__main__":
    jarvis()
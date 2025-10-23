# Search tool
from langchain_community.tools import DuckDuckGoSearchRun

search_tool = DuckDuckGoSearchRun()

result = search_tool.invoke("what is ipl")

print(result)

from langchain_community.tools import ShellTool

shell_tool = ShellTool()

output = shell_tool.invoke('whoami')

print(output)
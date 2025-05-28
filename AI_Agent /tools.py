from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain.tools import Tool
from datatime import datatime 

search = DuckDuckGoSearchRun()
search_tool = Tool(
    name = "search",
    func = search.run, 
    description = "Search the web for information", 
)
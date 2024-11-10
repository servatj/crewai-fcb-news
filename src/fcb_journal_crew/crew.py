from dotenv import load_dotenv
load_dotenv()

import os

from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import SerperDevTool


@CrewBase
class FcbJournalCrewCrew():
	"""FcbJournalCrew crew"""

	@agent
	def sports_analyst(self) -> Agent:
		return Agent(
				config=self.agents_config['sports_analyst'],
				tools=[SerperDevTool()],
				verbose=True
		)
	
	@agent
	def sports_writer(self) -> Agent:
		return Agent(
				config=self.agents_config['sports_writer']
		)
	
	@task
	def fetch_next_game_task(self) -> Task:
		return Task(
			config=self.tasks_config['fetch_next_game_task'],
		)
	
	@task
	def write_sports_article_task(self) -> Task:
		return Task(
			config=self.tasks_config['write_sports_article_task'],
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the FcbJournalCrew crew"""
		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=True,
			# process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
		)
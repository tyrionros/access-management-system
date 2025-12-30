from abc import ABC, abstractmethod

class BaseAgent(ABC):
    """
    Abstract base class for all specialized agents.
    """

    def __init__(self):
        self.tools = []

    @abstractmethod
    def get_persona(self) -> str:
        """
        Returns the persona of the agent (e.g., 'Requestor', 'Approver').
        """
        pass

    @abstractmethod
    def get_tools(self) -> list:
        """
        Returns the list of tools available to the agent.
        """
        pass

    @abstractmethod
    def process_request(self, query: str) -> str:
        """
        Processes a user query and returns a response.
        """
        pass

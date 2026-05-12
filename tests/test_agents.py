import unittest
from src.agents.orchestrator import AgentOrchestrator
from src.agents.requestor_agent import RequestorAgent
from src.agents.approver_agent import ApproverAgent
from src.agents.admin_agent import AdminAgent

class TestAgents(unittest.TestCase):

    def setUp(self):
        self.orchestrator = AgentOrchestrator()
        self.orchestrator.register_agent(RequestorAgent())
        self.orchestrator.register_agent(ApproverAgent())
        self.orchestrator.register_agent(AdminAgent())

    def test_requestor_search(self):
        response = self.orchestrator.route_request("Requestor", "find sales roles")
        self.assertIn("Salesperson", response)
        self.assertIn("D365 Sales", response)

    def test_requestor_no_results(self):
        response = self.orchestrator.route_request("Requestor", "find something nonexistent")
        self.assertIn("I couldn't find any roles matching", response)

    def test_approver_history(self):
        response = self.orchestrator.route_request("Approver", "view history for Priya")
        self.assertIn("Access history for priya", response)
        self.assertIn("Salesperson", response)

    def test_admin_audit_logs(self):
        response = self.orchestrator.route_request("Admin", "show me the audit logs")
        self.assertIn("Latest audit logs", response)
        self.assertIn("Updated Role", response)

if __name__ == '__main__':
    unittest.main()

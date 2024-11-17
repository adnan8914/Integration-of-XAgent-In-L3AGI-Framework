from dialogue_agent_with_tools import DialogueAgentWithTools

class ConversationalAgent:
    def __init__(self, system_message: str = None):
        self.system_message = system_message or "You are a helpful assistant."
        self.agent = DialogueAgentWithTools(
            name="ConversationalAgent",
            system_message=self.system_message
        )
        
    async def process_message(self, message: str) -> str:
        """Process message using XAgent-enabled DialogueAgent"""
        response = await self.agent.send(message)
        return response 
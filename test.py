import asyncio
from conversational import ConversationalAgent

async def test_xagent_integration():
    # Initialize agent
    agent = ConversationalAgent(
        system_message="You are a helpful assistant with XAgent capabilities."
    )
    
    # Test messages
    test_messages = [
        "Hello, can you help me?",
        "What can XAgent do?",
        "Process this request with XAgent"
    ]
    
    # Process test messages
    for message in test_messages:
        print(f"\nUser: {message}")
        response = await agent.process_message(message)
        print(f"Agent: {response}")

if __name__ == "__main__":
    # Run the test
    asyncio.run(test_xagent_integration()) 
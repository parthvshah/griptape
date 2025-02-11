import json
from griptape.memory.structure import ConversationMemory, Run


class TestConversationMemory:
    def test_is_empty(self):
        memory = ConversationMemory()

        assert memory.is_empty()

        memory.add_run(Run(input="test", output="test"))

        assert not memory.is_empty()

    def test_add_run(self):
        memory = ConversationMemory()
        run = Run(input="test", output="test")

        memory.add_run(run)

        assert memory.runs[0] == run

    def test_to_string(self):
        memory = ConversationMemory()
        run = Run(input="test", output="test")

        memory.add_run(run)

        assert "Input: test\nOutput: test" in memory.to_prompt_string()

    def test_to_json(self):
        memory = ConversationMemory()
        memory.add_run(Run(input="foo", output="bar"))

        assert json.loads(memory.to_json())["type"] == "ConversationMemory"
        assert json.loads(memory.to_json())["runs"][0]["input"] == "foo"

    def test_to_dict(self):
        memory = ConversationMemory()
        memory.add_run(Run(input="foo", output="bar"))

        assert memory.to_dict()["type"] == "ConversationMemory"
        assert memory.to_dict()["runs"][0]["input"] == "foo"

    def test_from_dict(self):
        memory = ConversationMemory()
        memory.add_run(Run(input="foo", output="bar"))
        memory_dict = memory.to_dict()

        assert isinstance(memory.from_dict(memory_dict), ConversationMemory)
        assert memory.from_dict(memory_dict).runs[0].input == "foo"

    def test_from_json(self):
        memory = ConversationMemory()
        memory.add_run(Run(input="foo", output="bar"))
        memory_dict = memory.to_dict()

        assert isinstance(memory.from_dict(memory_dict), ConversationMemory)
        assert memory.from_dict(memory_dict).runs[0].input == "foo"

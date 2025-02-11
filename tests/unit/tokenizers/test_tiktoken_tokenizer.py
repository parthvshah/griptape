import pytest
from griptape.tokenizers import TiktokenTokenizer


class TestTiktokenTokenizer:
    @pytest.fixture
    def tokenizer(self):
        return TiktokenTokenizer()

    def test_encode(self, tokenizer):
        assert tokenizer.encode("foo bar") == [8134, 3703]

    def test_decode(self, tokenizer):
        assert tokenizer.decode([8134, 3703]) == "foo bar"

    def test_token_count(self, tokenizer):
        assert tokenizer.token_count("foo bar huzzah") == 5

    def test_tokens_left(self, tokenizer):
        assert tokenizer.tokens_left("foo bar huzzah") == 4083

    def test_encoding(self, tokenizer):
        assert tokenizer.encoding.name == "cl100k_base"

    def test_chunk_tokens(self, tokenizer):
        tokens = tokenizer.encode("foo bar")

        assert [chunk for chunk in tokenizer.chunk_tokens(tokens)] == [(8134, 3703)]

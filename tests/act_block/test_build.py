import pytest

from flake8_aaa.act_block import ActBlock
from flake8_aaa.exceptions import NotActionBlock


# TODO act blocks need testing with 'result =' indented
# TODO act blocks need testing with indentation in general

@pytest.mark.parametrize(
    'code_str, expected_type', [
        ('result = do_thing()', ActBlock.RESULT_ASSIGNMENT),
        ('with pytest.raises(Exception):\n    do_thing()', ActBlock.PYTEST_RAISES),
        ('data[new_key] = value  # act', ActBlock.MARKED_ACT),
    ]
)
def test(code_str, expected_type, first_node_with_tokens):
    result = ActBlock.build(first_node_with_tokens)

    assert isinstance(result, ActBlock)
    assert result.node == first_node_with_tokens
    assert result.block_type == expected_type


@pytest.mark.parametrize(
    'code_str', [
        'act = "#"',
        'actions +=1  # actions speak louder than words!',
        'person = User("Rene")',
        'result += 1',
        'results = news.post()',
        'with open("data.txt") as f:\n    f.read()',
    ]
)
def test_not_actions(first_node_with_tokens):
    with pytest.raises(NotActionBlock):
        ActBlock.build(first_node_with_tokens)

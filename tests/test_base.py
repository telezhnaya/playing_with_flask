from app import create_app
from pytest import fixture

# Usage:
# python -m pytest


class TestBasics:
    # usage with context
    @fixture(autouse=True)
    def run_around_tests(self):
        # Before tests
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        yield
        # After tests
        self.app_context.pop()

    def test_app_exists(self):
        assert self.app_context


# usage without context
def test_qw():
    assert 42 == 42

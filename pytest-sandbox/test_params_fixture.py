#!/usr/bin/env python3
# vim: set fileencoding=utf-8 :

import pytest
import dataclasses
import typing


@dataclasses.dataclass(frozen=True)
class Fixture():
    name: str
    division: str = ""
    details: typing.List = dataclasses .field(default_factory=list)


targets = (
    Fixture("foo", details=[1, 2]),
    Fixture("bar", details=[1, 2, 3, 4]),
)


def idfunc(f: Fixture):
    return f'{f.name}'


@pytest.fixture(params=targets, ids=idfunc)
def fi(request):
    print("Start fixtur.")
    yield request.param
    print("End fixture.")


def pytest_generate_tests(metafunc):
    if 'details' in metafunc.fixturenames:
        metafunc.parametrize("details", range(5))


class Test_最初のシートテスト():
    """最初のシートテスト
    """

    def test_aがbであること(self, fi: Fixture):
        """テストAがBであること
        """
        print("hoge")
        assert 1 == 1

    def test_bがcでないこと(self, fi: Fixture, details):
        """～が～であること
        """
        assert 1 == 1


class Test_2つめのシート():
    """2つめのテスト用
    """
    def test_tashizan(self):
        assert 1 == 1


if __name__ == '__main__':
    pytest.main()

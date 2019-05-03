#!/usr/bin/env python3
# vim: set fileencoding=utf-8 :

import pytest
import dataclasses


@dataclasses.dataclass(frozen=True)
class Fixture():
    name: str
    division: str = ""


@pytest.mark.parametrize("fi", [
    Fixture("foo"),
    Fixture("bar"),
])
class Test_１つめのシートテスト():
    """最初のシートテスト
    """

    def test_最初のテスト群(self, fi: Fixture):

        def test_aがbであること(self, fi: Fixture):
            """テストAがBであること
            """
            assert fi.name == "foo"

        def test_bがcでないこと(self, fi: Fixture):
            """～が～であること
            """
            assert 1 == 3

        def test_ほげがふがであること(self, fi: Fixture):
            assert 1 == 1


class Test_２つめのシートテスト():
    """2つめのテスト用
    """
    def test_tashizan(self):
        assert 1 == 1


if __name__ == '__main__':
    pytest.main()

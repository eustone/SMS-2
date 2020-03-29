import pytest
from courses import subjects
def test_make_subject():
    sb1 = Subject('BK','BookKeeping','BookKeeping Accounting')
    assert sb1.__init__('BK','BookKeeping','BookKeeping Accounting')
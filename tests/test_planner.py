from datetime import date

from planner import completion_rate, days_left, is_urgent, sort_by_due


# This test is already written for you. Read it, then run pytest.
def test_days_left_counts_days_until_due():
    # Arrange
    today = date(2026, 10, 19)
    due = date(2026, 10, 22)
    # Act
    result = days_left(due, today)
    # Assert
    assert result == 3


# Now write the tests below. Use the same three steps: Arrange, Act, Assert.
# TODO 1: days_left is negative when the task is overdue.
def test_days_left_is_negative_when_overdue():
    today=date(2026,10,22)
    due=date(2026,10,20)
    result=days_left(due,today)
    assert result==-2

# TODO 2: is_urgent is True when the task is due tomorrow.
def test_is_urgent_true_when_due_tomorrow():
    today=date(2026,10,19)
    due=date(2026,10,20)
    result=is_urgent(due,today)
    assert result is True

# TODO 3: is_urgent is True when the task is due in exactly 2 days (the limit).
def test_is_urgent_when_due_exactly_2days():
    today=date(2026,10,19)
    due=date(2026,10,21)
    result=is_urgent(due,today)
    assert result is True

# TODO 4: is_urgent is False when the task is overdue.
def test_is_not_urgent_when_overdue():
    today=date(2026,10,19)
    due=date(2026,10,18)
    result=is_urgent(due,today)
    assert result is False

# TODO 5: sort_by_due puts the soonest task first.
def test_sort_by_due_puts_earliest_first():
    tasks=[
        {"title":"Submit FYP report","due":date(2026,10,25)},
        {"title":"Quiz","due":date(2026,10,20)},
        {"title":"Meeting with supervisor","due":date(2026,10,22)},
    ]
    result=sort_by_due(tasks)
    assert result[0]["title"]=="Quiz"
    assert result[1]["title"]=="Meeting with supervisor"
    assert result[2]["title"]=="Submit FYP report"

# TODO 6: completion_rate returns 0.0 when there are no tasks.
def test_completion_rate_returns_zero_when_no_tasks():
    done=0
    total=0
    result=completion_rate(done,total)
    assert result==0.0

# TODO 7: completion_rate(1, 3) returns 33.3.
def test_completion_rate_returns_one_third():
    done=1
    total=3
    result=completion_rate(done,total)
    assert result==33.3
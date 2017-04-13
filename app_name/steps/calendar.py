from behave import given
from app_name.pages.trainings import TrainingsPage
from app_name.pages.calendar import CalendarPage


@given("I am on Calendar-tr page")
def load_page(context):
    """
    This is done like this intentionally
    """
    TrainingsPage(context).navigate()
    at_page = CalendarPage(context).at()
    assert not at_page  # just a sample assert, not a real use

from behave import given
from app_name.pages.trainings import TrainingsPage


@given("I am on Trainings page")
def load_page(context):
    at_page = TrainingsPage(context).navigate().at()
    assert at_page  # just a sample assert, not a real use

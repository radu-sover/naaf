"""
This would be a generic steps module - common actions to Pages and Elements.
This steps were suposed to be implemented in the framework: naaf.page_steps,
but I had some issues with "reflection" and for now is here.

Should I continue with this generalization?
Feature files will be more conventions and will eliminate the need of separate
steps, meaning somebody will need to write more on a feature Given, When, Then.
"""
from behave import given, when, then, step
# from naaf.page_steps import *  # NOQA
from naaf.base import CurrentPage
from app_name.pages.calendar import *  # NOQA
from app_name.pages.trainings import *  # NOQA
from app_name.pages.navigation import *  # NOQA


@given('I am on "{page_class_name}" page')
def navigate_to_page(context, page_class_name):
    # this translates to: page_class_name(context).navigate()
    page_class = _str_to_class(page_class_name)
    page = page_class(context).navigate()
    assert page.at()


@when('I click on "{button_name}" from "{page_class_name}"')
def button_click(context, button_name, page_class_name):
    # this translates to: page_class_name(context).button_name()
    page_class = _str_to_class(page_class_name)
    page = page_class(context)
    button = getattr(page, button_name)
    button()


@when('I type "{text}" in "{form_element_name}" from "{page_class_name}"')
def type_text(context, text, form_element_name, page_class_name):
    # this translates to: page_class_name(context).form_name(text)
    page_class = _str_to_class(page_class_name)
    page = page_class(context)
    form_element = getattr(page, form_element_name)
    form_element(text)


@when(
    'I select "{option_text}" in "{select_element_name}" from "{page_class_name}"')
def select_option(context, option_text, select_element_name, page_class_name):
    # this translates to: page_class_name(context).select_name(option)
    page_class = _str_to_class(page_class_name)
    page = page_class(context)
    select_element = getattr(page, select_element_name)
    select_element(option_text)


@when(
    'I click on "{button_name}" for "{text}" training from "{page_class_name}"')
def button_click_in_list(context, button_name, text, page_class_name):
    # translates to: page_class_name(context).btn_edit_for_item(text)
    page_class = _str_to_class(page_class_name)
    page = page_class(context)

    contains_function = getattr(page, button_name + '_for_item')
    contains_function(text)


@when('I wait for {seconds:Number} seconds')
def wait_for_seconds(context, seconds):
    CurrentPage(context).wait(seconds)


@then('I see in page "{search_text}"')
def search_in_page(context, search_text):
    """
    Strange but does not find text in page_source.
    The content of page_source is correct.
    """
    assert search_text in CurrentPage(context)


@then('I am at "{page_class_name}" page')
def at_page(context, page_class_name):
    # this translates to: page_class_name(context).at()
    page_class = _str_to_class(page_class_name)
    assert page_class(context).at()


@step('I see the "{text}" in "{list_name}" from "{page_class_name}"')
def search_in_list(context, text, list_name, page_class_name):
    # translates to: page_class_name(context).list_name_contains(text)
    page_class = _str_to_class(page_class_name)
    page = page_class(context)

    contains_function = getattr(page, list_name + '_contains')
    assert contains_function(text)


@then('I do not see the "{text}" in "{list_name}" from "{page_class_name}"')
def search_in_list_not_finding(context, text, list_name, page_class_name):
    # translates to: page_class_name(context).list_name_contains(text)
    page_class = _str_to_class(page_class_name)
    page = page_class(context)

    contains_function = getattr(page, list_name + '_contains')
    assert not contains_function(text)


def _str_to_class(s):
    return globals().get(s)

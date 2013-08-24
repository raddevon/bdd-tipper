@when(u'I go to the tip calculator')
def step_impl(context):
    context.browser.get('http://localhost:5000')


@then(u'I should see the calculator form')
def step_impl(context):
    context.browser.title == "Tip calculator"


@when(u'I submit the form with a valid total and tip percentage')
def step_impl(context):
    br = context.browser
    br.get('http://localhost:5000')
    meal_cost = br.find_element_by_name('meal_cost')
    meal_cost.send_keys('30')
    tip_percentage = br.find_element_by_name('tip_percentage')
    tip_percentage.send_keys('20')
    br.find_element_by_id('submit').click()


@when(u'I enter a <{field}> of "{value}"')
def step_impl(context, field, value):
    br = context.browser
    field = br.find_element_by_name(field)
    if value != "(blank)":
        field.send_keys(value)


@when(u'I click submit')
def step_impl(context):
    context.browser.find_element_by_id('submit').click()


@then(u'I should see the results page')
def step_impl(context):
    br = context.browser
    assert br.find_element_by_id('results')


@then(u'I should see a result of "{result}"')
def step_impl(context, result):
    br = context.browser
    results_el = br.find_element_by_id('results')
    assert result in results_el.text

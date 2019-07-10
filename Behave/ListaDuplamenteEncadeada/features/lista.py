from behave import *

use_step_matcher("re")


@given("uma lista vazia")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Given uma lista vazia')


@when("eu crio o primeiro nó")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: When eu crio o primeiro nó')


@then("eu tenho uma lista com um nó")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Then eu tenho uma lista com um nó')


@given("uma lista não vazia")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Given uma lista não vazia')


@when("eu acrescento um nó")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: When eu acrescento um nó')


@then("eu tenho uma lista com mais de um nó")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Then eu tenho uma lista com mais de um nó')


@given("uma lista cheia")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Given uma lista cheia')


@when("eu tento acrescentar um nó")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: When eu tento acrescentar um nó')


@then("o sistema exibe uma mensagem de erro")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Then o sistema exibe uma mensagem de erro')
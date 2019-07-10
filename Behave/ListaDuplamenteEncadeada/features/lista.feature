# Created by dchristofolli at 09/07/2019
Feature: Cria um nó em uma lista duplamente encadeada

  Scenario: Cria o primeiro nó na lista.
    Given uma lista vazia
    When eu crio o primeiro nó
    Then eu tenho uma lista com um nó

  Scenario: Acrescenta um nó na lista.
    Given uma lista não vazia
    When eu acrescento um nó
    Then eu tenho uma lista com mais de um nó

  Scenario: Tenta criar um nó em uma lista cheia.
    Given uma lista cheia
    When eu tento acrescentar um nó
    Then o sistema exibe uma mensagem de erro
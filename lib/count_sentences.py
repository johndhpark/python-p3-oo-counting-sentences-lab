#!/usr/bin/env python3

import re

class MyString:
  def __init__(self, value = ""):
    self.value = value

  def set_value(self, value):
    if type(value) != str:
      print("The value must be a string.")
      return

    self._value = value

  def get_value(self):
    return self._value


  value = property(get_value, set_value)

  def is_sentence(self):
    return self._value.endswith(".")

  def is_question(self):
    return self._value.endswith("?")

  def is_exclamation(self):
    return self._value.endswith("!")

  def count_sentences(self):
    pattern = r"[.?!]+"

    sentences = re.split(pattern, self._value)

    print(sentences)

    return len(sentences) - 1

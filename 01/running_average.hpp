/*

CE LINK: https://godbolt.org/z/3oMzTGjhK

TODO: Identify properties that are worth testing,
 and implement tests for them.

 Suggested properties to test:
  - Average is correctly calculated for a small list
  - Item count is correct before/after adding items
*/

#pragma once
#include <cstddef>

class RunningAverage {
public:
  RunningAverage() : average(0.0), item_count(0) {}

  double current_average() { return average; }

  std::size_t current_item_count() { return item_count; }

  void add_item(double item) {
    auto total = average * item_count;
    auto new_total = total + item;
    item_count += 1;
    average = new_total / item_count;
  }

private:
  double average;
  std::size_t item_count;
};

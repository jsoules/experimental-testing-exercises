#pragma once
#include <cstddef>
#include <iostream>

class RunningAverage {
public:
  RunningAverage() : average(0.0), item_count(0) {}

  double current_average() {
    return average;
  }

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

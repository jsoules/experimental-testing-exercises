
/*

CE LINK: https://godbolt.org/z/f9Pbq3c8f

*/

#include <cmath>
#include <gtest/gtest.h>
#include <numeric>
#include <vector>

#include "running_average.hpp"

TEST(RunningAverage, InitialState) {
  RunningAverage ra{};
  EXPECT_DOUBLE_EQ(ra.current_average(), 0.0);
  EXPECT_EQ(ra.current_item_count(), 0);
}

TEST(RunningAverage, SingleItem) {
  RunningAverage ra{};
  ra.add_item(5.0);
  EXPECT_DOUBLE_EQ(ra.current_average(), 5.0);
  EXPECT_EQ(ra.current_item_count(), 1);
}

TEST(RunningAverage, MultipleItems) {
  RunningAverage ra{};
  std::vector<double> items = {2.0, 1e30, 4.0, 6.0, 0};

  for (const auto &item : items) {
    ra.add_item(item);
  }
  EXPECT_EQ(ra.current_item_count(), items.size());
  double expected_average =
      std::accumulate(items.begin(), items.end(), 0.0) / items.size();
  EXPECT_DOUBLE_EQ(ra.current_average(), expected_average);
}

int main(int argc, char **argv) {
  testing::InitGoogleTest(&argc, argv);
  return RUN_ALL_TESTS();
}

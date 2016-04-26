# include <iostream>
# include <cmath>

int
main() {
    auto n = 1;
    auto counter = 2;

    bool prime = true;
    while (counter <= 10001) {
        n += 2;
        prime = true;
        for (auto i = 2; i < static_cast<int>(sqrt(n)) +1; ++i) {
            if (n%i == 0) {
                prime = false;
                break;
            }
        }
        if (prime) {
            counter += 1;
        }
    }

    std::cout << "*** Computed " << n;
    std::cout << std::endl;

    return 0;
}

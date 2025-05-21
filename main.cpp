#include <iostream>
#include <sstream>
#include <string>

int main() {
    std::cout << "Simple Calculator" << std::endl;
    std::cout << "Enter expressions in the form: number operator number" << std::endl;
    std::cout << "Supported operators: + - * /" << std::endl;
    std::cout << "Type 'quit' to exit." << std::endl;

    std::string line;
    while (true) {
        std::cout << "> ";
        if (!std::getline(std::cin, line)) {
            break;
        }
        if (line == "quit" || line == "exit") {
            std::cout << "Goodbye!" << std::endl;
            break;
        }
        std::istringstream iss(line);
        double a, b;
        char op;
        if (!(iss >> a >> op >> b)) {
            std::cout << "Invalid expression" << std::endl;
            continue;
        }
        double result;
        switch (op) {
            case '+':
                result = a + b;
                break;
            case '-':
                result = a - b;
                break;
            case '*':
                result = a * b;
                break;
            case '/':
                if (b == 0) {
                    std::cout << "Error: Division by zero" << std::endl;
                    continue;
                }
                result = a / b;
                break;
            default:
                std::cout << "Unknown operator" << std::endl;
                continue;
        }
        std::cout << "Result: " << result << std::endl;
    }

    return 0;
}

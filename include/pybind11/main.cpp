#include "/pybind11/embed.h"

#include <iostream>
#include <vector>
#include <map>
#include <string> 
#include <set>
 
namespace py = pybind11; 

class CSPSolver {
public:
    using Variables = std::vector<std::string>;

    
    using Domains = std::map<std::string, std::set<std::string>>;
    
    using Constraints = std::vector<std::function<bool(const std::map<std::string, std::string>&)>>;

    // Constructor to initialize variables, domains, and constraints
    
    CSPSolver(const Variables& vars, const Domains& doms, const Constraints& cons)
        : variables(vars), domains(doms), constraints(cons) {}

    // Backtracking algorithm to find a solution

    bool backtrack(std::map<std::string, std::string>& assignment) {
        if (assignment.size() == variables.size()) {
            return true; // Solution found
        }

        std::string var = select_unassigned_variable(assignment);
        for (const auto& value : domains[var]) {
            if (is_consistent(var, value, assignment)) {
                assignment[var] = value;
                if (backtrack(assignment)) {
                    return true; // Solution found
                }
                assignment.erase(var);
            }
        }

        return false; // No solution found
    }

    // Method to solve the CSP
    std::map<std::string, std::string> solve() {

        
        std::map<std::string, std::string> assignment; 
        if (backtrack(assignment)) {
            return assignment; // Return the assignment if solution found
        } else {
            return {}; // Return empty assignment if no solution found
        }
    }

private:
    Variables variables; // List of variables
    Domains domains; // Map of variable domains
    Constraints constraints; // List of constraints

    // Method to select an unassigned variable
    std::string select_unassigned_variable(const std::map<std::string, std::string>& assignment) {
        for (const auto& var : variables) {
            if (assignment.find(var) == assignment.end()) {
                return var; // Return the first unassigned variable found
            }
        }
        throw std::runtime_error("No unassigned variables found");
    }

    // Method to check if an assignment is consistent with the constraints
    bool is_consistent(const std::string& var, const std::string& value, const std::map<std::string, std::string>& assignment) {
        std::map<std::string, std::string> local_assignment = assignment;
        local_assignment[var] = value;

        for (const auto& constraint : constraints) {
            if (!constraint(local_assignment)) {
                return false; // Assignment is not consistent with a constraint
            }
        }

        return true; // Assignment is consistent with all constraints
    }
};

int main() 

{
    py::scoped_interpreter guard{}; // Initialize Python interpreter

    py::module nltk = py::module::import("nltk");
    nltk.attr("download")("averaged_perceptron_tagger"); // Download NLTK data

    py::module pos_tag = py::module::import("nltk.tag").attr("pos_tag");

    std::string sentence = "The quick brown fox jumps over the lazy dog";
    py::list words = nltk.attr("word_tokenize")(sentence); // Tokenize the sentence
    py::list tagged_words = pos_tag(words); // Perform POS tagging

    std::vector<std::string> variables;
    std::map<std::string, std::set<std::string>> domains;

    // Extract words and their corresponding POS tags
    for (auto item : tagged_words) {
        std::string word = item[0].cast<std::string>();

        
        std::string tag = item[1].cast<std::string>();
        
        variables.push_back(word);
        
        domains[word] = {tag};
    }

    CSPSolver::Constraints constraints;
    // Add appropriate grammatical constraints here

    CSPSolver solver(variables, domains, constraints);
    auto solution = solver.solve(); // Solve the CSP

    // Print the solution (word : POS tag)
    for (const auto& pair : solution) 
    
    {
        std::cout << pair.first << ": " << pair.second << std::endl;
    }

    return 0;
}

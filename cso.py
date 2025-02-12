import numpy as np

class CelestialSwarmOptimizer:
    """
    Celestial Swarm Optimization (CSO) Algorithm.
    Inspired by gravitational forces in celestial mechanics, this algorithm balances 
    exploration and exploitation by pulling candidate solutions toward the global best 
    and a dynamically calculated center of mass.
    """

    def __init__(self, population_size=50, max_iterations=100, stagnation_thresh=10):
        """
        Initialize the CSO optimizer.

        :param population_size: Number of candidate solutions (swarm size).
        :param max_iterations: Maximum number of iterations.
        :param stagnation_thresh: Threshold for stagnation before a cosmic leap.
        """
        self.population_size = population_size
        self.max_iterations = max_iterations
        self.stagnation_thresh = stagnation_thresh
        self.epsilon = 1e-6  # Small constant for numerical stability

    def initialize_population(self, problem_size, lower_bound=0, upper_bound=1):
        """
        Initializes the population randomly within the given bounds.

        :param problem_size: Number of dimensions (tasks).
        :param lower_bound: Minimum value for each dimension.
        :param upper_bound: Maximum value for each dimension.
        :return: Initialized population and fitness values.
        """
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound

        # Randomly initialize candidate solutions
        self.population = np.random.uniform(lower_bound, upper_bound, 
                                            (self.population_size, problem_size))
        self.fitness = np.full(self.population_size, np.inf)
        self.stagnation_count = np.zeros(self.population_size, dtype=int)

    def evaluate_population(self, objective_function):
        """
        Evaluates the fitness of each candidate solution.

        :param objective_function: Function to evaluate optimization.
        """
        for i in range(self.population_size):
            self.fitness[i] = objective_function(self.population[i])

    def compute_center_of_mass(self):
        """
        Computes the center of mass of the swarm based on the fitness of solutions.

        :return: Center of mass vector.
        """
        # Compute weight inversely proportional to fitness
        weights = 1.0 / (self.fitness + self.epsilon)
        total_weight = np.sum(weights)

        # Compute weighted center of mass
        center_of_mass = np.sum(self.population * weights[:, np.newaxis], axis=0) / total_weight
        return center_of_mass

    def update_positions(self):
        """
        Updates the position of each solution using gravitational attraction to 
        both the best solution and the center of mass.
        """
        global_best_idx = np.argmin(self.fitness)
        global_best = self.population[global_best_idx]
        center_of_mass = self.compute_center_of_mass()

        # Update each solution's position
        for i in range(self.population_size):
            # Calculate gravitational attraction forces
            force_global = 0.4 * (global_best - self.population[i])
            force_center = 0.4 * (center_of_mass - self.population[i])
            noise = 0.1 * np.random.uniform(-1, 1, self.population.shape[1])

            # Update position
            self.population[i] += force_global + force_center + noise
            self.population[i] = np.clip(self.population[i], self.lower_bound, self.upper_bound)

    def apply_cosmic_leaps(self):
        """
        Reinitialize solutions that have stagnated for too long.
        """
        for i in range(self.population_size):
            if self.stagnation_count[i] >= self.stagnation_thresh:
                self.population[i] = np.random.uniform(self.lower_bound, self.upper_bound, 
                                                       self.population.shape[1])
                self.fitness[i] = np.inf
                self.stagnation_count[i] = 0  # Reset stagnation counter

    def solve(self, problem):
        """
        Runs the CSO algorithm to optimize the given problem.

        :param problem: Dictionary containing the objective function and problem size.
        :return: Best solution, best fitness value, and fitness history.
        """
        problem_size = problem["problem_size"]
        objective_function = problem["obj_func"]

        # Initialize population
        self.initialize_population(problem_size)
        self.evaluate_population(objective_function)

        fitness_history = []

        for iteration in range(self.max_iterations):
            self.update_positions()
            self.evaluate_population(objective_function)

            # Track best solution
            best_fitness_idx = np.argmin(self.fitness)
            best_fitness = self.fitness[best_fitness_idx]
            fitness_history.append(best_fitness)

            # Check stagnation
            for i in range(self.population_size):
                if self.fitness[i] >= best_fitness:
                    self.stagnation_count[i] += 1
                else:
                    self.stagnation_count[i] = 0

            self.apply_cosmic_leaps()

            # Print progress
            if iteration % 10 == 0 or iteration == self.max_iterations - 1:
                print(f"Iteration {iteration + 1}/{self.max_iterations}: Best Fitness = {best_fitness:.5f}")

        best_solution = self.population[best_fitness_idx]
        return best_solution, best_fitness, fitness_history

# import dataset
import random


gens = """
 abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOP
QRSTUVWXYZ 1234567890, .-;:_!\"#%&/()=?@${[]}"""

target_string = "ABCDEFGHIJKLMNOPQRST, Genetic Algorithm!"


# num individuals in population
population_size = 100
#mutation rate
mutation_rate = 0.01

# greate chromosome length => collection of genes
def individuals(length):
     return ''.join(random.choice(gens)  for _ in range(length))


# create population of individuals => size_population
def initialze_population(length):
     return [individuals(length) for _ in range(population_size)]


def fitness (target, test_string):
    score =0
    for i in range(len(target)):
         if target[i] == test_string[i]:
             score += 1
    return score

#  selection operator
def selection(population, scores):
    return random.choices(population, weights=scores)[0]


#  crossover single-piont to generate children
def crosover(p1, p2):
    pt = random.randint(1, len(p1)-1)
    return p1[:pt] + p2[pt:]
      

#mutation operator

def mutation (individual):
     mutated_genes = ""
     for gen in individual:
      if random.random() < mutation_rate:
       mutated_genes += random.choice(gens)
      else:
       mutated_genes += gen
     return mutated_genes


#  genetic algorithm
# def genetic_algorithm():
#     # create population
#     initialze_population = initialze_population(individuals(len(target_string)))
#     # evaluate population => fitness
#     for generation in range(population_size):
#         scores = [fitness(target_string, individual) for individual in initialze_population]
#         # selection
#         parents = selection(initialze_population, scores)
    

#         # crossover
#         child = crosover(parents[0], parents[1])
#         # mutation
#         child = mutation(child)


def genetic_algorithm():
    # create population
    population = initialze_population(len(target_string))
    # evaluate population => fitness
    
    for generation in range(population_size):
        scores = [fitness(target_string, individual) for individual in population]
        # selection
        parents = [selection(population, scores) for _ in range(2)]
        # p1 = selection(population, scores)
        # p2 = selection(population, scores)
        # find all generations
        next_generation = []
        while(len(next_generation) < population_size):
           p1, p2 = random.sample(parents, 2)
            # crossover
           child = crosover(p1, p2)
          # mutation
           child = mutation(child)
           next_generation.append(child)

        population = next_generation

        best_individual = population[scores.index(max(scores))]

        print("Generation: {} | Best individual: {} | Fitness: {}".format(generation, best_individual, max(scores)))




genetic_algorithm()
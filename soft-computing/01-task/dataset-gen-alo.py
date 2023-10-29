import csv
import random

def load_csv(filename):
 with open(filename, 'r') as csvFile:
    reader = csv.DictReader(csvFile)
    data = []
    for row in reader:
      data.append(row)
    return data
 
gens = load_csv('./populationbyyear.csv')
mutation_rate=0.01
population_size=len(gens)

target_pop = """{'Year': '1954', 'Total': '22611510', 'Male': '11495505', 'Femal': '11115997', 'Rural': 
'15058949', 'Urban': '7842649'}"""

#  selection random
def individuals (target):
    return([random.choice(gens) for _ in range(len(target) - 1)])

def fitness(target, individual):
#    target = eval(target)
#    individual = eval(individual)
   score=0
   for i in target:
    if (target[i] == individual[i]):
        score += 1
    return score/(len(target) - 1)

def selection(population, scores):
   return random.choices(population, weights=scores)[0]

def crossover(p1, p2):
    pt = random.randint(1, len(p1)-1)
    return p1[:pt] + p2[pt:]

def mutation (individual):
    mutated_genes = ""
    for gen in individual:
        if random.random() < mutation_rate:
            mutated_genes += random.choice(gens)
        else:
            mutated_genes += gen
    return mutated_genes


def genetic_algorithm():
   population =[str( individuals(target_pop)) for _ in range(population_size)]
   
   for generation in range(population_size):
     fitness_scores = [fitness(target_pop, ind) for ind in population]
     parents =  [selection(population, fitness_scores) for _ in range(2)]
     child = crossover(parents[0], parents[1])
     child= mutation(child)

     index = fitness_scores.index(max(fitness_scores))
     best_individual = population[index]

     print("Best individual: ", best_individual)
    


genetic_algorithm()

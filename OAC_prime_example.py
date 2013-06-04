import OAC_prime

context = OAC_prime.Context('input/context_gen_1x444x5193.txt')
min_density = 0.2

# returns a dictionary of triclusters {hash_key : [user, tag, resource]}
Triclusters = context.triclusters(min_density)
print 'Triclusters: ', Triclusters.values()

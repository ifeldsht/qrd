Tree1 = ("Math classroom",[])
Tree2 = ("Library",[])
Tree3 = ("Chemical lab",[])
Tree4 = ("Library",[])
Tree5 = ("Restroom",[])
Tree6 = ("2nd floor",[Tree4,Tree5])
Tree7 = ("3rd floor",[Tree1,Tree2,Tree3])
Tree8 = ("Right stair",[Tree6,Tree7])
Tree9 = ("Basement",[])
Tree10 = ("Gym",[])
Tree11 = ("Left stair",[Tree9,Tree10])
Tree12 = ("School",[Tree8,Tree11])
Tree13 = ("Ticket office",[])
Tree14 = ("Cinema",[Tree13])
Tree15 = ("Street",[Tree12,Tree14])
 
def print_node_names(T):
    print T[0]
    for child in T[1]: print_node_names(child)

print_node_names(Tree15)

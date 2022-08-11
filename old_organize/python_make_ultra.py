from ete3 import Tree

def main():

    with open('15.tree','r') as file:
        file_line = file.readlines()
    
    t = file_line[0]

    the_tree = Tree(t)

    the_tree.set_outgroup('HAEU')

    the_tree.convert_to_ultrametric()

    print(the_tree.write())

main()

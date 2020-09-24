def superset(list_in):
    # Create empty list
    out_list = ['']
    for _ in range(len(list_in)):
        # Add in_list item to the base list
        element = list_in.pop()
        # Concatenate the new element to each member of a duplicated list; then concatenate
        out_list += [element+x for x in out_list]
    return out_list

print(superset(list('ABCDE')))
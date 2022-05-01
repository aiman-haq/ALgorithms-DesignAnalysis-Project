import networkx as nx
import csv

def write_file(n_vals, data, filename) -> None:
    """Writes the results of the analysis performed to a CSV file.
    
    Args:
    - n_vals: a list with values corresponding to the number of elements
    - data: a list with the average number of comparisions for a particular
    number of elements 
    
    Returns:
    None.
    """

    # make the rows that will be written to the file 
    rows = zip(n_vals, data)

    # write all rows to a separate line without any spaces
    with open(f"Data/Dense/{filename}.csv", "w", newline="") as filehandle:
        writer = csv.writer(filehandle)
        # write column headings
        writer.writerow(("# of vertices", "Execution Time"))
        # write a row - value of n and its corresponding num. of comparisions
        for row in rows:
            writer.writerow(row)

def read_graph(file_no) -> dict:
    """Returns a dict of dicts representation after reading in a 
    weighted edgelist of a graph.
    
    Args:
    - file_no: a integer that corresponds to the file (i.e., graph)
    to read. 
    
    Returns:
    A dict of dicts representation of the specified graph.
    """

    fh = open(f"Graph Input Data Dense\graph_{file_no}.txt", "rb")
    graph = nx.read_weighted_edgelist(fh, create_using=nx.DiGraph())
    fh.close()

    return nx.to_dict_of_dicts(graph)
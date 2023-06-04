N, M = map(int,input().split())

if M == 0:
    print(N)

else:
    import numpy as np
    from scipy.sparse import csr_matrix
    from scipy.sparse.csgraph import connected_components

    edge = np.array([input().split() for _ in range(M)], dtype = np.int64).T
    # print(edge)
    tmp = np.ones(M, dtype = np.int64).T
    graph = csr_matrix((tmp, (edge[:] -1)), (N, N))

    print (connected_components(graph, return_labels=False, directed = False))
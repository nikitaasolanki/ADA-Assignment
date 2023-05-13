def distance_on_torus( point=[500,500] ):
    index_diff = [[1],[1],[0],[0],[0,1],[0,1],[0,1],[0,1]]
    coord_diff = [[-1],[1],[-1],[1],[-1,-1],[-1,1],[1,-1],[1,1]]
    
    tree = BallTree( ONES, leaf_size=5*n, metric='euclidean')
    
    dist, indi = tree.query([point],k=1, return_distance=True )

    distances = [dist[0]]

    for indici_to_shift, coord_direction in zip(index_diff, coord_diff):
        MIRROR = ONES.copy()
        for i,shift in zip(indici_to_shift,coord_direction):
            MIRROR[:,i] = MIRROR[:,i] + (shift * n)

        tree = BallTree( MIRROR, leaf_size=5*n, metric='euclidean')
        dist, indi = tree.query([point],k=1, return_distance=True )
        
        distances.append(dist[0])
        
    
    return np.min(distances)

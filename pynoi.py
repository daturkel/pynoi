class TowersOfHanoi:
    def __init__(self,n,verbose=True):
        self.n = n
        self.verbose = verbose
        self._step_count = None
        self.reset()
    
    def __str__(self):
        return str(self.posts)
    
    def __repr__(self):
        return f'TowersOfHanoi: {str(self.posts)}'
    
    ## Private method; returns a `posts` array in initial state
    def _reset_posts(self):
        return [[i for i in range(self.n,0,-1)],[],[]]
    
    ## Public method to reset the puzzle to its initial state
    def reset(self):
        self.posts = self._reset_posts()
    
    ## Public method to move the top piece from post a to post b
    ## Posts are 1-indexed (1,2,3)
    def move(self,a,b,verbose=None):
        verbose = verbose if verbose is not None else self.verbose
        # check to see if initial post has any discs
        if len(self.posts[a-1]) == 0:
            print(f'Post {a} has no discs to move.')
            return False
        else:
            pass
        # check to see if move would place a larger disc on top of a smaller one
        if len(self.posts[b-1]) > 0 and (self.posts[a-1][-1] > self.posts[b-1][-1]):
            print(f'Disc {self.posts[a-1][-1]} cannot be moved on top of disc {self.posts[b-1][-1]}.')
            return False
        else:
            pass
        # execute the move
        self.posts[b-1].append(self.posts[a-1].pop())
        self._step_count = self._step_count + 1 if self._step_count is not None else None
        if verbose:
            if self._step_count is not None:
                print(f'{self._step_count}. ({a},{b}): {self}')
            else:
                print(f'({a},{b}): {self}')
        return True
    
    ## Private method; move a stack of two pieces from post a to post b
    def _two_move(self,a,b,verbose=None):
        verbose = verbose if verbose is not None else self.verbose
        c = 6-a-b
        self.move(a,c,verbose)
        self.move(a,b,verbose)
        self.move(c,b,verbose)
    
    ## Private method; recursively move a stack of n pieces from post a to post b
    def _n_move(self,n,a,b,verbose=None):
        verbose = verbose if verbose is not None else self.verbose
        c = 6-a-b
        if n == 1:
            self.move(a,b,verbose)
        elif n == 2:
            self._two_move(a,b,verbose)
        elif n > 2:
            self._n_move(n-1,a,c,verbose)
            self._n_move(1,a,b,verbose)
            self._n_move(n-1,c,b,verbose)

    ## Public method; (reset and) solve the puzzle, moving all discs from post 1 to post 3
    def solve(self,verbose=None):
        self.reset()
        verbose = verbose if verbose is not None else self.verbose
        self._step_count = 0
        
        self._n_move(self.n,1,3,verbose=verbose)
        if not verbose:
            print(self)
        print(f'solved in {self._step_count} steps')
        
        self._step_count = None
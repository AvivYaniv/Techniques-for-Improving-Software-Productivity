
from chaotic    import chaotic
from mbg        import join, bottom, top, assign

succ      = { 
                1: {2}                                                                   , 
                2: {3}                                                    	             , 
                3: {}                   
            } # CFG edges

tr        = {
                (1, 2): lambda mbg: assign(mbg, 'x', ('5',())                       )   , 
                (2, 3): lambda mbg: assign(mbg, 'x', ('+', (('x',()), ('z',())))    )   ,
                        
            } # transfer function

tr_txt    = { 
                (1, 2): "x := 5"                                                        , 
                (2, 3): "x := y + z"                                                    , 
                (3, 3): "nop"           
            } # for debugging


iota      = set(['x', 'y', 'z'])

chaotic(succ, 1, iota, join, bottom, tr, tr_txt)

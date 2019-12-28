
from chaotic    import chaotic
from mbg        import join, meet, bottom, top, assign

succ      = {
                1:      {2}                                                             , 
                2:      {3}                                                             ,
                3:      {3, 4}                                                          , 
                4:      {}                                                              ,                
            } # CFG edges

tr        = {
                (1, 2): lambda mbg: assign(mbg, 'w', ('3', ())                      )   ,
                (2, 3): lambda mbg: assign(mbg, 'y', ('+', (('w',()), ('9',())))    )   ,
                (3, 3): lambda mbg: assign(mbg, 'x', ('*', (('x',()), ('2',())))    )   ,
                (3, 4): lambda mbg: assign(mbg, 'w', ('*', (('x',()), ('y',())))    )   ,
            } # transfer function

tr_txt    = {   
                (1, 2): "w := 3"                                                        ,
                (2, 3): "y := w + 9"                                                    ,                                
                (3, 3): "x := x * 2"                                                    ,
                (3, 4): "w := x * y"                                                    ,                
            } # for debugging


iota      = set(['x', 'y', 'z', 'w'])

chaotic(succ, 1, iota, join, bottom, tr, tr_txt)

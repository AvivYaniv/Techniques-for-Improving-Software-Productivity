
from chaotic    import chaotic
from mbg        import join, meet, bottom, top, assign

succ      = {
                1:      {2}                                                                 , 
                2:      {3, 4}                                                              ,
                3:      {5}                                                                 , 
                4:      {5}                                                                 , 
                5:      {6, 7}                                                              , 
                6:      {8}                                                                 ,
                7:      {8}                                                                 ,
                8:      {9}                                                                 ,
                9:      {}                                                                  ,
            } # CFG edges

tr        = {
                (1, 2): lambda mbg: assign(mbg, 'x', ('9', ())                      )       ,
                (2, 3): lambda mbg: mbg                                                     ,
                (2, 4): lambda mbg: mbg                                                     ,
                (3, 5): lambda mbg: assign(mbg, 'y', ('3', ())                      )       ,
                (4, 5): lambda mbg: mbg                                                     ,
                (5, 6): lambda mbg: mbg                                                     ,
                (5, 7): lambda mbg: mbg                                                     ,
                (6, 8): lambda mbg: assign(mbg, 'z', ('y', ())                      )       ,
                (7, 8): lambda mbg: mbg                                                     ,
                (8, 9): lambda mbg: assign(mbg, 'y', ('7', ())                      )       ,
            } # transfer function

tr_txt    = {   
                (1, 2): "x := 9"                                                            ,                
                (2, 3): "[x > 7]"                                                           ,
                (2, 4): "[x <= 7]"                                                          ,
                (3, 5): "y := 3"                                                            ,
                (4, 5): "nope"                                                              ,
                (5, 6): "[x > 7]"                                                           ,
                (5, 7): "[x <= 7]"                                                          ,
                (6, 8): "z := y"                                                            ,
                (7, 8): "nope"                                                              ,
                (8, 9): "y := 7"                                                            ,
            } # for debugging


iota      = set(['x', 'y', 'z'])

chaotic(succ, 1, iota, join, bottom, tr, tr_txt)

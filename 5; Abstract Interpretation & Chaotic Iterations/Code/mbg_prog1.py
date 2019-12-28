
from chaotic    import chaotic
from mbg        import join, meet, bottom, top, assign

succ      = {
                1:      {2}                                                             , 
                2:      {3}                                                             ,
                3:      {4, 5}                                                          , 
                4:      {6}                                                             , 
                5:      {6}                                                             , 
                6:      {7}                                                             ,
                7:      {}                                                              ,                
            } # CFG edges

tr        = {
                (1, 2): lambda mbg: assign(mbg, 'x', ('+', (('z',()), ('9',())))    )   ,
                (2, 3): lambda mbg: assign(mbg, 'y', ('5', ())                      )   ,
                (3, 4): lambda mbg: mbg                                                 ,
                (3, 5): lambda mbg: mbg                                                 ,
                (4, 6): lambda mbg: assign(mbg, 'z', ('y', ())                      )   ,
                (5, 6): lambda mbg: assign(mbg, 'z', ('+', (('y',()), ('1',())))    )   ,
                (6, 7): lambda mbg: assign(mbg, 'x', ('3', ())                      )   ,
            } # transfer function

tr_txt    = {   
                (1, 2): "x := z + 9"                                                    ,
                (2, 3): "y := 5"                                                        ,
                (3, 4): "[x != 7]"                                                      ,
                (3, 5): "[x = 7]"                                                       ,
                (4, 6): "z := y"                                                        ,
                (5, 6): "z := y + 1"                                                    ,
                (6, 7): "x := 3"                                                        ,
            } # for debugging


iota      = set(['x', 'y', 'z'])

chaotic(succ, 1, iota, join, bottom, tr, tr_txt)

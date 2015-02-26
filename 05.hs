result = length [(a1,a2,a3,a4,a5,a6) | 
                        a1 <- [0..7], 
                        a2 <- [0..7], 
                        a3 <- [0..7], 
                        a4 <- [0..7], 
                        a5 <- [0..7], 
                        a6 <- [0..7], 
                        a1+a2+a3==a4+a5+a6]

main = print result
